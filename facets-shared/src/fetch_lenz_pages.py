#!/usr/bin/env python3
"""
Step 0b: fetch the text of each source in input/lenz-org-sources.csv (links from AI safety organisations' sites).

Usage (from facets-shared/):
    uv run python src/fetch_lenz_pages.py
Writes data/1b-lenz-items.jsonl in the item format (see load_sources.py), with source "org". Each page's raw
paragraphs are cached in cache/lenz-pages.json (not committed), so reruns only fetch new links. Overlap with arXiv and LW items is removed later, in dedupe.py.
arXiv links use the arXiv API (abstract), LessWrong links the LW API, other pages their <p> text.
Text is cut to the first MAX_CHARS characters so these items weigh about the same as an abstract.
"""

import csv
import hashlib
import html
import json
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

from common import ARXIV_ID, CACHE, LENZ_ITEMS, LENZ_SOURCES, read_jsonl, write_jsonl

PAGES = CACHE / "lenz-pages.json"  # {url: item with its raw "paras"}
from fetch_lw_bodies import html_to_text

MAX_CHARS = 2500
UA = {"user-agent": "Mozilla/5.0 (shallow-review-2026 research crawler)"}
LW_POST = re.compile(r"lesswrong\.com/posts/([A-Za-z0-9]+)")


def get(url: str, data: bytes | None = None, headers: dict | None = None) -> str:
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            err = e
            time.sleep(2 * (attempt + 1))
    raise err


def from_arxiv(arxiv_id: str) -> tuple[str, str]:
    feed = ET.fromstring(get(f"https://export.arxiv.org/api/query?id_list={arxiv_id}"))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = feed.find("a:entry", ns)
    abstract = " ".join(entry.findtext("a:summary", "", ns).split())
    authors = ", ".join(a.findtext("a:name", "", ns) for a in entry.findall("a:author", ns))
    return abstract, authors


def from_lw(post_id: str) -> tuple[str, str]:
    q = '{ post(input:{selector:{_id:"%s"}}){ result{ contents{ html } user{ displayName } } } }' % post_id
    res = json.loads(get("https://www.lesswrong.com/graphql", json.dumps({"query": q}).encode(),
                         {"content-type": "application/json"}))["data"]["post"]["result"]
    return html_to_text((res.get("contents") or {}).get("html") or ""), (res.get("user") or {}).get("displayName", "")


def from_page(url: str) -> tuple[str, str]:
    page = get(url)
    meta = lambda name: next(iter(re.findall(
        rf'<meta[^>]+(?:name|property)="{name}"[^>]+content="([^"]*)"', page, re.I)), "")
    desc = html.unescape(meta("og:description") or meta("description"))
    body = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", page)
    paras = [html_to_text(p) for p in re.findall(r"(?is)<p[^>]*>(.*?)</p>", body)]
    paras = [p for p in paras if len(p) > 60]  # skip buttons, captions, cookie lines
    return list(dict.fromkeys([desc] + paras if desc else paras)), html.unescape(meta("author"))


def fetch(row: dict) -> dict:
    urls = row["urls"].split()
    text, authors, how = [], "", "none"
    for url in urls:
        try:
            if m := ARXIV_ID.search(url):
                text, authors = from_arxiv(m.group(1)); text, how = [text], "arxiv"
            elif m := LW_POST.search(url):
                text, authors = from_lw(m.group(1)); text, how = [text], "lesswrong"
            else:
                text, authors = from_page(url); how = "page"
        except Exception as e:
            print(f"  failed {url}: {e}")
        if sum(map(len, text)) > 200:
            break
    return {"id": "org:" + hashlib.sha1(row["url"].encode()).hexdigest()[:10], "source": "org",
            "title": row["title"], "authors": authors, "date": row["date"], "url": row["url"], "paras": text,
            "links": [{"source": "org", "url": u, "label": "link"} for u in urls], "popularity": {},
            "extra": {"orgs": row["orgs"], "fetched_via": how}, "sources": ["org"]}


def main():
    rows = list(csv.DictReader(LENZ_SOURCES.open()))
    cached = json.loads(PAGES.read_text()) if PAGES.exists() else {}
    todo = [r for r in rows if r["url"] not in cached]
    print(f"{len(rows)} sources, {len(rows) - len(todo)} cached, fetching {len(todo)}")
    with ThreadPoolExecutor(6) as pool:
        fetched = {i["url"]: i for i in pool.map(fetch, todo)}
    items = []
    for r in rows:  # refresh the CSV fields (org list, merged links) even for cached pages
        i = fetched.get(r["url"]) or cached[r["url"]]
        i.update(title=r["title"], date=r["date"], extra=i["extra"] | {"orgs": r["orgs"]},
                 links=[{"source": "org", "url": u, "label": "link"} for u in r["urls"].split()])
        items.append(i)
    # Drop site boilerplate (mission statements, nav bars, cookie notices): any sentence-run seen on 3+ pages.
    seen = Counter(p for i in items for p in set(i["paras"]))
    for i in items:
        i["text"] = " ".join(" ".join(p for p in i["paras"] if seen[p] < 3).split())[:MAX_CHARS]
    PAGES.parent.mkdir(parents=True, exist_ok=True)
    PAGES.write_text(json.dumps({i["url"]: i for i in items}, ensure_ascii=False))
    write_jsonl(LENZ_ITEMS, [{k: v for k, v in i.items() if k != "paras"} for i in items])
    thin = [i for i in items if len(i["text"]) < 300]
    print(f"{len(items)} items -> {LENZ_ITEMS.name}; {len(thin)} with under 300 chars of text:")
    for i in thin:
        print(f"  {len(i['text']):4}  {i['title'][:70]}  {i['url']}")


if __name__ == "__main__":
    main()
