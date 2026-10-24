#!/usr/bin/env python3
"""
Step 5: join items with their final tags and write site/data.js (read by site/index.html) and
output/items-tagged.csv.

Usage (from facets-shared/):
    uv run python src/build_site.py
Items scoped `exclude` are left out. Then serve the site:
    python3 -m http.server 8767 --directory site
"""

import csv
import json
from collections import Counter
from datetime import date

import yaml

from common import ITEMS_CSV, ITEMS_DEDUPED, SITE_DATA, TAGS_FINAL, TAXONOMY_2025, VOCAB, read_jsonl
from tag import NEW_AGENDA_PREFIX, agenda_names, load_agendas

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SOURCE_LABELS = {"arxiv": "arXiv", "lesswrong": "LW", "both": "arXiv+LW"}  # short, so filters read +source:arxiv+lw
COLORS = {"source": "teal", "scope": "outline", "evidence": "ink", "item_type": "blue", "scientific": "violet",
          "concept": "green", "phenomenon": "olive", "method": "orange", "substrate": "grey", "agenda": "rose",
          "area_2025": "rose", "subarea_2025": "rose", "by": "outline", "about": "outline", "month": "grey"}
NEW_2026_AREA = "New in 2026"  # items whose agendas are all new 2026 agendas
SKIP_2025_AREAS = {"labs_giant_companies"}  # organisations, not research areas; `by` covers them


def label(tag_id: str) -> str:
    return tag_id.replace("_", " ")


def load_tree_2025(path) -> tuple[dict[str, tuple[str, str]], list[dict], list[dict]]:
    """Last year's taxonomy as {leaf agenda name: (area, sub-area)}, plus the areas and sub-areas in taxonomy order.

    An area's sub-areas are its children; when a child is itself a leaf agenda, the leaf is its own sub-area."""
    leaf_to = {}
    areas, subareas = [], []

    def leaves(node):
        kids = node.get("children") or []
        return [n for k in kids for n in leaves(k)] if kids else [node]

    for area in yaml.safe_load(path.read_text())["taxonomy"]:
        if area["id"] in SKIP_2025_AREAS:
            continue
        areas.append({"name": area["name"], "description": area.get("description", "")})
        for sub in area.get("children") or [area]:
            subareas.append({"name": sub["name"], "description": sub.get("description", "")})
            for leaf in leaves(sub):
                leaf_to[leaf["name"]] = (area["name"], sub["name"])
    return leaf_to, areas, subareas


def areas_of(agendas: list[str], tree: dict[str, tuple[str, str]]) -> tuple[list[str], list[str]]:
    """2025 areas and sub-areas for an item's agenda tags, in first-seen order."""
    hits = [tree[a] for a in agendas if a in tree]
    if not hits:
        return ([NEW_2026_AREA], [NEW_2026_AREA]) if agendas else ([], [])
    return list(dict.fromkeys(a for a, _ in hits)), list(dict.fromkeys(s for _, s in hits))


def build_facets(vocab: dict, agendas: list[dict], areas: list[dict], subareas: list[dict]) -> list[dict]:
    def facet(fid, name, tags, descriptions, multi=True):
        return {"id": fid, "name": name, "multi": multi, "tags": tags, "descriptions": descriptions, "color": COLORS[fid]}

    facets = [facet("source", "Source", list(SOURCE_LABELS.values()),
                    {"arXiv": "arXiv paper", "LW": "LessWrong or Alignment Forum post",
                     "arXiv+LW": "arXiv paper with a LessWrong write-up"}, multi=False),
              facet("scope", "Scope", ["include", "borderline"],
                    {"borderline": "Reviewers could go either way on whether this is technical AI safety"}, multi=False)]
    for fid, f in vocab["facets"].items():
        facets.append(facet(fid, f["name"], [label(t) for t in f["tags"]],
                            {label(t): (s or {}).get("def", "") for t, s in f["tags"].items()},
                            multi=f["select"] != "one"))
    new = {NEW_AGENDA_PREFIX + label(k): (v or {}).get("def", "") for k, v in vocab["agenda_new_2026"].items()}
    new_note = {NEW_2026_AREA: "Only tagged with agendas that are new in 2026, not in last year's taxonomy"}
    facets += [facet("area_2025", "2025 area", [a["name"] for a in areas] + [NEW_2026_AREA],
                     {a["name"]: a["description"] for a in areas} | new_note),
               facet("subarea_2025", "2025 sub-area", [s["name"] for s in subareas] + [NEW_2026_AREA],
                     {s["name"]: s["description"] for s in subareas} | new_note),
               facet("agenda", "Agenda", agenda_names(vocab, agendas),
                     {**{a["name"]: a["description"] for a in agendas}, **new}),
               facet("by", "By (org)", list(vocab["org"]), {}),
               facet("about", "About (developer)", list(vocab["developers"]), {}),
               facet("month", "Month", MONTHS, {}, multi=False)]
    return facets


