#!/usr/bin/env python3
"""
Export The Draft
Walks the taxonomy tree and writes a markdown draft: one section per category with its agenda fields (empty ones are
left for editors) and the classified items that pass the score thresholds, sorted by shallow_review_inclusion.
Human feedback (include / exclude / reclassify) is applied on top of the LLM's output.

Basic usage (from the main-pipeline folder):
    uv run python src/export_draft.py --min-shallow-review 0.4 -o draft.md
Reads taxonomy-enriched.yaml from the data folder if it exists, otherwise taxonomy.yaml.
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from rich.console import Console

from terminal import run
from shallow_review.common import DATA_PATH
from shallow_review.data_db import data_db_locked
from shallow_review.taxonomy import Category, load_taxonomy
from shallow_review.utils import url_hash_short

# Printed to stderr, because stdout may be the draft
err_console = Console(stderr=True)

# Agenda field label (as written in the taxonomy's agenda_fields) -> key in a category's sr2024 block, for prefilling
SR2024_FIELD_KEYS = {
    "One-sentence summary": "summary",
    "Theory of change": "theory_of_change",
    "See also": "see_also",
    "Orthodox problems": "orthodox_problems",
    "Target case": "target_case",
    "Broad approach": "broad_approach",
    "Key people": "names",
    "Estimated FTEs": "ftes",
    "Critiques": "critiques",
    "Funded by": "funded_by",
    "Funding in {year}": "funding_2023_4",
}

HEADING_SIZES = ["1.6em", "1.5em", "1.4em", "1.3em", "1.2em", "1.1em"]
GREY = "color:#777"


def split_list(text: str) -> set[str]:
    return {part.strip() for part in text.split(",") if part.strip()}


# ---------------------------------------------------------------- feedback and database


def load_feedback(feedback_source: str) -> dict[str, dict]:
    """Human feedback per URL, consolidated over all of the URL's actions."""
    sql = "SELECT url, action, human_category, notes FROM feedback WHERE 1=1"
    params = []
    if feedback_source:
        sql += " AND feedback_source = ?"
        params.append(feedback_source)
    sql += " ORDER BY feedback_timestamp DESC"
    with data_db_locked() as db:
        rows = db.execute(sql, params).fetchall()

    actions_by_url = defaultdict(list)
    for row in rows:
        actions_by_url[row["url"]].append(row)

    feedback = {}
    for url, actions in actions_by_url.items():
        kinds = {a["action"] for a in actions}
        feedback[url] = {
            "has_include": "include" in kinds,
            "has_exclude": "exclude" in kinds,
            "has_reclassify": "reclassify" in kinds,
            "has_note": "note" in kinds,
            "human_categories": [
                a["human_category"] for a in actions if a["action"] == "reclassify" and a["human_category"]
            ],
            "notes": next((a["notes"] for a in actions if a["notes"]), None),
        }
    return feedback


def query_rows(args, include_urls: set[str], kinds: set[str], sources: set[str]) -> list:
    """Classified items that pass the thresholds, or have include feedback."""
    thresholds = "ai_safety_relevance >= ? AND shallow_review_inclusion >= ?"
    params = [args.min_ai_safety, args.min_shallow_review]
    if include_urls:
        where = f"({thresholds} OR url IN ({','.join('?' * len(include_urls))}))"
        params += list(include_urls)
    else:
        where = thresholds
    sql = f"""
        SELECT url, ai_safety_relevance, shallow_review_inclusion, kind, data
        FROM entries
        WHERE status = 'done' AND {where}
    """
    if kinds:
        sql += f" AND kind IN ({','.join('?' * len(kinds))})"
        params += list(kinds)
    if sources:
        sql += f" AND source IN ({','.join('?' * len(sources))})"
        params += list(sources)
    with data_db_locked() as db:
        return db.execute(sql, params).fetchall()


# ---------------------------------------------------------------- grouping items by category


