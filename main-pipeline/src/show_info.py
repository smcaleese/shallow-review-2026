#!/usr/bin/env python3
"""
Show Pipeline Info
Prints the configured paths and, for the scrape and entries tables of data/data.db, the number of entries per
status and histograms of scores, token counts and durations, then the first rows of the entries table.

Basic usage (from the main-pipeline folder):
    uv run python src/show_info.py
    uv run python src/show_info.py --source facets-arxiv-2026 --rows 20
"""

import argparse
import json

from rich.table import Table

from terminal import console, run
from shallow_review import __version__
from shallow_review.common import DATA_PATH, PROMPTS_PATH, ROOT_PATH, RUNS_PATH
from shallow_review.data_db import data_db_locked
from shallow_review.utils import one_line_histogram


def print_histogram(label: str, values: list) -> None:
    if values:
        console.print(f"  [dim]{label:<25}[/dim] {one_line_histogram(values, bins=20, field_width=12)}")


def select(db, sql: str, source: str | None) -> list:
    """Run a query whose WHERE clause is already started; adds the source filter when there is one."""
    if source:
        return db.execute(sql + " AND source = ?", [source]).fetchall()
    return db.execute(sql).fetchall()


def json_values(rows: list, key: str) -> list:
    """Truthy values of `key` in the JSON `data` column of the rows."""
    values = (json.loads(row["data"]).get(key) for row in rows)
    return [v for v in values if v]


def print_status_table(db, table: str, error_columns: dict[str, str], source: str | None) -> None:
    """Counts per status of the entries table. error_columns maps a column title to a status."""
    columns = {"Total": None, "New": "new", "Done": "done", **error_columns}
    counts = []
    for status in columns.values():
        sql = f"SELECT COUNT(*) AS cnt FROM {table} WHERE 1=1"
        if status:
            sql += f" AND status = '{status}'"
        counts.append(str(select(db, sql, source)[0]["cnt"]))

    rich_table = Table(title=f"{table.capitalize()} Table", show_header=True, header_style="bold cyan")
    for title in columns:
        rich_table.add_column(title, justify="right")
    rich_table.add_row(*counts)
    console.print(rich_table)


def show_scrape_stats(db) -> None:
    def count(where: str) -> str:
        return str(db.execute(f"SELECT COUNT(*) AS cnt FROM scrape WHERE {where}").fetchone()["cnt"])

    table = Table(title="Scrape Table", show_header=True, header_style="bold cyan")
    for title in ["Total", "Success (2xx)", "Errors"]:
        table.add_column(title, justify="right")
    table.add_row(
        count("1=1"),
        count("status_code >= 200 AND status_code < 300"),
        count("error IS NOT NULL OR status_code >= 400"),
    )
    console.print(table)

    rows = db.execute(
        "SELECT data FROM scrape WHERE data IS NOT NULL AND status_code >= 200 AND status_code < 300"
    ).fetchall()
    for key, label in [
        ("size_full", "size_full (bytes)"),
        ("size_compressed", "size_compressed"),
        ("tokens_full", "tokens_full"),
        ("tokens_stripped", "tokens_stripped"),
        ("scrape_duration", "scrape_duration"),
    ]:
        print_histogram(label, json_values(rows, key))


def show_entries_stats(db, source: str | None) -> None:
    print_status_table(db, "entries", {"Scrape Errors": "scrape_error", "Classify Errors": "classify_error"}, source)

    for column in ["ai_safety_relevance", "shallow_review_inclusion"]:
        rows = select(db, f"SELECT {column} FROM entries WHERE {column} IS NOT NULL", source)
        print_histogram(column, [row[column] for row in rows])

    rows = select(db, "SELECT data FROM entries WHERE status = 'done' AND data IS NOT NULL", source)
    for key in ["tokens_full", "tokens_stripped", "classify_duration"]:
        print_histogram(key, json_values(rows, key))


def show_entry_rows(db, source: str | None, limit: int) -> None:
    """The first `limit` rows of the entries table, oldest first (the order classify_entries.py processes them)."""
    sql = "SELECT url, source, status, kind, ai_safety_relevance, shallow_review_inclusion, added_at FROM entries"
    params: list = []
    if source:
        sql += " WHERE source = ?"
        params.append(source)
    sql += " ORDER BY added_at, url LIMIT ?"
    rows = db.execute(sql, [*params, limit]).fetchall()

    table = Table(title=f"First {limit} rows of the entries table", show_header=True, header_style="bold cyan")
    table.add_column("URL", overflow="ellipsis", no_wrap=True, min_width=20, max_width=70)
    table.add_column("Source", overflow="ellipsis", no_wrap=True, min_width=8)
    table.add_column("Status", no_wrap=True, min_width=6)
    table.add_column("Kind", no_wrap=True, min_width=8)
    table.add_column("AI safety", justify="right", no_wrap=True, min_width=9)
    table.add_column("Inclusion", justify="right", no_wrap=True, min_width=9)
    table.add_column("Added", no_wrap=True, min_width=16)

    def score(value) -> str:
        return "" if value is None else f"{value:.2f}"

    for row in rows:
        table.add_row(
            row["url"],
            row["source"],
            row["status"],
            row["kind"] or "",
            score(row["ai_safety_relevance"]),
            score(row["shallow_review_inclusion"]),
            row["added_at"][:16],
        )
    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show configuration, paths and database statistics.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--source", help="Filter the entries statistics by source")
    parser.add_argument("--rows", type=int, default=10, help="Number of entries rows to list (default: 10)")
    args = parser.parse_args()

    console.print("[bold]Shallow Review Configuration[/bold]\n")
    console.print(f"Version: {__version__}")
    console.print(f"Root path: {ROOT_PATH}")
    console.print(f"Data path: {DATA_PATH}")
    console.print(f"Prompts path: {PROMPTS_PATH}")
    console.print(f"Runs path: {RUNS_PATH}")
    if args.source:
        console.print(f"[cyan]Filter: source = {args.source}[/cyan]")
    console.print()

    console.print("[bold]Database Statistics[/bold]\n")
    with data_db_locked() as db:
        show_scrape_stats(db)
        console.print()
        show_entries_stats(db, args.source)
        console.print()
        show_entry_rows(db, args.source, args.rows)


if __name__ == "__main__":
    run(main)
