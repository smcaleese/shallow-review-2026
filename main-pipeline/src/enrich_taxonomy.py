#!/usr/bin/env python3
"""
Enrich The Taxonomy
Makes one LLM call per leaf category, with its classified items, and writes every agenda field (summary, theory of
change, see also, ...) to a copy of the taxonomy with an `agenda` block per category. The hand-written taxonomy.yaml
is not modified. Agendas already in the output file are kept (so hand edits survive) unless --overwrite or --only.

Basic usage (from the main-pipeline folder):
    uv run python src/enrich_taxonomy.py --workers 4
Reads data/taxonomy.yaml and writes data/taxonomy-enriched.yaml (inside the data folder set by DATA_PATH).
"""

import argparse
import io
import json
import logging
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml
from pydantic import BaseModel
from ruamel.yaml import YAML

from shallow_review.common import DATA_PATH, PROMPTS_PATH
from shallow_review.data_db import data_db_locked
from shallow_review.llm import get_completion
from shallow_review.taxonomy import Category, Taxonomy, load_taxonomy
from shallow_review.utils import url_hash_short
from terminal import console, run

logger = logging.getLogger(__name__)


class CritiqueRef(BaseModel):
    """A classified item that critiques the agenda."""

    paper_id: str  # url_hash_short(url) of the item
    note: str  # what it shows against the agenda


class AgendaResult(BaseModel):
    """LLM output for one agenda."""

    one_sentence_summary: str
    theory_of_change: str
    see_also: list[str]  # leaf category IDs
    general_approach: str
    target_case: str
    key_people: list[str]
    critiques: list[CritiqueRef]
    critique_fallback: str  # main objection in one sentence, used when no item critiques the agenda
    comment: str = ""


def load_papers() -> list[dict]:
    """All classified items with the fields the prompt needs, best fit to their category first."""
    with data_db_locked() as db:
        rows = db.execute(
            "SELECT url, data FROM entries WHERE status = 'done'"
        ).fetchall()
    papers = []
    for row in rows:
        data = json.loads(row["data"])
        if not data.get("categories"):
            continue
        papers.append(
            {
                "id": url_hash_short(row["url"]),
                "url": row["url"],
                "category": max(data["categories"], key=lambda c: c.get("score", 0))["id"],
                "score": max(c.get("score", 0) for c in data["categories"]),
                "title": data.get("title", ""),
                "authors": data.get("authors", []),
                "organizations": data.get("author_organizations", []),
                "date": data.get("date") or "",
                "summary": data.get("summary", ""),
            }
        )
    papers.sort(key=lambda paper: paper["score"], reverse=True)
    return papers


def leaves_with_paths(taxonomy: Taxonomy) -> list[tuple[Category, list[str]]]:
    """All leaf categories with their name path from the root."""
    out = []

    def walk(cat: Category, path: list[str]) -> None:
        path = path + [cat.name]
        if cat.is_leaf:
            out.append((cat, path))
        for child in cat.children:
            walk(child, path)

    for cat in taxonomy.taxonomy:
        walk(cat, [])
    return out


def field_options(taxonomy: Taxonomy, name: str) -> list[str]:
    """Allowed values of an agenda field, as set in the taxonomy's agenda_fields."""
    for field in taxonomy.agenda_fields:
        if field.name == name:
            assert field.options, f"Agenda field '{name}' has no options in the taxonomy"
            return field.options
    raise ValueError(f"Agenda field '{name}' is not in the taxonomy's agenda_fields")


def write_agenda(
    cat: Category,
    path: list[str],
    items: list[dict],
    leaves: list[tuple[Category, list[str]]],
    papers: list[dict],
    taxonomy: Taxonomy,
    model: str,
) -> dict:
    """Ask the LLM for one category's agenda fields. Returns them keyed by agenda field name, as markdown."""
    with open(PROMPTS_PATH / "agenda.yaml") as f:
        prompts = yaml.safe_load(f)["write_agenda"]
    general_options = field_options(taxonomy, "General approach")
    target_options = field_options(taxonomy, "Target case")

    result = get_completion(
        template_vars={
            "year": taxonomy.year,
            "categories": [
                {"id": c.id, "path": " > ".join(p), "description": " ".join(c.description.split())} for c, p in leaves
            ],
            "papers": papers,
            "path": " > ".join(path),
            "category_id": cat.id,
            "name": cat.name,
            "description": cat.description.strip(),
            "items": items,
            "general_approach_options": general_options,
            "target_case_options": target_options,
        },
        model=model,
        response_type=AgendaResult,
        system_prompt_template=prompts["system"],
        user_prompt_template=prompts["user"],
        system_cache_ttl="1h",  # categories and item index are the same for every call
        effort="medium",
        max_tokens=16000,
    )
    assert isinstance(result, AgendaResult)
    assert result.general_approach in general_options, f"{cat.id}: bad general_approach {result.general_approach!r}"
    assert result.target_case in target_options, f"{cat.id}: bad target_case {result.target_case!r}"

    # Key people must come from the items' authors (or organisations, for items without named authors)
    names = {n for item in items for n in item["authors"] + item["organizations"]}
    key_people = [p for p in result.key_people if p in names]
    if len(key_people) < len(result.key_people):
        logger.warning(f"{cat.id}: dropped key people not in the items: {set(result.key_people) - names}")

    # See also: other leaf categories, linked to their section in the draft
    names_by_id = {c.id: c.name for c, _ in leaves}
    see_also = [i for i in result.see_also if i in names_by_id and i != cat.id]
    if len(see_also) < len(result.see_also):
        logger.warning(f"{cat.id}: dropped see-also IDs: {set(result.see_also) - set(see_also)}")

    # Critiques: cited items only; without any, the LLM's one-sentence objection, marked as unsourced
    papers_by_id = {p["id"]: p for p in papers}
    # The LLM's note per critique only helps it choose; the draft lists the links alone
    critiques = [
        f"[{papers_by_id[c.paper_id]['title']}]({papers_by_id[c.paper_id]['url']})"
        for c in result.critiques
        if c.paper_id in papers_by_id
    ]
    if len(critiques) < len(result.critiques):
        logger.warning(f"{cat.id}: dropped critiques citing unknown item ids")

    agenda: dict = {
        "One-sentence summary": result.one_sentence_summary,
        "Theory of change": result.theory_of_change,
        "See also": ", ".join(f"[{names_by_id[i]}](#{i})" for i in see_also),
        "General approach": result.general_approach,
        "Target case": result.target_case,
        "Key people": key_people,
        "Critiques": ", ".join(critiques) if critiques else f"*(unsourced, LLM-drafted)* {result.critique_fallback}",
    }
    if result.comment:
        agenda["Comment (internal)"] = result.comment
    return agenda


