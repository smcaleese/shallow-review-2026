#!/usr/bin/env python3
"""
Rank the in-scope items (arXiv papers, LW/AF posts, org pages, Safety Stack docs) by impact, novelty and interest.

Two signals, kept separate so neither is counted twice:
- Claude's judgement of the content (impact, novelty, interest, 1-10 each). Claude sees every item at once (cached),
  so scores are relative to this year's set, and never sees citations or karma.
- Popularity: arXiv citations per month since publication, LW karma; each turned into a percentile within its
  source so papers and posts are comparable. Items that are both take the higher percentile. Org pages and Safety
  Stack docs have neither, so like very new papers they count as average popularity (the 50th percentile).

Score = (1 - POP_WEIGHT) * percentile of Claude's mean score + POP_WEIGHT * popularity percentile.

Usage (from facets-shared/):
    uv run python src/rank.py                  # score items not yet scored, then write the outputs
    uv run python src/rank.py --limit 20       # try it on a few items
    uv run python src/rank.py --offline        # no API calls: rebuild outputs from existing scores
Writes data/5-rankings-raw.jsonl (one line per item per pass), output/rankings.csv and output/top-papers.md.
src/select_budget.py then keeps the top items of each source.
"""

import argparse
import csv
import json
import logging
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import date

import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field, conint

from common import DATA, ITEMS_DEDUPED, OUTPUT, RANKINGS_CSV, ROOT, TAGS_FINAL, read_jsonl

load_dotenv(ROOT / ".env")
load_dotenv(ROOT.parent / "taxonomy" / ".env")  # facets-shared/.env may be empty; reuse the repo's existing key
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
logging.getLogger("httpx").setLevel(logging.WARNING)
log = logging.getLogger("rank")

RAW = DATA / "5-rankings-raw.jsonl"
CSV_OUT = RANKINGS_CSV
MD_OUT = OUTPUT / "top-papers.md"
DEFAULT_MODEL = "claude-opus-5-5"
BATCH = 10
MAX_PARALLEL = 8
POP_WEIGHT = 0.3
NEW_MONTHS = 2  # arXiv papers younger than this are counted as average popularity
TODAY = date.today()

SYSTEM = """You help select the most important AI safety research of 2026 for the Shallow Review of Technical AI \
Safety, read by expert researchers. Below are all {n} items in this year's review: arXiv papers (with abstracts), \
LessWrong / Alignment Forum posts (with their opening text), research posts from AI safety organisations' websites \
and other documents (papers, lab blog posts, system cards) with their abstract or opening text. Each has an id in brackets.

You will be given some item ids. Score each item from 1 to 10 on three dimensions, judged relative to the other \
items in this set:

- impact: how much the work should change what AI safety researchers believe or do, or how much it advances \
reducing catastrophic risk from AI. A solid result on a central problem beats a polished result on a niche one.
- novelty: a genuinely new result, technique, framing or argument, rather than an incremental extension, \
replication, survey or restatement of known views.
- interest: how surprising or notable an expert would find it; whether they'd tell colleagues about it.

Rules:
- Judge the content, not the authors, lab, venue or how widely it was shared.
- Arguments, agendas and conceptual posts can score highly if the idea is new and important; careful empirical \
work is not automatically high. Discount claims the text doesn't support.
- Use the whole range. Across the set, the median should be about 5 and only about a tenth of items should get \
8 or more on a dimension. Give 10 only to standout work.
- For each item, give one sentence on why it matters (or why it doesn't), specific enough to tell it apart.

ITEMS

{corpus}"""


class Score(BaseModel):
    id: str
    impact: conint(ge=1, le=10)
    novelty: conint(ge=1, le=10)
    interest: conint(ge=1, le=10)
    why: str = Field(description="One specific sentence")


class ScoreBatch(BaseModel):
    scores: list[Score]


# ---------- items ----------

def load_items() -> list[dict]:
    tags = {t["id"]: t for t in read_jsonl(TAGS_FINAL)}
    items = [i for i in read_jsonl(ITEMS_DEDUPED) if tags.get(i["id"], {}).get("scope", "exclude") != "exclude"]
    for i in items:
        i["summary"] = tags[i["id"]]["summary"]
        i["agenda"] = tags[i["id"]]["agenda"]
    items.sort(key=lambda i: i["id"])
    for n, i in enumerate(items, 1):
        i["rid"] = f"R{n:03d}"
    return items


