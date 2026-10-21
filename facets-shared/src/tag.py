#!/usr/bin/env python3
"""
Step 3: tag every item (arXiv papers and LW/AF posts) along the facets in vocab.yaml with Claude.

Usage (from facets-shared/):
    uv run python src/tag.py                 # tag items not yet tagged with the current vocab version
    uv run python src/tag.py --limit 5       # try the prompt on a few items
    PRINT_PROMPT=1 uv run python src/tag.py  # print the system prompt and one user message, no API calls
Reads data/2-items-deduped.jsonl and appends one JSON line per item to data/3-tags-raw.jsonl.
"""

import argparse
import json
import logging
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Literal

import anthropic
import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field, create_model

from common import ITEMS_DEDUPED, LW_BODIES, LW_ROSTER, ROOT, TAGS_RAW, TAXONOMY_2025, VOCAB, read_jsonl

load_dotenv(ROOT / ".env")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("tag")

DEFAULT_MODEL = "claude-sonnet-5-5"
DEFAULT_EFFORT = "medium"
MAX_TOKENS = 16000
MAX_PARALLEL = 8
SKIP_2025_GROUPS = {"labs_giant_companies"}  # organisations, not agendas; `by` covers them
NEW_AGENDA_PREFIX = "new 2026: "


def load_agendas(path: Path) -> list[dict]:
    """[{'name', 'group', 'description'}] for every leaf of last year's taxonomy."""
    def walk(nodes, group):
        for node in nodes:
            if node.get("children"):
                yield from walk(node["children"], group or node["name"])
            else:
                yield {"name": node["name"], "group": group or "", "description": node.get("description", "")}
    tree = [n for n in yaml.safe_load(path.read_text())["taxonomy"] if n["id"] not in SKIP_2025_GROUPS]
    return list(walk(tree, None))


def agenda_names(vocab: dict, agendas: list[dict]) -> list[str]:
    return [a["name"] for a in agendas] + [NEW_AGENDA_PREFIX + k.replace("_", " ") for k in vocab["agenda_new_2026"]]


def lit(values):
    return Literal[tuple(values)]


def build_schema(vocab: dict, agendas: list[dict]) -> type[BaseModel]:
    """Structured-output model: every tag field is constrained to its vocabulary."""
    By = create_model("By", org=(lit(vocab["org"]), ...), basis=(Literal["stated", "author_roster"], ...),
                      evidence=(str, Field(description="Short verbatim snippet, or 'roster: <author>'")))
    fields = {
        "summary": (str, Field(description="One or two plain sentences on what the work does and finds.")),
        "scope": (Literal["include", "exclude", "borderline"], ...),
        "scope_reason": (str, Field(description="One short sentence.")),
    }
    for facet_id, facet in vocab["facets"].items():
        tags = lit(list(facet["tags"]))
        if facet["select"] == "one":
            fields[facet_id] = (tags, ...)
        elif facet["select"] == "primary":
            fields[f"{facet_id}_primary"] = (tags, ...)
            fields[f"{facet_id}_secondary"] = (list[tags], ...)
        else:
            fields[facet_id] = (list[tags], ...)
    fields["agenda"] = (list[lit(agenda_names(vocab, agendas))], ...)
    fields["new_agenda"] = (str, Field(description="Empty unless no listed agenda fits; then a 2-5 word name."))
    fields["by"] = (list[By], ...)
    fields["about"] = (list[lit(vocab["developers"])], ...)
    fields["suggest"] = (list[str], Field(description="Up to 2 tags you wished existed, or empty."))
    return create_model("ItemTags", **fields)


def tag_lines(tags: dict) -> list[str]:
    lines = []
    for tag, spec in tags.items():
        spec = spec or {}
        line = f"- {tag}"
        if spec.get("def"):
            line += f": {spec['def']}"
        if spec.get("aliases"):
            line += f" (covers: {', '.join(map(str, spec['aliases']))})"
        lines.append(line)
    return lines


