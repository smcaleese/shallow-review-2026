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
LW_POSTS = INPUT / "lw-notable-posts.csv"
LW_SCOPE_OVERRIDES = INPUT / "lw-scope-overrides.json"
LW_ROSTER = INPUT / "lw-roster.json"
TAXONOMY_2025 = INPUT / "taxonomy-2025.yaml"

# Hand-edited files
VOCAB = ROOT / "vocab.yaml"
DEDUPE_OVERRIDES = ROOT / "dedupe-overrides.json"

# Pipeline outputs, in order
ITEMS = DATA / "1-items.jsonl"
LW_BODIES = CACHE / "lw-bodies.json"            # not committed: re-fetched from the LessWrong API
DEDUPE_CLAIMS = DATA / "2a-lw-paper-claims.jsonl"  # Claude's answer to "is this post a write-up of a paper?"
ITEMS_DEDUPED = DATA / "2-items-deduped.jsonl"
DEDUPE_REPORT = DATA / "2-dedupe-report.csv"
TAGS_RAW = DATA / "3-tags-raw.jsonl"
TAGS_FINAL = DATA / "4-tags-final.jsonl"
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
