"""
Shared setup for the pipeline scripts: .env loading, logging and Ctrl+C handling.

Import this module before any `shallow_review` module so the API keys in .env are loaded first.
"""

import logging
import signal
import sys
from typing import Callable

from dotenv import load_dotenv

load_dotenv()

from shallow_review.common import request_shutdown  # noqa: E402
from shallow_review.utils import console, setup_logging  # noqa: E402

logger = logging.getLogger(__name__)


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
