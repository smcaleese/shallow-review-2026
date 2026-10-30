#!/usr/bin/env python3
"""
Step 8: keep the review's budget of items: the top BUDGET[source] in-scope items of each source, by rank score.

Usage (from facets-shared/):
    uv run python src/select_budget.py
Reads output/rankings.csv (src/rank.py) and budget-overrides.json ({"include": [ids], "exclude": [ids]}: hand
decisions, applied on top of the budget). Items that are both an arXiv paper and a LW post count as arXiv.
Writes data/6-selected.json (read by build_site.py) and output/selected-sources.csv.
"""

import csv
import json
from collections import Counter

from common import BUDGET, BUDGET_OVERRIDES, OUTPUT, RANKINGS_CSV, SELECTED

OUT_CSV = OUTPUT / "selected-sources.csv"


def main():
    rows = list(csv.DictReader(RANKINGS_CSV.open()))  # already sorted by score, best first
    overrides = json.loads(BUDGET_OVERRIDES.read_text()) if BUDGET_OVERRIDES.exists() else {}
    include, exclude = set(overrides.get("include", [])), set(overrides.get("exclude", []))
    ranked_ids = {r["id"] for r in rows}
    missing = include - ranked_ids
    if missing:
        print(f"  warning: {len(missing)} override ids aren't ranked (out of scope or not loaded): {sorted(missing)}")

    taken, picked = Counter(), []
    for r in rows:
        if r["id"] in exclude:
            continue
        if taken[r["source"]] < BUDGET[r["source"]]:
            taken[r["source"]] += 1
            picked.append(r | {"why_kept": "budget"})
        elif r["id"] in include:
            picked.append(r | {"why_kept": "override"})

    SELECTED.write_text(json.dumps({"budget": BUDGET, "ids": [r["id"] for r in picked]}, indent=1))
    with OUT_CSV.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["source_rank", "why_kept"] + list(rows[0]))
        w.writeheader()
        n = Counter()
        for r in picked:
            n[r["source"]] += 1
            w.writerow(r | {"source_rank": n[r["source"]]})

    available = Counter(r["source"] for r in rows)
    print(f"Wrote {SELECTED.name} and {OUT_CSV.name}: {len(picked)} items")
    for source, budget in BUDGET.items():
        kept = [r for r in picked if r["source"] == source]
        cut = min((float(r["claude"]) for r in kept if r["why_kept"] == "budget"), default=0)
        print(f"  {source:13} {len(kept):4} kept of {available[source]:4} ranked (budget {budget}; "
              f"lowest Claude score kept {cut:.2f}; {sum(r['why_kept'] == 'override' for r in kept)} by override)")


if __name__ == "__main__":
    main()