def in_review_window(item: dict, review_year: int) -> bool:
    """Items dated before 1 November of the year before the review year are dropped; undated items are kept."""
    if item["date"]:
        try:
            return date.fromisoformat(item["date"]) >= date(review_year - 1, 11, 1)
        except (ValueError, TypeError):
            return True  # Invalid date format: include by default
    if item["published_year"]:
        try:
            return int(item["published_year"]) >= review_year - 1  # Only a year: accept it and the one before
        except (ValueError, TypeError):
            return True
    return True


def group_by_category(rows: list, feedback_by_url: dict, args, review_year: int) -> tuple[dict, dict]:
    """Returns ({category id: items sorted by inclusion score}, counts of what the feedback changed)."""
    items_by_category = defaultdict(list)
    counts = defaultdict(int)

    for row in rows:
        url = row["url"]
        feedback = feedback_by_url.get(url) if args.respect_feedback else None
        if feedback and feedback["has_exclude"]:
            counts["excluded"] += 1
            continue

        try:
            data = json.loads(row["data"])
        except json.JSONDecodeError as e:
            err_console.print(f"[yellow]Warning: Failed to parse data for {url}: {e}[/yellow]")
            continue
        # Sorted by score: older rows may not be
        categories = sorted(data.get("categories", []), key=lambda c: c.get("score", 0), reverse=True)
        if not categories:
            err_console.print(f"[yellow]Warning: Item {url} has no categories, skipping[/yellow]")
            continue

        notes = (feedback or {}).get("notes") or ""
        needs_recategorization = "NEEDS_RECATEGORIZATION" in notes
        obsolete_llm = bool(feedback and feedback["has_note"] and "RECLASSIFY_OBSOLETE_LLM" in notes)
        counts["needs_recategorization"] += needs_recategorization
        counts["obsolete_llm"] += obsolete_llm

        if feedback and feedback["has_reclassify"] and feedback["human_categories"]:
            category_ids = feedback["human_categories"]  # Can be several
            counts["reclassified"] += 1
        else:
            category_ids = [categories[0]["id"]]

        if (
            feedback
            and feedback["has_include"]
            and (row["shallow_review_inclusion"] < args.min_shallow_review or row["ai_safety_relevance"] < args.min_ai_safety)
        ):
            counts["included_by_feedback"] += 1

        item = {
            "url": url,
            "url_hash_short": url_hash_short(url),
            "title": data.get("title", "Untitled"),
            "authors": data.get("authors", []),
            "organization": data.get("organization", ""),
            "date": data.get("date", ""),
            "published_year": data.get("published_year"),
            "venue": data.get("venue", ""),
            "kind": row["kind"],
            "shallow_review_inclusion": row["shallow_review_inclusion"],
            "summary": data.get("summary", ""),
            "key_points": data.get("key_points", []),
            "needs_recategorization": needs_recategorization,
            "obsolete_llm_category": obsolete_llm,
            "category_count": len(category_ids),
        }
        if in_review_window(item, review_year):
            for category_id in category_ids:
                items_by_category[category_id].append(item)

    for items in items_by_category.values():
        items.sort(key=lambda item: item["shallow_review_inclusion"], reverse=True)
    return items_by_category, counts


# ---------------------------------------------------------------- markdown


