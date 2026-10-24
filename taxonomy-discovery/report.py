#!/usr/bin/env python3
"""For each method, write output/taxonomy.md (the taxonomy as a document) and output/graph.png (its clusters drawn
on a nearest-neighbour graph).

Methods 2 and 3 are drawn on their own neighbour graphs. Method 1 has no graph of its own, so its categories are
drawn on method 2's LLM neighbour graph (same layout as method 2's image), which shows how its top-down categories
sit on the bottom-up structure. No API calls.

Usage (from taxonomy-discovery/):
    uv run python report.py
"""

import json
import sys
import textwrap
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np

from shared import figures
from shared.data import RESULTS, load_items
from shared.graph import build_graph
from shared.taxonomy import OTHER, level_assignments, top_categories

# Colours from the dataviz reference palette (light mode). Clusters are identified by their labels, not by colour:
# ten categories can't be told apart by colour on a scatter, so one highlight hue + small multiples instead.
SURFACE, TEXT, TEXT_2, MUTED, HAIRLINE, HIGHLIGHT = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#2a78d6"
GRAPH_SOURCE = {"1-llm-taxonomy": "2-llm-knn-graph", "4-human-taxonomy": "2-llm-knn-graph"}  # no graph of their own


def load_votes(method: str, index: dict[str, int]) -> dict[tuple[int, int], float]:
    data = json.loads((ROOT / method / "output" / "neighbours.json").read_text())
    passes = list(data.values()) if all(k.startswith("pass ") for k in data) else [data]
    votes = defaultdict(float)
    for neighbours in passes:
        for target, nearest in neighbours.items():
            for pid in nearest:
                if target in index and pid in index:
                    votes[(index[target], index[pid])] += 1 / len(passes)
    return votes


def layout(g, groups: list[str], pull: float = 3.0, seed: int = 0) -> np.ndarray:
    """Force-directed layout where links inside a top-level category count `pull` times as much, so categories
    form visible regions. Links across categories still act, so related categories sit near each other."""
    w = [e["weight"] * (pull if groups[e.source] == groups[e.target] != OTHER else 1.0) for e in g.es]
    start = np.random.default_rng(seed).uniform(-1, 1, size=(g.vcount(), 2)).tolist()
    coords = np.array(g.layout_fruchterman_reingold(weights=w, niter=3000, seed=start).coords)
    coords -= coords.mean(axis=0)
    return coords / np.abs(coords).max()


def short(name: str, width: int) -> str:
    return textwrap.shorten(name, width=width, placeholder="…")


