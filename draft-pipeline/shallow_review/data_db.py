"""Unified database module for all pipeline tables.

All data stored in a single SQLite database: data/data.db

Tables:
- entries: One row per URL: status, source label and the classification result
- feedback: Human decisions (include / exclude / reclassify) per URL
"""

import json
import logging
import sqlite3
import threading
from contextlib import contextmanager

from .common import DATA_PATH

logger = logging.getLogger(__name__)

# Global database connection (lazy singleton)
_data_db: sqlite3.Connection | None = None
_data_db_init_lock = threading.Lock()

# Global database operation lock
# Use with data_db_locked() context manager for thread-safe operations
_data_db_op_lock = threading.Lock()


def _rename_old_tables(data_db: sqlite3.Connection) -> None:
    """Databases made before the rename have `classify` and `classify_feedback` tables; rename them in place."""
    tables = {row[0] for row in data_db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    if "classify" in tables and "entries" not in tables:
        old_indexes = data_db.execute(
            "SELECT name FROM sqlite_master WHERE type = 'index' AND name LIKE 'idx_classify_%'"
        ).fetchall()
        for (name,) in old_indexes:
            data_db.execute(f"DROP INDEX {name}")  # Recreated below as idx_entries_*
        data_db.execute("ALTER TABLE classify RENAME TO entries")
        logger.info("Renamed table classify -> entries")
    if "classify_feedback" in tables and "feedback" not in tables:
        data_db.execute("ALTER TABLE classify_feedback RENAME TO feedback")
        logger.info("Renamed table classify_feedback -> feedback")


# Old name -> new name of columns of `entries`
RENAMED_COLUMNS = {"data": "classifier_output", "processed_at": "classified_at", "error": "classify_error_message"}


def _rename_old_columns(data_db: sqlite3.Connection) -> None:
    """Databases made before the column renames get them renamed in place, and the fit scores in the classifier
    output's categories renamed from `score` to `fit`."""
    existing = {row[1] for row in data_db.execute("PRAGMA table_info(entries)")}
    for old, new in RENAMED_COLUMNS.items():
        if old in existing and new not in existing:
            data_db.execute(f"ALTER TABLE entries RENAME COLUMN {old} TO {new}")
            logger.info(f"Renamed column entries.{old} -> {new}")
    if "classifier_output" not in existing and "data" not in existing:
        return  # New database
    rows = data_db.execute(
        "SELECT url, classifier_output FROM entries WHERE classifier_output LIKE '%\"score\"%'"
    ).fetchall()
    renamed = 0
    for url, output_json in rows:
        output = json.loads(output_json)
        categories = output.get("categories") or []
        if not any("score" in category for category in categories):
            continue  # "score" appears elsewhere in the JSON
        output["categories"] = [
            {("fit" if key == "score" else key): value for key, value in category.items()} for category in categories
        ]
        data_db.execute("UPDATE entries SET classifier_output = ? WHERE url = ?", (json.dumps(output), url))
        renamed += 1
    if renamed:
        logger.info(f"Renamed categories[].score -> fit in the classifier output of {renamed} entries")


def _add_missing_columns(data_db: sqlite3.Connection) -> None:
    """Databases made before score_entries.py lack its columns of `entries`; add them in place."""
    existing = {row[1] for row in data_db.execute("PRAGMA table_info(entries)")}
    columns = [
        ("citation_count", "INTEGER"),
        ("lw_karma", "INTEGER"),
        ("attention_checked_at", "TEXT"),
        ("importance", "REAL"),
        ("importance_reason", "TEXT"),
    ]
    for column, sql_type in columns:
        if column not in existing:
            data_db.execute(f"ALTER TABLE entries ADD COLUMN {column} {sql_type}")
            logger.info(f"Added column entries.{column}")


def _create_tables(data_db: sqlite3.Connection, db_path: str) -> None:
    """Create all tables and indexes in the data database."""
    _rename_old_tables(data_db)
    _rename_old_columns(data_db)
    statements = [
        # Entries table
        """CREATE TABLE IF NOT EXISTS entries (
            url TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            source TEXT NOT NULL,
            added_at TEXT NOT NULL,
            classified_at TEXT,
            classifier_output JSON,
            classify_error_message TEXT,
            citation_count INTEGER,
            lw_karma INTEGER,
            attention_checked_at TEXT,
            importance REAL,
            importance_reason TEXT,
            CHECK(status IN ('new', 'scrape_error', 'classify_error', 'done'))
        )""",
        "CREATE INDEX IF NOT EXISTS idx_entries_status ON entries(status)",
        "CREATE INDEX IF NOT EXISTS idx_entries_source ON entries(source)",
        "CREATE INDEX IF NOT EXISTS idx_entries_added_at ON entries(added_at)",
        # Feedback table
        """CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            feedback_source TEXT NOT NULL,
            feedback_timestamp TEXT NOT NULL,
            action TEXT NOT NULL,
            human_category TEXT,
            paper_id TEXT,
            link_text TEXT,
            notes TEXT,
            CHECK(action IN ('include', 'exclude', 'reclassify', 'note'))
        )""",
        "CREATE INDEX IF NOT EXISTS idx_feedback_url ON feedback(url)",
        "CREATE INDEX IF NOT EXISTS idx_feedback_action ON feedback(action)",
        "CREATE INDEX IF NOT EXISTS idx_feedback_human_category ON feedback(human_category)",
        "CREATE INDEX IF NOT EXISTS idx_feedback_source ON feedback(feedback_source)",
        """CREATE UNIQUE INDEX IF NOT EXISTS idx_feedback_unique_single_action 
           ON feedback(url, feedback_source, action, feedback_timestamp) 
           WHERE action IN ('include', 'exclude', 'note')""",
        """CREATE UNIQUE INDEX IF NOT EXISTS idx_feedback_unique_reclassify 
           ON feedback(url, feedback_source, action, human_category, feedback_timestamp) 
           WHERE action = 'reclassify'""",
    ]

    for statement in statements:
        data_db.execute(statement)
    _add_missing_columns(data_db)
    data_db.execute("CREATE INDEX IF NOT EXISTS idx_entries_importance ON entries(importance)")

    data_db.commit()
    logger.info(f"Initialized unified database at {db_path}")


def get_data_db() -> sqlite3.Connection:
    """
    Get or create the unified data database connection (lazy singleton).
    
    DEPRECATED: Use data_db_locked() context manager instead for thread-safety.

    Creates all tables and indexes if they don't exist.
    Uses WAL mode for better concurrency.

    Returns:
        SQLite connection to data/data.db
    """
    global _data_db

    with _data_db_init_lock:
        if _data_db is None:
            db_path = DATA_PATH / "data.db"
            data_db = sqlite3.connect(
                str(db_path),
                check_same_thread=False,
                timeout=30.0,  # Wait up to 30 seconds for locks
                isolation_level=None,  # Autocommit mode (no transactions by default)
            )
            data_db.row_factory = sqlite3.Row
            
            # Enable WAL mode for better concurrency
            # WAL allows concurrent reads and one writer
            data_db.execute("PRAGMA journal_mode=WAL")
            data_db.execute("PRAGMA synchronous=NORMAL")  # Faster with WAL
            
            _create_tables(data_db, str(db_path))
            _data_db = data_db
        return _data_db


@contextmanager
def data_db_locked():
    """
    Context manager for thread-safe database operations.
    
    Acquires lock, yields database connection, releases lock on exit.
    Use for all database operations in multi-threaded code.
    
    Example:
        with data_db_locked() as db:
            cursor = db.execute("SELECT * FROM entries WHERE url = ?", (url,))
            row = cursor.fetchone()
            db.execute("INSERT INTO entries ...", (...))
            
    Note: Keep operations inside the context minimal. Don't hold lock
    while doing expensive operations like scraping or LLM calls.
    
    Yields:
        SQLite connection with lock held
    """
    # Ensure DB is initialized
    db = get_data_db()
    
    # Acquire lock for thread-safe operations
    with _data_db_op_lock:
        yield db