def render_header(args, kinds: set[str], sources: set[str], counts: dict, items_by_category: dict, year: int) -> list[str]:
    lines = [
        f"# AI Safety Shallow Review {year}",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}",
        "",
        f"**Filters:** shallow_review≥{args.min_shallow_review}, ai_safety≥{args.min_ai_safety}",
    ]
    if kinds:
        lines.append(f"**Kinds:** {', '.join(sorted(kinds))}")
    if sources:
        lines.append(f"**Sources:** {', '.join(sorted(sources))}")
    if args.respect_feedback:
        lines.append("**Human feedback:** Respected" + (f" (source: {args.feedback_source})" if args.feedback_source else ""))
        for key, label in [
            ("excluded", "Excluded by feedback"),
            ("reclassified", "Reclassified by feedback"),
            ("included_by_feedback", "Included by feedback (below thresholds)"),
            ("needs_recategorization", "⚠️ Needs recategorization (obsolete CSV category)"),
            ("obsolete_llm", "🔄 Re-classified (obsolete LLM category, one-time)"),
        ]:
            if counts[key] > 0:
                lines.append(f"  - {label}: {counts[key]}")
    lines.append("")
    # Unique URLs, since a paper can appear in several categories
    unique_urls = {item["url"] for items in items_by_category.values() for item in items}
    appearances = sum(len(items) for items in items_by_category.values())
    lines += [
        f"**Total unique papers:** {len(unique_urls)} (appearing {appearances} times across categories)",
        "",
        "---",
        "",
    ]
    return lines


def render_item(item: dict) -> str:
    """One list entry: - **Title**, *Authors*, Date, Venue [stats] Summary • Key points"""
    authors = ", ".join(item["authors"][:3]) + (" et al." if len(item["authors"]) > 3 else "")
    byline = f"*{authors}*" if authors else (f"*{item['organization']}*" if item["organization"] else "")
    date_part = item["date"] or (str(item["published_year"]) if item["published_year"] else "")

    markers = ""
    if item["needs_recategorization"]:
        markers += "⚠️"
    if item["obsolete_llm_category"]:
        markers += "🔄"
    if item["category_count"] > 1:
        markers += f"✌️(in {item['category_count']} categories)"
    if markers:
        markers += " "
    stats = (
        f'<span style="{GREY}">[{markers}{item["kind"]}, sr={item["shallow_review_inclusion"]:.2f}, '
        f'id:{item["url_hash_short"]}]</span>'
    )

    summary = item["summary"].replace("\n", " ").strip()
    key_points = " • ".join(kp.replace("\n", " ").strip() for kp in item["key_points"][:3])

    parts = [
        f"**[{item['title']}]({item['url']})**",
        byline,
        date_part,
        item["venue"],
        stats,
        f'<span style="{GREY}">Summary: {summary}</span>' if summary else "",
        f'<span style="{GREY}">Key points: {key_points}</span>' if key_points else "",
    ]
    return "- " + ", ".join(part for part in parts if part)


def render_agenda_fields(cat: Category, taxonomy, empty_fields: list[str]) -> list[str]:
    """The category's agenda fields: its own value, otherwise a placeholder (recorded in empty_fields)."""
    year = str(taxonomy.year)
    sr = cat.sr2024 or {}
    agenda = cat.agenda or {}
    lines = []
    for field in taxonomy.agenda_fields:
        label = field.name.replace("{year}", year)
        sr_key = SR2024_FIELD_KEYS.get(field.name)
        value = agenda.get(field.name)
        if isinstance(value, list):
            value = ", ".join(value)
        if value:
            lines.append(f"**{label}:** {value}  ")
            continue
        if label.startswith("Who edits"):
            lines.append(f'**<span style="{GREY}">{label}:</span>** **<span style="color:#da5">take me</span>**  ')
        elif field.options:
            lines.append(f"**{label}:** *(one of: {' / '.join(field.options)})*  ")
        elif sr_key and sr.get(sr_key):
            lines.append(f"**{label}:** *(SR2024: {sr[sr_key]})*  ")
        else:
            lines.append(f"**{label}:**  ")
        empty_fields.append(f"{cat.id}: {label}")

    if sr.get("outputs"):
        lines.append(f"**Outputs in {year}:**  \n*(SR2024 outputs: {sr['outputs']})*  ")
    else:
        lines.append(f"**Outputs in {year}:**  ")
    return lines


