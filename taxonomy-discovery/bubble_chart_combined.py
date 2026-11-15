"""Bubble chart of the combined taxonomy (combined-taxonomy.md): one bubble per agenda, sized by its sources.

51 agendas in 14 areas and 6 parts. Parts IV-V are one area each and share a column; bubble area is proportional to the
estimated number of sources. A dashed ring shows the size after adding the hand-picked sources of section 9.

Sizes are rough estimates from section 4 of combined-taxonomy.md, in this order of preference:
  1. the cross-method median when the methods found the agenda on its own;
  2. Draft 2's count, narrowed by hand (emergent misalignment: the ~28 entries that are EM proper);
  3. an area-level median split between its agendas in proportion to their Draft 1 counts
     (interpretability, evals 5.3/5.4, auditing 6.1/6.2, CoT, control, threat models);
  4. for thin or new agendas, the pipeline count given in the report.
Free (no LLM calls).

    uv run python bubble_chart_combined.py        # writes results/agenda-bubbles-combined.png
    uv run python bubble_chart_combined.py --from-db
        # sizes = sources the pipeline classified into each agenda (draft-pipeline/data/data.db, taxonomy.yaml);
        # writes results/agenda-bubbles-combined-classified.png
"""

import json
import sqlite3
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = Path(__file__).resolve().parent
OUT = HERE / "results" / "agenda-bubbles-combined.png"
PIPELINE_DATA = HERE.parent / "draft-pipeline" / "data"
T = "~"  # marks estimates; empty when the sizes are classified counts

# Parts in the categorical order of the dataviz reference palette (6 slots; validated: all checks pass on light)
PARTS = [
    ("I. Training aligned models", "#2a78d6"),
    ("II. Understanding models", "#eb6834"),
    ("III. Deploying models safely", "#1baf7a"),
    ("IV. Make AI solve it", "#eda100"),
    ("V. Theory & safety by construction", "#e87ba4"),
    ("VI. The wider picture", "#008300"),
]
COLUMNS = [[0], [1], [2], [3, 4], [5]]  # parts per column

# part index -> [(area, [(id, agenda, estimated sources now, sources to add by hand, methods out of 6 or None)])]
TAXONOMY = {
    0: [
        ("1. Training data & generalization", [
            ("1.1", "Data filtering & alignment pretraining", 14, 0, 3),
            ("1.2", "Subliminal learning & data attribution", 22, 0, 5),
            ("1.3", "Emergent misalignment", 28, 0, 5),
            ("1.4", "Inoculation prompting", 8, 0, 3),
            ("1.5", "Generalization science", 12, 0, 2),
        ]),
        ("2. RL & alignment training", [
            ("2.1", "Alignment training methods", 5, 0, None),
            ("2.2", "Reward hacking & specification gaming", 34, 4, 6),
            ("2.3", "Reward-seeking & fitness-seeking", 16, 0, 5),
            ("2.4", "Internals & monitors as training signals", 10, 0, 4),
        ]),
        ("3. Model character, values & welfare", [
            ("3.1", "Persona science", 17, 0, 5),
            ("3.2", "Model specs, constitutions & character training", 8, 7, 3),
            ("3.3", "Whose values: pluralistic & social-choice alignment", 0, 5, None),
            ("3.4", "Model welfare & moral status", 6, 3, 5),
        ]),
    ],
    1: [
        ("4. Interpretability", [
            ("4.1", "Methods & tools", 14, 0, 6),
            ("4.2", "Science of representations", 9, 0, None),
            ("4.3", "Steering & activation engineering", 5, 11, None),
            ("4.4", "Developmental interpretability & SLT", 6, 1, 3),
        ]),
        ("5. Evaluations", [
            ("5.1", "Dangerous-capability evals", 14, 0, 6),
            ("5.2", "Scheming, sabotage & training gaming", 32, 0, 5),
            ("5.3", "Situational & evaluation awareness", 12, 0, 5),
            ("5.4", "Eval science & validity", 15, 4, 5),
        ]),
        ("6. Alignment auditing & honesty", [
            ("6.1", "Auditing methods & agents", 15, 0, 5),
            ("6.2", "Model organisms & testbeds", 13, 0, 5),
            ("6.3", "Lie detection & deception probes", 18, 0, 5),
            ("6.4", "Introspection, confessions & self-report", 21, 0, 5),
        ]),
    ],
    2: [
        ("7. Chain-of-thought monitorability", [
            ("7.1", "Latent reasoning & new architectures", 22, 5, 6),
            ("7.2", "CoT control, obfuscation & steganography", 12, 0, 6),
            ("7.3", "How training affects monitorability", 12, 0, 6),
            ("7.4", "Measuring & improving faithfulness", 14, 0, 6),
        ]),
        ("8. Monitoring & control", [
            ("8.1", "Control settings & protocols", 27, 0, 6),
            ("8.2", "Monitors", 20, 0, 6),
            ("8.3", "Red-teaming monitors & control protocols", 19, 0, 6),
        ]),
        ("9. Security & misuse", [
            ("9.1", "Misuse safeguards & jailbreaks", 13, 0, 5),
            ("9.2", "Agent security & prompt injection", 17, 0, 5),
            ("9.3", "Open-weight tamper resistance & unlearning", 13, 0, 5),
            ("9.4", "Data poisoning & backdoors", 15, 0, None),
            ("9.5", "Weight & infrastructure security", 3, 0, None),
        ]),
    ],
    3: [
        ("10. Make AI solve it", [
            ("10.1", "Scalable oversight: debate, weak-to-strong & interactive proofs", 13, 5, 5),
            ("10.2", "Automated alignment research", 5, 4, None),
        ]),
    ],
    4: [
        ("11. Theory & foundations", [
            ("11.1", "Agent foundations & decision theory", 4, 22, None),
            ("11.2", "Corrigibility theory", 2, 9, None),
            ("11.3", "Natural abstractions", 0, 6, None),
            ("11.4", "Heuristic explanations & mechanistic estimation", 7, 1, None),
            ("11.5", "Brain-like AGI safety", 1, 3, None),
            ("11.6", "Scientist AI & non-agentic AI", 1, 2, None),
        ]),
    ],
    5: [
        ("12. Multi-agent safety", [
            ("12", "Multi-agent safety", 18, 2, 5),
        ]),
        ("13. Real-world evidence", [
            ("13.1", "Incidents & case studies", 21, 0, 6),
            ("13.2", "Effects on users & society", 11, 0, 5),
            ("13.3", "Lab disclosures: system cards & risk reports", 17, 0, 5),
        ]),
        ("14. Threat models & strategy", [
            ("14.1", "Misalignment arguments & failure scenarios", 19, 5, 6),
            ("14.2", "Research strategy, lab plans & deals with AIs", 11, 3, 6),
        ]),
    ],
}

