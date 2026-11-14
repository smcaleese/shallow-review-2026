#!/usr/bin/env python3
"""
Step 7: keep the review's sources: exactly the items in draft-pipeline's source lists (SOURCE_LIST_NAMES in common.py,
one URL per line), so the site shows the same sources the draft is built from.

An item is kept if any of its links (its arXiv page, LW post, org page, ...) is in a list, so an LW post that dedupe
merged into its arXiv paper still counts. Items the tagger scoped out are kept too: the lists are the selection.

Usage (from facets-shared/):
    uv run python src/select_budget.py
Reads data/2-items-deduped.jsonl and output/rankings.csv (src/rank.py, for the order). Writes data/6-selected.json
(read by build_site.py) and output/selected-sources.csv.
"""

import csv
import json
from collections import Counter

from common import ITEMS_DEDUPED, OUTPUT, RANKINGS_CSV, SELECTED, SOURCE_LIST_NAMES, SOURCE_LISTS, read_jsonl, source_key

OUT_CSV = OUTPUT / "selected-sources.csv"


def main():
    listed = {}  # key -> list name
    for name in SOURCE_LIST_NAMES:
        for line in (SOURCE_LISTS / f"{name}.txt").read_text().splitlines():
            if line.startswith("http"):
                listed.setdefault(source_key(line), name)

    items = read_jsonl(ITEMS_DEDUPED)
    found, picked = set(), []
    for item in items:
        keys = {source_key(item["url"])} | {source_key(link["url"]) for link in item["links"]}
        hits = keys & set(listed)
        if hits:
            found |= hits
            picked.append(item)

    # Best-ranked first; items without a rank (scoped out, so never ranked) go last
    order = {r["id"]: n for n, r in enumerate(csv.DictReader(RANKINGS_CSV.open()))} if RANKINGS_CSV.exists() else {}
    picked.sort(key=lambda i: order.get(i["id"], len(order)))

    SELECTED.write_text(json.dumps({"source_lists": SOURCE_LIST_NAMES, "ids": [i["id"] for i in picked]}, indent=1))
    with OUT_CSV.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_rank", "id", "source", "title", "url", "ranked"])
        n = Counter()
        for i in picked:
            n[i["source"]] += 1
            w.writerow([n[i["source"]], i["id"], i["source"], i["title"], i["url"], i["id"] in order])

    missing = set(listed) - found
    print(f"Wrote {SELECTED.name} and {OUT_CSV.name}: {len(picked)} items for {len(listed)} listed sources "
          f"({', '.join(f'{v} {k}' for k, v in Counter(i['source'] for i in picked).items())})")
    print(f"  {sum(i['id'] not in order for i in picked)} kept items are unranked (tagged out of scope)")
    if missing:
        print(f"  warning: {len(missing)} listed sources aren't loaded: {sorted(missing)[:10]}")


if __name__ == "__main__":
    main()