def item_block(i: dict) -> str:
    kind = {"arxiv": "arXiv paper", "lesswrong": "LessWrong post", "org": "research org post"}.get(
        i["source"], (i["extra"].get("doc_type") or "document").replace("_", " "))
    if len(i.get("sources", [])) > 1:
        kind += " (also on LessWrong)"
    text = " ".join(str(i.get("text") or "").split())
    return f"[{i['rid']}] ({kind}, {i['date'][:7]}) {i['title'].strip()}\n{text}"


# ---------- Claude scoring ----------

def score_batch(client, system: str, batch: list[dict], model: str, effort: str) -> list[dict]:
    wanted = {i["rid"]: i for i in batch}
    user = f"Score these items: {', '.join(wanted)}"
    try:
        response = client.beta.messages.parse(
            model=model, max_tokens=16000,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user}],
            output_config={"effort": effort}, output_format=ScoreBatch,
            betas=["server-side-fallback-2026-07-01"], fallbacks="default")
    except anthropic.AuthenticationError:
        raise
    except anthropic.APIError as e:
        log.error(f"{batch[0]['rid']}: error calling Claude API: {e}")
        return []
    if response.stop_reason in ("refusal", "max_tokens") or response.parsed_output is None:
        log.warning(f"{batch[0]['rid']}: no scores ({response.stop_reason})")
        return []
    u = response.usage
    with _lock:
        for k, v in (("input", u.input_tokens), ("output", u.output_tokens),
                     ("cache_read", u.cache_read_input_tokens or 0), ("cache_write", u.cache_creation_input_tokens or 0)):
            usage[k] += v
    return [s.model_dump() | {"item": wanted[s.id]["id"]} for s in response.parsed_output.scores if s.id in wanted]


_lock = threading.Lock()
usage = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}


def run_pass(client, items: list[dict], targets: list[dict], p: int, model: str, effort: str) -> list[dict]:
    """Score `targets` against the whole set. Each pass shuffles the item order and the batches."""
    order = list(items)
    random.Random(p).shuffle(order)
    system = SYSTEM.format(n=len(items), corpus="\n\n".join(item_block(i) for i in order))
    todo = list(targets)
    random.Random(100 + p).shuffle(todo)
    batches = [todo[k:k + BATCH] for k in range(0, len(todo), BATCH)]
    results = score_batch(client, system, batches[0], model, effort)  # writes the prompt cache
    with ThreadPoolExecutor(MAX_PARALLEL) as pool:
        for part in pool.map(lambda b: score_batch(client, system, b, model, effort), batches[1:]):
            results += part
    missing = [i for i in targets if i["id"] not in {r["item"] for r in results}]
    if missing:
        log.warning(f"pass {p}: retrying {len(missing)} unscored items")
        for k in range(0, len(missing), 5):
            results += score_batch(client, system, missing[k:k + 5], model, effort)
    return [r | {"pass": p, "model": model} for r in results]


# ---------- combining ----------

def percentiles(values: dict[str, float]) -> dict[str, float]:
    """Mid-rank percentile in (0, 1]; ties share a value."""
    ranked = sorted(values.values())
    n = len(ranked)
    out = {}
    for k, v in values.items():
        below = sum(x < v for x in ranked)
        equal = sum(x == v for x in ranked)
        out[k] = (below + (equal + 1) / 2) / n
    return out


def months_since(d: str) -> float:
    y, m, day = map(int, d[:10].split("-"))
    return max(1.0, ((TODAY - date(y, m, day)).days) / 30.4)


def popularity(items: list[dict]) -> tuple[dict[str, float], dict[str, str]]:
    """Popularity percentile per item, plus a readable note (e.g. '95 cites (10.2/mo)' or '771 karma')."""
    cites = {i["id"]: (i["popularity"].get("citations") or 0) / months_since(i["date"])
             for i in items if i["popularity"].get("citations") is not None}
    karma = {i["id"]: i["popularity"]["karma"] for i in items if i["popularity"].get("karma") is not None}
    pc, pk = percentiles(cites), percentiles(karma)
    pct, note = {}, {}
    for i in items:
        p = i["popularity"]
        pct[i["id"]] = max(pc.get(i["id"], 0), pk.get(i["id"], 0))
        parts = []
        if p.get("citations") is not None:
            parts.append(f"{p['citations']} cites ({cites[i['id']]:.1f}/mo)")
        if p.get("karma") is not None:
            parts.append(f"{p['karma']} karma")
        note[i["id"]] = ", ".join(parts)
    return pct, note