# Layout, in data units (the axes use an equal aspect)
COL_W = 30.0       # width of one part's column
BX = 4.0           # bubble centre, from the column's left edge
LX = 8.4           # label start, from the column's left edge
K = 0.62           # radius = K * sqrt(sources)
LH = 1.32          # height of one 9.5pt text line
MIN_ROW = 3.6      # minimum row height
AREA_HEAD = 2.4    # space for an area heading
SCALE = 0.15       # inches per data unit
AREA_GAP = 1.6     # space after an area
INK, MUTED, SURFACE = "#1f1f1e", "#5c5b56", "#fcfcfb"


def wrap(text: str, width: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    return lines + [line]


def stats(now: int, add: int, found: int | None) -> str:
    if not T:
        return f"{now} sources" + (f"  ·  {found}/6 methods" if found else "")
    size = f"~{now}" if not add else f"~{now} now, ~{now + add} with adds"
    return size + (f"  ·  {found}/6 methods" if found else "")


def use_classified_counts() -> None:
    """Replaces the estimates with the number of sources the pipeline classified into each agenda."""
    global T, OUT
    import yaml
    leaves = []
    def walk(nodes):
        for n in nodes:
            walk(n["children"]) if n.get("children") else leaves.append((n["id"], n["name"]))
    walk(yaml.safe_load(open(PIPELINE_DATA / "taxonomy.yaml"))["taxonomy"])
    db = sqlite3.connect(PIPELINE_DATA / "data.db")
    counts = {}
    for (out,) in db.execute("SELECT classifier_output FROM entries WHERE status = 'done'"):
        cats = sorted(json.loads(out)["categories"], key=lambda c: c.get("fit", 0), reverse=True)
        counts[cats[0]["id"]] = counts.get(cats[0]["id"], 0) + 1
    rows = [ags for areas in TAXONOMY.values() for _, ags in areas]
    flat = [a for ags in rows for a in ags]
    assert len(flat) == len(leaves), (len(flat), len(leaves))
    for (leaf_id, leaf_name), a in zip(leaves, flat):
        assert leaf_name.split(":")[0].split(" &")[0].lower()[:12] in a[1].lower(), (leaf_name, a[1])
    it = iter(leaves)
    for ags in rows:
        ags[:] = [(aid, name, counts.get(next(it)[0], 0), 0, found) for aid, name, _, _, found in ags]
    T, OUT = "", HERE / "results" / "agenda-bubbles-combined-classified.png"


def main() -> None:
    if "--from-db" in sys.argv:
        use_classified_counts()
    bottom = min(column(None, c) for c in range(len(COLUMNS)))
    width, height = len(COLUMNS) * COL_W, 2.2 - (bottom - 0.8)
    fig = plt.figure(figsize=(width * SCALE, height * SCALE), facecolor=SURFACE)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_facecolor(SURFACE)
    for c in range(len(COLUMNS)):
        column(ax, c)
    ax.set_xlim(0, width)
    ax.set_ylim(bottom - 0.8, 2.2)
    ax.axis("off")
    total_now = sum(a[2] for areas in TAXONOMY.values() for _, ags in areas for a in ags)
    total_add = sum(a[3] for areas in TAXONOMY.values() for _, ags in areas for a in ags)
    fig.text(0.008, 1.0, "2026 taxonomy: 6 parts, 14 areas, 51 agendas, sized by "
             + ("estimated sources" if T else "classified sources"),
             ha="left", va="bottom", fontsize=17, fontweight="bold", color=INK)
    note = (
        f"Bubble area = number of sources the pipeline classified into each agenda ({total_now} in all; each source "
        "counts once, in its best-fitting agenda). The draft keeps at most 10 per agenda.\n"
        "\"n/6 methods\" = how many of the six taxonomy-discovery methods found a matching category (for split agendas, "
        "the area's). Parts IV-V are a single area each, so their area heading is omitted."
    ) if not T else None
    fig.text(0.008, -0.01, note, fontsize=9.5, color=MUTED, va="top") if note else fig.text(
        0.008, -0.01,
        "Bubble area = estimated sources now (filled); dashed ring = after the hand-picked additions in section 9 of "
        f"combined-taxonomy.md (~{total_now} now, +{total_add}).\n"
        "Estimates: the cross-method median where the methods found the agenda on its own; otherwise an area-level "
        "median split by Draft 1's counts, or the pipeline count for thin agendas. Rough, not a classification run.\n"
        "\"n/6 methods\" = how many of the six taxonomy-discovery methods have a matching category (for split agendas, "
        "the area's). Parts IV-V are a single area each, so their area heading is omitted. "
        "Source: combined-taxonomy.md, sections 4 and 9.",
        fontsize=9.5, color=MUTED, va="top",
    )
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"Wrote {OUT}  ({total_now} now, +{total_add} hand-adds)")


