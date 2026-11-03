# Semantic map

An interactive 2D map of the 502 sources selected by facets-shared (`facets-shared/data/6-selected.json`), in the
style of [jdunbar.net's safety map](https://jdunbar.net/pages/safety_map/). Each dot is a source; nearby dots have
similar titles and abstracts. Hue is the top-level group, shade is the cluster within it.

## Run it

From `taxonomy-discovery/`:

```bash
uv run python 5-semantic-map/build.py             # writes site/data.js (~$0.09 for naming, cached after)
python3 -m http.server 8770 -d 5-semantic-map/site
```

Then open http://localhost:8770. In the desktop app the `semantic-map` entry in `.claude/launch.json` does the same.

Options: `--groups 8 --clusters 32` (how coarse each level is), `--seed`, `--no-llm` (keyword labels instead of
Claude names), `--model`, `--embedder`.

## How it works

1. **Embed.** Title + abstract (arXiv) or title + opening text (posts) with `BAAI/bge-large-en-v1.5`, locally.
   Same model and cache as method 3.
2. **Lay out.** UMAP (cosine, 15 neighbours) to 2D for the map.
3. **Cluster.** UMAP again to 10D, then one Ward tree cut twice: into 8 groups and 32 clusters. Because both cuts
   come from the same tree, every cluster sits inside exactly one group. Clustering in 10D keeps more structure than
   clustering the drawn 2D points, so a few dots sit closer to a neighbouring cluster on the map than to their own.
4. **Name.** Claude (Opus by default) names each group and cluster from its member titles in one call. It only
   names them; membership comes from step 3. Hovering a cluster row shows its keywords (class-based TF-IDF).

## The page

- Hover a dot for its title, source, date, rank, the tagger's one-line summary and its 2025 agenda tags; click to open it.
- Scroll to zoom, drag to pan. Zoomed out the map labels groups; zoomed in it labels clusters.
- Click a group or cluster row to filter (several can be on); hover a row to highlight its dots.
- Source chips hide arXiv / LessWrong / org posts / safety stack items; the search box matches title, authors,
  summary, agendas and cluster names (`/` to focus, `Esc` to clear).
- Counts and percentages in the sidebar are each row's share of the sources currently in view, so zooming into a
  region shows its make-up.
