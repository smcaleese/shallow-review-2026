"""Paths and small helpers shared by the pipeline scripts."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "input"
DATA = ROOT / "data"
CACHE = ROOT / "cache"
OUTPUT = ROOT / "output"
SITE = ROOT / "site"

# Inputs (copied in by sync_inputs.sh)
ARXIV_SHORTLIST = INPUT / "arxiv-papers-shortlisted.csv"
ARXIV_FILTERED_DIR = INPUT / "arxiv-papers-filtered"
LW_POSTS = INPUT / "lw-posts-shortlisted.csv"
LW_SCOPE_OVERRIDES = INPUT / "lw-scope-overrides.json"
LW_ROSTER = INPUT / "lw-roster.json"
LENZ_SOURCES = INPUT / "lenz-org-sources.csv"          # made from lenz-org-sources.md by src/parse_lenz_orgs.py
SAFETY_STACK = INPUT / "safety-stack-filtered.csv"     # Safety Stack docs rated relevant (safety-stack/ pipeline)
TAXONOMY_2025 = INPUT / "taxonomy-2025.yaml"

# Hand-edited files
VOCAB = ROOT / "vocab.yaml"
DEDUPE_OVERRIDES = ROOT / "dedupe-overrides.json"

# The review's sources: the site shows exactly the items in draft-pipeline's source lists (src/select_budget.py).
SOURCE_LISTS = ROOT.parent / "draft-pipeline" / "data" / "sources-links"
SOURCE_LIST_NAMES = ["shortlist-arxiv-2026", "shortlist-lw-2026", "facets-org-2026", "facets-safetystack-2026"]

# Pipeline outputs, in order
LENZ_ITEMS = DATA / "1b-lenz-items.jsonl"      # Lenz's org sources with their page text (src/fetch_lenz_pages.py)
ITEMS = DATA / "1-items.jsonl"
LW_BODIES = CACHE / "lw-bodies.json"            # not committed: re-fetched from the LessWrong API
DEDUPE_CLAIMS = DATA / "2a-lw-paper-claims.jsonl"  # Claude's answer to "is this post a write-up of a paper?"
ITEMS_DEDUPED = DATA / "2-items-deduped.jsonl"
DEDUPE_REPORT = DATA / "2-dedupe-report.csv"
TAGS_RAW = DATA / "3-tags-raw.jsonl"
TAGS_FINAL = DATA / "4-tags-final.jsonl"
RANKINGS_CSV = OUTPUT / "rankings.csv"
SELECTED = DATA / "6-selected.json"             # ids of the items in the source lists, read by build_site.py
ITEMS_CSV = OUTPUT / "items-tagged.csv"
SITE_DATA = SITE / "data.js"

ARXIV_ID = re.compile(r"(?:arxiv\.org/(?:abs|pdf|html)/|arXiv:\s?)(\d{4}\.\d{4,5})(?:v\d+)?", re.I)


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def write_jsonl(path: Path, records: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))


def base_arxiv_id(arxiv_id: str) -> str:
    """'2601.10387v2' -> '2601.10387'"""
    return re.sub(r"v\d+$", "", str(arxiv_id).strip())


def norm_title(title: str) -> str:
    """Lowercase, drop punctuation and a leading '[Paper]'-style tag, collapse spaces."""
    t = re.sub(r"^\s*\[[^\]]*\]\s*", "", str(title).lower())
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def source_key(url: str) -> str:
    """One key per work, to match items against URL lists: the arXiv ID, the LessWrong post ID, or the bare URL."""
    m = ARXIV_ID.search(url)
    if m:
        return f"arxiv:{m.group(1)}"
    m = re.search(r"(?:lesswrong\.com|alignmentforum\.org)/posts/(\w+)", url)
    if m:
        return f"lw:{m.group(1)}"
    return re.sub(r"^https?://(www\.)?", "", url.strip()).rstrip("/")
