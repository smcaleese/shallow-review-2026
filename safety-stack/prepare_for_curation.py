"""Turn output/safety-stack-2026-new.csv into the arXiv scraper's raw format, so its filter and shortlist scripts can
curate it unchanged.

Writes results/raw/2026/<month>/arxiv-papers-raw.csv (month = the document's published month). The `arxiv_id` column is
the curation key: the arXiv ID for arXiv papers, the Safety Stack doc_id for everything else.

The dataset withholds abstracts, so they are fetched:
- arXiv papers: the arXiv API (abstract, categories, comment, journal ref), plus Semantic Scholar citations and author
  h-indexes via the scraper's own semantic_scholar.py
- other papers with a DOI: Semantic Scholar, falling back to OpenAlex
- blogs, posts, system cards and anything still missing: the quotes the dataset includes for each document

Uses the scraping-scripts environment (it imports the scraper's helpers). From the repo root:
    uv run --project scraping-scripts python safety-stack/prepare_for_curation.py
"""

import os
import re
import sys
import time
from pathlib import Path

import arxiv
import pandas as pd
import requests

HERE = Path(__file__).resolve().parent
SCRAPER_SRC = HERE.parent / "scraping-scripts/arxiv-scraper/src"
sys.path.insert(0, str(SCRAPER_SRC))
from semantic_scholar import add_semantic_scholar_columns, citations_per_month, top_author, venue  # noqa: E402

IN_PATH = HERE / "output/safety-stack-2026-new.csv"
RAW_DIR = HERE / "results/raw"
RAW_FILENAME = "arxiv-papers-raw.csv"
CACHE = HERE / "cache"

ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", re.I)
S2_URL = "https://api.semanticscholar.org/graph/v1/paper/batch"


def fetch_arxiv(ids):
    """arXiv metadata for each ID (no version), cached so reruns are instant."""
    path = CACHE / "arxiv.jsonl"
    cached = pd.read_json(path, lines=True, dtype={"id": str}) if path.exists() else pd.DataFrame(columns=["id"])
    todo = sorted(set(ids) - set(cached["id"]))
    print(f"arXiv: {len(ids) - len(todo)} cached, fetching {len(todo)}")
    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=5)
    rows = []
    for start in range(0, len(todo), 100):
        for r in client.results(arxiv.Search(id_list=todo[start:start + 100], max_results=100)):
            rows.append({
                "id": re.sub(r"v\d+$", "", r.get_short_id()), "abstract": r.summary.replace("\n", " "),
                "primary_category": r.primary_category, "categories": ", ".join(r.categories),
                "comment": r.comment, "journal_ref": r.journal_ref, "doi": r.doi, "pdf_url": r.pdf_url,
            })
        print(f"  {min(start + 100, len(todo))}/{len(todo)}")
    if rows:
        CACHE.mkdir(exist_ok=True)
        cached = pd.concat([cached, pd.DataFrame(rows)], ignore_index=True)
        cached.to_json(path, orient="records", lines=True)
    return cached.set_index("id")


def fetch_s2_by_doi(dois):
    """Semantic Scholar records (abstract, citations, venue, authors) for DOIs; None where unknown."""
    headers = {"x-api-key": k} if (k := os.getenv("SEMANTIC_SCHOLAR_API_KEY")) else {}
    out = []
    for start in range(0, len(dois), 500):
        batch = [f"DOI:{d}" for d in dois[start:start + 500]]
        for attempt in range(5):
            resp = requests.post(S2_URL, params={"fields": "abstract,citationCount,venue,authors.name,authors.hIndex"},
                                 json={"ids": batch}, headers=headers, timeout=60)
            if resp.status_code == 200:
                out += resp.json()
                break
            time.sleep(2 ** (attempt + 1))
        else:
            out += [None] * len(batch)
    return out


def openalex_abstract(doi):
    """Rebuild an abstract from OpenAlex's inverted index, or None."""
    try:
        r = requests.get(f"https://api.openalex.org/works/doi:{doi}", params={"select": "abstract_inverted_index"}, timeout=30)
        inv = r.json().get("abstract_inverted_index") if r.ok else None
    except requests.RequestException:
        return None
    if not inv:
        return None
    words = sorted((pos, w) for w, positions in inv.items() for pos in positions)
    return " ".join(w for _, w in words)


