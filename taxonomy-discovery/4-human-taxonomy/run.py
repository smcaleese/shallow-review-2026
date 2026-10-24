#!/usr/bin/env python3
"""Method 4: a hand-written taxonomy (taxonomy.yaml), with items assigned by the same classifier method 1 uses.

The categories come from a person, not from the data; the classifier only sorts items into them (or "other"). This
puts a human design on the same footing as the automated methods, so compare.py and report.py treat it the same.

Usage (from taxonomy-discovery/):
    uv run python 4-human-taxonomy/run.py
"""

import argparse
import logging
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import yaml

from shared import llm
from shared.data import load_items, size_summary
from shared.taxonomy import OTHER, assign_items, leaf_categories, write_result

log = logging.getLogger("human-taxonomy")


def load_categories(path: Path) -> list[dict]:
    cats = []
    for t, top in enumerate(yaml.safe_load(path.read_text())["categories"], 1):
        cats.append({"id": f"c{t}", "name": top["name"], "description": top["description"].strip(), "parent": None})
        for s, sub in enumerate(top.get("subcategories") or [], 1):
            cats.append({"id": f"c{t}.{s}", "name": sub["name"], "description": sub["description"].strip(),
                         "parent": f"c{t}"})
    return cats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--taxonomy", type=Path, default=HERE / "taxonomy.yaml")
    ap.add_argument("--model", default=llm.DEFAULT_MODEL)
    ap.add_argument("--limit", type=int, help="use a fixed random sample of this many items")
    args = ap.parse_args()

    items = load_items(args.limit)
    categories = load_categories(args.taxonomy)
    leaves = leaf_categories({"categories": categories})
    assignments = assign_items(items, leaves, all_categories=categories, model=args.model, label="assign")
    log.info(f"{len(leaves)} leaves; {size_summary(assignments)}; "
             f"{sum(v == OTHER for v in assignments.values())} in other")
    write_result(HERE, "4-human-taxonomy", items, categories, assignments,
                 {"taxonomy": args.taxonomy.name, "model": args.model})
    log.info(llm.usage_report())


if __name__ == "__main__":
    main()
