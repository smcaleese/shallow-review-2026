"""Parse input/lenz-org-sources.md (links scraped from AI safety org pages) into input/lenz-org-sources.csv."""
import csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "input" / "lenz-org-sources.md"
OUT = ROOT / "input" / "lenz-org-sources.csv"  # common.LENZ_SOURCES

ITEM = re.compile(r"^\*\s+(?P<title>.+?)\s+\((?P<date>\d{4}(?:-\d{2}-\d{2})?)\)?\s*\\?-\s*\[.*?\]\((?P<url>[^)]+)\)")
SECTION = re.compile(r"^###\s+(.+?)(?:\s*\\?-?\s*\[.*)?$")


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def main():
    rows, by_key, raw_count, org = [], {}, 0, ""
    for line in SRC.read_text().splitlines():
        line = line.strip()
        if m := SECTION.match(line):
            org = m.group(1).strip()
            if org.startswith("Extracted papers"):
                org = "Gavin's link dump"
            continue
        m = ITEM.match(line)
        if not m:
            if line.startswith("*"):
                print("UNPARSED:", line[:120])
            continue
        raw_count += 1
        title = m["title"].replace("\\", "").strip()
        url = m["url"].strip()
        key = norm_title(title)
        if key in by_key:  # same paper listed under several orgs
            r = by_key[key]
            if org not in r["orgs"].split("; "):
                r["orgs"] += "; " + org
            if url not in r["urls"].split(" "):
                r["urls"] += " " + url
            if len(m["date"]) > len(r["date"]):
                r["date"] = m["date"]
            continue
        r = {"title": title, "date": m["date"], "url": url, "orgs": org, "urls": url}
        by_key[key] = r
        rows.append(r)

    for r in rows:
        r["n_orgs"] = len(r["orgs"].split("; "))
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "date", "url", "orgs", "n_orgs", "urls"])
        w.writeheader()
        w.writerows(rows)
    print(f"{raw_count} entries -> {len(rows)} unique sources -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
