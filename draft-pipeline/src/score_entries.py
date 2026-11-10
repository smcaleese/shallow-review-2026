#!/usr/bin/env python3
"""
Score Classified Entries
Rates how important each classified entry is for the review (0-1), so that `export_draft.py --top N` can keep each
category's N most important entries. Two steps:
1. Fetch the attention each entry has received: citation counts from Semantic Scholar (arXiv and DOI links by ID,
   other pages by exact title) and karma for LessWrong posts. Saved in the citation_count / lw_karma columns.
2. Send the cached page and that attention (as a rate per month since publication) to the LLM, which judges the work's
   significance, rigor and novelty, and weighs the reputation of its authors and the attention as minor factors.
   Saved in the importance / importance_reason columns.

Basic usage (from the draft-pipeline folder, after classify_entries.py):
    uv run python src/score_entries.py --limit 500 --workers 4
Only classified ('done') entries without a score are processed; add --rescore to score them all again.
Set SEMANTIC_SCHOLAR_API_KEY in .env for higher Semantic Scholar rate limits (it works without one, slowly).
"""

import argparse
import json
import logging
import os
import re
import threading
import time
from datetime import date, datetime, timezone

import requests
import yaml
from pydantic import BaseModel, Field
from tenacity import (
    RetryError,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from shallow_review.common import PROMPTS_PATH, EntryStatus
from shallow_review.data_db import data_db_locked
from shallow_review.llm import get_completion
from shallow_review.scrape import open_scraped
from shallow_review.stats import stats_context
from shallow_review.utils import WORKERS_HELP, preprocess_html, run_parallel
from terminal import console, run

logger = logging.getLogger(__name__)

S2_API = "https://api.semanticscholar.org/graph/v1/paper"
LW_GRAPHQL = "https://www.lesswrong.com/graphql"
S2_MIN_INTERVAL = 1.1  # Seconds between Semantic Scholar calls (the unauthenticated limit is about 1 per second)
DAYS_PER_MONTH = 30.44


class ImportanceResult(BaseModel):
    """What the LLM returns for a page."""

    importance: float = Field(ge=0.0, le=1.0, description="Importance of the work for the review")
    reason: str = Field(description="One sentence on why")


# ---------------------------------------------------------------- attention: citations and karma


def _is_retryable(e: BaseException) -> bool:
    """Rate limits and server errors are retried; other HTTP errors (404, ...) are not."""
    if isinstance(e, requests.HTTPError):
        return e.response.status_code == 429 or e.response.status_code >= 500
    return isinstance(e, (requests.ConnectionError, requests.Timeout))


_s2_lock = threading.Lock()
_s2_last_call = 0.0


@retry(retry=retry_if_exception(_is_retryable), wait=wait_exponential(min=2, max=60), stop=stop_after_attempt(8))
def _s2_request(method: str, url: str, **kwargs) -> requests.Response:
    """One Semantic Scholar call, spaced S2_MIN_INTERVAL from the previous one. Returns the response unless 4xx/5xx
    other than 404 (raised); 404 means the paper is not known."""
    global _s2_last_call
    headers = {"x-api-key": key} if (key := os.environ.get("SEMANTIC_SCHOLAR_API_KEY")) else {}
    with _s2_lock:
        time.sleep(max(0.0, _s2_last_call + S2_MIN_INTERVAL - time.monotonic()))
        _s2_last_call = time.monotonic()
        response = requests.request(method, url, headers=headers, timeout=60, **kwargs)
    if response.status_code != 404:
        response.raise_for_status()
    return response


def s2_id(url: str) -> str | None:
    """Semantic Scholar ID of an arXiv or DOI link (without arXiv version), or None."""
    if m := re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url):
        return f"arXiv:{m.group(1)}"
    if m := re.search(r"doi\.org/(10\..+)$", url):
        return f"DOI:{m.group(1)}"
    return None


