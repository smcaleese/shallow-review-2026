#!/usr/bin/env python3
"""Method 1: LLM direct taxonomy.

1. Propose: Claude reads every item at once and proposes a two-level taxonomy with inclusion-criterion descriptions.
2. Assign: a separate pass puts each item in one leaf (or "other") using only the names and descriptions.
3. Refine (--rounds times): Claude sees each category's members and the "other" pile, then merges, splits, renames
   and adds categories; items are reassigned.

Usage (from taxonomy-discovery/):
    uv run python 1-llm-taxonomy/run.py
    uv run python 1-llm-taxonomy/run.py --limit 40 --rounds 0     # smoke test on a sample
"""

import argparse
import logging
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from pydantic import BaseModel, Field

from shared import llm
from shared.data import corpus_text, load_items, size_summary, write_json
from shared.taxonomy import OTHER, assign_items, leaf_categories, write_result

log = logging.getLogger("llm-taxonomy")


class Sub(BaseModel):
    name: str = Field(description="2-6 words")
    description: str = Field(description="1-2 sentences: an inclusion criterion for this category")


class Top(BaseModel):
    name: str = Field(description="2-6 words")
    description: str = Field(description="1-2 sentences: an inclusion criterion for this area")
    subcategories: list[Sub] = Field(description="2-6 subcategories, or empty if the area is small")


class Taxonomy(BaseModel):
    categories: list[Top]


SHAPE = """Shape:
- {top_min}-{top_max} top-level areas, each with 2-6 subcategories (no subcategories if an area is small).
- Aim for leaves of roughly 5-25 items. No near-duplicate categories.
- Organise by research problem or agenda (what the work is trying to achieve for safety), not by method, model, \
or venue.
- Write every description as an inclusion criterion: someone who reads only the names and descriptions should be \
able to put each item in the right place, and tell neighbouring categories apart."""

PROPOSE_SYSTEM = """You design the taxonomy for the Shallow Review of Technical AI Safety, a map of the field \
read by expert researchers. Below are all {n} items in this year's review (arXiv papers and LessWrong / Alignment \
Forum posts).

Propose a two-level taxonomy that covers these items well.

{shape}

ITEMS

{corpus}"""

REFINE_SYSTEM = """You maintain the taxonomy for the Shallow Review of Technical AI Safety, a map of the field read \
by expert researchers. A classifier has sorted every item into the current taxonomy using only the category names \
and descriptions. You will see each category's members and the items it put in "other".

Return an improved taxonomy:
- Merge categories that overlap or that the members show are the same thing.
- Split categories that are too big or mix distinct agendas.
- Add categories for coherent groups in "other".
- Drop or fold in categories with very few members.
- Rewrite descriptions so the classifier would place items correctly.
Keep what already works; don't change things for the sake of it.

{shape}"""


def to_categories(tax: Taxonomy) -> list[dict]:
    cats = []
    for t, top in enumerate(tax.categories, 1):
        cats.append({"id": f"c{t}", "name": top.name, "description": top.description, "parent": None})
        for s, sub in enumerate(top.subcategories, 1):
            cats.append({"id": f"c{t}.{s}", "name": sub.name, "description": sub.description, "parent": f"c{t}"})
    return cats


def refine_message(categories: list[dict], assignments: dict[str, str], items: list[dict]) -> str:
    by_pid = {i["pid"]: i for i in items}
    members = defaultdict(list)
    for pid, cid in assignments.items():
        members[cid].append(pid)

    def item_line(pid):
        i = by_pid[pid]
        return f"  - {i['title']}: {i['text'][:200]}"

    lines = ["CURRENT TAXONOMY WITH MEMBERS"]
    leaves = {c["id"] for c in leaf_categories({"categories": categories})}
    for c in categories:
        if c["parent"] is None:
            lines += ["", f"# {c['name']}: {c['description']}"]
        if c["id"] in leaves:
            prefix = "##" if c["parent"] else "## (no subcategories)"
            lines += [f"{prefix} {c['name']} ({len(members[c['id']])} items): {c['description']}"]
            lines += [item_line(p) for p in members[c["id"]]]
    lines += ["", f"# Other ({len(members[OTHER])} items)"] + [item_line(p) for p in members[OTHER]]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=1, help="refinement rounds after the first assignment")
    ap.add_argument("--model", default=llm.DEFAULT_MODEL)
    ap.add_argument("--limit", type=int, help="use a fixed random sample of this many items")
    args = ap.parse_args()

    items = load_items(args.limit)
    small = len(items) < 100
    shape = SHAPE.format(top_min=3 if small else 8, top_max=6 if small else 12)

    log.info(f"proposing a taxonomy for {len(items)} items")
    tax = llm.parse(PROPOSE_SYSTEM.format(n=len(items), shape=shape, corpus=corpus_text(items)),
                    "Propose the taxonomy.", Taxonomy, model=args.model, effort="high", label="propose")
    if tax is None:
        sys.exit("Claude returned no taxonomy.")

    history = []
    for r in range(args.rounds + 1):
        categories = to_categories(tax)
        leaves = leaf_categories({"categories": categories})
        assignments = assign_items(items, leaves, all_categories=categories, model=args.model, label=f"assign r{r}")
        history.append({"round": r, "categories": categories, "assignments": assignments})
        log.info(f"round {r}: {len([c for c in categories if not c['parent']])} top-level, {len(leaves)} leaves; "
                 f"{size_summary(assignments)}; {sum(v == OTHER for v in assignments.values())} in other")
        if r == args.rounds:
            break
        new = llm.parse(REFINE_SYSTEM.format(shape=shape), refine_message(categories, assignments, items), Taxonomy,
                        model=args.model, effort="high", label=f"refine r{r}")
        if new is None:
            log.warning("refinement returned nothing; keeping the current taxonomy")
            break
        tax = new

    write_json(HERE / "output" / "history.json", history)
    write_result(HERE, "1-llm-taxonomy", items, categories, assignments,
                 {"rounds": args.rounds, "model": args.model})
    log.info(llm.usage_report())


if __name__ == "__main__":
    main()
