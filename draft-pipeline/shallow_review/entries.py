"""Entries: the URLs the pipeline processes, one row each in the `entries` table."""

import logging
import sqlite3
from datetime import datetime, timezone

from .common import EntryStatus
from .data_db import data_db_locked
from .stats import get_stats
from .utils import normalize_url

logger = logging.getLogger(__name__)


def add_entry(url: str, source: str) -> bool:
    """
    Add a URL to the entries table with status 'new', ready for classification.

    Args:
        url: URL to add (will be normalized)
        source: Source label, e.g. "facets-arxiv-2026"

    Returns:
        True if added (new), False if already exists
    """
    url = normalize_url(url)
    timestamp = datetime.now(timezone.utc).isoformat()

    try:
        with data_db_locked() as db:
            db.execute(
                """
                INSERT INTO entries
                (url, status, source, added_at)
                VALUES (?, ?, ?, ?)
                """,
                (url, EntryStatus.NEW.value, source, timestamp),
            )
    except sqlite3.IntegrityError:
        # URL already exists
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates_already_exist += 1
        except RuntimeError:
            pass
        logger.debug(f"Entry already exists: {url}")
        return False

    try:
        stats = get_stats()
        with stats.lock:
            stats.classify_candidates.new.add(url)
    except RuntimeError:
        pass
    logger.info(f"Added entry: {url}")
    return True
