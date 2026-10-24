#!/usr/bin/env python3
"""Method 3: embedding-only nearest-neighbour graph + Leiden (the baseline).

Embeds each item's title + text locally, links every item to its k most cosine-similar items, then runs the shared
Leiden + naming step. Same downstream as method 2, so the only difference is embeddings vs. LLM judgement.

Usage (from taxonomy-discovery/):
    uv run python 3-embedding-knn-graph/run.py
    uv run python 3-embedding-knn-graph/run.py --limit 40      # smoke test on a sample
"""

import argparse
import hashlib
import logging
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import numpy as np

from shared import llm
from shared.data import CACHE, load_items, size_summary, write_json
from shared.graph import graph_to_result
from shared.taxonomy import write_result

log = logging.getLogger("embedding-knn")
DEFAULT_EMBEDDER = "BAAI/bge-large-en-v1.5"


def embed(items: list[dict], model_name: str) -> np.ndarray:
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=15, help="neighbours per item")
    ap.add_argument("--top-target", type=int, default=10, help="roughly how many top-level clusters")
    ap.add_argument("--sub-size", type=int, default=10, help="roughly how many items per subcluster")
    ap.add_argument("--embedder", default=DEFAULT_EMBEDDER)
    ap.add_argument("--model", default=llm.DEFAULT_MODEL, help="Claude model for naming clusters")
    ap.add_argument("--limit", type=int, help="use a fixed random sample of this many items")
    args = ap.parse_args()

    items = load_items(args.limit)
    vectors = embed(items, args.embedder)
    sims = vectors @ vectors.T
    np.fill_diagonal(sims, -np.inf)
    k = min(args.k, len(items) - 1)
    neighbours = np.argsort(-sims, axis=1)[:, :k]
    votes = {(i, int(j)): 1.0 for i in range(len(items)) for j in neighbours[i]}
    write_json(HERE / "output" / "neighbours.json",
               {items[i]["pid"]: [items[int(j)]["pid"] for j in neighbours[i]] for i in range(len(items))})

    categories, assignments, params = graph_to_result(items, votes, top_target=args.top_target,
                                                      sub_size=args.sub_size, model=args.model)
    write_result(HERE, "3-embedding-knn-graph", items, categories, assignments,
                 params | {"k": k, "embedder": args.embedder, "model": args.model})
    log.info(f"top level: {size_summary({p: c.split('.')[0] for p, c in assignments.items()})}")
    log.info(llm.usage_report())


if __name__ == "__main__":
    main()
