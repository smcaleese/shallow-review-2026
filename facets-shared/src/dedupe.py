#!/usr/bin/env python3
"""
Step 2: merge LW/AF posts that are write-ups of an arXiv paper into that paper (arXiv wins).

Usage (from facets-shared/):
    uv run python src/dedupe.py              # uses Claude to classify each post (cached in data/2a-lw-paper-claims.jsonl)
    uv run python src/dedupe.py --no-claude  # links and titles only, no API calls
    uv run python src/dedupe.py --cached-only  # use cached Claude answers, no new calls

For each post it gathers candidate papers from all 2026 filtered arXiv papers (not just the shortlist):
  - arXiv links or IDs in the post's link, body links or text
  - papers whose title is close to the post title
  - papers whose title is close to the paper Claude says the post writes up
Then it decides:
  - write-up of a shortlisted paper      -> post merged into the paper (paper keeps the LW link and karma)
  - write-up of a filtered, non-shortlisted paper -> paper promoted into the site, with the LW link and karma
  - anything else (critiques, roundups, work not on arXiv, no match) -> post kept as its own item
Decisions can be forced in dedupe-overrides.json: {"lw:<post id>": "keep" | "arxiv:<id>"}.

Then org (Lenz) and Safety Stack items that duplicate an item already kept (same arXiv ID, LW post ID, URL or title) are
merged into it, in the order arXiv > LW > org > Safety Stack; the kept item gains their links and an "also_listed" note.

Writes data/2-items-deduped.jsonl and data/2-dedupe-report.csv (one row per post) for checking.
"""

import argparse
import csv
import json
import logging
import re
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher
from typing import Literal

import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from common import (ARXIV_FILTERED_DIR, ARXIV_ID, DEDUPE_CLAIMS, DEDUPE_OVERRIDES, DEDUPE_REPORT, ITEMS,
                    ITEMS_DEDUPED, LW_BODIES, ROOT, base_arxiv_id, norm_title, read_jsonl, write_jsonl)
from load_sources import arxiv_item

load_dotenv(ROOT / ".env")
load_dotenv(ROOT.parent / "taxonomy" / ".env")  # facets-shared/.env may be empty; reuse the repo's existing key
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("dedupe")

MODEL = "claude-sonnet-5-5"
TITLE_MATCH = 0.9        # post title vs paper title: enough on its own
CLAIM_TITLE_MATCH = 0.85  # title Claude reports vs paper title
LINKED_TITLE_MATCH = 0.6  # a paper the post links to, whose title is also fairly close to the post's
MAX_CANDIDATES = 8


class PaperClaim(BaseModel):
    relation: Literal["writeup", "discusses", "several", "none"] = Field(
        description="writeup: the post mainly presents or summarises ONE specific paper (usually by the post's authors; "
                    "a linkpost or crosspost counts). discusses: mainly responds to or critiques someone else's paper. "
                    "several: covers several papers (roundup, org update, review). none: not about a specific paper.")
    paper_title: str = Field(description="For writeup or discusses: the paper's title as given in the post, else empty.")
    reason: str = Field(description="One short sentence.")


SYSTEM = """You help deduplicate a review of 2026 AI safety research that combines arXiv papers with LessWrong posts.
For one LessWrong post, decide whether it is mainly a write-up of ONE specific research paper.
You are given the post's title, authors, outgoing links and opening text, plus arXiv papers it may correspond to.
A linkpost, crosspost, summary or announcement of a single paper is a write-up, even if it adds some commentary.
A post that critiques or responds to someone else's paper is "discusses". Roundups and org updates covering
several papers are "several". Original essays, agendas and results not presented as a paper are "none".
A post whose main content is NEW results beyond the paper (e.g. applying a paper's method or benchmark to a new
model, or a follow-up experiment) is "none", even if it is by the same authors and links the paper."""
PROMPT_VERSION = 2  # bump when SYSTEM changes so cached answers are redone