def build_system_prompt(vocab: dict, agendas: list[dict]) -> str:
    lines = [
        "You tag research for the Shallow Review of Technical AI Safety 2026, a map of the field published on "
        "LessWrong. Items are arXiv papers and LessWrong / Alignment Forum posts, tagged with one shared vocabulary. "
        "Readers are expert researchers who will notice sloppy tags.",
        "",
        "GENERAL RULES",
        "- Use ONLY the listed tags. Tag what the work is ABOUT and what it DOES, judged from the text, not the title.",
        "- Never tag a concept or method because it is mentioned in passing, listed, or argued to be absent.",
        "- Fewer, accurate tags beat many loose ones. Empty lists are fine.",
        "- arXiv papers come with only their abstract; LW posts come with their text (start and end).",
        "",
        "SCOPE: include = technical AI safety (empirical, theory, conceptual/threat models, metascience, technical "
        "agendas). exclude = governance/policy, forecasting/timelines, non-technical strategy, careers, community "
        "news, fiction, pure capabilities. borderline only when expert reviewers would genuinely split. arXiv papers "
        "were already screened, so mark them include unless clearly out of scope.",
        "",
    ]
    for facet_id, facet in vocab["facets"].items():
        if facet["select"] == "one":
            how = "exactly one"
        elif facet["select"] == "primary":
            how = f"one primary, plus 0-{facet.get('max_secondary', 2)} secondary"
        else:
            how = f"0-{facet['max']}" if facet_id != "substrate" else f"1-{facet['max']}"
        lines += [f"## {facet['name'].upper()} ({facet_id}): {how}", facet["description"].strip(), *tag_lines(facet["tags"]), ""]

    lines += ["## AGENDA (agenda): usually one, at most two",
              "The closest leaf of last year's review taxonomy. If none fits, use one of the new 2026 agendas "
              f"(listed with the '{NEW_AGENDA_PREFIX}' prefix). Only if none of those fits either, leave the list "
              "empty and name the agenda in new_agenda."]
    group = None
    for a in agendas:
        if a["group"] != group:
            group = a["group"]
            lines += ["", f"### {group}"]
        lines.append(f"- {a['name']}: {a['description']}")
    lines += ["", "### New 2026 agendas"]
    lines += tag_lines({NEW_AGENDA_PREFIX + k.replace("_", " "): v for k, v in vocab["agenda_new_2026"].items()})

    lines += [
        "", "## BY: organisations that PRODUCED the work. Each needs a basis:",
        "- stated: the text shows it (affiliation line, 'at X we', an official org post or crosspost from the org's "
        "blog, 'done as part of MATS'). Give a short verbatim evidence snippet.",
        "- author_roster (LW posts only): an author is in the roster matches given AND the post presents research or "
        "an agenda. Personal essays and opinions by staff do NOT get a roster-based tag. Evidence = 'roster: <author>'.",
        "NOT a basis: the work studies or discusses the org or its models; funders or thanks; an author's past "
        "employer; posts written 'in a personal capacity'. For arXiv papers, tag `by` only when the abstract or "
        "comment states the organisation. Programmes (MATS, SPAR, Anthropic Fellows, Astra) are their own orgs. "
        "University-led work is 'Academic' with the university in evidence.",
        "", "## ABOUT: developers whose models are experimental subjects or whose practices are a main topic "
        "(not passing mentions, not a model used only as a judge).",
    ]
    return "\n".join(lines)


def org_at(roster: dict, author: str, date: str) -> str | None:
    entry = roster.get(author)
    if not entry or entry.get("roster_tags") is False:
        return None
    if entry.get("until") and date >= entry["until"]:
        return entry.get("then")
    return entry["org"]


