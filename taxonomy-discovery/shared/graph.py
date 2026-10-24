"""Nearest-neighbour graph -> Leiden communities at two levels -> LLM-written names.

Methods 2 and 3 differ only in where the neighbour lists come from; everything here is shared so the comparison
isolates that one difference. The LLM only names the clusters at the end; it doesn't change membership.
"""

import logging
import math
from collections import Counter, defaultdict

import igraph as ig
import leidenalg
from pydantic import BaseModel, Field

from shared import llm
from shared.taxonomy import OTHER

log = logging.getLogger("graph")


def build_graph(n: int, votes: dict[tuple[int, int], float]) -> ig.Graph:
    """Undirected weighted graph from directed votes (i listed j as a neighbour, weight 0-1).

    Edge weight = average of the two directions, so a mutual pick weighs 1 and a one-way pick 0.5."""
    weights = defaultdict(float)
    for (i, j), w in votes.items():
        if i != j:
            weights[(min(i, j), max(i, j))] += w / 2
    g = ig.Graph(n=n, edges=list(weights), directed=False)
    g.es["weight"] = list(weights.values())
    return g


def leiden(g: ig.Graph, resolution: float, seed: int = 0) -> list[int]:
    part = leidenalg.find_partition(g, leidenalg.RBConfigurationVertexPartition, weights="weight",
                                    resolution_parameter=resolution, seed=seed, n_iterations=-1)
    return list(part.membership)


def leiden_target(g: ig.Graph, target: int, min_size: int = 3, seed: int = 0) -> tuple[list[int], float]:
    """Search the resolution so the number of clusters with >= min_size members is close to `target`."""
    lo, hi = math.log(0.01), math.log(20.0)
    best = None
    for _ in range(25):
        mid = (lo + hi) / 2
        membership = leiden(g, math.exp(mid), seed)
        k = sum(1 for n in Counter(membership).values() if n >= min_size)
        if best is None or abs(k - target) < abs(best[2] - target):
            best = (membership, math.exp(mid), k)
        if k == target:
            break
        if k < target:
            lo = mid
        else:
            hi = mid
    return best[0], best[1]


def absorb_small(g: ig.Graph, membership: list[int], min_size: int) -> list[int]:
    """Move members of clusters smaller than min_size into the large cluster they have the most edge weight to.

    Ranks large clusters by size (0 = largest). Nodes with no edges to any large cluster get -1."""
    sizes = Counter(membership)
    ranked = [c for c, n in sizes.most_common() if n >= min_size]
    rank = {c: k for k, c in enumerate(ranked)}
    out = [rank.get(c, -1) for c in membership]
    for v in range(g.vcount()):
        if out[v] == -1:
            pull = defaultdict(float)
            for e in g.incident(v):
                u = g.es[e].target if g.es[e].source == v else g.es[e].source
                if membership[u] in rank:
                    pull[rank[membership[u]]] += g.es[e]["weight"]
            if pull:
                out[v] = max(pull, key=pull.get)
    return out


def two_level_clusters(g: ig.Graph, top_target: int = 10, sub_size: int = 10, min_size: int = 3,
                       seed: int = 0) -> tuple[dict[int, str], dict]:
    """node -> "3" (top only), "3.1" (top + sub), or OTHER.

    Top level: Leiden tuned to ~top_target clusters. Sub level: Leiden on each top cluster's own subgraph, tuned to
    ~size/sub_size clusters. Members of clusters smaller than min_size join the large cluster they're most linked
    to; only nodes linked to no large cluster go to OTHER (top) or stay at the parent (sub)."""
    top_raw, resolution = leiden_target(g, top_target, min_size, seed)
    top = absorb_small(g, top_raw, min_size)
    labels, params = {}, {"top_resolution": round(resolution, 4), "sub_resolutions": {}}
    for c in sorted(set(top) - {-1}):
        nodes = [v for v in range(g.vcount()) if top[v] == c]
        name = str(c + 1)
        target = round(len(nodes) / sub_size)
        if target < 2:
            labels.update({v: name for v in nodes})
            continue
        sg = g.induced_subgraph(nodes)
        sub_raw, sub_res = leiden_target(sg, target, min_size, seed)
        sub = absorb_small(sg, sub_raw, min_size)
        params["sub_resolutions"][name] = round(sub_res, 4)
        if len(set(sub) - {-1}) < 2:
            labels.update({v: name for v in nodes})
            continue
        for v, s in zip(nodes, sub):
            labels[v] = f"{name}.{s + 1}" if s >= 0 else name
    for v in range(g.vcount()):
        labels.setdefault(v, OTHER)
    return labels, params


