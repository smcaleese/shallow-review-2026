#!/usr/bin/env python3
"""
Export The Draft
Walks the taxonomy tree and writes a markdown draft: one section per category with its agenda fields (empty ones are
left for editors) and the classified items, best fit first.
Human feedback (include / exclude / reclassify) is applied on top of the LLM's output.

Basic usage (from the draft-pipeline folder):
    uv run python src/export_draft.py -o draft.md
    uv run python src/export_draft.py --top 10 -o draft.md   # each category's 10 most important items (score_entries.py)
    uv run python src/export_draft.py --min-importance 0.5 --top 10 -o draft.md   # importance >= 0.5, at most 10 each
Reads taxonomy-enriched.yaml from the data folder if it exists, otherwise taxonomy.yaml.
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from rich.console import Console

from shallow_review.common import DATA_PATH
from shallow_review.data_db import data_db_locked
from shallow_review.taxonomy import Category, load_taxonomy
from shallow_review.utils import url_hash_short
from terminal import run

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


def query_rows(sources: set[str]) -> list:
    """The classified items, from the given sources if any."""
    sql = "SELECT url, classifier_output, importance FROM entries WHERE status = 'done'"
    params: list = []
    if sources:
        sql += f" AND source IN ({','.join('?' * len(sources))})"
        params += list(sources)
    with data_db_locked() as db:
        return db.execute(sql, params).fetchall()


# ---------------------------------------------------------------- grouping items by category


def in_review_window(item: dict, review_year: int) -> bool:
    """Items dated before 1 November of the year before the review year are dropped; undated items are kept."""
    parts = (item["date"] or "").split("-")
    try:
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 12  # Only a year: accept it and the one before
        day = int(parts[2]) if len(parts) > 2 else 1
        return date(year, month, day) >= date(review_year - 1, 11, 1)
    except (ValueError, IndexError):
        return True  # Undated or invalid date: include


def group_by_category(rows: list, feedback_by_url: dict, args, review_year: int) -> tuple[dict, dict]:
    """Returns ({category id: items, best fit first}, counts of what the feedback changed)."""
    items_by_category = defaultdict(list)
    counts = defaultdict(int)

    for row in rows:
        url = row["url"]
        feedback = feedback_by_url.get(url) if args.respect_feedback else None
        if feedback and feedback["has_exclude"]:
            counts["excluded"] += 1
            continue

        try:
            data = json.loads(row["classifier_output"])
        except json.JSONDecodeError as e:
            err_console.print(f"[yellow]Warning: Failed to parse data for {url}: {e}[/yellow]")
            continue
        # Sorted by fit: older rows may not be
        categories = sorted(data.get("categories", []), key=lambda c: c.get("fit", 0), reverse=True)
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

        item = {
            "url": url,
            "url_hash_short": url_hash_short(url),
            "title": data.get("title", "Untitled"),
            "authors": data.get("authors", []),
            "organizations": data.get("author_organizations", []),
            "date": data.get("date") or "",
            "fit": categories[0]["fit"],
            "importance": row["importance"],
            "summary": data.get("summary", ""),
            "needs_recategorization": needs_recategorization,
            "obsolete_llm_category": obsolete_llm,
            "category_count": len(category_ids),
        }
        if in_review_window(item, review_year):
            for category_id in category_ids:
                items_by_category[category_id].append(item)

    for category_id, items in items_by_category.items():
        if args.top or args.min_importance is not None:
            unscored = [item["url"] for item in items if item["importance"] is None]
            assert not unscored, f"--top / --min-importance need importance scores (run score_entries.py): {unscored}"
            # Importance is coarse (a few distinct values), so equal scores are ordered by category fit
            items.sort(key=lambda item: (item["importance"], item["fit"]), reverse=True)
            keep = len(items)
            if args.min_importance is not None:
                keep = sum(1 for item in items if item["importance"] >= args.min_importance)
            if args.top:
                keep = min(keep, args.top)
            counts["pruned"] += len(items) - keep
            del items[keep:]
        else:
            items.sort(key=lambda item: item["fit"], reverse=True)
    return items_by_category, counts


# ---------------------------------------------------------------- markdown


def is_printed(cat: Category, items_by_category: dict) -> bool:
    """Leaf categories are always printed; non-leaf ones only if some leaf below them has items."""
    return cat.is_leaf or any(leaf_id in items_by_category for leaf_id in cat.get_all_leaf_ids())


def render_taxonomy(taxonomy, items_by_category: dict) -> list[str]:
    """The taxonomy as a numbered outline linking to each category's section, with its one-line description."""
    lines = [f"# {taxonomy.year} Taxonomy", ""]

    def walk(categories: list[Category], prefix: str, depth: int) -> None:
        number = 0
        for cat in categories:
            if not is_printed(cat, items_by_category):
                continue
            number += 1
            label = f"{prefix}{number}"
            link = f"[{cat.name}](#{cat.id})"
            text = f"**{label}. {link}**" if depth == 0 else f"{label} {link}"
            lines.append(f"{'  ' * depth}- {text}: {cat.description.strip()}")
            walk(cat.children, f"{label}.", depth + 1)

    walk(taxonomy.taxonomy, "", 0)
    lines += ["", "---", ""]
    return lines


