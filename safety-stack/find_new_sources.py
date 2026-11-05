"""Find 2026 Safety Stack documents that the Shallow Review 2026 sources don't already have.

The Shallow Review sources are every arXiv paper and LessWrong/Alignment Forum post the scrapers collected for 2026
(raw, before any relevance filtering), plus the facets-shared inputs and the main pipeline's 2026 links. A Safety Stack
document counts as already covered if it shares an arXiv ID, a LessWrong/AF post ID, a URL or an exact (normalized)
title with any of them.

Run from this folder:  uv run python find_new_sources.py
Writes output/safety-stack-2026-new.csv (+ .jsonl) and output/safety-stack-2026-matches.csv.
"""

import glob
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path

import pandas as pd
from datasets import load_dataset

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "output"
SCRAPERS = ROOT / "scraping-scripts"

ARXIV_RE = re.compile(r"(?:arxiv\.org/(?:abs|pdf|html)/|arxiv\.)(\d{4}\.\d{4,5})", re.I)
LW_RE = re.compile(r"(?:lesswrong\.com|alignmentforum\.org|greaterwrong\.com)/posts/([A-Za-z0-9]{17})", re.I)


def arxiv_id(s):
    m = ARXIV_RE.search(str(s or ""))
    return m.group(1) if m else None


def lw_id(s):
    m = LW_RE.search(str(s or ""))
    return m.group(1) if m else None


def norm_url(s):
    s = str(s or "").strip().lower()
    if not s.startswith("http"):
        return None
    s = re.sub(r"^https?://(www\.)?", "", s).split("#")[0].split("?")[0].rstrip("/")
    return s or None


def norm_title(s):
    s = re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()
    return s if len(s) >= 15 else None  # skip very short titles, which collide by accident


# ---------- Shallow Review 2026 sources ----------

def read_csvs(pattern):
    files = sorted(glob.glob(str(pattern)))
    return pd.concat([pd.read_csv(f, dtype=str) for f in files], ignore_index=True) if files else pd.DataFrame()


def load_reference():
    """Returns one row per reference item: source, tier, arxiv, lw, url, title."""
    rows = []

    def add(source, tier, df, url_cols, title_col="title", id_col=None):
        for r in df.to_dict("records"):
            urls = [r.get(c) for c in url_cols if isinstance(r.get(c), str)]
            ax = arxiv_id(f"arxiv.org/abs/{r[id_col]}") if id_col and isinstance(r.get(id_col), str) else None
            ax = ax or next(filter(None, map(arxiv_id, urls)), None)
            rows.append({
                "source": source, "tier": tier, "arxiv": ax,
                "lw": next(filter(None, map(lw_id, urls)), None),
                "urls": [u for u in map(norm_url, urls) if u],
                "title": norm_title(r.get(title_col)),
            })

    arx = SCRAPERS / "arxiv-scraper"
    add("arxiv", "raw", read_csvs(arx / "results/raw/2026/*/*.csv"), ["pdf_url"], id_col="arxiv_id")
    add("arxiv", "filtered", read_csvs(arx / "results/filtered/2026/*/arxiv-papers-filtered.csv"), ["pdf_url"], id_col="arxiv_id")
    add("arxiv", "shortlisted", read_csvs(arx / "results/shortlisted/2026/arxiv-papers-shortlisted.csv"), ["pdf_url"], id_col="arxiv_id")
    add("arxiv", "shortlisted", read_csvs(arx / "results/shortlisted-20/2026/arxiv-papers-shortlisted.csv"), ["pdf_url"], id_col="arxiv_id")
    # The `id` column here was read as a float upstream (2601.00420 -> 2601.0042), so match on `url` instead.
    add("arxiv", "raw", read_csvs(arx / "input/ai_safety_papers_2026_jan-sep.csv"), ["url"])

    lw = SCRAPERS / "AF-and-LW-scraper/results"
    add("lw", "raw", read_csvs(lw / "1-lw-posts-raw.csv"), ["url", "link_url"])
    add("lw", "filtered", read_csvs(lw / "2-lw-posts-highly-relevant.csv"), ["url", "link_url"])

    fs = ROOT / "facets-shared/input"
    add("arxiv", "filtered", read_csvs(fs / "arxiv-papers-filtered/*.csv"), ["pdf_url"], id_col="arxiv_id")
    add("arxiv", "shortlisted", read_csvs(fs / "arxiv-papers-shortlisted.csv"), ["pdf_url"], id_col="arxiv_id")
    add("lw", "shortlisted", read_csvs(fs / "lw-notable-posts.csv"), ["url", "link_url"])

    links = [l.strip() for l in open(ROOT / "main-pipeline/data/sources-links/arxiv-2026.txt") if l.startswith("http")]
    db = sqlite3.connect(ROOT / "main-pipeline/data-2026/data.db")
    links += [u for (u,) in db.execute("select url from collect")]
    add("main-pipeline", "shortlisted", pd.DataFrame({"url": links}), ["url"])
    return pd.DataFrame(rows)


