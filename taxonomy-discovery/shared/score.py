"""Score one result: does each item fit its category, are categories distinct, and how does it compare to 2025?"""

import math
from collections import Counter

from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

from shared import llm
from shared.taxonomy import OTHER, assign_items, leaf_categories, level_assignments, top_categories


def balance(assignments: dict[str, str]) -> float:
    """Size entropy / max entropy over the non-other categories: 1 = all equal, near 0 = one giant category."""
    sizes = Counter(v for v in assignments.values() if v != OTHER)
    if len(sizes) < 2:
        return 0.0
    total = sum(sizes.values())
    entropy = -sum(n / total * math.log(n / total) for n in sizes.values())
    return entropy / math.log(len(sizes))


def score_result(result: dict, items: list[dict], refs: dict[str, str], model: str = llm.DEFAULT_MODEL) -> dict:
    names = {c["id"]: c["name"] for c in result["categories"]} | {OTHER: "other"}
    scores = {"method": result["method"], "n_items": len(items), "levels": {}}

    for level, cats in (("top", top_categories(result)), ("leaf", leaf_categories(result))):
        assigned = level_assignments(result, level)
        # Fit + distinctness: a fresh classifier sees only names and descriptions. Shuffled batches so the
        # prompts differ from any assignment step the method ran itself.
        reassigned = assign_items(items, cats, all_categories=result["categories"], model=model, shuffle_seed=1,
                                  label=f"score {result['method']} {level}")
        pids = [i["pid"] for i in items]
        agree = sum(reassigned[p] == assigned[p] for p in pids)
        pairs = Counter(frozenset((assigned[p], reassigned[p])) for p in pids if reassigned[p] != assigned[p])
        sizes = Counter(assigned[p] for p in pids)
        scores["levels"][level] = {
            "n_categories": len(cats),
            "other_share": round(sizes.get(OTHER, 0) / len(pids), 3),
            "balance": round(balance(assigned), 3),
            "largest": max((n for c, n in sizes.items() if c != OTHER), default=0),
            "smallest": min((n for c, n in sizes.items() if c != OTHER), default=0),
            "reassign_accuracy": round(agree / len(pids), 3),
            "top_confusions": [{"categories": sorted(names[c] for c in pair), "items": n}
                               for pair, n in pairs.most_common(5)],
            "reassigned": reassigned,
        }

    top = level_assignments(result, "top")
    pids = [i["pid"] for i in items]
    scores["vs_2025"] = {
        "nmi": round(normalized_mutual_info_score([refs[p] for p in pids], [top[p] for p in pids]), 3),
        "ari": round(adjusted_rand_score([refs[p] for p in pids], [top[p] for p in pids]), 3),
    }
    return scores