def similarity(a: str, b: str) -> float:
    a, b = norm_title(a), norm_title(b)
    if not a or not b:
        return 0.0
    matcher = SequenceMatcher(None, a, b)
    return matcher.ratio() if matcher.quick_ratio() >= 0.5 else 0.0


def load_arxiv_index() -> dict[str, dict]:
    """Every filtered 2026 arXiv paper (a superset of the shortlist), keyed by arXiv ID without version."""
    index = {}
    for path in sorted(ARXIV_FILTERED_DIR.glob("*.csv")):
        for row in csv.DictReader(path.open()):
            index[base_arxiv_id(row["arxiv_id"])] = row
    return index


def linked_ids(item: dict, body: dict | None) -> list[str]:
    hay = " ".join([item["extra"].get("link_url", ""), *(body or {}).get("links", []), (body or {}).get("text", "")[:6000]])
    return list(dict.fromkeys(m.group(1) for m in ARXIV_ID.finditer(hay)))


def best_title_matches(title: str, index: dict[str, dict], threshold: float) -> list[tuple[str, float]]:
    scored = [(pid, similarity(title, row["title"])) for pid, row in index.items()]
    return sorted([s for s in scored if s[1] >= threshold], key=lambda s: -s[1])


def ask_claude(client, item: dict, body: dict | None, candidates: list[tuple[str, str]]) -> dict | None:
    links = "\n".join((body or {}).get("links", [])[:40]) or "none"
    cand = "\n".join(f"- {pid}: {title}" for pid, title in candidates) or "none found"
    user = (f"Title: {item['title']}\nAuthors (forum usernames): {item['authors']}\n"
            f"Linked original: {item['extra'].get('link_url') or 'none'}\n\nOutgoing links:\n{links}\n\n"
            f"arXiv papers this post might correspond to:\n{cand}\n\n"
            f"Opening text:\n{((body or {}).get('text') or item['text'])[:3000]}")
    try:
        response = client.beta.messages.parse(
            model=MODEL, max_tokens=2000,
            system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user}], output_format=PaperClaim,
            output_config={"effort": "low"}, betas=["server-side-fallback-2026-07-01"], fallbacks="default")
    except anthropic.AuthenticationError:
        raise
    except anthropic.APIError as e:
        log.error(f"{item['id']}: {e}")
        return None
    if response.stop_reason in ("refusal", "max_tokens") or response.parsed_output is None:
        log.warning(f"{item['id']}: no answer ({response.stop_reason})")
        return None
    return response.parsed_output.model_dump()


def candidates_for(item: dict, body: dict | None, index: dict[str, dict]) -> tuple[list[str], dict[str, float]]:
    """Candidate paper IDs (linked ones first) and each candidate's title similarity to the post."""
    linked = [pid for pid in linked_ids(item, body) if pid in index]
    by_title = [pid for pid, _ in best_title_matches(item["title"], index, LINKED_TITLE_MATCH)]
    ids = list(dict.fromkeys(linked + by_title))[:MAX_CANDIDATES]
    return ids, {pid: similarity(item["title"], index[pid]["title"]) for pid in ids}


def decide(item, body, index, claim, override) -> tuple[str | None, str]:
    """Return (matched arXiv ID or None, how it was decided)."""
    if override == "keep":
        return None, "override"
    if override:
        return base_arxiv_id(override.removeprefix("arxiv:")), "override"

    linked = [pid for pid in linked_ids(item, body) if pid in index]
    link_url_ids = [m.group(1) for m in ARXIV_ID.finditer(item["extra"].get("link_url", ""))]
    title_hits = best_title_matches(item["title"], index, TITLE_MATCH)

    if claim is None:  # no Claude answer: only near-certain signals
        if link_url_ids and link_url_ids[0] in index:
            return link_url_ids[0], "linked original is the arXiv paper"
        if title_hits:
            return title_hits[0][0], f"title match ({title_hits[0][1]:.2f})"
        return None, "no strong link or title match"

    if claim["relation"] != "writeup":
        return None, f"claude: {claim['relation']}"
    # Claude says it's a write-up: find which paper
    if claim["paper_title"]:
        claim_hits = best_title_matches(claim["paper_title"], index, CLAIM_TITLE_MATCH)
        if claim_hits:
            return claim_hits[0][0], f"claude write-up + title match ({claim_hits[0][1]:.2f})"
    if title_hits:
        return title_hits[0][0], f"claude write-up + post title match ({title_hits[0][1]:.2f})"
    if link_url_ids and link_url_ids[0] in index:
        return link_url_ids[0], "claude write-up + linked original"
    # A post can link papers it only cites, so a linked paper needs a fairly close title too, and no
    # different paper named by Claude
    close = [pid for pid in linked if similarity(item["title"], index[pid]["title"]) >= LINKED_TITLE_MATCH]
    if not claim["paper_title"] and len(close) == 1:
        return close[0], "claude write-up + linked paper with a close title"
    return None, "claude write-up, but paper not in the 2026 arXiv data"


