#!/usr/bin/env python3
"""
Import Human Feedback
Records human decisions from a CSV (include, exclude, reclassify) in the feedback table of data/data.db.
export_draft.py applies them on top of the LLM's output.

Basic usage (from the main-pipeline folder):
    uv run python src/import_feedback.py feedback.csv --source SR2025-WIP-doc
The CSV has the columns URL,CATEGORY_ID,PAPER_ID,LINK_TEXT.
"""

import argparse
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from terminal import console, run
from shallow_review.feedback import get_action_counts, import_feedback_from_csv

MAX_DUPLICATES_SHOWN = 10


def print_duplicates(duplicates: list[dict]) -> None:
    """Show the entries that the unique indexes rejected, grouped by action."""
    by_action = defaultdict(list)
    for dup in duplicates:
        by_action[dup["action"]].append(dup)

    console.print("\n[yellow]Duplicate entries (caught by unique indexes):[/yellow]")
    for action, dups in sorted(by_action.items()):
        console.print(f"\n  [cyan]{action}[/cyan] ({len(dups)} duplicates):")
        for dup in dups[:MAX_DUPLICATES_SHOWN]:
            category = f" → {dup['category']}" if dup["category"] else ""
            console.print(f"    - {dup['url'][:70]}{category}")
        if len(dups) > MAX_DUPLICATES_SHOWN:
            console.print(f"    ... and {len(dups) - MAX_DUPLICATES_SHOWN} more")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Import human feedback from a CSV file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("csv_file", type=Path, help="CSV file with URL,CATEGORY_ID,PAPER_ID,LINK_TEXT")
    parser.add_argument("--source", default="manual", help="Feedback source label (default: manual)")
    parser.add_argument(
        "--detect-exclusions",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Detect excluded papers by comparing with exportable items (default: on)",
    )
    parser.add_argument(
        "--min-shallow-review",
        type=float,
        default=0.4,
        help="Threshold for 'exportable' items when detecting exclusions (default: 0.4)",
    )
    parser.add_argument(
        "--reclassify-obsolete-llm",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="ONE-TIME: reset papers with obsolete LLM categories to 'new' instead of excluding them",
    )
    args = parser.parse_args()

    if not args.csv_file.exists():
        console.print(f"[red]Error: CSV file not found: {args.csv_file}[/red]")
        sys.exit(1)

    console.print(f"[bold]Importing feedback from {args.csv_file.name}[/bold]")
    console.print(f"Source: {args.source}")
    console.print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    console.print()

    stats = import_feedback_from_csv(
        csv_path=args.csv_file,
        source=args.source,
        detect_exclusions=args.detect_exclusions,
        min_shallow_review=args.min_shallow_review,
        reclassify_obsolete_llm=args.reclassify_obsolete_llm,
    )

    console.print(f"Parsed {stats.urls_parsed} unique URLs from CSV ({stats.urls_skipped} skipped)")
    if stats.obsolete_csv_categories > 0:
        console.print(
            f"[yellow]⚠ Found {stats.obsolete_csv_categories} papers with obsolete category IDs "
            "(marked for recategorization)[/yellow]"
        )
    console.print()
    console.print(f"Added {stats.added_to_classify} new URLs to entries table")
    console.print()

    if args.detect_exclusions:
        console.print(f"Found {stats.excluded_count + stats.obsolete_llm_count} papers not in CSV:")
        console.print(f"  - Excluding: {stats.excluded_count}")
        if args.reclassify_obsolete_llm and stats.obsolete_llm_count > 0:
            console.print(f"  - Marked for re-classification (obsolete LLM category): {stats.obsolete_llm_count}")
            console.print(f"    Reset {stats.obsolete_llm_count} papers to status='new' for re-classification")
        console.print()

    console.print(f"[green]✓ Inserted {stats.feedback_inserted} feedback entries[/green]")
    if stats.feedback_duplicates > 0:
        console.print(f"[yellow]! Skipped {stats.feedback_duplicates} duplicate entries[/yellow]")
        if stats.duplicates_list:
            print_duplicates(stats.duplicates_list)

    console.print()
    console.print(f"[bold]Feedback summary for source '{args.source}':[/bold]")
    for action, count in sorted(get_action_counts(args.source).items()):
        console.print(f"  {action:<15} {count:>5}")


if __name__ == "__main__":
    run(main)
