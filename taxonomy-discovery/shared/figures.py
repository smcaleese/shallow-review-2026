"""The extra figures report.py draws for each method:

- matrix.png: the neighbour graph as a matrix, rows and columns sorted by category. Good categories are dark
  squares on the diagonal; shading off the diagonal is links between categories. No layout, so nothing is distorted.
- category_map.png: one circle per top-level category with lines for links between categories, plus the same
  numbers as a heatmap.
- treemap.png: the taxonomy as nested boxes sized by item count (hierarchy only, no links).

Categories are numbered by size (1 = largest) in every figure, matching graph.png and taxonomy.md.
"""

import textwrap
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import squarify
from matplotlib.colors import LinearSegmentedColormap

from shared.taxonomy import OTHER, level_assignments, top_categories

# Dataviz reference palette, light mode. Sequential = one hue (blue), light -> dark.
SURFACE, TEXT, TEXT_2, MUTED, HAIRLINE = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
BLUE_RAMP = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
SEQUENTIAL = LinearSegmentedColormap.from_list("blue", [SURFACE] + BLUE_RAMP)
LEAF_FILL = "#cde2fb"  # blue step 100

plt.rcParams.update({"font.size": 10, "text.color": TEXT, "axes.labelcolor": TEXT_2,
                     "xtick.color": TEXT_2, "ytick.color": TEXT_2, "axes.edgecolor": HAIRLINE})


def numbered_tops(result: dict) -> tuple[list[dict], dict[str, int], Counter]:
    """Top-level categories that have members, largest first, with their numbers and sizes."""
    sizes = Counter(level_assignments(result, "top").values())
    tops = sorted((c for c in top_categories(result) if sizes[c["id"]]), key=lambda c: -sizes[c["id"]])
    return tops, {c["id"]: n for n, c in enumerate(tops, 1)}, sizes


def short(name: str, width: int) -> str:
    return textwrap.shorten(name, width=width, placeholder="…")


def weight_matrix(g) -> np.ndarray:
    w = np.zeros((g.vcount(), g.vcount()))
    for e in g.es:
        w[e.source, e.target] = w[e.target, e.source] = e["weight"]
    return w


# ---------- 1. sorted adjacency matrix ----------

def draw_matrix(method: str, result: dict, pids: list[str], g, graph_label: str, out):
    tops, number, sizes = numbered_tops(result)
    top = level_assignments(result, "top")
    leaf = result["assignments"]
    w = weight_matrix(g)
    degree = w.sum(axis=1)
    rank = {c["id"]: n for n, c in enumerate(tops)} | {OTHER: len(tops)}
    # Sort by top-level category, then subcategory, then most-linked first.
    order = sorted(range(len(pids)), key=lambda v: (rank[top[pids[v]]], leaf[pids[v]], -degree[v]))
    m = w[np.ix_(order, order)]

    same_top = np.array([[top[pids[a]] == top[pids[b]] != OTHER for b in range(len(pids))] for a in range(len(pids))])
    within = w[same_top].sum() / w.sum()

    fig, ax = plt.subplots(figsize=(11, 10.5), facecolor=SURFACE)
    im = ax.imshow(m, cmap=SEQUENTIAL, vmin=0, vmax=1, interpolation="nearest")
    ax.set_facecolor(SURFACE)

    # Category boundaries: solid for top level, dotted for subcategories.
    sorted_top = [top[pids[v]] for v in order]
    sorted_leaf = [leaf[pids[v]] for v in order]
    ticks, labels, start = [], [], 0
    for k in range(1, len(order) + 1):
        if k == len(order) or sorted_top[k] != sorted_top[k - 1]:
            if k < len(order):
                ax.axhline(k - 0.5, color=TEXT_2, lw=0.8)
                ax.axvline(k - 0.5, color=TEXT_2, lw=0.8)
            cid = sorted_top[k - 1]
            ticks.append((start + k - 1) / 2)
            labels.append(str(number[cid]) if cid in number else "other")
            start = k
        elif sorted_leaf[k] != sorted_leaf[k - 1]:
            ax.axhline(k - 0.5, color=MUTED, lw=0.4, ls=(0, (2, 2)))
            ax.axvline(k - 0.5, color=MUTED, lw=0.4, ls=(0, (2, 2)))
    ax.set_xticks(ticks, labels)
    ax.set_yticks(ticks, labels)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cbar.set_label("Link strength (1 = picked each other every time)")
    cbar.outline.set_visible(False)
    ax.set_title(f"{method}: links between all {len(pids)} items, sorted by category\n"
                 f"{within:.0%} of all link strength falls inside a top-level category. Solid lines separate "
                 f"top-level categories, dotted lines subcategories.\nNumbers match graph.png and taxonomy.md. "
                 f"Graph: {graph_label}.", loc="left", fontsize=11, pad=12)
    fig.savefig(out, dpi=130, facecolor=SURFACE, bbox_inches="tight")
    plt.close(fig)
    return within


