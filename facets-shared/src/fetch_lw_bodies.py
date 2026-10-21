#!/usr/bin/env python3
"""
Fetch the text and outgoing links of every LW/AF post from the LessWrong API.

Usage (from facets-shared/):
    uv run python src/fetch_lw_bodies.py
Writes cache/lw-bodies.json: {post_id: {"text": ..., "links": [...]}}. Already-fetched posts are skipped.
The text keeps the first 6k and last 3k characters (as in jord-facets), so affiliations and acknowledgements
survive. Links are kept separately because dedupe looks for arXiv links, which plain text would lose.
"""

import html
import json
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from common import ITEMS, LW_BODIES, read_jsonl

HEAD, TAIL = 6000, 3000
QUERY = '{ post(input:{selector:{_id:"%s"}}){ result{ contents{ html } } } }'


def html_to_text(page: str) -> str:
    page = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", page or "")
    page = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</li>", "\n", page)
    text = html.unescape(re.sub(r"<[^>]+>", " ", page))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", text)).strip()


def fetch(post_id: str) -> tuple[str, dict | None]:
    body = json.dumps({"query": QUERY % post_id}).encode()
    request = urllib.request.Request("https://www.lesswrong.com/graphql", data=body,
                                     headers={"content-type": "application/json", "user-agent": "shallow-review-2026"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.load(response)["data"]["post"]["result"]
            page = (result.get("contents") or {}).get("html") or ""
            links = list(dict.fromkeys(html.unescape(u) for u in re.findall(r'href="([^"]+)"', page)))
            text = html_to_text(page)
            if len(text) > HEAD + TAIL:
                text = text[:HEAD] + "\n\n[... middle omitted ...]\n\n" + text[-TAIL:]
            return post_id, {"text": text, "links": links}
        except Exception:
            time.sleep(2 * (attempt + 1))
    return post_id, None


def main():
    bodies = json.loads(LW_BODIES.read_text()) if LW_BODIES.exists() else {}
    todo = [i["extra"]["post_id"] for i in read_jsonl(ITEMS) if i["source"] == "lesswrong"
            and i["extra"]["post_id"] not in bodies]
    print(f"{len(bodies)} posts cached, fetching {len(todo)}")
    LW_BODIES.parent.mkdir(parents=True, exist_ok=True)
    failed = []
    with ThreadPoolExecutor(3) as executor:
        for n, (post_id, body) in enumerate(executor.map(fetch, todo), 1):
            if body is None:
                failed.append(post_id)
            else:
                bodies[post_id] = body
            if n % 25 == 0 or n == len(todo):
                LW_BODIES.write_text(json.dumps(bodies))
                print(f"  {n}/{len(todo)}")
    print(f"Have {len(bodies)} post bodies; {len(failed)} failed {failed if failed else ''}")


if __name__ == "__main__":
    main()
