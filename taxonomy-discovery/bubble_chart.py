"""Bubble chart of the data-driven taxonomy: one bubble per agenda, sized by its number of sources.

The sizes are the cross-method estimates in data-driven-taxonomy.md (the median, over the six taxonomy-discovery
methods, of the items in the categories matched to each agenda; for an agenda merged from several candidates, the
sum of their medians), so the chart summarises all methods at once rather
than one of them. Bubbles are coloured and grouped by top-level area. Free (no LLM calls).

    uv run python bubble_chart.py        # writes results/agenda-bubbles.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

HERE = Path(__file__).resolve().parent
OUT = HERE / "results" / "agenda-bubbles.png"
TOTAL = 624  # sources in the taxonomy-discovery snapshot

# (area, colour) in the categorical order of the dataviz reference palette
AREAS = {
    "Training": "#2a78d6",
    "Inspection": "#eb6834",
    "Deployment": "#1baf7a",
    "Strategy": "#eda100",
}

# (agenda, area, items: cross-method estimate from data-driven-taxonomy.md section 2, methods that found it out of 6)
AGENDAS = [
    ("Reward hacking and reward-seeking", "Training", 60, 6),
    ("Emergent misalignment", "Training", 41, 5),
    ("Training-data effects", "Training", 22, 5),
    ("Model character and values", "Training", 53, 6),
    ("Scalable oversight and debate", "Training", 10, 5),
    ("Scheming and training gaming", "Inspection", 36, 5),
    ("Evaluation awareness", "Inspection", 33, 5),
    ("Honesty, lie detection, self-report", "Inspection", 39, 5),
    ("Alignment auditing and incidents", "Inspection", 39, 6),
    ("Interpretability foundations", "Inspection", 42, 6),
    ("CoT monitorability", "Deployment", 59, 6),
    ("AI control and agent monitoring", "Deployment", 65, 6),
    ("Misuse, robustness, dangerous capabilities", "Deployment", 62, 6),
    ("Multi-agent risks", "Deployment", 18, 5),
    ("Strategy, threat models, risk reports", "Strategy", 41, 6),
]

# Where each area's cluster is pulled to (data units; the radius of a 60-item bubble is ~7.7). Far apart, so
# the clusters stay separate and their labels have room
ANCHORS = {"Training": (-24, 16), "Inspection": (24, 16), "Deployment": (-24, -22), "Strategy": (24, -22)}
GAP = 0.6  # space between bubbles


def pack(radii: np.ndarray, anchors: np.ndarray, steps: int = 4000) -> np.ndarray:
    """Places circles near their anchors without overlap: attraction to the anchor, pairwise repulsion."""
    rng = np.random.default_rng(0)
    pos = anchors + rng.normal(scale=3, size=anchors.shape)
    for step in range(steps):
        pos += 0.02 * (anchors - pos)  # pull towards the area's anchor
        diff = pos[:, None, :] - pos[None, :, :]
        dist = np.linalg.norm(diff, axis=2) + np.eye(len(pos))
        overlap = radii[:, None] + radii[None, :] + GAP - dist
        np.fill_diagonal(overlap, 0)
        push = np.clip(overlap, 0, None) / dist
        pos += 0.5 * (push[:, :, None] * diff).sum(axis=1)
    return pos


def wrap(text: str, width: int) -> str:
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    return "\n".join(lines + [line])


def main() -> None:
    items = np.array([a[2] for a in AGENDAS], dtype=float)
    radii = np.sqrt(items)        # area proportional to the number of items
    anchors = np.array([ANCHORS[a[1]] for a in AGENDAS], dtype=float)
    pos = pack(radii, anchors)

    fig, ax = plt.subplots(figsize=(13, 11), facecolor="#fcfcfb")
    ax.set_facecolor("#fcfcfb")
    for (name, area, n, found), (x, y), r in zip(AGENDAS, pos, radii):
        colour = AREAS[area]
        ax.add_patch(Circle((x, y), r, facecolor=colour, alpha=0.22, edgecolor=colour, linewidth=2))
        stats = f"~{n} ({n / TOTAL:.0%})\n{found}/6 methods"
        if r < 4:  # too small to hold its label: write it beside the bubble, on the side away from its cluster
            side = -1 if x < pos[[a[1] == area for a in AGENDAS], 0].mean() else 1
            lx, ha = x + side * (r + 0.6), "right" if side < 0 else "left"
            ax.text(lx, y, wrap(name, 16), ha=ha, va="bottom", fontsize=8.5,
                    color="#1f1f1e", fontweight="bold", linespacing=1.1)
            ax.text(lx, y - 0.2, stats, ha=ha, va="top", fontsize=8, color="#5c5b56")
            continue
        size = 8.5 if r > 5 else 7.5
        width = max(10, int(r * 2.6))
        ax.text(x, y + 0.35 * min(r, 4), wrap(name, width), ha="center", va="bottom", fontsize=size,
                color="#1f1f1e", fontweight="bold", linespacing=1.1)
        ax.text(x, y - 0.25, stats, ha="center", va="top",
                fontsize=size - 0.5, color="#5c5b56", linespacing=1.15)

    # Area labels above each cluster
    for area, colour in AREAS.items():
        idx = [i for i, a in enumerate(AGENDAS) if a[1] == area]
        top = max(pos[i, 1] + radii[i] for i in idx)
        cx = np.mean([pos[i, 0] for i in idx])
        share = sum(AGENDAS[i][2] for i in idx) / items.sum()
        ax.text(cx, top + 1.2, f"{area}  ({share:.0%})", ha="center", va="bottom", fontsize=13,
                fontweight="bold", color="#1f1f1e")

    lo = (pos - radii[:, None]).min(axis=0) - 2
    hi = (pos + radii[:, None]).max(axis=0) + 4
    ax.set_xlim(lo[0], hi[0])
    ax.set_ylim(lo[1], hi[1])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(
        "2026 AI safety agendas: sources per agenda, summarised across six taxonomy-discovery methods",
        fontsize=14, color="#1f1f1e", pad=12, loc="left",
    )
    fig.text(
        0.02, 0.015,
        f"Bubble area = number of sources: the median over the methods that found the agenda (for an agenda merged from "
        f"several candidates, the sum of their medians).\n{TOTAL} sources in all. "
        "Area shares are of the 15 agendas' total.\n"
        "\"n/6 methods\" = how many of the six methods have a matching category. Source: data-driven-taxonomy.md.",
        fontsize=9, color="#5c5b56",
    )
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