def draw(method: str, result: dict, items: list[dict], graph_method: str, out: Path):
    pids = [i["pid"] for i in items]
    index = {p: n for n, p in enumerate(pids)}
    g = build_graph(len(pids), load_votes(graph_method, index))
    top = level_assignments(result, "top")
    xy = layout(g, [top[p] for p in pids])
    # Draw only mutual links (both items listed each other); one-way links still shape the layout.
    keep = np.array(g.es["weight"]) >= 0.99
    edges = np.array(g.get_edgelist())[keep]
    weights = np.array(g.es["weight"])[keep]

    leaf = result["assignments"]
    names = {c["id"]: c["name"] for c in result["categories"]}
    sizes = Counter(top.values())
    tops = sorted((c for c in top_categories(result) if sizes[c["id"]]), key=lambda c: -sizes[c["id"]])
    number = {c["id"]: n for n, c in enumerate(tops, 1)}
    halo = [pe.withStroke(linewidth=3, foreground=SURFACE)]

    ncols = 5
    nrows = -(-len(tops) // ncols)
    fig = plt.figure(figsize=(20, 11 + 4.2 * nrows), facecolor=SURFACE)
    grid = fig.add_gridspec(1 + nrows, ncols, height_ratios=[11] + [4.2] * nrows, hspace=0.25, wspace=0.05)

    def base(ax, node_color, node_size, edge_alpha):
        ax.set_facecolor(SURFACE)
        ax.axis("off")
        segs = np.stack([xy[edges[:, 0]], xy[edges[:, 1]]], axis=1)
        from matplotlib.collections import LineCollection
        ax.add_collection(LineCollection(segs, colors=HAIRLINE, linewidths=0.3 + 0.5 * weights, alpha=edge_alpha,
                                         zorder=1))
        ax.scatter(xy[:, 0], xy[:, 1], s=node_size, c=node_color, linewidths=0.6, edgecolors=SURFACE, zorder=2)
        ax.set_xlim(-1.08, 1.08)
        ax.set_ylim(-1.08, 1.08)
        ax.set_aspect("equal")

    # Overview: every item, a numbered marker per top-level category at its members' median position, and a
    # numbered legend beside it with each category's size and subcategories.
    ax = fig.add_subplot(grid[0, :3])
    base(ax, MUTED, 22, 0.9)
    for c in tops:
        members = [index[p] for p in pids if top[p] == c["id"]]
        cx, cy = np.median(xy[members], axis=0)
        ax.text(cx, cy, str(number[c["id"]]), ha="center", va="center", fontsize=12, color=SURFACE,
                fontweight="bold", zorder=4, bbox=dict(boxstyle="circle,pad=0.35", fc=TEXT, ec=SURFACE, lw=2))
    legend = fig.add_subplot(grid[0, 3:])
    legend.axis("off")
    subs_of = defaultdict(list)
    for c in result["categories"]:
        if c["parent"]:
            subs_of[c["parent"]].append(c["name"])
    wrapped = {c["id"]: textwrap.wrap("; ".join(subs_of[c["id"]]), 70) for c in tops}
    needed = sum(0.034 + 0.027 * len(wrapped[c["id"]]) + 0.012 for c in tops)
    scale = min(1.0, 1.0 / needed)  # shrink spacing and text so long legends stay inside the overview row
    y = 1.0
    for c in tops:
        legend.text(0, y, f"{number[c['id']]}  {c['name']} ({sizes[c['id']]})", fontsize=11 * max(scale, 0.8),
                    color=TEXT, fontweight="bold", va="top", transform=legend.transAxes)
        y -= 0.034 * scale
        for line in wrapped[c["id"]]:
            legend.text(0.035, y, line, fontsize=9 * max(scale, 0.8), color=TEXT_2, va="top",
                        transform=legend.transAxes)
            y -= 0.027 * scale
        y -= 0.012 * scale
    n_other = sizes.get(OTHER, 0)
    drawn_on = "its own" if graph_method == method else f"the {graph_method} neighbour"
    ax.set_title(f"{method}: {len(pids)} items, {len(tops)} top-level categories"
                 + (f", {n_other} in other" if n_other else "")
                 + f"\nEach dot is an item; lines link items that picked each other as nearest neighbours "
                   f"({drawn_on} graph).\nThe layout pulls items in the same category together. Numbers sit at each "
                   "category's median position; panels below highlight one category each.",
                 loc="left", fontsize=13, color=TEXT, pad=12)

    # Small multiples: one category highlighted per panel, subcategories labelled.
    for k, c in enumerate(tops):
        ax = fig.add_subplot(grid[1 + k // ncols, k % ncols])
        inside = np.array([top[p] == c["id"] for p in pids])
        base(ax, np.where(inside, HIGHLIGHT, HAIRLINE), np.where(inside, 16, 6), 0.5)
        subs = Counter(leaf[p] for p in pids if top[p] == c["id"] and leaf[p] != c["id"])
        spots = sorted(((*np.median(xy[[index[p] for p in pids if leaf[p] == sub]], axis=0), sub)
                        for sub, n in subs.items() if n >= 3), key=lambda s: -s[1])
        placed = []
        for sx, sy, sub in spots:  # push a label down until it clears the ones already placed
            while any(abs(sy - py) < 0.11 and abs(sx - px) < 0.9 for px, py in placed):
                sy -= 0.03
            placed.append((sx, sy))
            ax.text(sx, sy, short(names[sub], 26), ha="center", va="center", fontsize=7.5, color=TEXT_2,
                    path_effects=halo, zorder=4)
        ax.set_title("\n".join(textwrap.wrap(f"{number[c['id']]}. {c['name']} ({sizes[c['id']]})", 34)),
                     fontsize=10, color=TEXT, loc="left")

    fig.savefig(out, dpi=110, facecolor=SURFACE, bbox_inches="tight")
    plt.close(fig)


def write_taxonomy_md(method: str, result: dict, items: list[dict], scores: dict | None, out: Path):
    by_pid = {i["pid"]: i for i in items}
    top = level_assignments(result, "top")
    sizes = Counter(top.values()) | Counter(result["assignments"].values())
    children = defaultdict(list)
    for c in result["categories"]:
        if c["parent"]:
            children[c["parent"]].append(c)
    members = defaultdict(list)
    for pid, cid in result["assignments"].items():
        members[cid].append(pid)

    def examples(cid, n=3):
        return [f"  - *{by_pid[p]['title']}*" for p in members[cid][:n]]

    tops = sorted((c for c in top_categories(result) if sizes[c["id"]]), key=lambda c: -sizes[c["id"]])
    lines = [f"# Taxonomy from {method}", "",
             f"{len(items)} items (arXiv papers and LW/AF posts), {len(tops)} top-level areas, "
             f"{sum(len(children[c['id']]) or 1 for c in tops)} leaf categories"
             + (f", {sizes[OTHER]} items in other" if sizes.get(OTHER) else "") + ".", ""]
    if scores:
        t, l = scores["levels"]["top"], scores["levels"]["leaf"]
        lines += [f"Scores: reassignment accuracy {t['reassign_accuracy']:.0%} (top) / {l['reassign_accuracy']:.0%} "
                  f"(leaf), balance {t['balance']:.2f}, agreement with 2025 groups NMI {scores['vs_2025']['nmi']:.2f}. "
                  "See `results/comparison.md`.", ""]
    lines += ["![The taxonomy as nested boxes](treemap.png)", "",
              "More figures: [graph](graph.png) (items on the neighbour graph), [matrix](matrix.png) (links sorted "
              "by category), [category map](category_map.png) (how categories connect).", "", "## Overview", ""]
    lines += [f"{n}. **{c['name']}** ({sizes[c['id']]}): " + ", ".join(s["name"] for s in children[c["id"]])
              for n, c in enumerate(tops, 1)]
    for n, c in enumerate(tops, 1):
        lines += ["", f"## {n}. {c['name']} ({sizes[c['id']]} items)", "", c["description"], ""]
        if members[c["id"]]:
            lines += [f"- Not in a subcategory ({len(members[c['id']])}), e.g.:"] + examples(c["id"])
        for s in sorted(children[c["id"]], key=lambda s: -sizes[s["id"]]):
            lines += [f"- **{s['name']}** ({sizes[s['id']]}): {s['description']} Examples:"] + examples(s["id"])
    if members.get(OTHER):
        lines += ["", f"## Other ({sizes[OTHER]} items)", ""] + examples(OTHER, 10)
    out.write_text("\n".join(lines) + "\n")


def main():
    all_items = {i["pid"]: i for i in load_items()}
    scores_path = RESULTS / "scores.json"
    scores = json.loads(scores_path.read_text())["scores"] if scores_path.exists() else {}
    for path in sorted(ROOT.glob("[0-9]-*/output/clusters.json")):
        method = path.parent.parent.name
        result = json.loads(path.read_text())
        items = [all_items[p] for p in sorted(result["assignments"])]
        graph_method = GRAPH_SOURCE.get(method, method)
        graph_neighbours = ROOT / graph_method / "output" / "neighbours.json"
        out = path.parent
        figures.draw_treemap(method, result, out / "treemap.png")
        written = ["taxonomy.md", "treemap.png"]
        if graph_neighbours.exists():
            graph_pids = set(json.loads(graph_neighbours.read_text()).get("pass 0", {})) or \
                set(json.loads(graph_neighbours.read_text()))
            if graph_pids >= set(result["assignments"]):
                draw(method, result, items, graph_method, out / "graph.png")
                pids = [i["pid"] for i in items]
                g = build_graph(len(pids), load_votes(graph_method, {p: n for n, p in enumerate(pids)}))
                label = "its own" if graph_method == method else f"{graph_method}'s LLM neighbour graph"
                within = figures.draw_matrix(method, result, pids, g, label, out / "matrix.png")
                print(f"{method}: {within:.0%} of link strength inside top-level categories ({label})")
                figures.draw_category_map(method, result, pids, g, label, out / "category_map.png")
                written += ["graph.png", "matrix.png", "category_map.png"]
            else:
                print(f"{method}: {graph_method}'s graph doesn't cover the same items; skipping graph images")
        write_taxonomy_md(method, result, items, scores.get(method), out / "taxonomy.md")
        print(f"{method}: wrote {', '.join(written)}")


if __name__ == "__main__":
    main()
