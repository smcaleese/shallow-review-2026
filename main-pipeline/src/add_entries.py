#!/usr/bin/env python3
"""
Add URLs To The Pipeline
Reads URLs (one per line, '#' for comments) and queues them for classification in data/data.db. Nothing is scraped or
classified yet; classify_entries.py does that. URLs already in the database are skipped, so reruns are safe.

Basic usage (from the main-pipeline folder):
    uv run python src/add_entries.py data/sources-links/facets-arxiv-2026.txt
The entries are labelled with a source, by default the file name without extension (here facets-arxiv-2026).
"""

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

from shallow_review.entries import add_entry
from terminal import console, run


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)


def read_urls(path: Path) -> list[str]:
    """Valid URLs in the file; prints the invalid ones."""
    urls = []
    invalid = []
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if is_valid_url(line):
            urls.append(line)
        else:
            invalid.append((line_number, line))

    if invalid:
        console.print("[yellow]⚠ Warning: Invalid URLs found (skipped):[/yellow]")
        for line_number, url in invalid[:10]:
            console.print(f"  Line {line_number}: {url[:80]}")
        if len(invalid) > 10:
            console.print(f"  ... and {len(invalid) - 10} more")
        console.print()
    return urls


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add URLs to the entries table, ready for classification.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("file", type=Path, help="File with URLs (one per line)")
    parser.add_argument("--source", help="Source label for tracking (default: the file name without extension)")
    args = parser.parse_args()

    if not args.file.exists():
        console.print(f"[red]Error: File not found: {args.file}[/red]")
        sys.exit(1)
    urls = read_urls(args.file)
    if not urls:
        console.print("[yellow]No valid URLs found in file[/yellow]")
        return

    source = args.source or args.file.stem
    console.print(f"Adding {len(urls)} URLs with source '{source}'...\n")
    added = 0
    for n, url in enumerate(urls, 1):
        is_new = add_entry(url, source)
        added += is_new
        mark = "[green]✓[/green]" if is_new else "[yellow]⊙[/yellow]"
        console.print(f"[{n}/{len(urls)}] {mark} {url[:70]}{'' if is_new else ' (already exists)'}")

    console.print()
    console.print(f"[green]✓ Added {added} new URLs[/green]")
    if added < len(urls):
        console.print(f"[yellow]! {len(urls) - added} URLs already existed[/yellow]")


if __name__ == "__main__":
    run(main)
