#!/usr/bin/env python3
"""Semantic map of the 502 selected sources: embed, lay out with UMAP, cluster, name, write the site's data.

Each source's title + abstract (or opening text) is embedded locally. UMAP projects the embeddings twice: to 2D for
the map, and to 10D for clustering, since clustering in 10D keeps more structure than clustering what's drawn. One
Ward tree over the 10D points is cut twice, into a few groups and more clusters, so every cluster sits inside one
group. Claude names the groups and clusters from their members' titles in one call (cached on disk); --no-llm uses
keywords instead.

Usage (from taxonomy-discovery/):
    uv run python 5-semantic-map/build.py
    uv run python 5-semantic-map/build.py --groups 8 --clusters 32 --no-llm
Then serve the site:
    python3 -m http.server 8770 -d 5-semantic-map/site
"""

import argparse
import csv
import hashlib
import json
import logging
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import numpy as np
from pydantic import BaseModel, Field

from shared import llm
from shared.data import CACHE, FACETS, LIVE_ITEMS_PATH, LIVE_TAGS_PATH, read_jsonl

log = logging.getLogger("semantic-map")
SELECTED_PATH = FACETS / "data" / "6-selected.json"
RANKS_PATH = FACETS / "output" / "selected-sources.csv"
DEFAULT_EMBEDDER = "BAAI/bge-large-en-v1.5"


def load_selected() -> list[dict]:
    """The selected sources in rank order, with the tagger's one-line summary and 2025 agenda tags."""
    ids = json.loads(SELECTED_PATH.read_text())["ids"]
    items = {i["id"]: i for i in read_jsonl(LIVE_ITEMS_PATH)}
    tags = {t["id"]: t for t in read_jsonl(LIVE_TAGS_PATH)}
    ranks = {r["id"]: int(r["rank"]) for r in csv.DictReader(RANKS_PATH.open())}
    out = []
    for n, id_ in enumerate(ids, 1):
        item, tag = items[id_], tags.get(id_, {})
        out.append({
            "id": id_, "rank": ranks.get(id_, n), "source": item["source"], "title": item["title"].strip(),
            "text": " ".join(str(item.get("text") or "").split()), "url": item.get("url", ""),
            "date": item.get("date") or "", "authors": item.get("authors") or "",
            "summary": tag.get("summary", ""), "agendas": tag.get("agenda") or [],
        })
    return out


def embed(items: list[dict], model_name: str) -> np.ndarray:
    """Same embedding and cache as method 3."""
    texts = [f"{i['title']}\n{i['text']}" for i in items]
    key = hashlib.sha256(("\n\x00".join([model_name] + texts)).encode()).hexdigest()[:16]
    path = CACHE / "embeddings" / f"{key}.npy"
    if path.exists():
        return np.load(path)
    from sentence_transformers import SentenceTransformer  # slow import; only when needed
    log.info(f"embedding {len(texts)} items with {model_name}")
    vectors = SentenceTransformer(model_name).encode(texts, normalize_embeddings=True, show_progress_bar=True,
                                                     batch_size=16)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, vectors)
    return vectors


def project(vectors: np.ndarray, dims: int, min_dist: float, seed: int) -> np.ndarray:
    import umap
    return umap.UMAP(n_components=dims, n_neighbors=15, min_dist=min_dist, metric="cosine",
                     random_state=seed).fit_transform(vectors)


def nested_clusters(points: np.ndarray, n_groups: int, n_clusters: int) -> tuple[np.ndarray, np.ndarray]:
    """Cut one Ward tree at two heights. Groups are numbered by size, clusters by size within their group."""
    from scipy.cluster.hierarchy import fcluster, linkage
    tree = linkage(points, method="ward")
    raw_groups = fcluster(tree, n_groups, criterion="maxclust")
    raw_clusters = fcluster(tree, n_clusters, criterion="maxclust")
    group_order = [g for g, _ in Counter(raw_groups).most_common()]
    groups = np.array([group_order.index(g) for g in raw_groups])
    clusters = np.zeros(len(points), dtype=int)
    next_id = 0
    for g in range(len(group_order)):
        members = Counter(raw_clusters[groups == g])
        for c, _ in members.most_common():
            clusters[raw_clusters == c] = next_id
            next_id += 1
    return groups, clusters


STOP = set("""a an the and or of to in on for with by from as at is are be been was were this that these those it its we
our their they them can could may might will would should using use used via into than more most such which who what when
how not no but also both each other between over under about across based show shows find results paper post model models
language large llm llms ai new approach method methods work study we've i you your one two three do does""".split())


def keywords(items: list[dict], labels: np.ndarray, top: int = 3) -> dict[int, list[str]]:
    """Distinctive title words per label (class-based TF-IDF over titles and summaries)."""
    counts = defaultdict(Counter)
    for item, label in zip(items, labels):
        words = re.findall(r"[a-z][a-z\-]{2,}", f"{item['title']} {item['summary']}".lower())
        counts[int(label)].update(w for w in words if w not in STOP)
    df = Counter(w for c in counts.values() for w in c)
    n = len(counts)
    return {label: [w for w, _ in sorted(c.items(), key=lambda kv: -kv[1] * np.log(1 + n / df[kv[0]]))[:top]]
            for label, c in counts.items()}