SCRAPE_CUTOFF = pd.Timestamp("2026-10-10")
TIER_ORDER = {"raw": 0, "filtered": 1, "shortlisted": 2}


def build_index(ref):
    """key -> (best tier seen, sources)"""
    idx = {}
    for r in ref.itertuples():
        keys = [("arxiv", r.arxiv), ("lw", r.lw), ("title", r.title)] + [("url", u) for u in r.urls]
        for k in keys:
            if k[1]:
                tier, srcs = idx.get(k, ("raw", set()))
                idx[k] = (max(tier, r.tier, key=TIER_ORDER.get), srcs | {r.source})
    return idx


# ---------- Safety Stack 2026 ----------

def payload(ann, kind):
    a = ann.get(kind)
    return (a or {}).get("payload") or {}


def doc_keys(row):
    urls = [row["canonical_url"]] + [m["canonical_url"] for m in row["identity"]["members"]]
    keys = {("url", u) for u in map(norm_url, urls) if u}
    for m in row["identity"]["members"]:
        v = m["key_value"]
        if m["key_kind"] == "fm_post":
            keys.add(("lw", v))
        urls.append(v)
    keys |= {("arxiv", a) for a in map(arxiv_id, urls) if a}
    keys |= {("lw", l) for l in map(lw_id, urls) if l}
    keys |= {("title", t) for t in {norm_title(row["title"])} | {norm_title(m["title"]) for m in row["identity"]["members"]} if t}
    return keys


def main():
    ref = load_reference()
    print("Shallow Review 2026 reference items:", Counter(zip(ref.source, ref.tier)))
    idx = build_index(ref)

    docs = load_dataset("thesafetystack/the-safety-stack", split="train")
    d26 = docs.filter(lambda r: r["published_date"] is not None and r["published_date"].year == 2026)

    out = []
    for row in d26:
        hits = [(k, idx[k]) for k in doc_keys(row) if k in idx]
        ann = row["annotations"]
        sr = payload(ann, "shallow_review_relevance")
        url = row["canonical_url"] or ""
        out.append({
            "doc_id": row["doc_id"],
            "title": row["title"],
            "url": url,
            "published_date": row["published_date"],
            "doc_type": row["doc_type"],
            "domain": re.sub(r"^www\.", "", url.split("/")[2]) if url.count("/") >= 2 else None,
            "channels": ",".join(row["identity"]["channels"]),
            "authors": "; ".join(a["name"] for a in row["authors"] or [])[:300],
            "sr_verdict": sr.get("verdict"),
            "sr_confidence": sr.get("confidence"),
            "sr_category": sr.get("category"),
            "sr_agenda": sr.get("agenda"),
            "stack_verdict": payload(ann, "stack_relevance").get("verdict"),
            "sr_quote": ((sr.get("quotes") or [{}])[0].get("text") or "")[:400],
            # The dataset withholds abstracts and full text, so these quotes are the only text it ships
            "excerpt": " … ".join(dict.fromkeys(
                q["text"] for kind in ("screen", "stack_relevance", "shallow_review_relevance")
                for q in payload(ann, kind).get("quotes") or [] if q.get("text")
            ))[:2500],
            "matched": bool(hits),
            "matched_by": ",".join(sorted({k[0] for k, _ in hits})),
            "matched_tier": max((v[0] for _, v in hits), key=TIER_ORDER.get, default=None),
            "matched_sources": ",".join(sorted(set().union(*(v[1] for _, v in hits)))) if hits else "",
        })
    df = pd.DataFrame(out)

    print(f"\nSafety Stack 2026 docs: {len(df)}")
    print("Already in Shallow Review sources:", df.matched.sum())
    print(df[df.matched].groupby(["matched_sources", "matched_tier"]).size().to_string())
    print("Matched by:", Counter(df[df.matched].matched_by).most_common())

    # The arXiv scrape stops on Oct 9 and the LessWrong scrape on Oct 10, so later docs are missing just because they're newer.
    df["after_scrape_cutoff"] = pd.to_datetime(df.published_date) > SCRAPE_CUTOFF
    df["verdict_rank"] = df.sr_verdict.map({"relevant": 0, "borderline": 1, "irrelevant": 2})
    new = df[~df.matched].sort_values(["verdict_rank", "sr_confidence"], ascending=[True, False]).drop(columns="verdict_rank")
    df = df.drop(columns="verdict_rank")
    print(f"\nNot in Shallow Review sources: {len(new)}")
    print(new.doc_type.value_counts().to_string())
    print(new.domain.value_counts().head(20).to_string())
    print(new.sr_verdict.value_counts().to_string())
    print("Published after the scrape cutoff:", new.after_scrape_cutoff.sum())

    OUT.mkdir(exist_ok=True)
    new.to_csv(OUT / "safety-stack-2026-new.csv", index=False)
    new.to_json(OUT / "safety-stack-2026-new.jsonl", orient="records", lines=True, date_format="iso")
    df[df.matched].to_csv(OUT / "safety-stack-2026-matches.csv", index=False)
    print(f"\nWrote {OUT}/safety-stack-2026-new.csv and .jsonl")


if __name__ == "__main__":
    main()
