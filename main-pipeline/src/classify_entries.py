#!/usr/bin/env python3
"""
Classify Queued URLs
Scrapes each queued URL (cached in data/scraped/) and sends the page to the LLM with the whole taxonomy. The LLM returns 1-3 leaf categories with fit scores and basic metadata (title, authors, date, summary), which are saved in data/data.db.

Basic usage (from the main-pipeline folder):
    uv run python src/classify_entries.py --limit 500 --workers 4
Only entries with status 'new' are processed; add --retry-errors to include 'classify_error' entries too.
"""

import argparse
import json
import logging
from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import TypeVar

import yaml
from pydantic import BaseModel, Field

from shallow_review.common import (
    PROMPTS_PATH,
    EntryStatus,
    RunClassifyConfig,
    is_shutdown_requested,
)
from shallow_review.data_db import data_db_locked
from shallow_review.llm import get_completion
from shallow_review.scrape import compute_scrape, open_scraped
from shallow_review.stats import get_stats, stats_context
from shallow_review.taxonomy import format_taxonomy_for_prompt, load_taxonomy
from shallow_review.utils import format_error
from terminal import console, run

logger = logging.getLogger(__name__)


# Pydantic models for LLM responses
class CategoryAssignment(BaseModel):
    """A category assignment with score."""

    id: str = Field(description="Leaf category ID from taxonomy")
    score: float = Field(ge=0.0, le=1.0, description="Fit score for this category")


class ClassificationResult(BaseModel):
    """What the LLM returns for a page: its basic metadata and the categories it belongs to."""

    content_available: bool  # False if the page is an error page, a paywall, empty, ...
    title: str
    authors: list[str]
    author_organizations: list[str]
    date: str | None = None  # YYYY-MM-DD, or YYYY-MM or YYYY
    summary: str
    categories: list[CategoryAssignment] = Field(max_length=3)  # Best fit first
    tokens_full: int | None = None  # Full HTML token count (set by the script)
    tokens_stripped: int | None = None  # Stripped HTML token count (set by the script)


