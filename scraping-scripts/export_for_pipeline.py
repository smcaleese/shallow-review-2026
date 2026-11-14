#!/usr/bin/env python3
"""
Export the arXiv and LessWrong shortlists as plain URL lists for `draft-pipeline`.

Reads the combined shortlists written by arxiv-scraper/src/shortlist_arxiv_papers.py and
AF-and-LW-scraper/src/shortlist_forum_posts.py, and writes `shortlist-arxiv-<label>.txt` and
`shortlist-lw-<label>.txt` (one URL per line, '#' header) into draft-pipeline/data/sources-links/. Add them with
(from draft-pipeline):

    uv run python src/add_entries.py data/sources-links/shortlist-arxiv-2026.txt
"""

import argparse
import csv
import re
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_ARXIV = HERE / "arxiv-scraper/results/shortlisted/2026/arxiv-papers-shortlisted.csv"
DEFAULT_LW = HERE / "AF-and-LW-scraper/results/shortlisted/2026/lw-posts-shortlisted.csv"
DEFAULT_OUT_DIR = HERE.parent / "draft-pipeline/data/sources-links"


def read_csv(path: Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def arxiv_urls(path: Path) -> list[str]:
    """Shortlisted papers as arxiv.org/abs URLs, without the version suffix (matching the pipeline's other lists)."""
    return [f"https://arxiv.org/abs/{re.sub(r'v[0-9]+$', '', r['arxiv_id'])}" for r in read_csv(path)]


def post_urls(path: Path) -> list[str]:
    """Shortlisted posts' LessWrong URLs."""
    return [r["url"] for r in read_csv(path)]


def write_list(out: Path, urls: list[str], input_path: Path) -> None:
    urls = list(dict.fromkeys(urls))  # dedupe, keep order
    header = f"# Exported {date.today()} from {input_path.parent.parent.name}/{input_path.parent.name}/{input_path.name}: {len(urls)} URLs\n"
    out.write_text(header + "\n".join(urls) + "\n", encoding="utf-8")
    print(f"{out}: {len(urls)} URLs")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--label", default="2026", help="Suffix for output files, e.g. shortlist-arxiv-2026.txt")
    p.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    p.add_argument("--arxiv", type=Path, default=DEFAULT_ARXIV, help="Combined arXiv shortlist CSV")
    p.add_argument("--lw", type=Path, default=DEFAULT_LW, help="Combined LessWrong shortlist CSV")
    args = p.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, path, make_urls in [("arxiv", args.arxiv.resolve(), arxiv_urls), ("lw", args.lw.resolve(), post_urls)]:
        if not path.exists():
            raise SystemExit(f"{name}: {path} not found; run its shortlist script first")
        write_list(args.out_dir / f"shortlist-{name}-{args.label}.txt", make_urls(path), path)


if __name__ == "__main__":
    main()
