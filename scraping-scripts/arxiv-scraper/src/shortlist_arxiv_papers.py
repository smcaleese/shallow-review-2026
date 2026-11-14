#!/usr/bin/env python3
"""
ArXiv Shortlisting Script
Uses Claude to compare each month's filtered papers side by side and pick the most important ones for the review.

Basic usage (from the arxiv-scraper folder):
    uv run python src/shortlist_arxiv_papers.py
For each results/filtered/<year>/<month>/arxiv-papers-filtered.csv, writes
results/shortlisted/<year>/<month>/arxiv-papers-shortlisted.csv (best first), plus a combined
results/shortlisted/<year>/arxiv-papers-shortlisted.csv per year. Months whose shortlist is newer than their filtered
file are skipped, so reruns only redo months that changed.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
import pandas as pd
import anthropic
from pydantic import BaseModel
from dotenv import load_dotenv
from terminal import setup_logging, print_summary
from filter_arxiv_papers import FILTERED_FILENAME, RATED_FILENAME, DEFAULT_OUTPUT_DIR as DEFAULT_FILTERED_DIR

# Load environment variables from .env file
load_dotenv()

# Setup logging
log = setup_logging("arxiv-shortlist")

# Initialize Claude client (reads ANTHROPIC_API_KEY from the environment / .env)
client = anthropic.Anthropic()

# On a safety-classifier refusal, retry on Anthropic's recommended fallback model
FALLBACK_BETAS = ["server-side-fallback-2026-07-01"]

# Default configuration
DEFAULT_OUTPUT_DIR = "results/shortlisted"
SHORTLISTED_FILENAME = "arxiv-papers-shortlisted.csv"
DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_EFFORT = "medium"  # Comparing a whole month of papers is worth the extra thinking
DEFAULT_SHARE = 0.2  # Share of each month's filtered papers to shortlist (~350 of ~1,800 a year)
MAX_TOKENS = 16000
MAX_PARALLEL_MONTHS = 12  # Months are independent, so their calls run at the same time

SYSTEM_PROMPT = """You are an expert in technical AI alignment research helping to write a 2026 shallow review of the field, to be published on LessWrong.

Every paper you will see has already been judged relevant to AI safety and alignment. Your job is the final cut: compare the papers side by side and pick the ones a reader of the review most needs to know about.

How the papers reached you, to calibrate how selective to be:
- Each month, an arXiv keyword search finds roughly 1,000-1,800 candidate papers (about 12,000 across the year).
- A first filter rated each one alone and kept the 10-15% that are clearly relevant, so you will receive roughly 100-270 papers per month.
- You pick about 20% of those: typically 20-55 papers per month, and only 300-400 for the whole year.
So the bar is high: a paper belongs on your list only if it is plausibly among the 300-400 most important AI safety papers of the year. Most of the papers you see are solid work that should not make the cut.

Prefer papers that:
- Report a novel and important finding, technique, or phenomenon, rather than an incremental improvement on an existing method (surveys are judged differently, see below)
- Show results on frontier or large open-weight models rather than toy settings
- Open or substantially move forward a research direction, or release a benchmark, dataset, or tool others are likely to build on
- Are likely to be widely discussed or cited (citations, venue, and well-known authors are tie-breakers, never requirements)
- Are high-quality literature reviews or surveys of an area of AI safety (e.g. the state of mechanistic interpretability, scalable oversight, or AI control): a careful, comprehensive survey that maps an area's methods, results and open problems is valuable to the review's readers even though it reports no new results. Pick at most the best one or two surveys of any one area, and skip short, shallow or mostly derivative ones

Treat dangerous-capability evaluations (e.g. cyber offense, biosecurity uplift) and the science of frontier model behaviour as core safety work, alongside alignment, interpretability, oversight and control, and misuse defences.

Aim for a selection that covers the month's important work across research areas: when several papers make a similar contribution, pick the strongest one or two rather than all of them.

Return exactly the number of papers asked for, best first, each with its arXiv ID exactly as given and a one-sentence reason it made the cut."""

PAPER_TEMPLATE = """<paper>
arXiv ID: {arxiv_id}
Title: {title}
Authors: {authors}
Published: {published}
Abstract: {abstract}
Comment: {comment}
Venue: {venue}
Citations: {citations}
Top author h-index: {top_author}
Relevance score from the first filter: {relevance}/5 ({reasoning})
</paper>"""

USER_PROMPT_TEMPLATE = """Here are {n_papers} AI safety papers from {month}, kept by the first filter out of {n_scraped} papers the keyword search found that month.

Pick the {n_pick} most important for the review ({pick_share:.0%} of these papers), best first.