def compute_classify(url: str, config: RunClassifyConfig, force_recompute: bool = False) -> ClassificationResult:
    """
    Classify a URL and extract metadata.

    Workflow:
    1. Scrape the page
    2. Preprocess HTML (strip scripts/styles/base64)
    3. Check token limit
    4. Load taxonomy and format for prompt
    5. Run LLM classification
    6. Store results in database

    Args:
        url: URL to classify
        config: Configuration for classification run
        force_recompute: If True, re-run classification even if status is classify_error

    Returns:
        ClassificationResult with extracted metadata

    Raises:
        RuntimeError: If scraping, preprocessing, or classification fails
    """
    import time

    classify_start = time.time()

    # Check if already processed
    with data_db_locked() as db:
        cursor = db.execute("SELECT status FROM entries WHERE url = ?", (url,))
        row = cursor.fetchone()

        if row and row["status"] != EntryStatus.NEW.value:
            # Allow retrying classify_error with force_recompute
            if force_recompute and row["status"] == EntryStatus.CLASSIFY_ERROR.value:
                logger.info(f"Retrying classification for {url} (was classify_error)")
                db.execute(
                    "UPDATE entries SET status = ? WHERE url = ?",
                    (EntryStatus.NEW.value, url),
                )
            elif row["status"] == EntryStatus.DONE.value:
                logger.warning(f"URL {url} already classified successfully")
                # Return cached result
                cursor = db.execute("SELECT data FROM entries WHERE url = ?", (url,))
                data_row = cursor.fetchone()
                if data_row and data_row["data"]:
                    data = json.loads(data_row["data"])
                    return ClassificationResult(**data)
                raise RuntimeError(f"URL {url} marked done but no data found")
            else:
                raise RuntimeError(f"URL {url} in status {row['status']}, use --retry-errors for classify_error")

    timestamp = datetime.now(timezone.utc).isoformat()

    # Step 1: Scrape the page
    try:
        compute_scrape(url, headless=True)
    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to scrape {url}: {error_msg}")
        with data_db_locked() as db:
            db.execute(
                """
                UPDATE entries
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (EntryStatus.SCRAPE_ERROR.value, timestamp, error_msg, url),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"Scrape error: {e}") from e

    # Step 2: Read and preprocess HTML (use stripped version)
    try:
        with open_scraped(url, "rt", encoding="utf-8") as f:
            raw_html = f.read()

        cleaned_html, preprocessing_stats = preprocess_html(raw_html, config.model)

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to preprocess HTML for {url}: {error_msg}")
        with data_db_locked() as db:
            db.execute(
                """
                UPDATE entries
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (EntryStatus.CLASSIFY_ERROR.value, timestamp, error_msg, url),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"Preprocessing error: {e}") from e

    # Step 3: Check token limit
    tokens_after = preprocessing_stats["tokens_after"]
    if tokens_after > config.max_html_tokens:
        error_msg = (
            f"HTML exceeds max_html_tokens limit: {tokens_after} > {config.max_html_tokens}"
        )
        logger.error(f"{error_msg} for {url}")

        db.execute(
            """
            UPDATE entries
            SET status = ?, processed_at = ?, error = ?
            WHERE url = ?
            """,
            (
                EntryStatus.CLASSIFY_ERROR.value,
                timestamp,
                error_msg,
                url,
            ),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(error_msg)

    # Step 4: Load taxonomy and format for prompt
    try:
        taxonomy = load_taxonomy()
        taxonomy_text = format_taxonomy_for_prompt(taxonomy)
    except Exception as e:
        error_msg = f"Failed to load taxonomy: {format_error(e, levels=2)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg) from e

    # Step 5: Run LLM classification
    try:
        # Load prompts
        prompts_file = PROMPTS_PATH / "classify.yaml"
        with open(prompts_file) as f:
            prompts = yaml.safe_load(f)

        # Prepare template variables
        template_vars = {
            "url": url,
            "content": cleaned_html,
            "taxonomy": taxonomy_text,
        }

        # Call LLM with 1-hour cache for system prompt (taxonomy changes infrequently)
        result = get_completion(
            template_vars=template_vars,
            model=config.model,
            stats_subtree="classify_tokens",
            response_type=ClassificationResult,
            system_prompt_template=prompts["classify_content"]["system"],
            user_prompt_template=prompts["classify_content"]["user"],
            system_cache_ttl="1h",  # Cache system prompt (with taxonomy) for 1 hour
            effort="medium",
            max_tokens=16000,
        )

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed LLM classification for {url}: {error_msg}")
        with data_db_locked() as db:

            db.execute(
            """
            UPDATE entries
            SET status = ?, processed_at = ?, error = ?
            WHERE url = ?
            """,
            (
                EntryStatus.CLASSIFY_ERROR.value,
                timestamp,
                error_msg,
                url,
            ),
        )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"LLM classification error: {e}") from e

    # Step 7: Add preprocessing stats and timing to result
    classify_duration = time.time() - classify_start
    result.tokens_full = preprocessing_stats["tokens_before"]
    result.tokens_stripped = preprocessing_stats["tokens_after"]

    # Step 8: Fail pages that are not the content (error page, paywall, ...), then validate categories against taxonomy
    if not result.content_available or not result.categories:
        error_msg = "The page has no readable content (error page, paywall or empty)"
        logger.error(f"{error_msg}: {url}")
        with data_db_locked() as db:
            db.execute(
                "UPDATE entries SET status = ?, processed_at = ?, error = ? WHERE url = ?",
                (EntryStatus.CLASSIFY_ERROR.value, timestamp, error_msg, url),
            )
        raise RuntimeError(error_msg)

    valid_leaf_ids = set(taxonomy.get_all_leaf_ids())
    for cat in result.categories:
        if cat.id not in valid_leaf_ids:
            error_msg = f"Invalid category ID: {cat.id} (not a valid leaf category)"
            logger.error(error_msg)
            with data_db_locked() as db:
                db.execute(
                    """
                    UPDATE entries
                    SET status = ?, processed_at = ?, error = ?
                    WHERE url = ?
                    """,
                    (EntryStatus.CLASSIFY_ERROR.value, timestamp, error_msg, url),
                )
            raise RuntimeError(error_msg)

    # Step 9: Update database with results
    # Best-fitting category first: the draft files each item under its first category only
    result.categories.sort(key=lambda c: c.score, reverse=True)
    data_dict = result.model_dump()
    data_dict["classify_duration"] = round(classify_duration, 2)
    data_json = json.dumps(data_dict)

    # Extract top category for indexed column
    top_category_id = result.categories[0].id if result.categories else None

    with data_db_locked() as db:
        db.execute(
            """
            UPDATE entries
            SET status = ?, processed_at = ?, data = ?
            WHERE url = ?
            """,
            (EntryStatus.DONE.value, timestamp, data_json, url),
        )

    # Update stats
    try:
        stats = get_stats()
        with stats.lock:
            stats.classify_candidates.cached.add(url)
            # Track preprocessing stats
            stats.classify_preprocessing.append(preprocessing_stats)
    except RuntimeError:
        pass

    logger.info(
        f"Successfully classified {url} "
        f"(top category: {top_category_id}, score: {result.categories[0].score:.2f})"
    )

    return result


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


# Token counting - use tiktoken for approximation
try:
    import tiktoken

    _tiktoken_available = True
