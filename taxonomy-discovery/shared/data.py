"""Load the items to cluster and the 2025 reference labels.

Items come from facets-shared (arXiv shortlist + notable LW/AF posts, already deduplicated). Each item gets a short
stable id (P001, P002, ...) so prompts and outputs stay readable.
"""

import json
import random
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
FACETS = REPO / "facets-shared"
ITEMS_PATH = FACETS / "data" / "2-items-deduped.jsonl"
TAGS_PATH = FACETS / "data" / "4-tags-final.jsonl"
TAXONOMY_2025 = FACETS / "input" / "taxonomy-2025.yaml"
CACHE = ROOT / "cache"
RESULTS = ROOT / "results"

SKIP_2025_GROUPS = {"labs_giant_companies"}  # organisations, not research areas


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def load_items(limit: int | None = None, include_out_of_scope: bool = False) -> list[dict]:
    """In-scope items sorted by id, each with a short id `pid`. `limit` takes a fixed random sample (for smoke tests)."""
    tags = {t["id"]: t for t in read_jsonl(TAGS_PATH)}
    items = sorted(read_jsonl(ITEMS_PATH), key=lambda i: i["id"])
    if not include_out_of_scope:
        items = [i for i in items if tags.get(i["id"], {}).get("scope") != "exclude"]
    out = [{"pid": f"P{n:03d}", "id": i["id"], "source": i["source"], "title": i["title"].strip(),
            "text": " ".join(str(i.get("text") or "").split()), "url": i.get("url", "")}
           for n, i in enumerate(items, 1)]
    if limit:
        out = sorted(random.Random(0).sample(out, min(limit, len(out))), key=lambda i: i["pid"])
    return out


def item_block(item: dict, max_chars: int | None = None) -> str:
    text = item["text"] if max_chars is None else item["text"][:max_chars]
    kind = "arXiv paper" if item["source"] == "arxiv" else "LessWrong post"
    return f"[{item['pid']}] ({kind}) {item['title']}\n{text}"


def corpus_text(items: list[dict]) -> str:
    return "\n\n".join(item_block(i) for i in items)


def load_2025_groups() -> dict[str, str]:
    """Leaf agenda name -> top-level group name in last year's taxonomy."""
    leaf_to_group = {}

    def walk(nodes, group):
        for node in nodes:
            if node.get("children"):
                walk(node["children"], group or node["name"])
            else:
                leaf_to_group[node["name"]] = group or node["name"]

    tree = [n for n in yaml.safe_load(TAXONOMY_2025.read_text())["taxonomy"] if n["id"] not in SKIP_2025_GROUPS]
    walk(tree, None)
    return leaf_to_group


def reference_labels(items: list[dict]) -> dict[str, str]:
    """pid -> 2025 top-level group of the item's first agenda tag (from facets-shared's tagger).

    Items tagged only with a new 2026 agenda get 'new 2026'; untagged items get 'none'."""
    tags = {t["id"]: t for t in read_jsonl(TAGS_PATH)}
    groups = load_2025_groups()
    labels = {}
    for item in items:
        agendas = tags.get(item["id"], {}).get("agenda") or []
        if not agendas:
            labels[item["pid"]] = "none"
        elif agendas[0] in groups:
            labels[item["pid"]] = groups[agendas[0]]
        else:
            labels[item["pid"]] = "new 2026"
    return labels


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def size_summary(assignments: dict[str, str]) -> str:
    sizes = sorted(Counter(assignments.values()).values(), reverse=True)
    return f"{len(sizes)} groups, sizes {sizes}"
