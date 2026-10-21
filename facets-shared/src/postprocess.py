#!/usr/bin/env python3
"""
Step 4: enforce tagging rules in code that the tagger doesn't follow reliably (adapted from jord-facets).

Usage (from facets-shared/):
    uv run python src/postprocess.py
Reads data/3-tags-raw.jsonl (latest record per item) and writes data/4-tags-final.jsonl. Every changed record gets
a `pp` list saying what changed, so the rules can be audited.

Rules:
 1. A proposal as the primary move makes a `position` a `research_agenda`.
 2. Items with no work of their own (positions, agendas, reviews, ...) ran no experiments: substrate = [no_system],
    and evidence can't be tested/measured/observed (-> argued, or surveyed for reviews).
 3. frontier_internal only when a frontier lab is a stated producer.
 4. Phenomena: drop `generalisation` when a more specific child is present; argued items drop effect claims.
 5. Argued items drop behavioural_evals unless they propose an eval.
 6. `by`: roster tags only for LW research posts led by (or mostly by) that org's people, never with a
    personal-capacity disclaimer; `Academic` needs a university in the evidence; arXiv papers get no roster tags.
 7. Jord's reviewer scope decisions for LW posts (input/lw-scope-overrides.json) win over the tagger's.
"""

import json
import re
from collections import Counter

from common import LW_BODIES, LW_ROSTER, LW_SCOPE_OVERRIDES, TAGS_FINAL, TAGS_RAW, ITEMS_DEDUPED, read_jsonl, write_jsonl

LABS = {"Anthropic", "OpenAI", "Google DeepMind", "Meta", "xAI"}
PROGRAMMES = {"MATS", "SPAR", "MARS", "Anthropic Fellows", "Astra Fellowship (Constellation)", "LASR Labs"}
OWN_WORK_TYPES = {"empirical_study", "method_paper", "benchmark", "theory", "field_observations", "technical_report"}
EMPIRICAL_MOVES = {"notable_phenomenon", "measurement", "replication", "new_technique", "technique_improvement",
                   "stress_test", "toy_model", "observation"}
RESEARCH_TYPES = OWN_WORK_TYPES - {"field_observations"} | {"research_agenda", "open_questions", "org_update",
                                                            "position", "incident_report"}
GENERALISATION_CHILDREN = {"emergent_misalignment", "weird_generalisation", "subliminal_learning"}
EFFECT_CLAIMS = {"generalisation", "training_dynamics"}
DISCLAIMER = re.compile(r"personal capacity|views (are|expressed (here )?are) (my|our) own|not (necessarily )?"
                        r"(those|the views) of my employer|do not represent (the views of )?my employer", re.I)
UNIVERSITY = re.compile(r"universit|college|institute of technology|\bMIT\b|stanford|berkeley|oxford|cambridge|"
                        r"\bETH\b|EPFL|CMU|carnegie|princeton|harvard|NYU|toronto|mila|tsinghua", re.I)


def org_at(roster: dict, author: str, date: str) -> str | None:
    entry = roster.get(author)
    if not entry or entry.get("roster_tags") is False:
        return None
    if entry.get("until") and date >= entry["until"]:
        return entry.get("then")
    return entry["org"]


