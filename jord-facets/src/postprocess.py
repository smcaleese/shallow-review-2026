"""Deterministic rule enforcement on tagger output (rules the LLM did not follow reliably).

Usage: python postprocess.py IN_JSONL BODIES_JSON ROSTER_JSON OUT_JSONL [SCOPE_OVERRIDES_JSON]
Each changed record gets a `pp` list describing what was changed, for auditability.

Rules (from round-2 reader reviews):
 1. substrate: posts with no research_output / field_observations / incident_report post type ran no
    experiments -> substrate = [no_system].
 2. frontier_internal only when a frontier lab is a stated producer; otherwise it is dropped
    (research outputs fall back to frontier_closed, others to no_system).
 3. phenomenon: drop `generalisation` when a more specific child is present.
 4. by-org from the author roster only when: the post is research or a research-area essay (anything but
    field_observations or review); the first author, or at least half the authors, map to that org at
    the post date; and the text has no personal-capacity disclaimer.
 5. Academic only with a university-like evidence string.
 6. scope overrides from reviewer decisions, if given.
 0. posts whose primary move is `proposal` are research_agenda, not position.
 7. derived `evidence` grade: tested (research_output) / observed (field_observations, or an incident report
    whose own move is empirical) / argued. Commentary on others' incidents is argued.
 8. argued posts (no own empirical work) lose effect-claim phenomena (generalisation, training_dynamics) and
    behavioural_evals (unless proposing an eval).
 10. a "views are my own"/personal-capacity disclaimer blocks every non-programme by-tag, stated or roster.
 9. roster tags are ADDED for a lead author when all roster rules pass and no programme tag explains the work.
"""
import json, re, sys

inp, bodies_p, roster_p, out_p = sys.argv[1:5]
overrides = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
bodies = json.load(open(bodies_p))
roster = json.load(open(roster_p))
LABS = {"Anthropic", "OpenAI", "Google DeepMind", "Meta", "xAI"}
PROGRAMMES = {"MATS", "SPAR", "MARS", "Anthropic Fellows", "Astra Fellowship (Constellation)", "LASR Labs"}
RESEARCH_META = {"research_output", "org_update", "research_agenda", "open_questions", "position", "incident_report"}  # not field_observations or review
EMPIRICAL_META = {"research_output", "field_observations"}
EMPIRICAL_MOVES = {"notable_phenomenon", "measurement", "replication", "explanation", "new_technique",
                   "technique_improvement", "stress_test", "toy_model", "observation"}
ARGUED_ONLY_PHEN = {"generalisation", "training_dynamics"}   # effect claims that need evidence
CHILDREN = {"emergent_misalignment", "weird_generalisation", "subliminal_learning"}
DISCLAIMER = re.compile(r"personal capacity|views (are|expressed (here )?are) (my|our) own|not (necessarily )?(those|the views) of my employer|do not represent (the views of )?my employer", re.I)
UNI = re.compile(r"universit|college|institute of technology|\bMIT\b|stanford|berkeley|oxford|cambridge|ETH|EPFL|CMU|carnegie|princeton|harvard|NYU|toronto|mila|tsinghua", re.I)

def L(v):
    if isinstance(v, list):
        return v
    if not v:
        return []
    try:
        x = json.loads(v)
        return x if isinstance(x, list) else [x]
    except Exception:
        return [s.strip() for s in str(v).split(",") if s.strip()]

def org_at(a, date):
    e = roster.get(a)
    if not e or e.get("roster_tags") is False:
        return None
    if e.get("until") and date >= e["until"]:
        return e.get("then")
    return e["org"]

