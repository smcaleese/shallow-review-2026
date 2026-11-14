#!/usr/bin/env python3
"""Freeze the items to cluster: every source in draft-pipeline's source lists, with its title and text.

Reads draft-pipeline/data/sources-links/*-2026.txt and takes each URL's text from where it was selected:
- shortlist-arxiv: the arXiv shortlist CSV (abstract)
- shortlist-lw: the LessWrong shortlist CSV (opening ~2,000 characters)
- facets-org, facets-safetystack: facets-shared's items (page opening or abstract)
An item in several lists is kept once (an arXiv paper wins). Writes data/items-<date>.jsonl, which the methods read
through shared/data.py; rerunning this renumbers the short ids (P001...), so every method has to be rerun after it.

Usage (from taxonomy-discovery/):
    uv run python build_snapshot.py
"""

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
LINKS = REPO / "draft-pipeline" / "data" / "sources-links"
ARXIV_SHORTLIST = REPO / "scraping-scripts/arxiv-scraper/results/shortlisted/2026/arxiv-papers-shortlisted.csv"
LW_SHORTLIST = REPO / "scraping-scripts/AF-and-LW-scraper/results/shortlisted/2026/lw-posts-shortlisted.csv"
FACETS_ITEMS = [REPO / "facets-shared/data/1-items.jsonl", REPO / "facets-shared/data/2-items-deduped.jsonl"]


def clean(text) -> str:
    return " ".join(str(text or "").split())


def key(url: str) -> str:
    """One key per work: the arXiv ID without version, the LessWrong post ID, or the bare URL."""
    if m := re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url):
        return f"arxiv:{m.group(1)}"
    if m := re.search(r"(?:lesswrong\.com|alignmentforum\.org)/posts/(\w+)", url):
        return f"lw:{m.group(1)}"
    return re.sub(r"^https?://(www\.)?", "", url.strip()).rstrip("/")


def read_list(name: str) -> list[str]:
    return [line.strip() for line in (LINKS / f"{name}-2026.txt").read_text().splitlines() if line.startswith("http")]


def main():
    items = {}

    for r in csv.DictReader(ARXIV_SHORTLIST.open()):
        k = key(f"https://arxiv.org/abs/{r['arxiv_id']}")
        items[k] = {"id": k, "source": "arxiv", "title": clean(r["title"]), "authors": r["authors"],
                    "date": r["published"], "url": f"https://arxiv.org/abs/{k.split(':')[1]}",
                    "text": clean(r["abstract"])}
    for r in csv.DictReader(LW_SHORTLIST.open()):
        k = key(r["url"])
        items[k] = {"id": k, "source": "lesswrong", "title": clean(r["title"]), "authors": r["authors"],
                    "date": r["posted"], "url": r["url"], "text": clean(r["excerpt"])}

    # Org and Safety Stack items: text from facets-shared, matched on the item's URL or any of its links
    facets = {}
    for path in FACETS_ITEMS:
        for line in path.read_text().splitlines():
            i = json.loads(line)
            for u in [i.get("url")] + [lk.get("url") if isinstance(lk, dict) else lk for lk in i.get("links") or []]:
                if u:
                    facets.setdefault(key(u), i)
    for name, source in (("facets-org", "org"), ("facets-safetystack", "safety_stack")):
        for url in read_list(name):
            k = key(url)
            if k in items:
                continue  # already in a shortlist
            i = facets[k]  # a KeyError means the list has a URL facets-shared doesn't know
            items[k] = {"id": k, "source": source, "title": clean(i["title"]), "authors": i.get("authors") or "",
                        "date": i.get("date") or "", "url": url, "text": clean(i.get("text"))}

    # Every URL in the lists must be covered, and nothing else
    listed = {key(u) for name in ("shortlist-arxiv", "shortlist-lw", "facets-org", "facets-safetystack")
              for u in read_list(name)}
    assert listed == set(items), f"lists and items differ: {sorted(listed ^ set(items))[:10]}"
    empty = [k for k, i in items.items() if not i["text"]]
    if empty:
        print(f"warning: {len(empty)} items have no text: {empty[:5]}", file=sys.stderr)

    out = ROOT / "data" / f"items-{date.today()}.jsonl"
    out.parent.mkdir(exist_ok=True)
    out.write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in sorted(items.values(), key=lambda i: i["id"])))
    counts = {s: sum(i["source"] == s for i in items.values()) for s in ("arxiv", "lesswrong", "org", "safety_stack")}
    print(f"{out}: {len(items)} items {counts}")


if __name__ == "__main__":
    main()
