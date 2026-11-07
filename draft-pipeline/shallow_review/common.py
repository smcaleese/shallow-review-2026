"""Shared types, constants, and global state for shallow-review pipeline."""

import threading
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field

# Paths - derived from package location, independent of pwd
ROOT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = ROOT_PATH / "data"
PROMPTS_PATH = ROOT_PATH / "prompts"
RUNS_PATH = ROOT_PATH / "runs"
SCRAPED_PATH = DATA_PATH / "scraped"

# Ensure directories exist
DATA_PATH.mkdir(exist_ok=True, parents=True)
RUNS_PATH.mkdir(exist_ok=True, parents=True)
SCRAPED_PATH.mkdir(exist_ok=True, parents=True)

# Global shutdown flag for graceful termination
_shutdown_event = threading.Event()


def is_shutdown_requested() -> bool:
    """Check if shutdown has been requested."""
    return _shutdown_event.is_set()


def request_shutdown() -> None:
    """Request shutdown of all threads."""
    _shutdown_event.set()


# Enums
class EntryStatus(str, Enum):
    """Processing status of an entry."""

    NEW = "new"  # Not yet processed
    SCRAPE_ERROR = "scrape_error"  # Failed to scrape
    CLASSIFY_ERROR = "classify_error"  # LLM classification failed
    DONE = "done"  # Successfully completed


# Configuration objects
class RunClassifyConfig(BaseModel):
    """Configuration for classify phase runs."""

    model_config = {"frozen": True}

    limit: int = Field(default=100, ge=1, description="Max candidates to process")
    workers: int = Field(default=4, ge=1, le=128, description="Number of worker threads")
    model: str = Field(default="claude-sonnet-5-5", description="LLM model to use")
    max_html_tokens: int = Field(
        default=100000, ge=1000, description="Max tokens in HTML before error"
    )


# Common base models (extend as needed)
class Item(BaseModel):
    """Base item type for pipeline objects."""

    id: str
    url: str