out = []
for line in open(inp):
    r = json.loads(line)
    if "error" in r:
        out.append(r); continue
    pp = []
    meta_l = L(r["meta"])
    if r.get("scientific_primary") == "proposal" and "research_agenda" not in meta_l:
        meta_l = ["research_agenda" if m == "position" else m for m in meta_l] if "position" in meta_l else meta_l + ["research_agenda"]
        pp.append("meta position -> research_agenda (primary move is a proposal)")
    r["meta"] = list(dict.fromkeys(meta_l))
    meta = set(r["meta"])
    sub = L(r["substrate"])
    by = [b for b in L(r["by"]) if isinstance(b, dict)]
    stated = {b["org"] for b in by if b.get("basis") == "stated"}

    # incident reports count as empirical only when the authors' own move is empirical
    own_empirical = bool(meta & EMPIRICAL_META) or ("incident_report" in meta and r.get("scientific_primary") in EMPIRICAL_MOVES - {"explanation"})

    # 1 + 2 substrate
    if not own_empirical and sub != ["no_system"]:
        pp.append(f"substrate {sub} -> [no_system] (no empirical post type)"); sub = ["no_system"]
    if "frontier_internal" in sub and not stated & LABS and not ("research_output" in meta and stated):
        repl = "frontier_closed" if "research_output" in meta else "no_system"
        sub = list(dict.fromkeys([repl if s == "frontier_internal" else s for s in sub]))
        if len(sub) > 1 and "no_system" in sub:
            sub.remove("no_system")
        pp.append(f"frontier_internal -> {repl} (no stated producer with internal access)")
    r["substrate"] = sub

    # 3 phenomenon stacking
    ph = L(r["phenomenon"])
    if "generalisation" in ph and CHILDREN & set(ph):
        ph = [p for p in ph if p != "generalisation"]; pp.append("dropped generalisation (child present)")
    if not own_empirical and ARGUED_ONLY_PHEN & set(ph):
        pp.append(f"dropped {sorted(ARGUED_ONLY_PHEN & set(ph))} (argued post)")
        ph = [p for p in ph if p not in ARGUED_ONLY_PHEN]
    r["phenomenon"] = ph
    me = L(r["method"])
    if not own_empirical and "behavioural_evals" in me and r.get("scientific_primary") != "proposal":
        me = [m for m in me if m != "behavioural_evals"]; pp.append("dropped behavioural_evals (no experiments)")
    r["method"] = me

    # 4 + 5 attribution
    auths = [a.strip() for a in r["authors"].split(",") if a.strip()]
    body = bodies.get(r["id"], "")
    keep = []
    for b in by:
        if b.get("basis") == "author_roster":
            org = b["org"]
            mapped = [org_at(a, r["posted"]) for a in auths]
            lead = bool(auths) and mapped[0] == org
            half = auths and sum(m == org for m in mapped) * 2 >= len(auths)
            why = None
            if not meta & RESEARCH_META or meta & {"field_observations", "review"}:
                why = "not a research post"
            elif org in LABS and not meta & {"research_output", "org_update"}:
                why = "frontier-lab staff essay, not lab output"
            elif not (lead or half):
                why = "not first author / majority"
            elif DISCLAIMER.search(body):
                why = "personal-capacity disclaimer"
            if why:
                pp.append(f"dropped roster by:{org} ({why})"); continue
        if DISCLAIMER.search(body) and b["org"] not in PROGRAMMES and b.get("basis") != "author_roster":
            pp.append(f"dropped by:{b['org']} (post says views are the author's own)"); continue
        if b["org"] == "Academic" and not UNI.search(b.get("evidence", "")):
            pp.append("dropped Academic (no university evidence)"); continue
        keep.append(b)
    # add roster tags the tagger missed when every rule passes
    if auths and meta & RESEARCH_META and not meta & {"field_observations", "review"} and not DISCLAIMER.search(body):
        lead_org = org_at(auths[0], r["posted"])
        have = {b["org"] for b in keep}
        prog = have & {"MATS", "SPAR", "MARS", "Anthropic Fellows", "Astra Fellowship (Constellation)"}
        if lead_org and lead_org not in have and not prog and not (lead_org in LABS and not meta & {"research_output", "org_update"}):
            keep.append({"org": lead_org, "basis": "author_roster", "evidence": f"roster: {auths[0]}"})
            pp.append(f"added roster by:{lead_org} (lead author {auths[0]})")
    r["by"] = keep

    # 6 scope overrides
    if r["id"] in overrides and overrides[r["id"]] != r["scope"]:
        pp.append(f"scope {r['scope']} -> {overrides[r['id']]} (reviewer decision)"); r["scope"] = overrides[r["id"]]

    # 7 evidence grade
    sp = r.get("scientific_primary")
    if "research_output" in meta:
        r["evidence"] = "tested"
    elif "field_observations" in meta or sp == "observation" or ("incident_report" in meta and sp in EMPIRICAL_MOVES - {"explanation"}):
        r["evidence"] = "observed"
    else:
        r["evidence"] = "argued"
    r["pp"] = pp
    out.append(r)

with open(out_p, "w") as f:
    f.writelines(json.dumps(r) + "\n" for r in out)
changed = [r for r in out if r.get("pp")]
print(f"{len(changed)} of {len(out)} records adjusted")
import collections
print(collections.Counter(p.split(" (")[0].split(" ->")[0] for r in changed for p in r["pp"]).most_common())
