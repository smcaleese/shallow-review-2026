#!/usr/bin/env python3
"""
Forum Post Shortlisting Script
Uses Claude to compare each month's highly relevant posts side by side and pick the most important ones for the review.
The LessWrong counterpart of arxiv-scraper/src/shortlist_arxiv_papers.py.

Basic usage (from the AF-and-LW-scraper folder):
    uv run python src/shortlist_forum_posts.py
Reads results/2-lw-posts-highly-relevant.csv and, for each month, writes
results/shortlisted/<year>/<month>/lw-posts-shortlisted.csv (best first), plus a combined
results/shortlisted/<year>/lw-posts-shortlisted.csv per year. A month whose candidate posts are the same as last time
is skipped, so reruns only redo months that changed (the filter rewrites its output on every run, so file times
can't be used for this).
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path
import pandas as pd
import anthropic
from pydantic import BaseModel
from dotenv import load_dotenv
from terminal import setup_logging, print_summary
from filter_forum_posts import SITE_PREFIXES, DEFAULT_SITE

# Load environment variables from .env file
load_dotenv()

# Setup logging
log = setup_logging("forum-shortlist")

# Initialize Claude client (reads ANTHROPIC_API_KEY from the environment / .env)
client = anthropic.Anthropic()

# On a safety-classifier refusal, retry on Anthropic's recommended fallback model
FALLBACK_BETAS = ["server-side-fallback-2026-07-01"]

# Default configuration
DEFAULT_OUTPUT_DIR = "results/shortlisted"
CANDIDATES_FILENAME = "candidates.txt"  # IDs of the posts a month's shortlist was picked from, to detect changes
DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_EFFORT = "medium"
DEFAULT_SHARE = 0.12  # Share of each month's highly relevant posts to shortlist (~160 of ~1,300 a year)
DAYS_PER_MONTH = 30.4
MAX_TOKENS = 16000
MAX_PARALLEL_MONTHS = 12  # Months are independent, so their calls run at the same time

SYSTEM_PROMPT = """You are an expert in technical AI alignment research helping to write a 2026 shallow review of the field, to be published on LessWrong.

Every post you will see is from LessWrong or the Alignment Forum and has already been judged highly relevant to technical AI alignment. Your job is the final cut: compare the posts side by side and pick the ones a reader of the review most needs to know about.

How the posts reached you, to calibrate how selective to be:
- Each month, roughly 400-700 posts are published on LessWrong (about 6,000 across the year).
- A first filter rated each one alone from its title, tags and opening, and kept the ~20% it judged highly relevant, so you will receive roughly 80-180 posts per month.
- You pick about 12% of those: typically 10-25 posts per month, and only 100-200 for the whole year.
So the bar is high: a post belongs on your list only if it is plausibly among the 100-200 most important AI safety posts of the year. Most of the posts you see are solid work that should not make the cut.

Prefer posts that:
- Report new empirical results, a new technique, or a newly observed phenomenon, especially on frontier or large open-weight models
- Make a conceptual or theoretical argument that changes how people think about an alignment problem
- Set out or substantially update a research agenda, or give a careful critique of one
- Are the main write-up of a significant piece of work, rather than a short update, a link post with little commentary, or a thin summary of others' work
- Are high-quality literature reviews or overviews of an area of AI safety: a careful, comprehensive review that maps an area's work, results and open problems is valuable to the review's readers even though it reports no new results. Pick at most the best one or two of any one area

Karma, Alignment Forum karma and comment counts show how much the community engaged with a post. Treat them as useful evidence, but not as the deciding factor: popular posts are not always important, and recent posts have had less time to collect votes, so use the karma per month and the post's age. Alignment Forum posts and well-known authors are tie-breakers, never requirements.

Treat dangerous-capability evaluations and the science of frontier model behaviour as core safety work, alongside alignment, interpretability, oversight and control, and misuse defences.

Aim for a selection that covers the month's important work across research areas: when several posts make a similar contribution, pick the strongest one or two rather than all of them.

Return exactly the number of posts asked for, best first, each with its post ID exactly as given and a one-sentence reason it made the cut."""

POST_TEMPLATE = """<post>
Post ID: {id}
Title: {title}
Authors: {authors}
Posted: {posted} ({months_old:.1f} months ago)
Alignment Forum: {af}
Karma: {karma} ({karma_per_month:.1f}/month), Alignment Forum karma: {af_karma}, comments: {comment_count}
Words: {word_count}
Tags: {tags}
Opening: {excerpt}
First filter's reasoning: {reasoning}
</post>"""

USER_PROMPT_TEMPLATE = """Here are {n_posts} highly relevant posts from {month}, kept by the first filter out of {n_scraped} posts published that month.

Pick the {n_pick} most important for the review ({pick_share:.0%} of these posts), best first.