except ImportError:
    _tiktoken_available = False


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Count approximate tokens in text for a given model.

    Uses tiktoken for accurate counting. Falls back to character-based estimate
    if tiktoken is not available.

    Args:
        text: Text to count tokens for
        model: Model name (e.g., "gpt-4", "claude-sonnet-4")

    Returns:
        Approximate token count
    """
    if not _tiktoken_available:
        # Fallback: rough estimate (1 token ≈ 4 characters for English)
        return len(text) // 4

    # Map model names to tiktoken encodings
    # Claude models use similar tokenization to GPT-4
    if "claude" in model.lower() or "sonnet" in model.lower():
        encoding_name = "cl100k_base"  # GPT-4/Claude approximation
    elif "gpt-4" in model.lower():
        encoding_name = "cl100k_base"
    elif "gpt-3.5" in model.lower():
        encoding_name = "cl100k_base"
    else:
        # Default to GPT-4 encoding
        encoding_name = "cl100k_base"

    try:
        encoding = tiktoken.get_encoding(encoding_name)
        return len(encoding.encode(text))
    except Exception:
        # Fallback on any error
        return len(text) // 4


def preprocess_html(html: str, model: str = "gpt-4") -> tuple[str, dict[str, int]]:
    """
    Preprocess HTML for LLM consumption by removing unnecessary elements.

    Removes completely:
    - <script> tags and content
    - <style> tags and content
    - <link> tags and content
    - <noscript> tags and content
    - <svg> tags and content
    - HTML comments (via BeautifulSoup)
    - Base64-encoded images (data: URIs in src/href attributes)
    
    Unwraps (removes tag but keeps content):
    - <div> tags
    - <span> tags
    
    Strips attributes:
    - Keeps only href on <a>, src/alt on <img>
    - Removes all other attributes (data-*, id, class, style, etc.)
    
    Cleans whitespace:
    - Collapses excessive newlines and spaces

    Args:
        html: Raw HTML content
        model: Model name for token counting

    Returns:
        Tuple of (cleaned_html, stats) where stats contains:
        - tokens_before: Token count before cleaning
        - tokens_after: Token count after cleaning
        - tokens_saved: Tokens saved by cleaning
        - reduction_pct: Percentage reduction
    """
    import re

    from bs4 import BeautifulSoup, Comment

    # Count tokens before
    tokens_before = count_tokens(html, model)

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Remove script tags
    for script in soup.find_all("script"):
        script.decompose()

    # Remove style tags
    for style in soup.find_all("style"):
        style.decompose()

    # Remove link tags (stylesheets, fonts, etc.)
    for link in soup.find_all("link"):
        link.decompose()

    # Remove noscript tags
    for noscript in soup.find_all("noscript"):
        noscript.decompose()

    # Remove svg tags
    for svg in soup.find_all("svg"):
        svg.decompose()

    # Remove HTML comments (via BeautifulSoup, not regex)
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Remove base64 images (data: URIs) and clean up attributes
    # Define which attributes to keep per tag
    attributes_to_keep = {
        "a": ["href"],
        "img": ["src", "alt"],
    }

    for tag in soup.find_all(True):  # Find all tags
        # Handle base64 in src/href first
        if tag.has_attr("src") and tag["src"].startswith("data:"):
            tag["src"] = "[base64-image-removed]"
        if tag.has_attr("href") and tag["href"].startswith("data:"):
            tag["href"] = "[base64-data-removed]"

        # Remove all attributes except those we want to keep
        tag_name = tag.name
        keep_attrs = attributes_to_keep.get(tag_name, [])
        
        # Get list of attrs to remove (can't modify dict during iteration)
        attrs_to_remove = [attr for attr in tag.attrs if attr not in keep_attrs]
        
        for attr in attrs_to_remove:
            del tag[attr]

    # Unwrap div and span tags (remove tag but keep contents)
    for div in soup.find_all("div"):
        div.unwrap()
    for span in soup.find_all("span"):
        span.unwrap()

    # Get cleaned HTML
    cleaned_html = str(soup)

    # Remove excessive whitespace
    cleaned_html = re.sub(r"\n\s*\n+", "\n\n", cleaned_html)
    cleaned_html = re.sub(r"[ \t]+", " ", cleaned_html)

    # Count tokens after
    tokens_after = count_tokens(cleaned_html, model)
    tokens_saved = tokens_before - tokens_after
    reduction_pct = (tokens_saved / tokens_before * 100) if tokens_before > 0 else 0

    stats = {
        "tokens_before": tokens_before,
        "tokens_after": tokens_after,
        "tokens_saved": tokens_saved,
        "reduction_pct": reduction_pct,
    }

    return cleaned_html, stats


WORKERS_HELP = "Number of worker threads (safe with Selenium, use 1 with Playwright)"

Item = TypeVar("Item")
Result = TypeVar("Result")


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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape and classify queued URLs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--limit", type=int, default=100, help="Maximum candidates to process (default: 100)")
    parser.add_argument("--workers", type=int, default=1, help=WORKERS_HELP)
    parser.add_argument("--model", default="claude-sonnet-5-5", help="LLM model to use")
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
    console.print(f"Config: limit={args.limit}, workers={args.workers}, model={args.model}")
    if args.retry_errors:
        console.print("[yellow]Retry mode: Will retry candidates with classify_error status[/yellow]")
    console.print()

    candidates = select_candidates(args.limit, args.retry_errors)
    if not candidates:
        console.print("[yellow]No candidates to process[/yellow]")
        return
    console.print(f"Found {len(candidates)} candidates to process\n")

    def on_done(n: int, url: str, result) -> None:
        top_category = result.categories[0].id
        console.print(
            f"[{n}/{len(candidates)}] [green]✓[/green] {url[:60]}: "
            f"cat={top_category}, "
            f"score={result.categories[0].score:.2f}"
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