def save_enriched(input_path: Path, output_path: Path, agendas: dict[str, dict]) -> None:
    """Write the input taxonomy to output_path with each category's `agenda` block, keeping comments and layout."""
    ryaml = YAML()
    ryaml.preserve_quotes = True
    ryaml.width = 120
    ryaml.indent(mapping=2, sequence=2, offset=0)
    with open(input_path) as f:
        doc = ryaml.load(f)

    def walk(nodes: list) -> None:
        for node in nodes:
            if node["id"] in agendas:
                node["agenda"] = agendas[node["id"]]
            walk(node.get("children") or [])

    walk(doc["taxonomy"])
    out = io.StringIO()
    out.write(f"# Generated by `src/enrich_taxonomy.py` from {input_path.name}. Agenda blocks may be edited by\n")
    out.write("# hand: re-running keeps them unless --overwrite or --only. Edit categories in the input file instead.\n\n")
    ryaml.dump(doc, out)
    # ruamel leaves a trailing space where it wraps long plain scalars
    output_path.write_text("\n".join(line.rstrip() for line in out.getvalue().split("\n")))


def enrich_taxonomy(
    input_path: Path, output_path: Path, model: str, workers: int, overwrite: bool, only: set[str] | None
) -> tuple[int, list[str], dict[str, str]]:
    """Enrich the taxonomy. Returns (number of agendas written, categories without items, errors by category id)."""
    taxonomy = load_taxonomy(input_path)
    leaves = leaves_with_paths(taxonomy)
    leaf_ids = {c.id for c, _ in leaves}
    if only:
        assert only <= leaf_ids, f"Not leaf categories: {only - leaf_ids}"

    # Keep agendas from an earlier run (possibly edited by hand) for categories that still exist
    agendas: dict[str, dict] = {}
    if output_path.exists():
        for cat, _ in leaves_with_paths(load_taxonomy(output_path)):
            if cat.agenda and cat.id in leaf_ids:
                agendas[cat.id] = cat.agenda

    papers = load_papers()
    items_by_cat: dict[str, list[dict]] = defaultdict(list)
    for p in papers:
        items_by_cat[p["category"]].append(p)

    todo, no_items = [], []
    for cat, path in leaves:
        redo = cat.id in only if only else (overwrite or cat.id not in agendas)
        if not redo:
            continue
        if not items_by_cat.get(cat.id):
            logger.warning(f"{cat.id}: no classified items, skipped")
            no_items.append(cat.id)
            continue
        todo.append((cat, path))

    errors: dict[str, str] = {}
    written = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(write_agenda, cat, path, items_by_cat[cat.id], leaves, papers, taxonomy, model): cat.id
            for cat, path in todo
        }
        for future in as_completed(futures):
            cat_id = futures[future]
            try:
                agendas[cat_id] = future.result()
                written += 1
                logger.info(f"{cat_id}: agenda written")
            except Exception as e:
                logger.error(f"{cat_id}: failed: {e}")
                errors[cat_id] = str(e)

    save_enriched(input_path, output_path, agendas)
    return written, no_items, errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write each leaf category's agenda fields with an LLM.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input", type=Path, default=DATA_PATH / "taxonomy.yaml", help="Hand-written taxonomy (default: <data>/taxonomy.yaml)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DATA_PATH / "taxonomy-enriched.yaml",
        help="Enriched taxonomy to write (default: <data>/taxonomy-enriched.yaml)",
    )
    parser.add_argument("--model", default="claude-sonnet-5-5", help="LLM model to use")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel LLM calls (default: 4)")
    parser.add_argument("--overwrite", action="store_true", help="Rewrite agendas already in the output file")
    parser.add_argument(
        "--only", default="", help="Comma-separated category IDs to (re)write (default: all missing ones)"
    )
    args = parser.parse_args()

    assert args.input.resolve() != args.output.resolve(), "Output must differ from the input taxonomy"
    only_ids = {s.strip() for s in args.only.split(",") if s.strip()} or None

    console.print(
        f"[bold]Enriching {args.input} -> {args.output}[/bold] (model={args.model}, workers={args.workers})\n"
    )
    written, no_items, errors = enrich_taxonomy(
        args.input, args.output, args.model, args.workers, args.overwrite, only_ids
    )
    console.print(f"\nWrote {written} agendas to {args.output}")
    if no_items:
        console.print(f"[yellow]No classified items (fields left empty): {', '.join(no_items)}[/yellow]")
    for category_id, error in errors.items():
        console.print(f"[red]{category_id}: {error}[/red]")


if __name__ == "__main__":
    run(main)
