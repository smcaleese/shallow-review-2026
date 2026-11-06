"""Shared types, constants, and global state for shallow-review pipeline."""

import threading
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field

# Paths - derived from package location, independent of pwd
ROOT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = ROOT_PATH / "data-2026-facets"
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


class EntryKind(str, Enum):
    """Content type of an entry (independent of AI safety/alignment relevancy).
    
    Note: All kinds can have any relevancy and inclusion scores. For example,
    a paper can have high safety relevance (0.9) but low inclusion (0.1) if not technical,
    or high relevance (0.9) and high inclusion (0.9) if presenting novel safety research.
    Use ai_safety_relevance and shallow_review_inclusion fields to determine scores.
    """

    # Research outputs
    PAPER_PUBLISHED = "paper_published"  # Peer-reviewed paper in journal/conference
    PAPER_PREPRINT = "paper_preprint"  # Preprint (arXiv, SSRN, etc.)
    BLOG_POST = "blog_post"  # Blog post or article (general blogs, personal blogs)
    LESSWRONG = "lesswrong"  # LessWrong or AI Alignment Forum post (special category)
    VIDEO = "video"  # Video, talk recording, lecture
    PODCAST = "podcast"  # Podcast episode or audio content
    CODE_TOOL = "code_tool"  # Software, library, tool, implementation
    DATASET_BENCHMARK = "dataset_benchmark"  # Dataset or benchmark release
    AGENDA_MANIFESTO = "agenda_manifesto"  # Research agenda, roadmap, manifesto
    NEWS_ANNOUNCEMENT = "news_announcement"  # News article or official announcement
    SOCIAL_MEDIA = "social_media"  # Social media post (strict criteria: major announcements only)
    COURSE_EDUCATIONAL = "course_educational"  # Course materials, tutorials, educational content
    # Non-research content
    COMMERCIAL = "commercial"  # Product/service pages, company pages
    PERSONAL_PAGE = "personal_page"  # Personal homepages, bios
    # Access issues
    BLOCKED = "blocked"  # Blocked access (captcha, login wall, paywall - content exists but inaccessible)
    ERROR_DETECTED = "error_detected"  # Content could not be accessed (429, 404, 5xx, format errors, etc.)
    OTHER = "other"  # Other content type


# Configuration objects
class RunClassifyConfig(BaseModel):
    """Configuration for classify phase runs."""

    model_config = {"frozen": True}

    limit: int = Field(default=100, ge=1, description="Max candidates to process")
    workers: int = Field(default=4, ge=1, le=128, description="Number of worker threads")
    model: str = Field(default="claude-sonnet-4", description="LLM model to use")
    max_html_tokens: int = Field(
        default=100000, ge=1000, description="Max tokens in HTML before error"
    )


# Common base models (extend as needed)
class Item(BaseModel):
    """Base item type for pipeline objects."""

    id: str
    url: str


