#!/usr/bin/env python3
"""
Export scraper outputs as plain URL lists for `main-pipeline`.

Reads the CSVs produced by arxiv-scraper and AF-and-LW-scraper and writes one
`<name>-<label>.txt` file per source (one URL per line, '#' header) into the
pipeline's data/sources-links/ directory. Load them with:

    pipeline.py add data/sources-links/*-<label>.txt --phase classify
"""

import argparse
import csv
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
DEFAULT_ARXIV = HERE / "arxiv-scraper/results/6-arxiv_curated_relevant_only.csv"
DEFAULT_AF = HERE / "AF-and-LW-scraper/results/1-af_raw_posts.csv"
DEFAULT_LW = HERE / "AF-and-LW-scraper/results/1-lw_raw_posts.csv"
DEFAULT_OUT_DIR = HERE.parent / "main-pipeline/data/sources-links"


def read_csv(path: Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def arxiv_urls(path: Path) -> list[str]:
    """Curated papers marked relevant, as arxiv.org/abs URLs."""
    rows = [r for r in read_csv(path) if r.get("is_relevant", "").strip().lower() == "y"]
    return [f"https://arxiv.org/abs/{r['arxiv_id']}" for r in rows]


def post_urls(path: Path, top: int | None) -> list[str]:
    """AF/LW post URLs, optionally only the `top` by score (then comment count)."""
    rows = [r for r in read_csv(path) if r.get("url")]

    def num(x: str) -> float:
        try:
            return float(x)
        except ValueError:
            return 0.0

    if top is not None:
        rows.sort(key=lambda r: (num(r["score"]), num(r["commentCount"])), reverse=True)
        rows = rows[:top]
    return [r["url"] for r in rows]


def write_list(out: Path, urls: list[str], input_path: Path) -> None:
    urls = list(dict.fromkeys(urls))  # dedupe, keep order
    header = f"# Exported {date.today()} from {input_path.name}: {len(urls)} URLs\n"
    out.write_text(header + "\n".join(urls) + "\n", encoding="utf-8")
    print(f"{out}: {len(urls)} URLs")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--label", default="2026", help="Suffix for output files, e.g. arxiv-2026.txt")
    p.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    p.add_argument("--arxiv", type=Path, default=DEFAULT_ARXIV, help="Curated arXiv CSV (6-...)")
    p.add_argument("--af", type=Path, default=DEFAULT_AF, help="Raw AF posts CSV")
    p.add_argument("--lw", type=Path, default=DEFAULT_LW, help="Raw LW posts CSV")
    p.add_argument("--af-top", type=int, default=None, help="Keep only top N AF posts by score (default: all)")
    p.add_argument("--lw-top", type=int, default=300, help="Keep only top N LW posts by score (default: 300)")
    args = p.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    # A missing input is skipped explicitly; a malformed one raises.
    for name, path, make_urls in [
        ("arxiv", args.arxiv, lambda pth: arxiv_urls(pth)),
        ("af", args.af, lambda pth: post_urls(pth, args.af_top)),
        ("lw", args.lw, lambda pth: post_urls(pth, args.lw_top)),
    ]:
        if not path.exists():
            print(f"Skipping {name}: {path} not found")
            continue
        write_list(args.out_dir / f"{name}-{args.label}.txt", make_urls(path), path)


if __name__ == "__main__":
    main()