def process(tags: dict, item: dict, body: str, roster: dict, scope_overrides: dict) -> dict:
    t, pp = dict(tags), []
    primary = t["scientific_primary"]

    # 1
    if primary == "proposal" and t["item_type"] == "position":
        t["item_type"] = "research_agenda"
        pp.append("type position -> research_agenda (primary move is a proposal)")

    # 2
    own_work = t["item_type"] in OWN_WORK_TYPES or (t["item_type"] == "incident_report" and primary in EMPIRICAL_MOVES)
    if not own_work:
        if t["substrate"] != ["no_system"]:
            pp.append(f"substrate {t['substrate']} -> [no_system] (no experiments of its own)")
            t["substrate"] = ["no_system"]
        if t["evidence"] in ("tested", "measured", "observed"):
            new = "surveyed" if t["item_type"] == "review" else "argued"
            pp.append(f"evidence {t['evidence']} -> {new} (no experiments of its own)")
            t["evidence"] = new

    # 3
    stated = {b["org"] for b in t["by"] if b["basis"] == "stated"}
    if "frontier_internal" in t["substrate"] and not stated & LABS:
        replacement = "frontier_closed" if own_work else "no_system"
        t["substrate"] = list(dict.fromkeys(replacement if s == "frontier_internal" else s for s in t["substrate"]))
        pp.append(f"frontier_internal -> {replacement} (no stated frontier-lab producer)")

    # 4 + 5
    if "generalisation" in t["phenomenon"] and GENERALISATION_CHILDREN & set(t["phenomenon"]):
        t["phenomenon"] = [p for p in t["phenomenon"] if p != "generalisation"]
        pp.append("dropped generalisation (more specific phenomenon present)")
    if t["evidence"] == "argued":
        if EFFECT_CLAIMS & set(t["phenomenon"]):
            pp.append(f"dropped {sorted(EFFECT_CLAIMS & set(t['phenomenon']))} (argued item)")
            t["phenomenon"] = [p for p in t["phenomenon"] if p not in EFFECT_CLAIMS]
        if "behavioural_evals" in t["method"] and primary != "proposal":
            t["method"] = [m for m in t["method"] if m != "behavioural_evals"]
            pp.append("dropped behavioural_evals (argued item)")

    # 6
    disclaimer = bool(DISCLAIMER.search(body))
    authors = [a.strip() for a in item["authors"].split(",") if a.strip()]
    keep = []
    for b in t["by"]:
        org = b["org"]
        if b["basis"] == "author_roster":
            mapped = [org_at(roster, a, item["date"]) for a in authors]
            why = None
            if item["source"] != "lesswrong":
                why = "roster tags are for LW posts only"
            elif t["item_type"] not in RESEARCH_TYPES:
                why = "not a research post"
            elif org in LABS and t["item_type"] not in OWN_WORK_TYPES | {"org_update"}:
                why = "frontier-lab staff essay, not lab output"
            elif not (mapped and (mapped[0] == org or 2 * sum(m == org for m in mapped) >= len(authors))):
                why = "not first author or majority"
            elif disclaimer:
                why = "personal-capacity disclaimer"
            if why:
                pp.append(f"dropped roster by:{org} ({why})")
                continue
        elif disclaimer and org not in PROGRAMMES:
            pp.append(f"dropped by:{org} (text says views are the author's own)")
            continue
        if org == "Academic" and not UNIVERSITY.search(b.get("evidence", "")):
            pp.append("dropped by:Academic (no university in the evidence)")
            continue
        keep.append(b)
    t["by"] = keep

    # 7
    post_id = item["extra"].get("post_id")
    if post_id in scope_overrides and scope_overrides[post_id] != t["scope"]:
        pp.append(f"scope {t['scope']} -> {scope_overrides[post_id]} (reviewer decision)")
        t["scope"] = scope_overrides[post_id]

    t["pp"] = pp
    return t


def main():
    items = {i["id"]: i for i in read_jsonl(ITEMS_DEDUPED)}
    latest = {r["id"]: r for r in read_jsonl(TAGS_RAW)}  # later records (retags) win
    bodies = json.loads(LW_BODIES.read_text()) if LW_BODIES.exists() else {}
    roster = json.loads(LW_ROSTER.read_text())
    scope_overrides = json.loads(LW_SCOPE_OVERRIDES.read_text())

    out = []
    for item_id, tags in latest.items():
        item = items.get(item_id)
        if item is None:
            continue  # item no longer in the inputs
        body = item["text"] if item["source"] == "arxiv" else bodies.get(item["extra"]["post_id"], {}).get("text", "")
        out.append(process(tags, item, body, roster, scope_overrides))
    write_jsonl(TAGS_FINAL, out)

    changed = [r for r in out if r["pp"]]
    print(f"Wrote {TAGS_FINAL.name}: {len(out)} items, {len(changed)} adjusted by rules")
    for rule, n in Counter(p.split(" (")[0].split(" ->")[0] for r in changed for p in r["pp"]).most_common():
        print(f"  {n:4d}  {rule}")
    print("Scope:", dict(Counter(r["scope"] for r in out)))


if __name__ == "__main__":
    main()
