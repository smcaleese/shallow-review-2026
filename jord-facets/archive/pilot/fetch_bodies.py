"""Fetch post bodies from the LessWrong API (first ~8k chars of plain text).

Usage: python fetch_bodies.py IN_CSV OUT_JSON
Writes {post_id: text}. Resumes if OUT_JSON exists.
"""
import csv, html, json, os, re, sys, time, concurrent.futures as cf
import urllib.request

inp, out_p = sys.argv[1:3]
MAX = 8000
Q = '{ post(input:{selector:{_id:"%s"}}){ result{ contents{ html } } } }'

def strip(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h or "")
    h = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</li>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", t)).strip()

def fetch(pid):
    body = json.dumps({"query": Q % pid}).encode()
    req = urllib.request.Request("https://www.lesswrong.com/graphql", data=body,
                                 headers={"content-type": "application/json", "user-agent": "shallow-review-2026"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.load(r)["data"]["post"]["result"]
            return pid, strip((d.get("contents") or {}).get("html"))[:MAX]
        except Exception as e:
            time.sleep(2 * (attempt + 1))
    return pid, None

done = json.load(open(out_p)) if os.path.exists(out_p) else {}
ids = [r["id"] for r in csv.DictReader(open(inp)) if r["id"] not in done]
with cf.ThreadPoolExecutor(3) as ex:
    for i, (pid, text) in enumerate(ex.map(fetch, ids)):
        if text is not None:
            done[pid] = text
        if i % 25 == 0:
            json.dump(done, open(out_p, "w"))
            print(i, "/", len(ids), flush=True)
json.dump(done, open(out_p, "w"))
print("have", len(done), "bodies; failed", sum(1 for p in ids if p not in done))
