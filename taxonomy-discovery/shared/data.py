"""Load the items to cluster.

Items are every source in draft-pipeline's source lists (arXiv and LessWrong shortlists, org pages, Safety Stack),
frozen by build_snapshot.py. Each item gets a short stable id (P001, P002, ...) so prompts and outputs stay readable.
"""

import json
import random
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
# The methods are compared on a frozen snapshot of the sources (build_snapshot.py, 624 items as of 2026-11-13).
# Short ids (P001...) are positions in this list, so every method's clusters.json depends on it staying fixed.
ITEMS_PATH = ROOT / "data" / "items-2026-11-13.jsonl"
CACHE = ROOT / "cache"
RESULTS = ROOT / "results"

SOURCE_KINDS = {"arxiv": "arXiv paper", "lesswrong": "LessWrong post", "org": "organisation page",
                "safety_stack": "paper or post"}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def load_items(limit: int | None = None) -> list[dict]:
    """Items sorted by id, each with a short id `pid`. `limit` takes a fixed random sample (for smoke tests)."""
    items = sorted(read_jsonl(ITEMS_PATH), key=lambda i: i["id"])
    out = [{"pid": f"P{n:03d}", "id": i["id"], "source": i["source"], "title": i["title"].strip(),
            "text": " ".join(str(i.get("text") or "").split()), "url": i.get("url", ""),
            "authors": i.get("authors") or "", "date": i.get("date") or ""}
           for n, i in enumerate(items, 1)]
    if limit:
        out = sorted(random.Random(0).sample(out, min(limit, len(out))), key=lambda i: i["pid"])
    return out


def item_block(item: dict, max_chars: int | None = None) -> str:
    text = item["text"] if max_chars is None else item["text"][:max_chars]
    kind = SOURCE_KINDS[item["source"]]
    return f"[{item['pid']}] ({kind}) {item['title']}\n{text}"


def corpus_text(items: list[dict]) -> str:
    return "\n\n".join(item_block(i) for i in items)


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def size_summary(assignments: dict[str, str]) -> str:
    sizes = sorted(Counter(assignments.values()).values(), reverse=True)
    return f"{len(sizes)} groups, sizes {sizes}"