# ---------- 2. category-level map + heatmap ----------

def category_density(result: dict, pids: list[str], g) -> tuple[list[dict], np.ndarray, Counter, dict]:
    """Average link strength between items of each pair of top-level categories (diagonal: within one)."""
    tops, number, sizes = numbered_tops(result)
    top = level_assignments(result, "top")
    idx = {c["id"]: k for k, c in enumerate(tops)}
    total = np.zeros((len(tops), len(tops)))
    for e in g.es:
        a, b = top[pids[e.source]], top[pids[e.target]]
        if a in idx and b in idx:
            total[idx[a], idx[b]] += e["weight"]
            if a != b:
                total[idx[b], idx[a]] += e["weight"]
    n = np.array([sizes[c["id"]] for c in tops], dtype=float)
    pairs = np.outer(n, n)
    np.fill_diagonal(pairs, n * (n - 1) / 2)
    return tops, total / pairs, sizes, number


def draw_category_map(method: str, result: dict, pids: list[str], g, graph_label: str, out):
    tops, dens, sizes, number = category_density(result, pids, g)
    k = len(tops)
    fig, (ax_map, ax_heat) = plt.subplots(1, 2, figsize=(23, 10), facecolor=SURFACE,
                                          gridspec_kw={"width_ratios": [1.1, 1], "wspace": 0.55})

    # Map: categories on a circle (largest at the top, clockwise), lines for the strongest cross links.
    angles = np.pi / 2 - 2 * np.pi * np.arange(k) / k
    xy = np.c_[np.cos(angles), np.sin(angles)]
    off = dens.copy()
    np.fill_diagonal(off, 0)
    cut = np.quantile(off[np.triu_indices(k, 1)], 0.6) if k > 2 else 0
    peak = off.max() or 1
    for a in range(k):
        for b in range(a + 1, k):
            if off[a, b] > cut:
                ax_map.plot(*xy[[a, b]].T, color=BLUE_RAMP[3], lw=0.5 + 9 * off[a, b] / peak,
                            alpha=0.25 + 0.6 * off[a, b] / peak, zorder=1, solid_capstyle="round")
    max_size = max(sizes[c["id"]] for c in tops)
    for i, c in enumerate(tops):
        r = 0.05 + 0.09 * np.sqrt(sizes[c["id"]] / max_size)
        ax_map.add_patch(plt.Circle(xy[i], r, color=BLUE_RAMP[4], ec=SURFACE, lw=2, zorder=2))
        ax_map.text(*xy[i], str(number[c["id"]]), ha="center", va="center", color=SURFACE, fontsize=12,
                    fontweight="bold", zorder=3)
        lx, ly = xy[i] * (1.0 + r + 0.06)
        ha = "left" if lx > 0.3 else "right" if lx < -0.3 else "center"
        va = "center" if ha != "center" else ("bottom" if ly > 0 else "top")
        ax_map.text(lx, ly, "\n".join(textwrap.wrap(f"{c['name']} ({sizes[c['id']]})", 26)), ha=ha,
                    va=va, fontsize=10, color=TEXT)
    ax_map.set_xlim(-1.85, 1.85)
    ax_map.set_ylim(-1.6, 1.6)
    ax_map.set_aspect("equal")
    ax_map.axis("off")
    ax_map.set_title(f"{method}: how top-level categories connect\nCircle area = items. Lines = the 40% most "
                     f"strongly linked pairs; thicker = stronger average link between their items.\n"
                     f"Graph: {graph_label}.", loc="left", fontsize=11)

    # Heatmap: the same numbers, every pair. Diagonal (within a category) is on a different scale, so it's
    # shown as text on a neutral fill instead of coloured.
    shown = np.ma.masked_array(off, mask=np.eye(k, dtype=bool))
    im = ax_heat.imshow(shown, cmap=SEQUENTIAL, vmin=0, vmax=peak)
    for a in range(k):
        for b in range(k):
            v = dens[a, b] * 100
            if a == b:
                ax_heat.add_patch(plt.Rectangle((b - 0.5, a - 0.5), 1, 1, color=HAIRLINE))
                ax_heat.text(b, a, f"{v:.0f}", ha="center", va="center", fontsize=9, color=TEXT, fontweight="bold")
            else:
                dark = off[a, b] > 0.55 * peak
                ax_heat.text(b, a, f"{v:.1f}", ha="center", va="center", fontsize=8,
                             color=SURFACE if dark else TEXT_2)
    labels = [f"{number[c['id']]}  {short(c['name'], 34)}" for c in tops]
    ax_heat.set_yticks(range(k), labels, fontsize=9)
    ax_heat.set_xticks(range(k), [str(number[c["id"]]) for c in tops])
    ax_heat.tick_params(length=0)
    for spine in ax_heat.spines.values():
        spine.set_visible(False)
    cbar = fig.colorbar(im, ax=ax_heat, fraction=0.04, pad=0.02)
    cbar.outline.set_visible(False)
    cbar.set_label("Average link strength between items (×100 in cells)")
    ax_heat.set_title("Average link strength ×100. Grey diagonal: within the category (higher = tighter).\n"
                      "Off-diagonal: between two categories (higher = more overlap).", loc="left", fontsize=11)
    fig.savefig(out, dpi=110, facecolor=SURFACE, bbox_inches="tight")
    plt.close(fig)