def s2_citations_by_id(ids: list[str]) -> dict[str, int]:
    """Citation counts of papers by Semantic Scholar ID; unknown papers are left out."""
    counts: dict[str, int] = {}
    for start in range(0, len(ids), 500):  # The batch endpoint takes at most 500 IDs
        batch = ids[start : start + 500]
        response = _s2_request("POST", f"{S2_API}/batch", params={"fields": "citationCount"}, json={"ids": batch})
        for paper_id, paper in zip(batch, response.json()):
            if paper is not None:
                counts[paper_id] = paper["citationCount"]
    return counts


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def s2_citations_by_title(title: str) -> int | None:
    """Citation count of the paper with exactly this title (up to case and punctuation), or None."""
    response = _s2_request(
        "GET", f"{S2_API}/search/match", params={"query": title, "fields": "title,citationCount"}
    )
    if response.status_code == 404:
        return None
    paper = response.json()["data"][0]
    return paper["citationCount"] if normalize_title(paper["title"]) == normalize_title(title) else None


def lw_karma(url: str) -> int | None:
    """Karma of a LessWrong post, or None if the URL is not a post."""
    m = re.search(r"lesswrong\.com/posts/([A-Za-z0-9]+)", url)
    if not m:
        return None
    query = '{post(input:{selector:{_id:"%s"}}){result{baseScore}}}' % m.group(1)
    response = requests.post(LW_GRAPHQL, json={"query": query}, timeout=60)
    response.raise_for_status()
    post = response.json()["data"]["post"]
    return post["result"]["baseScore"] if post else None


def fetch_attention(urls: list[str]) -> None:
    """Fetch and save citation_count / lw_karma for the URLs (unknown values stay NULL), and when they were checked.
    Entries whose lookup Semantic Scholar refused get no attention_checked_at, so the next run tries them again."""
    with data_db_locked() as db:
        rows = db.execute(
            f"SELECT url, classifier_output FROM entries WHERE url IN ({','.join('?' * len(urls))})", urls
        ).fetchall()
    titles = {row["url"]: json.loads(row["classifier_output"])["title"] for row in rows}

    citations: dict[str, int | None] = {}
    karma: dict[str, int | None] = {}
    ids = {url: paper_id for url in urls if (paper_id := s2_id(url))}
    if ids:
        console.print(f"Fetching citations of {len(ids)} arXiv / DOI papers from Semantic Scholar")
        counts = s2_citations_by_id(sorted(set(ids.values())))
        citations.update({url: counts.get(paper_id) for url, paper_id in ids.items()})
    failed = []
    for url in urls:
        if url in ids:
            continue
        if "lesswrong.com/posts/" in url:
            karma[url] = lw_karma(url)
        else:
            try:
                citations[url] = s2_citations_by_title(titles[url])
            except RetryError as e:  # Semantic Scholar kept refusing: score the entry without citations
                logger.warning(f"Title lookup failed for {url}: {e.last_attempt.exception()}")
                failed.append(url)
        console.print(f"  [dim]{url[:70]}: citations={citations.get(url)}, karma={karma.get(url)}[/dim]")
    if failed:
        console.print(
            f"[red]Semantic Scholar refused the title lookup of {len(failed)} entries (rate limit); they are scored "
            f"without citations. Set SEMANTIC_SCHOLAR_API_KEY and rerun with --rescore to fix this.[/red]"
        )

    checked_at = datetime.now(timezone.utc).isoformat()
    with data_db_locked() as db:
        for url in urls:
            db.execute(
                "UPDATE entries SET citation_count = ?, lw_karma = ?, attention_checked_at = ? WHERE url = ?",
                (citations.get(url), karma.get(url), None if url in failed else checked_at, url),
            )
    found = sum(v is not None for v in citations.values()) + sum(v is not None for v in karma.values())
    console.print(f"Found citations or karma for {found} of {len(urls)} entries\n")


def months_since(date_text: str | None, today: date) -> float | None:
    """Months from a YYYY-MM-DD / YYYY-MM / YYYY date to today, at least 1; None if there is no date."""
    parts = (date_text or "").split("-")
    try:
        published = date(int(parts[0]), int(parts[1]) if len(parts) > 1 else 7, int(parts[2]) if len(parts) > 2 else 15)
    except (ValueError, IndexError):
        return None
    return max(1.0, (today - published).days / DAYS_PER_MONTH)


