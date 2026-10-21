#!/usr/bin/env python3
"""
Step 1: load the arXiv shortlist and the notable LW/AF posts into one list of items with a common format.

Usage (from facets-shared/):
    uv run python src/load_sources.py
Writes data/1-items.jsonl. Every item has:
    id                 "arxiv:<id without version>" or "lw:<post id>"
    source             "arxiv" or "lesswrong"
    title, authors, date (YYYY-MM-DD), url
    text               the arXiv abstract, or the post excerpt (step 2 swaps in the full post text)
    links              every place the work appears: [{"source", "url", "label"}]
    popularity         {"citations"} for papers; {"karma", "af_karma", "comments"} for posts
    shortlist_reason   why it was selected (papers: Claude's shortlist reason; posts: which top lists it is in)
    extra              source-specific fields kept for the site and CSV
"""

import csv

from common import ARXIV_SHORTLIST, ITEMS, LW_POSTS, base_arxiv_id, write_jsonl


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
        "shortlist_reason": "Top LW/AF post by " + ", ".join(row.get("picked_by", "").split("|")),
        "extra": {"post_id": row["id"], "alignment_forum": af, "link_url": row.get("link_url", ""),
                  "forum_tags": row.get("tags", ""), "word_count": num(row.get("word_count"), int),
                  "scope_first_pass": row.get("scope_first_pass", "")},
    }


def main():
    papers = [arxiv_item(r) for r in csv.DictReader(ARXIV_SHORTLIST.open())]
    posts = [lw_item(r) for r in csv.DictReader(LW_POSTS.open())]
    items = papers + posts
    ids = [i["id"] for i in items]
    assert len(ids) == len(set(ids)), "duplicate ids in the inputs"
    write_jsonl(ITEMS, items)
    print(f"Wrote {ITEMS.relative_to(ITEMS.parent.parent)}: {len(papers)} arXiv papers + {len(posts)} LW/AF posts")


if __name__ == "__main__":
    main()