def popularity_percentiles(items: list[dict]) -> dict[str, float]:
    """Rank items within their own source (citations for papers, karma for posts) so the two can be sorted together."""
    pct = {}
    for source, key in (("arxiv", "citations"), ("lesswrong", "karma")):
        group = [i for i in items if i["source"] == source]
        ranked = sorted(group, key=lambda i: i["popularity"].get(key) or 0)
        for n, i in enumerate(ranked):
            pct[i["id"]] = (n + 1) / len(ranked)
    return pct


def item_record(item: dict, t: dict, pct: float, tree: dict[str, tuple[str, str]]) -> dict:
    source = "both" if len(item["sources"]) > 1 else item["source"]
    agendas = list(t["agenda"])
    if t.get("new_agenda"):
        agendas.append(NEW_AGENDA_PREFIX + t["new_agenda"].strip().lower())
    area, subarea = areas_of(agendas, tree)
    tags = {
        "source": [SOURCE_LABELS[source]], "scope": [t["scope"]],
        "evidence": [t["evidence"]], "item_type": [label(t["item_type"])],
        "scientific": [label(t["scientific_primary"])] + [label(s) for s in t["scientific_secondary"]
                                                          if s != t["scientific_primary"]],
        **{f: [label(x) for x in t[f]] for f in ("concept", "phenomenon", "method", "substrate")},
        "area_2025": area, "subarea_2025": subarea,
        "agenda": agendas, "by": [b["org"] for b in t["by"]], "about": list(t["about"]),
        "month": [MONTHS[int(item["date"][5:7]) - 1]],
    }
    return {
        "id": item["id"], "source": source, "title": item["title"], "authors": item["authors"], "date": item["date"],
        "url": item["url"], "links": item["links"], "popularity": item["popularity"], "pop_pct": round(pct, 4),
        "summary": t["summary"], "text": item["text"], "text_label": "abstract" if item["source"] == "arxiv" else "excerpt",
        "shortlist_reason": item.get("shortlist_reason", ""), "promoted": bool(item.get("promoted_by")),
        "by_evidence": [f"{b['org']}: {b['evidence']}" for b in t["by"]], "rule_changes": t["pp"], "tags": tags,
    }


def write_csv(records: list[dict]):
    ITEMS_CSV.parent.mkdir(parents=True, exist_ok=True)
    fixed = ["id", "source", "title", "authors", "date", "url", "summary"]
    facet_ids = list(records[0]["tags"]) if records else []
    with ITEMS_CSV.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fixed + ["citations", "karma", "other_links"] + facet_ids + ["rule_changes"])
        for r in records:
            writer.writerow([r[k] for k in fixed]
                            + [r["popularity"].get("citations"), r["popularity"].get("karma"),
                               "; ".join(l["url"] for l in r["links"] if l["url"] != r["url"])]
                            + ["; ".join(r["tags"][fid]) for fid in facet_ids] + ["; ".join(r["rule_changes"])])


def main():
    vocab = yaml.safe_load(VOCAB.read_text())
    agendas = load_agendas(TAXONOMY_2025)
    tree, areas, subareas = load_tree_2025(TAXONOMY_2025)
    items = read_jsonl(ITEMS_DEDUPED)
    tags = {t["id"]: t for t in read_jsonl(TAGS_FINAL)}
    tagged = [i for i in items if i["id"] in tags]
    shown = [i for i in tagged if tags[i["id"]]["scope"] != "exclude"]
    pct = popularity_percentiles(shown)
    records = [item_record(i, tags[i["id"]], pct.get(i["id"], 0), tree) for i in shown]

    counts = Counter(r["source"] for r in records)
    models = sorted({tags[i["id"]]["model"] for i in tagged})
    data = {
        "meta": {"n_items": len(records), "by_source": {SOURCE_LABELS[k]: v for k, v in counts.items()},
                 "models": models, "vocab_version": vocab["version"], "built": date.today().isoformat()},
        "facets": build_facets(vocab, agendas, areas, subareas),
        "items": records,
    }
    SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
    SITE_DATA.write_text("window.SR_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    write_csv(records)

    print(f"Wrote {SITE_DATA.name} and {ITEMS_CSV.name}: {len(records)} items "
          f"({', '.join(f'{v} {SOURCE_LABELS[k]}' for k, v in counts.items())})")
    if len(tagged) < len(items):
        print(f"  {len(items) - len(tagged)} items have no tags yet and are left out; run src/tag.py")
    if len(shown) < len(tagged):
        print(f"  {len(tagged) - len(shown)} items scoped exclude are left out")


if __name__ == "__main__":
    main()