def main():
    parser = argparse.ArgumentParser(description="Merge LW posts that are write-ups of arXiv papers into the papers")
    parser.add_argument("--no-claude", action="store_true", help="Skip the Claude check; use links and titles only")
    parser.add_argument("--cached-only", action="store_true",
                        help="Use cached Claude answers but make no new calls (uncached posts fall back to links and titles)")
    args = parser.parse_args()

    items = read_jsonl(ITEMS)
    bodies = json.loads(LW_BODIES.read_text()) if LW_BODIES.exists() else {}
    if not bodies:
        log.warning("No post bodies cached; run src/fetch_lw_bodies.py first for better matching")
    index = load_arxiv_index()
    overrides = json.loads(DEDUPE_OVERRIDES.read_text()) if DEDUPE_OVERRIDES.exists() else {}
    posts = [i for i in items if i["source"] == "lesswrong"]
    log.info(f"{len(posts)} posts vs {len(index)} filtered arXiv papers")

    # Claude's classification of each post, cached so reruns are free
    claims = {c["id"]: c for c in read_jsonl(DEDUPE_CLAIMS) if c.get("prompt_version") == PROMPT_VERSION}
    if not args.no_claude and not args.cached_only:
        client = anthropic.Anthropic()
        todo = [p for p in posts if p["id"] not in claims]
        log.info(f"{len(claims)} posts already classified, asking Claude about {len(todo)}")
        lock = threading.Lock()

        def work(post):
            body = bodies.get(post["extra"]["post_id"])
            ids, _ = candidates_for(post, body, index)
            claim = ask_claude(client, post, body, [(pid, index[pid]["title"]) for pid in ids])
            if claim:
                with lock:
                    claims[post["id"]] = {"id": post["id"], "prompt_version": PROMPT_VERSION, **claim}
                    DEDUPE_CLAIMS.parent.mkdir(parents=True, exist_ok=True)
                    with DEDUPE_CLAIMS.open("a") as f:
                        f.write(json.dumps(claims[post["id"]]) + "\n")

        with ThreadPoolExecutor(8) as executor:
            list(executor.map(work, todo))

    kept = [i for i in items if i["source"] == "arxiv"]
    by_id = {i["id"]: i for i in kept}
    report = []
    for post in posts:
        body = bodies.get(post["extra"]["post_id"])
        claim = None if args.no_claude else claims.get(post["id"])
        pid, how = decide(post, body, index, claim, overrides.get(post["id"]))
        row = {"post_id": post["id"], "post_title": post["title"], "karma": post["popularity"]["karma"],
               "decision": "kept", "paper_id": "", "paper_title": "", "how": how,
               "claude_relation": (claim or {}).get("relation", ""), "claude_paper": (claim or {}).get("paper_title", ""),
               "claude_reason": (claim or {}).get("reason", "")}
        if pid:
            if pid not in index:
                row["how"] += " (override ID not in the arXiv data; post kept)"
                kept.append(post)
                report.append(row)
                continue
            key = f"arxiv:{pid}"
            if key not in by_id:  # filtered but not shortlisted: promote it
                paper = arxiv_item(index[pid])
                paper["promoted_by"] = post["id"]
                paper["shortlist_reason"] = f"Not shortlisted on arXiv; added because the LW post \"{post['title']}\" " \
                                            f"({post['popularity']['karma']} karma) writes it up."
                by_id[key] = paper
                kept.append(paper)
                row["decision"] = "promoted"
            else:
                row["decision"] = "merged"
            paper = by_id[key]
            paper.setdefault("merged_posts", []).append(post["id"])
            paper["links"] += [l for l in post["links"] if l["url"] not in {x["url"] for x in paper["links"]}]
            pop = paper["popularity"]
            for k in ("karma", "af_karma", "comments"):
                if post["popularity"].get(k) is not None:
                    pop[k] = max(pop.get(k) or 0, post["popularity"][k])
            paper["extra"].setdefault("lw_titles", []).append(post["title"])
            row.update(paper_id=key, paper_title=paper["title"])
        else:
            kept.append(post)
        report.append(row)

    merged_extra = merge_listings(kept, [i for i in items if i["source"] in ("org", "safety_stack")])
    for item in kept:
        item["sources"] = sorted({item["source"]} | ({"lesswrong"} if item.get("merged_posts") else set()))
    write_jsonl(ITEMS_DEDUPED, kept)
    DEDUPE_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with DEDUPE_REPORT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(report[0]))
        writer.writeheader()
        writer.writerows(sorted(report, key=lambda r: (r["decision"] == "kept", -(r["karma"] or 0))))

    counts = {d: sum(r["decision"] == d for r in report) for d in ("merged", "promoted", "kept")}
    by_source = Counter(i["source"] for i in kept)
    log.info(f"Posts: {counts['merged']} merged into shortlisted papers, {counts['promoted']} promoted a paper, "
             f"{counts['kept']} kept. Items: {len(kept)} ({', '.join(f'{v} {k}' for k, v in by_source.items())})")
    log.info(f"Org and Safety Stack items: {merged_extra} merged into an existing item")
    log.info(f"Wrote {ITEMS_DEDUPED.name} and {DEDUPE_REPORT.name}")


