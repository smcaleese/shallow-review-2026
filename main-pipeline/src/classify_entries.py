#!/usr/bin/env python3
"""
Classify Queued URLs
Scrapes each queued URL (cached in data/scraped/) and sends the page to the LLM with the whole taxonomy in the system
prompt. The LLM returns relevance scores, a kind, 1-3 leaf categories and metadata, which are saved in data/data.db.

Basic usage (from the main-pipeline folder):
    uv run python src/classify_entries.py --limit 500 --workers 4
Only entries with status 'new' are processed; add --retry-errors to include 'classify_error' entries too.
"""

import argparse
import logging

from terminal import WORKERS_HELP, console, run, run_parallel, scrape_backend
from shallow_review.classify import compute_classify
from shallow_review.common import EntryStatus, RunClassifyConfig
from shallow_review.data_db import data_db_locked
from shallow_review.stats import stats_context

logger = logging.getLogger(__name__)


def select_candidates(limit: int, retry_errors: bool) -> list[str]:
    """URLs waiting to be classified, oldest first."""
    statuses = [EntryStatus.NEW.value]
    if retry_errors:
        statuses.append(EntryStatus.CLASSIFY_ERROR.value)
    placeholders = ",".join("?" * len(statuses))
    with data_db_locked() as db:
        rows = db.execute(
            f"""
            SELECT url FROM entries
            WHERE status IN ({placeholders})
            ORDER BY added_at
            LIMIT ?
            """,
            (*statuses, limit),
        ).fetchall()
    return [row["url"] for row in rows]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape and classify queued URLs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--limit", type=int, default=100, help="Maximum candidates to process (default: 100)")
    parser.add_argument("--workers", type=int, default=1, help=WORKERS_HELP)
    parser.add_argument("--model", default="anthropic/claude-sonnet-5-5", help="LLM model to use")
    parser.add_argument("--max-tokens", type=int, default=100000, help="Max HTML tokens before error")
    parser.add_argument(
        "--retry-errors", action="store_true", help="Retry candidates with classify_error status"
    )
    args = parser.parse_args()

    config = RunClassifyConfig(
        limit=args.limit,
        workers=args.workers,
        model=args.model,
        max_html_tokens=args.max_tokens,
    )

    console.print("[bold]Starting classification phase...[/bold]\n")
    backend = scrape_backend(args.workers)
    console.print(f"Config: limit={args.limit}, workers={args.workers}, model={args.model}, backend={backend}")
    if args.retry_errors:
        console.print("[yellow]Retry mode: Will retry candidates with classify_error status[/yellow]")
    console.print()

    candidates = select_candidates(args.limit, args.retry_errors)
    if not candidates:
        console.print("[yellow]No candidates to process[/yellow]")
        return
    console.print(f"Found {len(candidates)} candidates to process\n")

    def on_done(n: int, url: str, result) -> None:
        top_category = result.categories[0].id if result.categories else "none"
        console.print(
            f"[{n}/{len(candidates)}] [green]✓[/green] {url[:60]}: "
            f"safety={result.ai_safety_relevance:.2f}, "
            f"incl={result.shallow_review_inclusion:.2f}, "
            f"cat={top_category}, "
            f"conf={result.confidence:.2f}"
        )

    def on_error(n: int, url: str, error: Exception) -> None:
        logger.error(f"Failed to classify {url}: {error}", exc_info=error)
        console.print(f"[{n}/{len(candidates)}] [red]✗[/red] {url[:60]}: {str(error)[:60]}")

    with stats_context(commandline=f"classify_entries --limit {args.limit}") as stats:
        run_parallel(
            candidates,
            lambda url: compute_classify(url, config, args.retry_errors),
            args.workers,
            on_done,
            on_error,
        )
        console.print()
        stats.print_summary()


if __name__ == "__main__":
    run(main)