def combine(items: list[dict], raw: list[dict], pop_weight: float) -> list[dict]:
    by_item = {}
    for r in raw:
        by_item.setdefault(r["item"], []).append(r)
    pop_pct, pop_note = popularity(items)
    rows = []
    for i in items:
        rs = by_item.get(i["id"])
        if not rs:
            continue
        mean = lambda k: sum(r[k] for r in rs) / len(rs)
        rows.append({"id": i["id"], "title": i["title"].strip(), "url": i["url"], "source": i["source"],
                     "both": len(i.get("sources", [])) > 1, "date": i["date"], "agenda": i["agenda"],
                     "impact": mean("impact"), "novelty": mean("novelty"), "interest": mean("interest"),
                     "why": rs[0]["why"], "passes": len(rs), "pop_pct": pop_pct[i["id"]], "pop": pop_note[i["id"]]})
    for r in rows:
        r["claude"] = (r["impact"] + r["novelty"] + r["interest"]) / 3
    claude_pct = percentiles({r["id"]: r["claude"] for r in rows})
    for r in rows:
        r["claude_pct"] = claude_pct[r["id"]]
        # Papers this new have had no time to be cited, so their citations say nothing yet: assume average
        # popularity (the 50th percentile) rather than penalise them or score them on Claude alone, which would
        # favour them over older work. LW karma mostly arrives within days, so posts keep their popularity.
        r["too_new"] = r["source"] == "arxiv" and not r["both"] and months_since(r["date"]) < NEW_MONTHS
        if r["too_new"]:
            r["pop_pct"] = 0.5
            r["pop"] += ", too new: counted as average"
        elif r["source"] in ("org", "safety_stack"):  # no citations or karma collected
            r["pop_pct"] = 0.5
            r["pop"] = "no popularity data: counted as average"
        r["score"] = (1 - pop_weight) * r["claude_pct"] + pop_weight * r["pop_pct"]
    rows.sort(key=lambda r: (-r["score"], -r["claude"]))
    for n, r in enumerate(rows, 1):
        r["rank"] = n
    return rows


# ---------- outputs ----------

def write_csv(rows: list[dict]):
    cols = ["rank", "score", "claude", "impact", "novelty", "interest", "claude_pct", "pop_pct", "pop", "title",
            "source", "date", "url", "why", "id"]
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow([round(r[c], 3) if isinstance(r[c], float) else r[c] for c in cols])


SOURCE_SHORT = {"arxiv": "arXiv", "lesswrong": "LW", "org": "Org list", "safety_stack": "Safety Stack"}


