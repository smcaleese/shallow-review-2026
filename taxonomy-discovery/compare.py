#!/usr/bin/env python3
"""Score every method's output/clusters.json the same way and write results/comparison.md.

Usage (from taxonomy-discovery/):
    uv run python compare.py
"""

import json
import logging
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sklearn.metrics import adjusted_rand_score

from shared import llm
from shared.data import RESULTS, ROOT, load_items, reference_labels, write_json
from shared.score import score_result
from shared.taxonomy import level_assignments

log = logging.getLogger("compare")


def main():
    results = {}
    for path in sorted(ROOT.glob("[0-9]-*/output/clusters.json")):
        results[path.parent.parent.name] = json.loads(path.read_text())
    if not results:
        sys.exit("No method has been run yet: no */output/clusters.json found.")

    all_items = {i["pid"]: i for i in load_items()}
    refs = reference_labels(list(all_items.values()))
    scores = {}
    for name, result in results.items():
        items = [all_items[p] for p in sorted(result["assignments"])]
        log.info(f"scoring {name} ({len(items)} items)")
        scores[name] = score_result(result, items, refs)

    # How much do the methods agree with each other (top level, on the items they share)?
    agreement = {}
    for a, b in combinations(results, 2):
        ta, tb = level_assignments(results[a], "top"), level_assignments(results[b], "top")
        shared = sorted(set(ta) & set(tb))
        if len(shared) >= 10:
            agreement[f"{a} vs {b}"] = round(adjusted_rand_score([ta[p] for p in shared], [tb[p] for p in shared]), 3)

    write_json(RESULTS / "scores.json", {"scores": scores, "method_agreement_ari": agreement})
    (RESULTS / "comparison.md").write_text(render(scores, agreement))
    print((RESULTS / "comparison.md").read_text())
    log.info(llm.usage_report())


def pct(x):
    return f"{100 * x:.0f}%"


def render(scores: dict, agreement: dict) -> str:
    lines = [
        "# Taxonomy method comparison", "",
        "Reassignment accuracy: a fresh classifier, given only category names and descriptions, puts the item back in "
        "the same category. Balance: 1 = equal sizes. vs 2025: agreement of the top level with each item's 2025 "
        "top-level group (from facets-shared's agenda tag); 0 = chance, 1 = identical.", "",
        "| Method | Items | Top cats | Leaves | Other | Balance (top) | Sizes (top) | Reassign top | Reassign leaf "
        "| NMI vs 2025 | ARI vs 2025 |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for name, s in scores.items():
        top, leaf = s["levels"]["top"], s["levels"]["leaf"]
        lines.append(f"| {name} | {s['n_items']} | {top['n_categories']} | {leaf['n_categories']} | "
                     f"{pct(top['other_share'])} | {top['balance']:.2f} | {top['smallest']}–{top['largest']} | "
                     f"{pct(top['reassign_accuracy'])} | {pct(leaf['reassign_accuracy'])} | "
                     f"{s['vs_2025']['nmi']:.2f} | {s['vs_2025']['ari']:.2f} |")
    if agreement:
        lines += ["", "## Agreement between methods (top level, adjusted Rand index)", ""]
        lines += [f"- {pair}: {ari:.2f}" for pair, ari in agreement.items()]
    lines += ["", "## Most-confused category pairs", ""]
    for name, s in scores.items():
        lines.append(f"**{name}**")
        for level in ("top", "leaf"):
            for c in s["levels"][level]["top_confusions"][:3]:
                lines.append(f"- {level}: {' ↔ '.join(c['categories'])} ({c['items']} items)")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
