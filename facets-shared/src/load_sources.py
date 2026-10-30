#!/usr/bin/env python3
"""
Step 1: load the arXiv shortlist, LW/AF posts, Lenz's org sources and Safety Stack documents into one list of items
with a common format.

LW posts are Jord's notable list plus the LW_EXTRA highest-karma posts his first-pass scope check marked include
that the list missed. Org items come from data/1b-lenz-items.jsonl (src/fetch_lenz_pages.py). Safety Stack items
are the dataset's documents the relevance filter kept (exact duplicate titles dropped).

Usage (from facets-shared/):
    uv run python src/load_sources.py
Writes data/1-items.jsonl. Every item has:
    id                 "arxiv:<id without version>", "lw:<post id>", "org:<hash of url>" or "ss:<doc id>"
    source             "arxiv", "lesswrong", "org" or "safety_stack"
    title, authors, date (YYYY-MM-DD), url
    text               the arXiv abstract, the post excerpt (step 2 swaps in the full post text), the page text, or
                       the Safety Stack abstract (from arXiv, Semantic Scholar or OpenAlex, else the dataset's quotes)
    links              every place the work appears: [{"source", "url", "label"}]
    popularity         {"citations"} for papers; {"karma", "af_karma", "comments"} for posts
    shortlist_reason   why it was selected (papers: Claude's shortlist reason; posts: which top lists it is in)
    extra              source-specific fields kept for the site and CSV
"""

import csv
import json

from common import (ARXIV_SHORTLIST, ITEMS, LENZ_ITEMS, LW_EXTRA, LW_POSTS, LW_RAW, LW_SCOPE_FIRST_PASS, SAFETY_STACK,
                    base_arxiv_id, norm_title, read_jsonl, write_jsonl)


def num(value, cast=float):
    try:
        return cast(float(value))
    except (TypeError, ValueError):
        return None


def clean(text) -> str:
    return " ".join(str(text or "").split())


def arxiv_item(row: dict) -> dict:
    """One shortlisted arXiv paper in the common format."""
    arxiv_id = base_arxiv_id(row["arxiv_id"])
    url = f"https://arxiv.org/abs/{arxiv_id}"
    return {
        "id": f"arxiv:{arxiv_id}", "source": "arxiv", "title": clean(row["title"]), "authors": clean(row["authors"]),
        "date": row["published"][:10], "url": url, "text": clean(row["abstract"]),
        "links": [{"source": "arxiv", "url": url, "label": "arXiv"}],
        "popularity": {"citations": num(row.get("citation_count"), int)},
        "shortlist_reason": clean(row.get("shortlist_reason")),
        "extra": {"arxiv_id": row["arxiv_id"], "rank": num(row.get("shortlist_rank"), int), "venue": clean(row.get("venue")),
                  "categories": clean(row.get("categories")), "comment": clean(row.get("comment"))},
    }


def lw_item(row: dict) -> dict:
    """One notable LW/AF post in the common format."""
    af = row.get("af") == "True"
    links = [{"source": "lesswrong", "url": row["url"], "label": "Alignment Forum" if af else "LessWrong"}]
    if row.get("link_url"):
        links.append({"source": "external", "url": row["link_url"], "label": "linked original"})
    return {
        "id": f"lw:{row['id']}", "source": "lesswrong", "title": clean(row["title"]), "authors": clean(row["authors"]),
        "date": row["posted"][:10], "url": row["url"], "text": clean(row.get("excerpt")), "links": links,
        "popularity": {"karma": num(row.get("karma"), int), "af_karma": num(row.get("af_karma"), int),
                       "comments": num(row.get("comment_count"), int)},
        "shortlist_reason": ("Top LW/AF post by " + ", ".join(row["picked_by"].split("|")) if row.get("picked_by")
                             else "In scope and high karma, but not in the notable list"),
        "extra": {"post_id": row["id"], "alignment_forum": af, "link_url": row.get("link_url", ""),
                  "forum_tags": row.get("tags", ""), "word_count": num(row.get("word_count"), int),
                  "scope_first_pass": row.get("scope_first_pass", "")},
    }


def extra_lw_rows(notable: set[str]) -> list[dict]:
    """The LW_EXTRA highest-karma posts marked include by the first-pass scope check and not already notable."""
    scope = {}
    for line in LW_SCOPE_FIRST_PASS.read_text().splitlines():
        d = json.loads(line)
        scope[d["id"]] = d.get("scope")
    pool = [r for r in csv.DictReader(LW_RAW.open()) if scope.get(r["id"]) == "include" and r["id"] not in notable]
    return sorted(pool, key=lambda r: -int(r["karma"] or 0))[:LW_EXTRA]


def org_item(item: dict) -> dict:
    """One of Lenz's org sources, already in the item format."""
    item["shortlist_reason"] = f"Listed on {item['extra']['orgs']}'s research page (Lenz's org list)"
    item["popularity"] = {}
    return item


def safety_stack_items() -> list[dict]:
    items, seen = [], set()
    for row in csv.DictReader(SAFETY_STACK.open()):
        if norm_title(row["title"]) in seen:
            continue
        seen.add(norm_title(row["title"]))
        items.append({
            "id": f"ss:{row['doc_id']}", "source": "safety_stack", "title": clean(row["title"]),
            "authors": clean(row["authors"]).replace(";", ","), "date": row["published"][:10], "url": row["url"],
            "text": clean(row["abstract"]), "links": [{"source": "safety_stack", "url": row["url"], "label": row["domain"]}],
            "popularity": {},
            "shortlist_reason": f"In the Safety Stack dataset but none of the scrapes; rated {row['relevance']}/5 relevant",
            "extra": {"doc_type": row["doc_type"], "domain": row["domain"], "arxiv_id": row.get("arxiv_id") or "",
                      "after_scrape_cutoff": row["after_scrape_cutoff"] == "True", "abstract_source": row["abstract_source"],
                      "categories": clean(row.get("categories")), "venue": clean(row.get("venue"))},
        })
    return items


def main():
    papers = [arxiv_item(r) for r in csv.DictReader(ARXIV_SHORTLIST.open())]
    notable = list(csv.DictReader(LW_POSTS.open()))
    extra = extra_lw_rows({r["id"] for r in notable})
    posts = [lw_item(r) for r in notable + extra]
    orgs = [org_item(i) for i in read_jsonl(LENZ_ITEMS)]
    stack = safety_stack_items()
    items = papers + posts + orgs + stack
    ids = [i["id"] for i in items]
    assert len(ids) == len(set(ids)), "duplicate ids in the inputs"
    write_jsonl(ITEMS, items)
    print(f"Wrote {ITEMS.relative_to(ITEMS.parent.parent)}: {len(papers)} arXiv papers + {len(posts)} LW/AF posts "
          f"({len(extra)} beyond the notable list) + {len(orgs)} org sources + {len(stack)} Safety Stack docs")


if __name__ == "__main__":
    main()
