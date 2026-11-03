#!/usr/bin/env python3
"""
Export the selected sources (the ~500 items on the site) as URL lists for main-pipeline.

Usage (from facets-shared/):
    uv run python src/export_for_pipeline.py
Reads output/selected-sources.csv (src/select_budget.py) and writes one list per source to
../main-pipeline/data/sources-links/facets-<source>-2026.txt, in the format scraping-scripts/export_for_pipeline.py
uses: a '#' header line, then one URL per line. Items that are both an arXiv paper and a LW post are in the arXiv list.
Load them in main-pipeline with:
    uv run pipeline.py add data/sources-links/facets-arxiv-2026.txt --phase classify --source facets-arxiv-2026
"""

import csv
from collections import defaultdict
from datetime import date

from common import OUTPUT, ROOT

SELECTED_CSV = OUTPUT / "selected-sources.csv"
OUT_DIR = ROOT.parent / "main-pipeline" / "data" / "sources-links"
NAMES = {"arxiv": "arxiv", "lesswrong": "lw", "org": "org", "safety_stack": "safetystack"}


def main():
    rows = list(csv.DictReader(SELECTED_CSV.open()))
    by_source = defaultdict(list)
    for r in rows:
        by_source[r["source"]].append(r["url"])

    assert set(by_source) <= set(NAMES), f"unknown sources: {set(by_source) - set(NAMES)}"
    for source, urls in by_source.items():
        urls = list(dict.fromkeys(urls))
        out = OUT_DIR / f"facets-{NAMES[source]}-2026.txt"
        header = f"# Exported {date.today()} from facets-shared/output/selected-sources.csv ({source}): {len(urls)} URLs\n"
        out.write_text(header + "\n".join(urls) + "\n", encoding="utf-8")
        print(f"  {out.relative_to(ROOT.parent)}: {len(urls)} URLs")
    print(f"  {len(rows)} selected sources in total")


if __name__ == "__main__":
    main()