def user_message(item: dict, bodies: dict, roster: dict) -> str:
    if item["source"] == "arxiv":
        extra = item["extra"]
        msg = (f"Source: arXiv paper\nTitle: {item['title']}\nAuthors: {item['authors']}\nPublished: {item['date']}\n"
               f"arXiv categories: {extra.get('categories') or 'none'}\nComment: {extra.get('comment') or 'none'}\n"
               f"Venue: {extra.get('venue') or 'none'}\n\nAbstract:\n{item['text']}")
        for post_id, title in zip(item.get("merged_posts", []), item["extra"].get("lw_titles", [])):
            body = bodies.get(post_id.removeprefix("lw:"), {}).get("text", "")
            msg += f"\n\nA LessWrong write-up of this paper (\"{title}\"), opening:\n{body[:3000]}"
        return msg
    authors = [a.strip() for a in item["authors"].split(",") if a.strip()]
    matches = [f"{a}: {org_at(roster, a, item['date'])}" for a in authors if org_at(roster, a, item["date"])]
    link = item["extra"].get("link_url")
    body = bodies.get(item["extra"]["post_id"], {}).get("text") or item["text"]
    return (f"Source: {'Alignment Forum' if item['extra'].get('alignment_forum') else 'LessWrong'} post\n"
            f"Title: {item['title']}\nAuthors (forum usernames): {item['authors']}\nPosted: {item['date']}\n"
            f"Forum tags: {item['extra'].get('forum_tags') or 'none'}\n"
            + (f"Crossposted from / links to: {link}\n" if link else "")
            + f"Author roster matches: {'; '.join(matches) if matches else 'none'}\n\n"
            f"Post text (start and end; middle may be omitted):\n{body}")


def tag_item(client, item, schema, system_prompt, user, model, effort) -> dict | None:
    try:
        response = client.beta.messages.parse(
            model=model, max_tokens=MAX_TOKENS,
            system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": f"Tag this item.\n\n{user}"}],
            output_config={"effort": effort}, output_format=schema,
            betas=["server-side-fallback-2026-07-01"], fallbacks="default")
    except anthropic.AuthenticationError:
        raise
    except anthropic.APIError as e:
        log.error(f"{item['id']}: error calling Claude API: {e}")
        return None
    if response.stop_reason in ("refusal", "max_tokens") or response.parsed_output is None:
        log.warning(f"{item['id']}: no tags ({response.stop_reason})")
        return None
    return response.parsed_output.model_dump()


def main():
    parser = argparse.ArgumentParser(description="Tag arXiv papers and LW posts along vocab.yaml with Claude")
    parser.add_argument("--limit", type=int, help="Only tag the first N untagged items")
    parser.add_argument("--only", choices=["arxiv", "lesswrong"], help="Only tag items from one source")
    parser.add_argument("--overwrite", action="store_true", help="Retag items that already have tags")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--effort", default=DEFAULT_EFFORT, choices=["low", "medium", "high", "xhigh", "max"])
    args = parser.parse_args()

    vocab = yaml.safe_load(VOCAB.read_text())
    agendas = load_agendas(TAXONOMY_2025)
    schema = build_schema(vocab, agendas)
    system_prompt = build_system_prompt(vocab, agendas)
    items = read_jsonl(ITEMS_DEDUPED)
    bodies = json.loads(LW_BODIES.read_text()) if LW_BODIES.exists() else {}
    roster = json.loads(LW_ROSTER.read_text())

    if os.environ.get("PRINT_PROMPT"):
        example = next(i for i in items if i["source"] == (args.only or "lesswrong"))
        print(system_prompt, "\n\n===== example user message =====\n", user_message(example, bodies, roster))
        return

    done = set() if args.overwrite else {r["id"] for r in read_jsonl(TAGS_RAW) if r.get("vocab_version") == vocab["version"]}
    todo = [i for i in items if i["id"] not in done and (not args.only or i["source"] == args.only)]
    if args.limit:
        todo = todo[:args.limit]
    log.info(f"{len(items)} items, {len(done)} already tagged, tagging {len(todo)} with {args.model}")
    if not todo:
        return

    client = anthropic.Anthropic()
    TAGS_RAW.parent.mkdir(parents=True, exist_ok=True)
    lock, failed = threading.Lock(), []

    def work(item):
        tags = tag_item(client, item, schema, system_prompt, user_message(item, bodies, roster), args.model, args.effort)
        if tags is None:
            failed.append(item["id"])
            return
        record = {"id": item["id"], "model": args.model, "vocab_version": vocab["version"], **tags}
        with lock, TAGS_RAW.open("a") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        log.info(f"Tagged {item['id']}: {item['title'][:70]}")

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as executor:
        list(executor.map(work, todo))
    log.info(f"Done: {len(todo) - len(failed)} tagged, {len(failed)} failed {failed if failed else ''}")


if __name__ == "__main__":
    main()
