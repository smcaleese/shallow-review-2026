"""The result format every method writes, plus the LLM classifier that assigns items to categories.

A result (output/clusters.json in each method folder):
    {
      "method": "...", "n_items": 285, "params": {...},
      "categories": [{"id": "c1", "name": ..., "description": ..., "parent": null},
                     {"id": "c1.1", "name": ..., "description": ..., "parent": "c1"}, ...],
      "assignments": {"P001": "c1.1", ...}   # a leaf (or a top category with no children), or "other"
    }
"""

import logging
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, create_model

from shared import llm
from shared.data import item_block, write_json

log = logging.getLogger("taxonomy")
OTHER = "other"


# ---------- reading a result ----------

def parent_of(result: dict) -> dict[str, str]:
    """category id -> its top-level category id (top-level ids map to themselves)."""
    cats = {c["id"]: c for c in result["categories"]}
    return {cid: (c["parent"] or cid) for cid, c in cats.items()} | {OTHER: OTHER}


def leaf_categories(result: dict) -> list[dict]:
    has_children = {c["parent"] for c in result["categories"] if c["parent"]}
    return [c for c in result["categories"] if c["id"] not in has_children]


def top_categories(result: dict) -> list[dict]:
    return [c for c in result["categories"] if not c["parent"]]


def level_assignments(result: dict, level: str) -> dict[str, str]:
    if level == "leaf":
        return dict(result["assignments"])
    tops = parent_of(result)
    return {pid: tops[cid] for pid, cid in result["assignments"].items()}


# ---------- assigning items with an LLM ----------

def category_listing(categories: list[dict], all_categories: list[dict] | None = None) -> str:
    """Bulleted list of the categories to choose from, under their parent's heading when they have one."""
    by_id = {c["id"]: c for c in (all_categories or categories)}
    lines, current_parent = [], None
    for c in categories:
        parent = c.get("parent")
        if parent and parent != current_parent:
            p = by_id[parent]
            lines += ["", f"## {p['name']}: {p['description']}"]
            current_parent = parent
        lines.append(f"- {c['id']} | {c['name']}: {c['description']}")
    return "\n".join(lines).strip()


ASSIGN_SYSTEM = """You sort AI safety research (arXiv papers and LessWrong / Alignment Forum posts) into the categories \
of a taxonomy for the Shallow Review of Technical AI Safety.

Put each item in the ONE category whose description best fits what the item is mainly about: the research \
problem or agenda it advances, judged from its text, not its title. Use "other" only when no category is a \
reasonable fit. Return one entry per item, using the category id (the part before "|").

CATEGORIES
{listing}"""


def assign_items(items: list[dict], categories: list[dict], *, all_categories: list[dict] | None = None,
                 model: str = llm.DEFAULT_MODEL, effort: str = "low", batch_size: int = 20,
                 shuffle_seed: int | None = None, label: str = "assign") -> dict[str, str]:
    """pid -> category id (or "other") for every item, using only the categories' names and descriptions."""
    ids = [c["id"] for c in categories] + [OTHER]
    Entry = create_model("Entry", pid=(str, ...), category=(Literal[tuple(ids)], ...))
    Batch = create_model("AssignedBatch", assignments=(list[Entry], ...))
    system = ASSIGN_SYSTEM.format(listing=category_listing(categories, all_categories))

    order = list(items)
    if shuffle_seed is not None:
        random.Random(shuffle_seed).shuffle(order)

    def run(batch):
        user = "Assign each of these items.\n\n" + "\n\n".join(item_block(i) for i in batch)
        out = llm.parse(system, user, Batch, model=model, effort=effort, label=f"{label} {batch[0]['pid']}")
        wanted = {i["pid"] for i in batch}
        return {a.pid: a.category for a in (out.assignments if out else []) if a.pid in wanted}

    batches = [order[k:k + batch_size] for k in range(0, len(order), batch_size)]
    result = {}
    for part in llm.run_parallel(run, [(b,) for b in batches]):
        result.update(part)
    missing = [i for i in order if i["pid"] not in result]
    if missing:  # one retry, in small batches
        log.warning(f"{label}: {len(missing)} items unassigned, retrying")
        for part in llm.run_parallel(run, [(missing[k:k + 5],) for k in range(0, len(missing), 5)]):
            result.update(part)
    for i in order:
        result.setdefault(i["pid"], OTHER)
    return result


# ---------- writing a result ----------

def write_result(method_dir: Path, method: str, items: list[dict], categories: list[dict],
                 assignments: dict[str, str], params: dict | None = None):
    """Write output/clusters.json and a readable output/clusters.md."""
    result = {"method": method, "n_items": len(items), "params": params or {},
              "categories": categories, "assignments": dict(sorted(assignments.items()))}
    out = method_dir / "output"
    write_json(out / "clusters.json", result)
    (out / "clusters.md").write_text(render_markdown(result, items))
    log.info(f"wrote {out / 'clusters.json'} and clusters.md")
    return result


def render_markdown(result: dict, items: list[dict]) -> str:
    titles = {i["pid"]: f"{i['title']} ({'arXiv' if i['source'] == 'arxiv' else 'LW'})" for i in items}
    members = defaultdict(list)
    for pid, cid in result["assignments"].items():
        members[cid].append(pid)
    tops = parent_of(result)
    top_sizes = Counter(tops[c] for c in result["assignments"].values())
    children = defaultdict(list)
    for c in result["categories"]:
        if c["parent"]:
            children[c["parent"]].append(c)

    lines = [f"# {result['method']}", "", f"{result['n_items']} items, {len(top_categories(result))} top-level "
             f"categories, {len(leaf_categories(result))} leaves, {len(members.get(OTHER, []))} in other.", ""]
    for top in sorted(top_categories(result), key=lambda c: -top_sizes[c["id"]]):
        lines += [f"## {top['name']} ({top_sizes[top['id']]})", "", top["description"], ""]
        lines += [f"- {titles[p]}" for p in members.get(top["id"], [])]
        for sub in sorted(children[top["id"]], key=lambda c: -len(members[c["id"]])):
            lines += ["", f"### {sub['name']} ({len(members[sub['id']])})", "", sub["description"], ""]
            lines += [f"- {titles[p]}" for p in members[sub["id"]]]
        lines.append("")
    if members.get(OTHER):
        lines += [f"## Other ({len(members[OTHER])})", ""] + [f"- {titles[p]}" for p in members[OTHER]] + [""]
    return "\n".join(lines)
