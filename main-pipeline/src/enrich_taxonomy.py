#!/usr/bin/env python3
"""
Enrich The Taxonomy
Makes one LLM call per leaf category, with its classified items, and writes every agenda field (summary, theory of
change, see also, ...) to a copy of the taxonomy with an `agenda` block per category. The hand-written taxonomy.yaml
is not modified. Agendas already in the output file are kept (so hand edits survive) unless --overwrite or --only.

Basic usage (from the main-pipeline folder):
    uv run python src/enrich_taxonomy.py --workers 4
Reads data/taxonomy.yaml and writes data/taxonomy-enriched.yaml (inside the data folder set by DATA_PATH).
"""

import argparse
from pathlib import Path

from terminal import console, run
from shallow_review.agendas import enrich_taxonomy
from shallow_review.common import DATA_PATH


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write each leaf category's agenda fields with an LLM.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input", type=Path, default=DATA_PATH / "taxonomy.yaml", help="Hand-written taxonomy (default: <data>/taxonomy.yaml)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DATA_PATH / "taxonomy-enriched.yaml",
        help="Enriched taxonomy to write (default: <data>/taxonomy-enriched.yaml)",
    )
    parser.add_argument("--model", default="anthropic/claude-sonnet-5-5", help="LLM model to use")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel LLM calls (default: 4)")
    parser.add_argument("--overwrite", action="store_true", help="Rewrite agendas already in the output file")
    parser.add_argument(
        "--only", default="", help="Comma-separated category IDs to (re)write (default: all missing ones)"
    )
    args = parser.parse_args()

    assert args.input.resolve() != args.output.resolve(), "Output must differ from the input taxonomy"
    only_ids = {s.strip() for s in args.only.split(",") if s.strip()} or None

    console.print(
        f"[bold]Enriching {args.input} -> {args.output}[/bold] (model={args.model}, workers={args.workers})\n"
    )
    written, no_items, errors = enrich_taxonomy(
        args.input, args.output, args.model, args.workers, args.overwrite, only_ids
    )
    console.print(f"\nWrote {written} agendas to {args.output}")
    if no_items:
        console.print(f"[yellow]No classified items (fields left empty): {', '.join(no_items)}[/yellow]")
    for category_id, error in errors.items():
        console.print(f"[red]{category_id}: {error}[/red]")


if __name__ == "__main__":
    run(main)
