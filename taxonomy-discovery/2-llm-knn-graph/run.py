#!/usr/bin/env python3
"""Method 2: LLM-only nearest-neighbour graph + Leiden.

Claude sees the whole set of items (cached in the system prompt) and, for each item, lists the k items nearest to it
by research agenda. Each pass shows the items in a different order to reduce position bias; edge weights average
over passes and over both directions. Then the shared Leiden + naming step runs, exactly as in method 3.

Usage (from taxonomy-discovery/):
    uv run python 2-llm-knn-graph/run.py
    uv run python 2-llm-knn-graph/run.py --limit 40 --passes 1    # smoke test on a sample
"""

import argparse
import logging
import random
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from pydantic import BaseModel, Field

from shared import llm
from shared.data import corpus_text, load_items, size_summary, write_json
from shared.graph import graph_to_result
from shared.taxonomy import write_result

log = logging.getLogger("llm-knn")

SYSTEM = """You map the field of technical AI safety for the Shallow Review of Technical AI Safety. Below are all \
{n} items in this year's review (arXiv papers and LessWrong / Alignment Forum posts), each with an id in brackets.

You will be given target item ids. For each target, list the {k} OTHER items nearest to it by research agenda: \
items working on the same research problem or advancing the same line of work, so that a reader of the review \
would expect to find them in the same section. Sharing a method, a model, or a buzzword is not enough on its own. \
Order the list from nearest to least near. Use only ids that appear below, and never the target itself.

ITEMS

{corpus}"""


class Neighbours(BaseModel):
    target: str
    nearest: list[str] = Field(description="ids of the nearest items, nearest first")


class NeighbourBatch(BaseModel):
    results: list[Neighbours]


def order_for_pass(items: list[dict], p: int) -> list[dict]:
    if p == 0:
        return list(items)
    if p == 1:
        return list(reversed(items))
    shuffled = list(items)
    random.Random(p).shuffle(shuffled)
    return shuffled


def run_pass(items: list[dict], p: int, k: int, batch_size: int, model: str, effort: str) -> dict[str, list[str]]:
    valid = {i["pid"] for i in items}
    system = SYSTEM.format(n=len(items), k=k, corpus=corpus_text(order_for_pass(items, p)))
    targets = [i["pid"] for i in items]
    batches = [targets[s:s + batch_size] for s in range(0, len(targets), batch_size)]

    def run(batch):
        user = f"Targets: {', '.join(batch)}\n\nFor each target, list its {k} nearest items."
        out = llm.parse(system, user, NeighbourBatch, model=model, effort=effort, label=f"pass {p} {batch[0]}")
        found = {}
        for r in (out.results if out else []):
            if r.target in batch:
                seen = []
                for pid in r.nearest:
                    pid = pid.strip().strip("[]")
                    if pid in valid and pid != r.target and pid not in seen:
                        seen.append(pid)
                found[r.target] = seen[:k]
        return found

    # First call alone so it writes the prompt cache; the rest then read it.
    neighbours = run(batches[0])
    for part in llm.run_parallel(run, [(b,) for b in batches[1:]]):
        neighbours.update(part)
    missing = [t for t in targets if t not in neighbours]
    if missing:
        log.warning(f"pass {p}: no neighbours for {len(missing)} targets, retrying one at a time")
        for part in llm.run_parallel(run, [([t],) for t in missing]):
            neighbours.update(part)
    invalid = sum(k - len(v) for v in neighbours.values())
    log.info(f"pass {p}: {len(neighbours)}/{len(targets)} targets answered; {invalid} neighbour slots unfilled "
             f"(invalid, duplicate or missing ids). {llm.usage_report()}")
    return neighbours


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=15, help="neighbours per item")
    ap.add_argument("--passes", type=int, default=2, help="item orderings to average over (1 = original order)")
    ap.add_argument("--batch-size", type=int, default=5, help="targets per Claude call")
    ap.add_argument("--top-target", type=int, default=10, help="roughly how many top-level clusters")
    ap.add_argument("--sub-size", type=int, default=10, help="roughly how many items per subcluster")
    ap.add_argument("--model", default=llm.DEFAULT_MODEL)
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--limit", type=int, help="use a fixed random sample of this many items")
    args = ap.parse_args()

    items = load_items(args.limit)
    k = min(args.k, len(items) - 1)
    index = {i["pid"]: n for n, i in enumerate(items)}
    votes = defaultdict(float)
    all_passes = []
    for p in range(args.passes):
        neighbours = run_pass(items, p, k, args.batch_size, args.model, args.effort)
        all_passes.append(neighbours)
        for target, nearest in neighbours.items():
            for pid in nearest:
                votes[(index[target], index[pid])] += 1 / args.passes
    write_json(HERE / "output" / "neighbours.json", {f"pass {p}": n for p, n in enumerate(all_passes)})
    if args.passes > 1:
        overlaps = [len(set(all_passes[0].get(t, [])) & set(all_passes[1].get(t, []))) / k for t in index]
        log.info(f"passes 0 and 1 agree on {100 * sum(overlaps) / len(overlaps):.0f}% of neighbours")

    categories, assignments, params = graph_to_result(items, dict(votes), top_target=args.top_target,
                                                      sub_size=args.sub_size, model=args.model)
    write_result(HERE, "2-llm-knn-graph", items, categories, assignments,
                 params | {"k": k, "passes": args.passes, "model": args.model, "effort": args.effort})
    log.info(f"top level: {size_summary({p: c.split('.')[0] for p, c in assignments.items()})}")
    log.info(llm.usage_report())


if __name__ == "__main__":
    main()