def main():
    df = pd.read_csv(IN_PATH, dtype=str)
    df["arxiv"] = df["url"].str.extract(ARXIV_RE, expand=False)
    df["doi_value"] = df["url"].str.extract(r"doi\.org/(.+)$", expand=False)
    df["published"] = df["published_date"].str[:10]
    # One row per curation key (a few docs share an arXiv ID)
    df["arxiv_id"] = df["arxiv"].fillna(df["doc_id"])
    df = df.drop_duplicates("arxiv_id").reset_index(drop=True)

    # Columns the scraper's raw CSVs have
    for col in ["abstract", "primary_category", "categories", "comment", "journal_ref", "doi", "pdf_url"]:
        df[col] = None
    df["matched_groups"] = "safety-stack"
    df["abstract_source"] = None

    # arXiv papers
    ax = df["arxiv"].notna()
    meta = fetch_arxiv(df.loc[ax, "arxiv"].tolist())
    for col in ["abstract", "primary_category", "categories", "comment", "journal_ref", "doi", "pdf_url"]:
        df.loc[ax, col] = df.loc[ax, "arxiv"].map(meta[col])
    df.loc[ax & df["abstract"].notna(), "abstract_source"] = "arxiv"
    df.loc[ax, "pdf_url"] = df.loc[ax, "pdf_url"].fillna(df.loc[ax, "url"])
    arx = add_semantic_scholar_columns(df[ax].copy())
    s2_cols = ["citation_count", "citations_per_month", "venue", "max_author_h_index", "max_h_index_author"]

    # Everything else: Semantic Scholar by DOI, then OpenAlex
    rest = df[~ax].copy()
    rest["pdf_url"] = rest["url"]
    rest["categories"] = rest["doc_type"].fillna("unknown") + " (" + rest["domain"].fillna("") + ")"
    rest["comment"] = "Source: " + rest["domain"].fillna("") + ", " + rest["doc_type"].fillna("unknown type")
    has_doi = rest["doi_value"].notna()
    recs = fetch_s2_by_doi(rest.loc[has_doi, "doi_value"].tolist())
    rest.loc[has_doi, "doi"] = rest.loc[has_doi, "doi_value"]
    rest.loc[has_doi, "abstract"] = [(r or {}).get("abstract") for r in recs]
    rest["citation_count"] = pd.array([None] * len(rest), dtype="Int64")
    rest.loc[has_doi, "citation_count"] = pd.array([(r or {}).get("citationCount") for r in recs], dtype="Int64")
    rest["citations_per_month"] = citations_per_month(rest["citation_count"], rest["published"])
    rest["venue"] = None
    rest.loc[has_doi, "venue"] = [venue(r) for r in recs]
    tops = [top_author(r) for r in recs]
    rest["max_author_h_index"] = pd.array([None] * len(rest), dtype="Int64")
    rest.loc[has_doi, "max_author_h_index"] = pd.array([h for h, _ in tops], dtype="Int64")
    rest["max_h_index_author"] = None
    rest.loc[has_doi, "max_h_index_author"] = [n for _, n in tops]
    rest.loc[rest["abstract"].notna(), "abstract_source"] = "semantic_scholar"
    need = has_doi & rest["abstract"].isna()
    print(f"OpenAlex: fetching {need.sum()} abstracts")
    rest.loc[need, "abstract"] = [openalex_abstract(d) for d in rest.loc[need, "doi_value"]]
    rest.loc[need & rest["abstract"].notna(), "abstract_source"] = "openalex"

    out = pd.concat([arx, rest], ignore_index=True)
    # Last resort: the dataset's quotes from the document
    missing = out["abstract"].isna() | (out["abstract"].str.len() < 50)
    out.loc[missing, "abstract"] = "[No abstract available. Excerpts from the document:] " + out.loc[missing, "excerpt"].fillna("")
    out.loc[missing, "abstract_source"] = "excerpts"
    print("Abstract sources:", out["abstract_source"].value_counts().to_dict())

    # Same columns as the scraper's raw CSVs, then the Safety Stack fields
    cols = ["title", "authors", "published", "updated", "abstract", "primary_category", "categories", "arxiv_id",
            "pdf_url", "doi", "comment", "journal_ref", "matched_groups", *s2_cols,
            "doc_id", "url", "doc_type", "domain", "sr_verdict", "sr_category", "sr_agenda", "after_scrape_cutoff",
            "abstract_source"]
    out["updated"] = out["published"]
    out = out[cols]
    month = pd.to_datetime(out["published"]).dt.strftime("%b").str.lower()
    for m, group in out.groupby(month):
        path = RAW_DIR / "2026" / m / RAW_FILENAME
        path.parent.mkdir(parents=True, exist_ok=True)
        group.sort_values("published").to_csv(path, index=False)
        print(f"{path.relative_to(HERE)}: {len(group)}")


if __name__ == "__main__":
    main()