{papers}"""


class ShortlistedPaper(BaseModel):
    """One paper picked for the shortlist."""
    arxiv_id: str
    reason: str  # One sentence on why it made the cut


class Shortlist(BaseModel):
    """Structured output: the picked papers, best first."""
    papers: list[ShortlistedPaper]


def find_months(filtered_dir: Path) -> list[tuple[datetime, Path]]:
    """
    Find the filtered months under filtered_dir (filtered_dir/<year>/<month>/arxiv-papers-filtered.csv).

    Returns:
        (first day of month, month folder relative to filtered_dir) pairs, earliest first
    """
    months = []
    for path in filtered_dir.glob(f"*/*/{FILTERED_FILENAME}"):
        month_folder = path.parent.relative_to(filtered_dir)
        year, month = month_folder.parts
        months.append((datetime.strptime(f"{year} {month}", "%Y %b"), month_folder))
    return sorted(months)


def format_paper(row: pd.Series) -> str:
    """Render one filtered paper for the prompt, with the metadata the first filter saw plus its verdict."""
    def value(column):
        return row[column] if column in row and pd.notna(row[column]) else "N/A"

    if pd.notna(row.get("citation_count")):
        citations = f"{int(row['citation_count'])} total, {row['citations_per_month']:.2f}/month"
    else:
        citations = "unknown"
    if pd.notna(row.get("max_author_h_index")):
        top_author = f"{int(row['max_author_h_index'])} ({row['max_h_index_author']})"
    else:
        top_author = "unknown"
    return PAPER_TEMPLATE.format(
        arxiv_id=row["arxiv_id"], title=row["title"], authors=row["authors"], published=row["published"],
        abstract=row["abstract"], comment=value("comment"), venue=value("venue"), citations=citations,
        top_author=top_author, relevance=int(row["relevance"]), reasoning=value("reasoning"),
    )


def call_claude_api(df: pd.DataFrame, month: datetime, n_pick: int, n_scraped: int, model: str,
                    effort: str) -> Shortlist | None:
    """
    Ask Claude to pick the n_pick most important papers from one month's filtered papers.
    n_scraped (the month's keyword-search total) is only shown to Claude, for context.

    Returns:
        Parsed Shortlist, or None if the request failed or was declined
    """
    user_message = USER_PROMPT_TEMPLATE.format(
        n_papers=len(df), month=f"{month:%B %Y}", n_scraped=n_scraped, n_pick=n_pick, pick_share=n_pick / len(df),
        papers="\n\n".join(format_paper(row) for _, row in df.iterrows()),
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


def shortlist_month(filtered_path: Path, output_path: Path, month: datetime, n_pick: int,
                    model: str, effort: str) -> int | None:
    """
    Shortlist one month and write its CSV: the picked filtered papers in rank order, with shortlist_rank and
    shortlist_reason columns.

    Returns:
        Number of papers shortlisted, or None if the month failed
    """
    df = pd.read_csv(filtered_path, dtype={"arxiv_id": str})
    # The rated file next to the filtered one has every paper the scraper found that month
    rated_path = filtered_path.parent / RATED_FILENAME
    n_scraped = len(pd.read_csv(rated_path)) if rated_path.exists() else len(df)
    if df.empty:
        log.info(f"{month:%Y-%m}: no filtered papers")
        picked = df.assign(shortlist_rank=pd.Series(dtype="Int64"), shortlist_reason=pd.Series(dtype=str))
    else:
        n_pick = min(n_pick, len(df))
        log.info(f"{month:%Y-%m}: asking {model} to pick {n_pick} of {len(df)} papers...")
        shortlist = call_claude_api(df, month, n_pick, n_scraped, model, effort)
        if shortlist is None:
            return None

        # Keep picks that match a paper in the month, once each, in Claude's order
        known = set(df["arxiv_id"])
        ranks, reasons = {}, {}
        for paper in shortlist.papers:
            if paper.arxiv_id not in known:
                log.warning(f"{month:%Y-%m}: ignoring unknown arXiv ID from Claude: {paper.arxiv_id}")
            elif paper.arxiv_id not in ranks:
                ranks[paper.arxiv_id] = len(ranks) + 1
                reasons[paper.arxiv_id] = paper.reason
        if len(ranks) != n_pick:
            log.warning(f"{month:%Y-%m}: asked for {n_pick} papers, got {len(ranks)}")

        picked = df[df["arxiv_id"].isin(ranks)].copy()
        picked["shortlist_rank"] = picked["arxiv_id"].map(ranks)
        picked["shortlist_reason"] = picked["arxiv_id"].map(reasons)
        picked = picked.sort_values("shortlist_rank")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    picked.to_csv(output_path, index=False)
    log.info(f"{month:%Y-%m}: saved {len(picked)} papers to {output_path}")
    return len(picked)


def write_year_files(output_dir: Path) -> list[Path]:
    """Combine each year's monthly shortlists into output_dir/<year>/arxiv-papers-shortlisted.csv, earliest month first."""
    written = []
    for year_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        month_files = sorted(
            year_dir.glob(f"*/{SHORTLISTED_FILENAME}"),
            key=lambda p: datetime.strptime(f"{year_dir.name} {p.parent.name}", "%Y %b"),
        )
        frames = [pd.read_csv(p, dtype={"arxiv_id": str}).assign(month=p.parent.name) for p in month_files]
        if frames:
            year_path = year_dir / SHORTLISTED_FILENAME
            pd.concat(frames, ignore_index=True).to_csv(year_path, index=False)
            written.append(year_path)
    return written


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Shortlist the most important filtered arXiv papers, month by month",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Shortlist every filtered month (~9% of each month's papers)
  python src/shortlist_arxiv_papers.py

  # Exactly 12 papers per month
  python src/shortlist_arxiv_papers.py --per-month 12

  # One month, redone from scratch
  python src/shortlist_arxiv_papers.py --start-month 2026-01 --end-month 2026-01 --overwrite
        """
    )
    parser.add_argument("--filtered-dir", default=DEFAULT_FILTERED_DIR,
                        help=f"Folder of per-month filtered results from filter_arxiv_papers.py (default: {DEFAULT_FILTERED_DIR})")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR,
                        help=f"Folder for per-month shortlists (default: {DEFAULT_OUTPUT_DIR})")
    size = parser.add_mutually_exclusive_group()
    size.add_argument("--share", type=float, default=DEFAULT_SHARE,
                      help=f"Share of each month's filtered papers to shortlist (default: {DEFAULT_SHARE})")
    size.add_argument("--per-month", type=int, help="Fixed number of papers to shortlist per month (overrides --share)")
    parser.add_argument("--start-month", help="First month to shortlist, YYYY-MM (default: earliest filtered month)")
    parser.add_argument("--end-month", help="Last month to shortlist, YYYY-MM (default: latest filtered month)")
    parser.add_argument("--overwrite", action="store_true", help="Redo months that already have an up-to-date shortlist")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Claude model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--effort", default=DEFAULT_EFFORT, choices=["low", "medium", "high", "xhigh", "max"],
                        help=f"Effort level (default: {DEFAULT_EFFORT})")
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()

    filtered_dir, output_dir = Path(args.filtered_dir), Path(args.output_dir)
    months = find_months(filtered_dir)
    if args.start_month:
        months = [(m, folder) for m, folder in months if m >= datetime.strptime(args.start_month, "%Y-%m")]
    if args.end_month:
        months = [(m, folder) for m, folder in months if m <= datetime.strptime(args.end_month, "%Y-%m")]
    if not months:
        log.error(f"No filtered months found in {filtered_dir}. Please run src/filter_arxiv_papers.py first.")
        return

    summary, jobs = {}, []
    for month, folder in months:
        filtered_path = filtered_dir / folder / FILTERED_FILENAME
        output_path = output_dir / folder / SHORTLISTED_FILENAME
        n_filtered = len(pd.read_csv(filtered_path))

        # A shortlist saved after its filtered file was last written is up to date
        if (not args.overwrite and output_path.exists()
                and output_path.stat().st_mtime > filtered_path.stat().st_mtime):
            log.info(f"{month:%Y-%m}: shortlist is up to date, skipping")
            summary[month] = f"{len(pd.read_csv(output_path))}/{n_filtered} (already done)"
            continue

        n_pick = args.per_month if args.per_month else max(1, round(args.share * n_filtered))
        jobs.append((month, filtered_path, output_path, n_pick, n_filtered))

    # Shortlist the remaining months in parallel; map() re-raises a worker's exception (e.g. a bad API key)
    if jobs:
        log.info(f"Shortlisting {len(jobs)} month(s) in parallel...")
        with ThreadPoolExecutor(max_workers=min(len(jobs), MAX_PARALLEL_MONTHS)) as executor:
            results = executor.map(
                lambda job: shortlist_month(job[1], job[2], job[0], job[3], args.model, args.effort), jobs
            )
            for (month, _, _, _, n_filtered), n_saved in zip(jobs, results):
                summary[month] = "failed" if n_saved is None else f"{n_saved}/{n_filtered}"

    year_files = write_year_files(output_dir)
    for path in year_files:
        log.info(f"Combined shortlist: {path} ({len(pd.read_csv(path))} papers)")
    print_summary("Shortlisted / filtered", [(f"{m:%Y-%m}", summary[m]) for m in sorted(summary)])


if __name__ == "__main__":
    main()