def describe_attention(row, today: date) -> str:
    """The attention an entry has received, as a line for the prompt."""
    date_text = json.loads(row["classifier_output"]).get("date")
    months = months_since(date_text, today)
    age = f"published {date_text}, {months:.1f} months ago" if months else "publication date unknown"
    if row["lw_karma"] is not None:
        rate = f", {row['lw_karma'] / months:.1f} per month" if months else ""
        return f"LessWrong karma: {row['lw_karma']} ({age}{rate})"
    if row["citation_count"] is not None:
        rate = f", {row['citation_count'] / months:.1f} per month" if months else ""
        return f"Citations (Semantic Scholar): {row['citation_count']} ({age}{rate})"
    return f"No citation or karma data ({age})"


# ---------------------------------------------------------------- scoring


def select_entries(limit: int, rescore: bool) -> list[str]:
    """Classified URLs to score, oldest first."""
    sql = "SELECT url FROM entries WHERE status = ?"
    if not rescore:
        sql += " AND importance IS NULL"
    with data_db_locked() as db:
        rows = db.execute(sql + " ORDER BY added_at LIMIT ?", (EntryStatus.DONE.value, limit)).fetchall()
    return [row["url"] for row in rows]


def score_entry(url: str, prompts: dict, model: str, max_html_tokens: int) -> ImportanceResult:
    """Score one entry from its cached page and attention, and save the result."""
    with data_db_locked() as db:
        row = db.execute("SELECT classifier_output, citation_count, lw_karma FROM entries WHERE url = ?", (url,)).fetchone()
    with open_scraped(url, "rt", encoding="utf-8") as f:
        content, preprocessing_stats = preprocess_html(f.read(), model)
    tokens = preprocessing_stats["tokens_after"]
    if tokens > max_html_tokens:
        raise RuntimeError(f"HTML exceeds max_html_tokens limit: {tokens} > {max_html_tokens}")

    result = get_completion(
        template_vars={"url": url, "content": content, "attention": describe_attention(row, date.today())},
        model=model,
        stats_subtree="score_tokens",
        response_type=ImportanceResult,
        system_prompt_template=prompts["system"],
        user_prompt_template=prompts["user"],
        system_cache_ttl="1h",
        effort="medium",
        max_tokens=16000,
    )
    with data_db_locked() as db:
        db.execute(
            "UPDATE entries SET importance = ?, importance_reason = ? WHERE url = ?",
            (result.importance, result.reason, url),
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rate the importance of classified entries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--limit", type=int, default=100, help="Maximum entries to score (default: 100)")
    parser.add_argument("--workers", type=int, default=1, help=WORKERS_HELP)
    parser.add_argument("--model", default="claude-sonnet-5-5", help="LLM model to use")
    parser.add_argument("--max-tokens", type=int, default=100000, help="Max HTML tokens before error")
    parser.add_argument("--rescore", action="store_true", help="Also score entries that already have a score")
    args = parser.parse_args()

    with open(PROMPTS_PATH / "score.yaml") as f:
        prompts = yaml.safe_load(f)["score_importance"]

    urls = select_entries(args.limit, args.rescore)
    if not urls:
        console.print("[yellow]No entries to score[/yellow]")
        return
    # Attention checked by an earlier run is kept, unless rescoring
    with data_db_locked() as db:
        checked = {row["url"] for row in db.execute("SELECT url FROM entries WHERE attention_checked_at IS NOT NULL")}
    to_fetch = urls if args.rescore else [url for url in urls if url not in checked]
    if to_fetch:
        fetch_attention(to_fetch)
    console.print(f"Scoring {len(urls)} entries with {args.model}\n")

    def on_done(n: int, url: str, result: ImportanceResult) -> None:
        console.print(f"[{n}/{len(urls)}] [green]✓[/green] {url[:60]}: importance={result.importance:.2f}")

    def on_error(n: int, url: str, error: Exception) -> None:
        logger.error(f"Failed to score {url}: {error}", exc_info=error)
        console.print(f"[{n}/{len(urls)}] [red]✗[/red] {url[:60]}: {str(error)[:60]}")

    with stats_context(commandline=f"score_entries --limit {args.limit}") as stats:
        run_parallel(
            urls,
            lambda url: score_entry(url, prompts, args.model, args.max_tokens),
            args.workers,
            on_done,
            on_error,
        )
        stats.print_summary()


if __name__ == "__main__":
    run(main)