class ClusterName(BaseModel):
    key: str = Field(description="The cluster key exactly as given, e.g. 'C3'")
    name: str = Field(description="2-5 words")


class GroupName(BaseModel):
    key: str = Field(description="The group key exactly as given, e.g. 'G1'")
    name: str = Field(description="2-5 words")
    description: str = Field(description="One sentence on what the group's members share")
    clusters: list[ClusterName]


class MapNames(BaseModel):
    groups: list[GroupName]


NAME_SYSTEM = """You label a semantic map of AI safety research (arXiv papers, LessWrong / Alignment Forum posts, \
and lab or org blog posts) for the Shallow Review of Technical AI Safety. A clustering algorithm grouped the items by \
embedding similarity into groups, each split into clusters; you only name them, you don't move items.

Name each group and cluster for the research problem or agenda most of its members share, in plain words a \
researcher would recognise (e.g. "Sparse autoencoders", "Reward hacking in RL"). Keep sibling cluster names distinct \
from each other and from their group's name. If a cluster looks mixed, name what most members share."""


def name_with_claude(items, groups, clusters, model) -> MapNames | None:
    lines = []
    for g in sorted(set(groups)):
        lines.append(f"## Group G{g + 1}")
        for c in sorted(set(clusters[groups == g])):
            members = [items[i] for i in np.where(clusters == c)[0]]
            lines.append(f"### Cluster C{c + 1} ({len(members)} items)")
            lines += [f"- {m['title']}" for m in members]
        lines.append("")
    return llm.parse(NAME_SYSTEM, "\n".join(lines), MapNames, model=model, effort="medium", label="name map")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", type=int, default=8, help="top-level groups (hue)")
    ap.add_argument("--clusters", type=int, default=32, help="clusters in total (shade within a group)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--embedder", default=DEFAULT_EMBEDDER)
    ap.add_argument("--model", default=llm.DEFAULT_MODEL, help="Claude model for naming")
    ap.add_argument("--no-llm", action="store_true", help="label clusters with keywords instead of Claude")
    args = ap.parse_args()

    items = load_selected()
    log.info(f"{len(items)} selected sources")
    vectors = embed(items, args.embedder)
    xy = project(vectors, 2, 0.1, args.seed)
    groups, clusters = nested_clusters(project(vectors, 10, 0.0, args.seed), args.groups, args.clusters)

    group_kw, cluster_kw = keywords(items, groups), keywords(items, clusters)
    names = None if args.no_llm else name_with_claude(items, groups, clusters, args.model)
    group_names = {g.key: g for g in names.groups} if names else {}
    cluster_names = {c.key: c.name for g in names.groups for c in g.clusters} if names else {}

    meta_groups = []
    for g in sorted(int(g) for g in set(groups)):
        named = group_names.get(f"G{g + 1}")
        meta_groups.append({
            "id": g, "key": f"G{g + 1}", "name": named.name if named else ", ".join(group_kw[g][:2]),
            "description": named.description if named else "", "keywords": group_kw[g],
            "clusters": [{"id": int(c), "key": f"C{c + 1}", "keywords": cluster_kw[int(c)],
                          "name": cluster_names.get(f"C{c + 1}", ", ".join(cluster_kw[int(c)][:2]))}
                         for c in sorted(set(clusters[groups == g]))],
        })

    # Scale the layout to [0, 1] on its longer side so the page doesn't depend on UMAP's arbitrary units.
    xy = xy - xy.min(axis=0)
    xy = xy / xy.max()
    points = [{
        "id": it["id"], "rank": it["rank"], "title": it["title"], "url": it["url"], "source": it["source"],
        "date": it["date"], "authors": it["authors"], "summary": it["summary"] or it["text"][:400],
        "agendas": it["agendas"], "x": round(float(xy[i, 0]), 5), "y": round(float(xy[i, 1]), 5),
        "group": int(groups[i]), "cluster": int(clusters[i]),
    } for i, it in enumerate(items)]
    data = {"embedder": args.embedder, "named_by": None if args.no_llm or not names else args.model,
            "groups": meta_groups, "points": points}
    out = HERE / "site" / "data.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("window.MAP_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    log.info(f"wrote {out.relative_to(HERE.parent)}: {len(points)} points, {len(meta_groups)} groups, "
             f"{len(set(clusters))} clusters")
    for g in meta_groups:
        log.info(f"  {g['key']} {g['name']} ({int((groups == g['id']).sum())}): "
                 + "; ".join(f"{c['name']} ({int((clusters == c['id']).sum())})" for c in g["clusters"]))
    log.info(llm.usage_report())


if __name__ == "__main__":
    main()
