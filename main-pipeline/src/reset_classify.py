#!/usr/bin/env python3
"""
Reset Classify Queue
Puts matching entries back to status 'new' so that classify_entries.py processes them again, optionally
deleting their cached scrapes. With no filters every entry is reset.

Basic usage (from the main-pipeline folder):
    uv run python src/reset_classify.py --source arxiv-2026 --remove-scrapes
"""

import argparse

from terminal import console, run
from shallow_review.common import SCRAPED_PATH, EntryStatus
from shallow_review.data_db import data_db_locked
from shallow_review.scrape import get_scrape_path
from shallow_review.utils import url_hash


def delete_scrapes(urls: list[str]) -> int:
    """Delete the scrape rows and cached files of the URLs. Returns the number of rows deleted."""
    with data_db_locked() as db:
        placeholders = ",".join("?" * len(urls))
        cursor = db.execute(f"DELETE FROM scrape WHERE url IN ({placeholders})", urls)
        rows_deleted = cursor.rowcount
        db.commit()
    console.print(f"[green]✓ Deleted {rows_deleted} scrape table rows[/green]")

    files_deleted = 0
    stripped_deleted = 0
    for url in urls:
        scrape_path = get_scrape_path(url)
        if scrape_path.exists():
            scrape_path.unlink()
            files_deleted += 1
        # Stripped HTML file, saved when SAVE_STRIPPED_HTML is enabled
        stripped_path = SCRAPED_PATH / f"{url_hash(url)}-stripped.html"
        if stripped_path.exists():
            stripped_path.unlink()
            stripped_deleted += 1
    if files_deleted:
        console.print(f"[green]✓ Deleted {files_deleted} scrape files[/green]")
    if stripped_deleted:
        console.print(f"[green]✓ Deleted {stripped_deleted} stripped HTML files[/green]")
    return rows_deleted


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reset entries to 'new' so they are classified again.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--kind", help="Only entries of this kind")
    parser.add_argument("--source", help="Only entries from this source")
    parser.add_argument("--status", help="Only entries with this current status")
    parser.add_argument("--remove-scrapes", action="store_true", help="Also delete scrapes for matching URLs")
    args = parser.parse_args()

    conditions = []
    params = []
    for column, value in [("kind", args.kind), ("source", args.source), ("status", args.status)]:
        if value:
            conditions.append(f"{column} = ?")
            params.append(value)
    where = " WHERE " + " AND ".join(conditions) if conditions else ""

    with data_db_locked() as db:
        rows = db.execute(f"SELECT url, status FROM entries{where}", params).fetchall()
    if not rows:
        console.print("[yellow]No matching entries found[/yellow]")
        return

    already_new = sum(1 for row in rows if row["status"] == EntryStatus.NEW.value)
    to_change = len(rows) - already_new
    console.print(f"[bold]Found {len(rows)} matching entries[/bold]")
    if to_change == 0:
        console.print("[yellow]All entries are already 'new', nothing to change[/yellow]")
        if not args.remove_scrapes:
            return
    else:
        console.print(f"  - {already_new} already 'new'")
        console.print(f"  - {to_change} will be reset to 'new'")
    console.print()

    if to_change > 0:
        with data_db_locked() as db:
            db.execute(
                f"UPDATE entries SET status = ?{where or ' WHERE 1=1'} AND status != ?",
                [EntryStatus.NEW.value, *params, EntryStatus.NEW.value],
            )
            db.commit()
        console.print(f"[green]✓ Reset {to_change} entries to 'new'[/green]")

    scrapes_deleted = delete_scrapes([row["url"] for row in rows]) if args.remove_scrapes else 0

    console.print()
    console.print("[bold]Summary:[/bold]")
    console.print(f"  Total affected: {len(rows)}")
    console.print(f"  Changed to 'new': {to_change}")
    if args.remove_scrapes:
        console.print(f"  Scrapes deleted: {scrapes_deleted}")


if __name__ == "__main__":
    run(main)