def render_header(args, sources: set[str], counts: dict, items_by_category: dict, year: int) -> list[str]:
    lines = [
        f"# AI Safety Shallow Review {year}",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}",
    ]
    if sources:
        lines.append(f"**Sources:** {', '.join(sorted(sources))}")
    if args.top or args.min_importance is not None:
        rule = [f"importance at least {args.min_importance}"] if args.min_importance is not None else []
        rule += [f"at most the {args.top} most important"] if args.top else []
        lines.append(f"**Kept per category:** {', '.join(rule)} ({counts['pruned']} pruned)")
    if args.respect_feedback:
        for key, label in [
            ("excluded", "Excluded by feedback"),
            ("reclassified", "Reclassified by feedback"),
            ("needs_recategorization", "⚠️ Needs recategorization (obsolete CSV category)"),
            ("obsolete_llm", "🔄 Re-classified (obsolete LLM category, one-time)"),
        ]:
            if counts[key] > 0:
                lines.append(f"**{label}:** {counts[key]}")
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


def render_item(item: dict, details: bool) -> str:
    """One list entry: - **[Title](url)**, *Authors*, Date; with details also the grey [markers fit, id] and Summary."""
    authors = ", ".join(item["authors"][:3]) + (" et al." if len(item["authors"]) > 3 else "")
    organizations = ", ".join(item["organizations"][:3])
    byline = f"*{authors}*" if authors else (f"*{organizations}*" if organizations else "")

    markers = ""
    if item["needs_recategorization"]:
        markers += "⚠️"
    if item["obsolete_llm_category"]:
        markers += "🔄"
    if item["category_count"] > 1:
        markers += f"✌️(in {item['category_count']} categories)"
    if markers:
        markers += " "
    importance = f'importance={item["importance"]:.2f}, ' if item["importance"] is not None else ""
    stats = f'<span style="{GREY}">[{markers}fit={item["fit"]:.2f}, {importance}id:{item["url_hash_short"]}]</span>'

    summary = item["summary"].replace("\n", " ").strip()

    parts = [f"**[{item['title']}]({item['url']})**", byline, item["date"]]
    if details:
        parts += [stats, f'<span style="{GREY}">Summary: {summary}</span>' if summary else ""]
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


def render_category(
    cat: Category, level: int, taxonomy, items_by_category: dict, lines: list[str], empty_fields: list[str], details: bool
) -> None:
    """Append the category's section and, recursively, its children's. Non-leaf categories without items are skipped."""
    if not is_printed(cat, items_by_category):
        return

    heading = "#" * (level + 1)
    lines.append(f'{heading} <span id="{cat.id}" style="font-size:{HEADING_SIZES[level]}">{cat.name}</span>\n')
    if cat.is_leaf:
        lines += render_agenda_fields(cat, taxonomy, empty_fields)
        items = items_by_category.get(cat.id, [])
        if items:
            lines += [render_item(item, details) for item in items]
            lines.append("")
    lines.append("\n---\n")
    if not cat.is_leaf:
        for child in cat.children:
            render_category(child, level + 1, taxonomy, items_by_category, lines, empty_fields, details)


# ---------------------------------------------------------------- main


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export the taxonomy with classified items as a markdown draft.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("-o", "--output", type=Path, help="Draft file to write (default: stdout, mixed with log lines)")
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
    parser.add_argument(
        "--details",
        action="store_true",
        help="Also print each item's grey fit score, id and summary (default: only title link, authors and date)",
    )
    parser.add_argument(
        "--top",
        type=int,
        help="Keep only each category's N most important items, most important first (needs score_entries.py)",
    )
    parser.add_argument(
        "--min-importance",
        type=float,
        help="Keep only items with at least this importance, most important first (needs score_entries.py); "
        "with --top, also at most N per category",
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
    sources = split_list(args.source)

    feedback_by_url = load_feedback(args.feedback_source) if args.respect_feedback else {}
    rows = query_rows(sources)
    if not rows and not feedback_by_url:
        err_console.print("[yellow]No items found matching filters[/yellow]")
        return

    items_by_category, counts = group_by_category(rows, feedback_by_url, args, taxonomy.year)

    lines = render_taxonomy(taxonomy, items_by_category) + render_header(args, sources, counts, items_by_category, taxonomy.year)
    empty_fields: list[str] = []  # "category_id: field", for --strict
    for top_category in taxonomy.taxonomy:
        render_category(top_category, 1, taxonomy, items_by_category, lines, empty_fields, args.details)

    if args.strict and empty_fields:
        err_console.print(f"[red]--strict: {len(empty_fields)} empty agenda fields, nothing written:[/red]")
        for entry in empty_fields:
            err_console.print(f"  {entry}")
        sys.exit(1)

    draft = "\n".join(lines) + "\n"
    # Every item is one list line that starts with its link, so count those lines
    links = sum(1 for line in lines if line.startswith("- **["))
    available = sum(len(items) for items in items_by_category.values())
    if args.output:
        args.output.write_text(draft)
        err_console.print(f"Wrote {args.output}")
    else:
        # Plain print, not the rich console, which would add formatting
        print(draft, end="")
    err_console.print(f"Added {links} links to the draft")
    if links < available:
        err_console.print(
            f"[yellow]{available - links} items were left out: their category is not in the taxonomy[/yellow]"
        )


if __name__ == "__main__":
    run(main)
