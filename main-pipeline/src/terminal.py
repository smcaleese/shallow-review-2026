"""
Shared setup for the pipeline scripts: .env loading, logging, Ctrl+C handling and a parallel-run helper.

Import this module before any `shallow_review` module so the API keys in .env are loaded first.
"""

import logging
import signal
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterable, TypeVar

from dotenv import load_dotenv

load_dotenv()

from shallow_review.common import is_shutdown_requested, request_shutdown  # noqa: E402
from shallow_review.utils import console, setup_logging  # noqa: E402

logger = logging.getLogger(__name__)

Item = TypeVar("Item")
Result = TypeVar("Result")

WORKERS_HELP = "Number of worker threads (safe with Selenium, use 1 with Playwright)"


def _on_interrupt(signum, frame) -> None:
    """Ask the worker threads to stop once their current item is done."""
    console.print("\n[yellow]⚠ Received interrupt signal, shutting down gracefully...[/yellow]")
    request_shutdown()


def run(main: Callable[[], None]) -> None:
    """Run a script's main(): set up logging (runs/<date>_<pid>.log) and graceful Ctrl+C, report fatal errors."""
    signal.signal(signal.SIGINT, _on_interrupt)
    signal.signal(signal.SIGTERM, _on_interrupt)
    setup_logging()
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        logger.exception("Fatal error")
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


def scrape_backend(workers: int) -> str:
    """Name of the scraping backend; warns when several workers are used with Playwright."""
    from shallow_review.scrape import USE_SELENIUM

    if workers > 1 and not USE_SELENIUM:
        console.print(
            "[yellow]⚠ WARNING: Playwright backend with workers > 1 may cause errors. "
            "Switch USE_SELENIUM=True in shallow_review/scrape.py.[/yellow]"
        )
    return "selenium" if USE_SELENIUM else "playwright"


def run_parallel(
    items: Iterable[Item],
    work: Callable[[Item], Result],
    workers: int,
    on_done: Callable[[int, Item, Result], None],
    on_error: Callable[[int, Item, Exception], None],
) -> None:
    """
    Call work(item) for every item in a thread pool and report each finished item, numbered from 1.

    on_done(n, item, result) or on_error(n, item, exception) is called as each item completes. Cancels the
    remaining items once a shutdown has been requested (Ctrl+C).
    """
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(work, item): item for item in items}
        for n, future in enumerate(as_completed(futures), 1):
            if is_shutdown_requested():
                console.print("\n[yellow]Shutdown requested, stopping...[/yellow]")
                executor.shutdown(wait=False, cancel_futures=True)
                break
            item = futures[future]
            try:
                result = future.result()
            except Exception as e:
                on_error(n, item, e)
            else:
                on_done(n, item, result)