def render_category(cat: Category, level: int, taxonomy, items_by_category: dict, lines: list[str], empty_fields: list[str]) -> None:
    """Append the category's section and, recursively, its children's. Non-leaf categories without items are skipped."""
    if not cat.is_leaf and not any(leaf_id in items_by_category for leaf_id in cat.get_all_leaf_ids()):
        return

    heading = "#" * (level + 1)
    lines.append(
        f'{heading} <span id="{cat.id}" style="font-size:{HEADING_SIZES[level]}">{cat.name}</span> '
        f'<span style="color:#bbb">[cat:{cat.id}]</span>\n'
    )
    if cat.is_leaf:
        lines += render_agenda_fields(cat, taxonomy, empty_fields)
        items = items_by_category.get(cat.id, [])
        if items:
            lines += [render_item(item) for item in items]
            lines.append("")
    lines.append("\n---\n")
    if not cat.is_leaf:
        for child in cat.children:
            render_category(child, level + 1, taxonomy, items_by_category, lines, empty_fields)


# ---------------------------------------------------------------- main


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export the taxonomy with classified items as a markdown draft.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("-o", "--output", type=Path, help="Draft file to write (default: stdout, mixed with log lines)")
    parser.add_argument("--min-shallow-review", type=float, default=0.1, help="Minimum shallow_review_inclusion score")
    parser.add_argument("--min-ai-safety", type=float, default=0.1, help="Minimum ai_safety_relevance score")
    parser.add_argument("--kinds", default="", help="Comma-separated list of accepted kinds (default: all)")
    parser.add_argument("--source", default="", help="Comma-separated list of accepted sources (default: all)")
    parser.add_argument(
        "--respect-feedback",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Respect human feedback (include/exclude/reclassify) (default: on)",
    )
    parser.add_argument("--feedback-source", default="", help="Only respect feedback from this source (default: all)")
    parser.add_argument(
        "--taxonomy",
        type=Path,
        help="Taxonomy to export (default: taxonomy-enriched.yaml in the data folder if present, else taxonomy.yaml)",
    )
    parser.add_argument("--strict", action="store_true", help="Fail if any agenda field of a printed category is empty")
    args = parser.parse_args()

    if args.taxonomy:
        taxonomy_path = args.taxonomy
    elif (DATA_PATH / "taxonomy-enriched.yaml").exists():
        taxonomy_path = DATA_PATH / "taxonomy-enriched.yaml"
    else:
        taxonomy_path = DATA_PATH / "taxonomy.yaml"
    err_console.print(f"Taxonomy: {taxonomy_path}")
    taxonomy = load_taxonomy(taxonomy_path)
    kinds = split_list(args.kinds)
    sources = split_list(args.source)

    feedback_by_url = load_feedback(args.feedback_source) if args.respect_feedback else {}
    include_urls = {url for url, fb in feedback_by_url.items() if fb["has_include"]}
    rows = query_rows(args, include_urls, kinds, sources)
    if not rows and not feedback_by_url:
        err_console.print("[yellow]No items found matching filters[/yellow]")
        return

    items_by_category, counts = group_by_category(rows, feedback_by_url, args, taxonomy.year)

    lines = render_header(args, kinds, sources, counts, items_by_category, taxonomy.year)
    empty_fields: list[str] = []  # "category_id: field", for --strict
    for top_category in taxonomy.taxonomy:
        render_category(top_category, 1, taxonomy, items_by_category, lines, empty_fields)

    if args.strict and empty_fields:
        err_console.print(f"[red]--strict: {len(empty_fields)} empty agenda fields, nothing written:[/red]")
        for entry in empty_fields:
            err_console.print(f"  {entry}")
        sys.exit(1)

    draft = "\n".join(lines) + "\n"
    if args.output:
        args.output.write_text(draft)
        err_console.print(f"Wrote {args.output}")
    else:
        # Plain print, not the rich console, which would add formatting
        print(draft, end="")


if __name__ == "__main__":
    run(main)