# ---------- naming ----------

class SubName(BaseModel):
    key: str = Field(description="The subcluster key exactly as given, e.g. '3.1'")
    name: str = Field(description="2-6 words")
    description: str = Field(description="1-2 sentences saying what belongs here, usable to decide membership")


class ClusterName(BaseModel):
    name: str = Field(description="2-6 words")
    description: str = Field(description="1-2 sentences saying what belongs here, usable to decide membership")
    subclusters: list[SubName]


NAME_SYSTEM = """You name clusters of AI safety research (arXiv papers and LessWrong / Alignment Forum posts) for the \
Shallow Review of Technical AI Safety. A clustering algorithm grouped the items; you only name and describe the \
groups, you don't move items.

Name each group for the research problem or agenda its members share. Write each description as an inclusion \
criterion: someone reading only the descriptions should be able to put a new item in the right group. If a group \
looks mixed, describe what most members share. Keep sibling subcluster names distinct from each other."""


def name_clusters(items: list[dict], labels: dict[str, str], model: str = llm.DEFAULT_MODEL) -> list[dict]:
    """Categories in the shared result format, named by Claude from their members. labels: pid -> "3.1"/"3"/OTHER."""
    by_pid = {i["pid"]: i for i in items}
    groups = defaultdict(lambda: defaultdict(list))
    for pid, label in labels.items():
        if label != OTHER:
            top, _, sub = label.partition(".")
            groups[top][label if sub else ""].append(pid)

    def describe(top):
        parts = [f"Top-level cluster {top}."]
        for key, pids in sorted(groups[top].items()):
            heading = f"Subcluster {key}" if key else "Members not in any subcluster"
            parts.append(f"\n## {heading} ({len(pids)} items)")
            parts += [f"- {by_pid[p]['title']}: {by_pid[p]['text'][:300]}" for p in pids]
        subs = sorted(k for k in groups[top] if k)
        parts.append(f"\nName the top-level cluster and each subcluster ({', '.join(subs) or 'none'}).")
        return "\n".join(parts)

    def run(top):
        return top, llm.parse(NAME_SYSTEM, describe(top), ClusterName, model=model, label=f"name cluster {top}")

    categories = []
    for top, named in llm.run_parallel(run, [(t,) for t in sorted(groups, key=int)]):
        cid = f"c{top}"
        categories.append({"id": cid, "name": named.name if named else f"Cluster {top}",
                           "description": named.description if named else "", "parent": None})
        sub_names = {s.key: s for s in (named.subclusters if named else [])}
        for key in sorted(k for k in groups[top] if k):
            s = sub_names.get(key)
            categories.append({"id": f"c{key}", "name": s.name if s else f"Cluster {key}",
                               "description": s.description if s else "", "parent": cid})
    return categories


def graph_to_result(items: list[dict], votes: dict[tuple[int, int], float], *, top_target: int, sub_size: int,
                    model: str, seed: int = 0) -> tuple[list[dict], dict[str, str], dict]:
    """Votes between item indexes -> (categories, assignments, params) in the shared result format."""
    g = build_graph(len(items), votes)
    node_labels, params = two_level_clusters(g, top_target=top_target, sub_size=sub_size, seed=seed)
    labels = {items[v]["pid"]: lab for v, lab in node_labels.items()}
    log.info(f"graph: {g.vcount()} nodes, {g.ecount()} edges; "
             f"{len({l.split('.')[0] for l in labels.values() if l != OTHER})} top clusters, "
             f"{sum(l == OTHER for l in labels.values())} items in other")
    categories = name_clusters(items, labels, model=model)
    assignments = {pid: (OTHER if lab == OTHER else f"c{lab}") for pid, lab in labels.items()}
    params |= {"edges": g.ecount(), "top_target": top_target, "sub_size": sub_size}
    return categories, assignments, params