{posts}"""


class ShortlistedPost(BaseModel):
    """One post picked for the shortlist."""
    id: str
    reason: str  # One sentence on why it made the cut


class Shortlist(BaseModel):
    """Structured output: the picked posts, best first."""
    posts: list[ShortlistedPost]


def format_post(row: pd.Series, as_of: date) -> str:
    """Render one highly relevant post for the prompt, with its engagement and the first filter's reasoning."""
    months_old = max((as_of - date.fromisoformat(row["posted"])).days / DAYS_PER_MONTH, 0.5)
    return POST_TEMPLATE.format(
        id=row["id"], title=row["title"], authors=row["authors"], posted=row["posted"], months_old=months_old,
        af="yes" if str(row["af"]) == "True" else "no", karma=row["karma"],
        karma_per_month=int(row["karma"]) / months_old, af_karma=row["af_karma"],
        comment_count=row["comment_count"], word_count=row["word_count"], tags=row["tags"] or "none",
        excerpt=row["excerpt"], reasoning=row["reasoning"],
    )


def call_claude_api(df: pd.DataFrame, month: datetime, n_pick: int, n_scraped: int, as_of: date, model: str,
                    effort: str) -> Shortlist | None:
    """
    Ask Claude to pick the n_pick most important posts from one month's highly relevant posts.
    n_scraped (all posts published that month) is only shown to Claude, for context.

    Returns:
        Parsed Shortlist, or None if the request failed or was declined
    """
    user_message = USER_PROMPT_TEMPLATE.format(
        n_posts=len(df), month=f"{month:%B %Y}", n_scraped=n_scraped, n_pick=n_pick, pick_share=n_pick / len(df),
        posts="\n\n".join(format_post(row, as_of) for _, row in df.iterrows()),
    )
    try:
        response = client.beta.messages.parse(
            model=model,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
            output_config={"effort": effort},
            output_format=Shortlist,
            betas=FALLBACK_BETAS,
            fallbacks="default",
        )
    except anthropic.AuthenticationError:
        raise  # Missing/invalid API key: stop instead of failing every month
    except anthropic.APIError as e:
        log.error(f"Error calling Claude API: {e}")
        return None

    if response.stop_reason == "refusal":
        category = response.stop_details.category if response.stop_details else None
        log.warning(f"Claude declined to shortlist {month:%Y-%m} (category: {category})")
        return None
    if response.stop_reason == "max_tokens":
        log.error(f"{month:%Y-%m}: response hit max_tokens ({MAX_TOKENS}) before finishing")
        return None
    return response.parsed_output


def shortlist_month(df: pd.DataFrame, month_dir: Path, month: datetime, n_pick: int, n_scraped: int, as_of: date,
                    filename: str, model: str, effort: str) -> int | None:
    """
    Shortlist one month and write its CSV: the picked posts in rank order, with shortlist_rank and shortlist_reason
    columns. Also records the candidate post IDs, so an unchanged month is skipped next time.

    Returns:
        Number of posts shortlisted, or None if the month failed
    """
    n_pick = min(n_pick, len(df))
    log.info(f"{month:%Y-%m}: asking {model} to pick {n_pick} of {len(df)} posts...")
    shortlist = call_claude_api(df, month, n_pick, n_scraped, as_of, model, effort)
    if shortlist is None:
        return None

    # Keep picks that match a post in the month, once each, in Claude's order
    known = set(df["id"])
    ranks, reasons = {}, {}
    for post in shortlist.posts:
        if post.id not in known:
            log.warning(f"{month:%Y-%m}: ignoring unknown post ID from Claude: {post.id}")
        elif post.id not in ranks:
            ranks[post.id] = len(ranks) + 1
            reasons[post.id] = post.reason
    if len(ranks) != n_pick:
        log.warning(f"{month:%Y-%m}: asked for {n_pick} posts, got {len(ranks)}")

    picked = df[df["id"].isin(ranks)].copy()
    picked["shortlist_rank"] = picked["id"].map(ranks)
    picked["shortlist_reason"] = picked["id"].map(reasons)
    picked = picked.sort_values("shortlist_rank")

    month_dir.mkdir(parents=True, exist_ok=True)
    picked.to_csv(month_dir / filename, index=False)
    (month_dir / CANDIDATES_FILENAME).write_text("\n".join(sorted(df["id"])) + "\n")
    log.info(f"{month:%Y-%m}: saved {len(picked)} posts to {month_dir / filename}")
    return len(picked)


def is_up_to_date(month_dir: Path, filename: str, df: pd.DataFrame) -> bool:
    """Whether the month already has a shortlist picked from exactly these candidate posts."""
    candidates_path = month_dir / CANDIDATES_FILENAME
    if not (month_dir / filename).exists() or not candidates_path.exists():
        return False
    return candidates_path.read_text().split() == sorted(df["id"])