LISTING_LABEL = {"org": "Lenz's org list", "safety_stack": "Safety Stack"}
LW_POST = re.compile(r"(?:lesswrong\.com|alignmentforum\.org)/posts/([A-Za-z0-9]{17})")


def keys_of(item: dict) -> set[str]:
    """Identity keys: arXiv IDs, LW post IDs, URLs and the normalised title."""
    urls = [item["url"]] + [l["url"] for l in item["links"]]
    keys = {"t:" + norm_title(item["title"])}
    for u in urls:
        keys.add("u:" + re.sub(r"^https?://(www\.)?", "", u.lower()).rstrip("/"))
        keys.update("a:" + base_arxiv_id(m) for m in ARXIV_ID.findall(u))
        keys.update("p:" + m for m in LW_POST.findall(u))
    if item["source"] == "arxiv":
        keys.add("a:" + item["id"].removeprefix("arxiv:"))
    if item["source"] == "lesswrong":
        keys.add("p:" + item["extra"]["post_id"])
    if item["extra"].get("arxiv_id"):
        keys.add("a:" + base_arxiv_id(item["extra"]["arxiv_id"]))
    return keys


def merge_listings(kept: list[dict], extra: list[dict]) -> int:
    """Append org and Safety Stack items to `kept`, merging any that duplicate an item already there."""
    owner = {k: i for i in kept for k in keys_of(i)}
    merged = 0
    for item in extra:  # org items come before Safety Stack ones, so Lenz's copy wins
        keys = keys_of(item)
        match = next((owner[k] for k in keys if k in owner), None)
        if match is None:
            kept.append(item)
            owner.update({k: item for k in keys})
            continue
        merged += 1
        match["links"] += [l for l in item["links"] if l["url"] not in {x["url"] for x in match["links"]}]
        match.setdefault("also_listed", []).append(LISTING_LABEL[item["source"]])
    return merged


if __name__ == "__main__":
    main()