def row(name: str, aid: str, now: int, add: int) -> tuple[list[str], float]:
    lines = wrap(f"{aid}  {name}", 30)
    r_all = K * (now + add) ** 0.5
    return lines, max(MIN_ROW, 2 * r_all + 0.8, LH * (len(lines) + 1) + 0.9)


def column(ax, c: int) -> float:
    """Lays out (and, if ax is given, draws) one column; returns its bottom y."""
    x0, y = c * COL_W, 0.0
    for p in COLUMNS[c]:
        part, colour = PARTS[p]
        areas = TAXONOMY[p]
        part_total = sum(a[2] for _, agendas in areas for a in agendas)
        if ax:
            ax.text(x0 + 1, y, part, ha="left", va="bottom", fontsize=14, fontweight="bold", color=INK)
            ax.text(x0 + 1, y - 0.4, f"{T}{part_total} sources" + (" now" if T else ""), ha="left", va="top", fontsize=9.5, color=MUTED)
            ax.plot([x0 + 1, x0 + COL_W - 1.5], [y - 2.3, y - 2.3], color=colour, linewidth=3,
                    solid_capstyle="round")
        y -= 3.4
        for area, agendas in areas:
            if len(areas) > 1:  # a single-area part has no separate area heading
                if ax:
                    area_total = sum(a[2] for a in agendas)
                    ax.text(x0 + 1, y, area, ha="left", va="top", fontsize=11, fontweight="bold", color=INK)
                    ax.text(x0 + 1, y - LH, f"{T}{area_total} sources", ha="left", va="top", fontsize=8.5,
                            color=MUTED)
                y -= LH + AREA_HEAD
            for aid, name, now, add, found in agendas:
                name_lines, h = row(name, aid, now, add)
                if ax:
                    draw_agenda(ax, x0, y - h / 2, colour, name_lines, now, add, found)
                y -= h
            y -= AREA_GAP
        y -= 2.6  # room for the next part's heading
    return y + 2.6


def draw_agenda(ax, x0: float, cy: float, colour: str, name_lines: list[str], now: int, add: int,
                found: int | None) -> None:
    r_now, r_all = K * now ** 0.5, K * (now + add) ** 0.5
    if add:  # size after the hand-adds: dashed ring
        ax.add_patch(Circle((x0 + BX, cy), r_all, facecolor="none", edgecolor=colour, linewidth=1.4,
                            linestyle=(0, (3, 2))))
    if now:
        ax.add_patch(Circle((x0 + BX, cy), r_now, facecolor=colour, alpha=0.28, edgecolor="none"))
        ax.add_patch(Circle((x0 + BX, cy), r_now, facecolor="none", edgecolor=colour, linewidth=2))
    else:  # nothing in the pipeline yet: a small marker so the row isn't empty
        ax.plot(x0 + BX, cy, marker="o", markersize=3, color=colour)
    text_top = cy + LH * (len(name_lines) + 1) / 2
    ax.text(x0 + LX, text_top, "\n".join(name_lines), ha="left", va="top", fontsize=9.5, fontweight="bold",
            color=INK, linespacing=1.15)
    ax.text(x0 + LX, text_top - LH * len(name_lines), stats(now, add, found), ha="left", va="top", fontsize=8.5,
            color=MUTED)


if __name__ == "__main__":
    main()