def write_year_files(output_dir: Path, filename: str) -> list[Path]:
    """Combine each year's monthly shortlists into output_dir/<year>/<filename>, earliest month first."""
    written = []
    for year_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        month_files = sorted(
            year_dir.glob(f"*/{filename}"),
            key=lambda p: datetime.strptime(f"{year_dir.name} {p.parent.name}", "%Y %b"),
        )
        frames = [pd.read_csv(p, dtype={"id": str}, keep_default_na=False).assign(month=p.parent.name)
                  for p in month_files]
        if frames:
            year_path = year_dir / filename
            pd.concat(frames, ignore_index=True).to_csv(year_path, index=False)
            written.append(year_path)
    return written


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Shortlist the most important highly relevant forum posts, month by month",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Shortlist every month (~12% of each month's highly relevant posts)
  python src/shortlist_forum_posts.py

  # Exactly 15 posts per month
  python src/shortlist_forum_posts.py --per-month 15

  # One month, redone from scratch
  python src/shortlist_forum_posts.py --start-month 2026-01 --end-month 2026-01 --overwrite
        """
    )
    parser.add_argument("--site", choices=list(SITE_PREFIXES), default=DEFAULT_SITE,
                        help=f"Which site's files to use for the default paths (default: {DEFAULT_SITE})")
    parser.add_argument("--input", help="Highly relevant posts CSV (default: results/2-<site>-posts-highly-relevant.csv)")
    parser.add_argument("--raw", help="Raw posts CSV, to count each month's posts (default: results/1-<site>-posts-raw.csv)")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR,
                        help=f"Folder for per-month shortlists (default: {DEFAULT_OUTPUT_DIR})")
    size = parser.add_mutually_exclusive_group()
    size.add_argument("--share", type=float, default=DEFAULT_SHARE,
                      help=f"Share of each month's highly relevant posts to shortlist (default: {DEFAULT_SHARE})")
    size.add_argument("--per-month", type=int, help="Fixed number of posts to shortlist per month (overrides --share)")
    parser.add_argument("--start-month", help="First month to shortlist, YYYY-MM (default: earliest month)")
    parser.add_argument("--end-month", help="Last month to shortlist, YYYY-MM (default: latest month)")
    parser.add_argument("--overwrite", action="store_true", help="Redo months that already have an up-to-date shortlist")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Claude model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--effort", default=DEFAULT_EFFORT, choices=["low", "medium", "high", "xhigh", "max"],
                        help=f"Effort level (default: {DEFAULT_EFFORT})")
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()
    prefix = SITE_PREFIXES[args.site]
    input_path = Path(args.input or f"results/2-{prefix}-posts-highly-relevant.csv")
    raw_path = Path(args.raw or f"results/1-{prefix}-posts-raw.csv")
    output_dir = Path(args.output_dir)
    filename = f"{prefix}-posts-shortlisted.csv"

    if not input_path.exists():
        log.error(f"Input file not found: {input_path}. Please run src/filter_forum_posts.py first.")
        return
    df = pd.read_csv(input_path, dtype={"id": str}, keep_default_na=False)
    raw = pd.read_csv(raw_path, dtype={"id": str}, keep_default_na=False) if raw_path.exists() else df
    df["month"] = pd.to_datetime(df["posted"]).dt.to_period("M")
    scraped_per_month = pd.to_datetime(raw["posted"]).dt.to_period("M").value_counts()
    as_of = date.today()

    months = sorted(df["month"].unique())
    if args.start_month:
        months = [m for m in months if m >= pd.Period(args.start_month, "M")]
    if args.end_month:
        months = [m for m in months if m <= pd.Period(args.end_month, "M")]
    if not months:
        log.error(f"No posts to shortlist in {input_path} for the months asked for.")
        return

    summary, jobs = {}, []
    for period in months:
        month = period.to_timestamp().to_pydatetime()
        month_df = df[df["month"] == period].drop(columns="month").reset_index(drop=True)
        month_dir = output_dir / str(period.year) / f"{month:%b}".lower()
        if not args.overwrite and is_up_to_date(month_dir, filename, month_df):
            log.info(f"{month:%Y-%m}: candidates unchanged since the last shortlist, skipping")
            summary[month] = f"{len(pd.read_csv(month_dir / filename))}/{len(month_df)} (already done)"
            continue
        n_pick = args.per_month if args.per_month else max(1, round(args.share * len(month_df)))
        jobs.append((month, month_df, month_dir, n_pick, int(scraped_per_month.get(period, len(month_df)))))

    # Shortlist the remaining months in parallel; map() re-raises a worker's exception (e.g. a bad API key)
    if jobs:
        log.info(f"Shortlisting {len(jobs)} month(s) in parallel...")
        with ThreadPoolExecutor(max_workers=min(len(jobs), MAX_PARALLEL_MONTHS)) as executor:
            results = executor.map(
                lambda job: shortlist_month(job[1], job[2], job[0], job[3], job[4], as_of, filename,
                                            args.model, args.effort),
                jobs,
            )
            for (month, month_df, _, _, _), n_saved in zip(jobs, results):
                summary[month] = "failed" if n_saved is None else f"{n_saved}/{len(month_df)}"

    for path in write_year_files(output_dir, filename):
        log.info(f"Combined shortlist: {path} ({len(pd.read_csv(path))} posts)")
    print_summary("Shortlisted / highly relevant", [(f"{m:%Y-%m}", summary[m]) for m in sorted(summary)])


if __name__ == "__main__":
    main()