# ---------- 4. treemap ----------

def draw_treemap(method: str, result: dict, out):
    tops, number, sizes = numbered_tops(result)
    leaf_sizes = Counter(result["assignments"].values())
    children = {c["id"]: [s for s in result["categories"] if s["parent"] == c["id"] and leaf_sizes[s["id"]]]
                for c in tops}
    W, H, FIG_W = 100.0, 62.0, 20.0  # treemap units; figure width in inches
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_W * H / W), facecolor=SURFACE)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)  # so axes units -> inches is known
    per_inch = FIG_W * 0.98 / W
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")

    def fits(text, w, h, size, bold=False):
        chars = max(1, int(w * per_inch * 72 / (size * (0.68 if bold else 0.6))))
        lines = textwrap.wrap(text, chars, break_long_words=False)
        too_wide = any(len(line) > chars for line in lines)
        return lines, not too_wide and len(lines) * size * 1.25 / 72 <= h * per_inch - 0.08

    def label(x, y, w, h, text, size, weight="normal", color=TEXT):
        for s in (size, size - 1.5, size - 3):
            lines, ok = fits(text, w - 0.8, h - 0.4, s, weight == "bold")
            if ok:
                ax.text(x + 0.5, y + 0.4, "\n".join(lines), fontsize=s, va="top", ha="left", color=color,
                        fontweight=weight, linespacing=1.15)
                return

    boxes = squarify.squarify(squarify.normalize_sizes([sizes[c["id"]] for c in tops], W, H), 0, 0, W, H)
    for c, box in zip(tops, boxes):
        x, y, w, h = box["x"], box["y"], box["dx"], box["dy"]
        ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=SURFACE, edgecolor=SURFACE, lw=0))
        title = f"{number[c['id']]}. {c['name']} ({sizes[c['id']]})"
        title_lines, _ = fits(title, w - 0.8, h, 11.5, bold=True)
        header = min(h * 0.45, len(title_lines) * 11.5 * 1.2 / 72 / per_inch + 0.3)
        label(x, y, w, header + 0.6, title, 11.5, "bold")
        inner = (x + 0.35, y + header + 0.5, max(w - 0.7, 0.1), max(h - header - 0.85, 0.1))
        subs = sorted(children[c["id"]], key=lambda s: -leaf_sizes[s["id"]])
        own = leaf_sizes[c["id"]]  # items directly in the top category, not in a subcategory
        parts = [(s["name"], leaf_sizes[s["id"]]) for s in subs] + ([("(no subcategory)", own)] if own else [])
        sub_boxes = squarify.squarify(squarify.normalize_sizes([n for _, n in parts], inner[2], inner[3]), *inner)
        for (name, n), sb in zip(parts, sub_boxes):
            ax.add_patch(plt.Rectangle((sb["x"], sb["y"]), sb["dx"], sb["dy"], facecolor=LEAF_FILL,
                                       edgecolor=SURFACE, lw=2))
            label(sb["x"], sb["y"], sb["dx"], sb["dy"], f"{name} ({n})", 9.5, color=TEXT)
        ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, edgecolor=TEXT_2, lw=1.2))
    if sizes.get(OTHER):
        ax.text(0, H + 1.5, f"{sizes[OTHER]} items in other (not shown).", fontsize=10, color=TEXT_2, va="top")
    ax.set_title(f"{method}: the taxonomy as nested boxes, area = number of items\nOutlined boxes are top-level "
                 "categories (numbered by size, as in graph.png); shaded boxes inside are subcategories.",
                 loc="left", fontsize=12, pad=10)
    fig.savefig(out, dpi=110, facecolor=SURFACE, bbox_inches="tight")
    plt.close(fig)