def md_table(rows: list[dict]) -> list[str]:
    lines = ["| # | Item | Impact | Novelty | Interest | Popularity | Why it matters |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        src = "arXiv+LW" if r["both"] else SOURCE_SHORT[r["source"]]
        title = r["title"].replace("|", "\\|")
        lines.append(f"| {r['rank']} | [{title}]({r['url']}) ({src}, {r['date'][:7]}) | {r['impact']:.1f} | "
                     f"{r['novelty']:.1f} | {r['interest']:.1f} | {r['pop']} ({r['pop_pct']:.0%}) | "
                     f"{r['why'].replace('|', '/')} |")
    return lines


def write_markdown(rows: list[dict], top: int, pop_weight: float, model: str, passes: int):
    gems = sorted((r for r in rows if r["pop_pct"] < 0.5 and r["rank"] > top and not r["too_new"]),
                  key=lambda r: -r["claude"])[:10]
    recent = sorted((r for r in rows if r["too_new"] and r["rank"] > top), key=lambda r: -r["claude"])[:10]
    lines = [
        "# Most impactful and interesting AI safety research of 2026", "",
        f"Ranked from the {len(rows)} in-scope candidate items for the shallow review (arXiv shortlist, notable "
        "LessWrong / Alignment Forum posts, Lenz's list of AI safety org research pages, and Safety Stack "
        "documents the scrapes missed).", "",
        f"**How the score works.** {model} read every item and scored each 1–10 on *impact* (should it change what "
        "safety researchers believe or do?), *novelty* (new result or idea vs. incremental) and *interest* "
        f"(would an expert tell colleagues?), relative to the rest of the set ({passes} pass"
        f"{'es' if passes > 1 else ''} averaged; Claude never saw citations or karma). *Popularity* is citations "
        "per month since publication for papers and karma for posts, as a percentile within each source. "
        f"Score = {1 - pop_weight:.0%} Claude's judgement (as a percentile) + {pop_weight:.0%} popularity, except "
        f"for arXiv papers under {NEW_MONTHS} months old (they haven't had time to be cited) and org / Safety Stack "
        "items (no citations or karma collected): they're counted as average popularity (50th percentile). "
        "Treat it as a shortlist to read, not a verdict: scores come from abstracts and post openings, and no "
        "person has checked them.", "",
        f"## Top {top}", "",
        *md_table(rows[:top]), "",
        "## Highly rated but little noticed", "",
        f"Outside the top {top}, rated highest by Claude but in the bottom half for popularity: candidates that "
        "may deserve more attention than they got.", "",
        *md_table(gems), "",
        "## Recent papers to watch", "",
        f"arXiv papers from the last {NEW_MONTHS} months, outside the top {top}, rated highest by Claude. Too new "
        "for citations to say anything yet.", "",
        *md_table(recent), "",
        f"The full ranking of all {len(rows)} items is in `output/rankings.csv`.", "",
    ]
    MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    MD_OUT.write_text("\n".join(lines))


def spearman(a: dict[str, float], b: dict[str, float]) -> float:
    keys = sorted(set(a) & set(b))
    ra, rb = percentiles({k: a[k] for k in keys}), percentiles({k: b[k] for k in keys})
    n = len(keys)
    ma, mb = sum(ra.values()) / n, sum(rb.values()) / n
    cov = sum((ra[k] - ma) * (rb[k] - mb) for k in keys)
    va = sum((ra[k] - ma) ** 2 for k in keys) ** 0.5
    vb = sum((rb[k] - mb) ** 2 for k in keys) ** 0.5
    return cov / (va * vb)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--passes", type=int, default=2, help="scoring passes to average (different orders/batches)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--pop-weight", type=float, default=POP_WEIGHT, help="weight of popularity in the score, 0-1")
    ap.add_argument("--top", type=int, default=40, help="items in the main table of top-papers.md")
    ap.add_argument("--limit", type=int, help="only score this many items (a fixed random sample)")
    ap.add_argument("--offline", action="store_true", help="no API calls; rebuild outputs from existing scores")
    args = ap.parse_args()

    items = load_items()
    raw = [r for r in read_jsonl(RAW) if r["model"] == args.model]
    if not args.offline:
        targets = items if not args.limit else random.Random(0).sample(items, args.limit)
        client = anthropic.Anthropic(timeout=900, max_retries=4)
        for p in range(args.passes):
            done = {r["item"] for r in raw if r["pass"] == p}
            todo = [i for i in targets if i["id"] not in done]
            if not todo:
                continue
            log.info(f"pass {p}: scoring {len(todo)} items")
            new = run_pass(client, items, todo, p, args.model, args.effort)
            with RAW.open("a") as f:
                f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in new)
            raw += new
        cost = (usage["input"] * 4 + usage["output"] * 20 + usage["cache_read"] * 0.2 + usage["cache_write"] * 5) / 1e6
        log.info(f"tokens: {usage}; about ${cost:.2f} at Opus 5.5 prices")

    passes = sorted({r["pass"] for r in raw})
    if len(passes) > 1:
        means = [{r["item"]: (r["impact"] + r["novelty"] + r["interest"]) / 3 for r in raw if r["pass"] == p}
                 for p in passes[:2]]
        log.info(f"agreement between passes 0 and 1 (Spearman, mean score): {spearman(*means):.2f}")
    rows = combine(items, raw, args.pop_weight)
    write_csv(rows)
    write_markdown(rows, min(args.top, len(rows)), args.pop_weight, args.model, len(passes))
    log.info(f"wrote {CSV_OUT.name} and {MD_OUT.name}: {len(rows)} items ranked")


if __name__ == "__main__":
    main()
