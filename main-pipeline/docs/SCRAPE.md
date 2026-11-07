# Scrape Process

Minimal documentation for the scraping infrastructure.

## Purpose

Scraping fetches and caches HTML content for later processing. All scrapes are cached indefinitely to avoid repeated network requests.

## Key Functions

**`compute_scrape(url, headless=True, wait_for="networkidle", scroll=True)`**
- Scrapes the URL (Selenium by default, Playwright if `USE_SELENIUM` is False)
- Stores the HTML in `data/scraped/<hash>.html.zst` (Zstandard compression level 15)
- Returns the path; if the file already exists, returns it without scraping
- Raises on scrape failure

**`get_scrape_path(url)`**
- Returns pathlib.Path to scraped file (may not exist yet)

**`open_scraped(url, mode)`**
- Opens scraped file with smart_open (handles .zst compression)

## Scrape Behavior

- **User agent**: Realistic browser UA with playwright
- **Wait strategy**: Configurable wait_for parameter ("load", "networkidle", etc.)
- **Scrolling**: Scrolls page to trigger lazy-loaded content
- **Caching**: successful scrapes only, by file existence. One file per URL.

## arXiv

arXiv URLs (`arxiv.org/abs|pdf|html/<id>`, matched by `ARXIV_RE`) are not scraped with the browser. `scrape_arxiv`
gets the title, authors, submission date, category and abstract from the arXiv API and the full text from
`arxiv.org/pdf/<id>` (the PDF always exists, unlike the HTML version), and caches a small HTML page: that metadata
followed by one `<pre>` block per PDF page. Requests are spaced `ARXIV_DELAY_SECONDS` (3 s) apart, shared across
workers, so scraping 270 papers takes about 30 minutes.

## PDFs

Browsers return an empty viewer page for PDFs, so PDF URLs are downloaded and converted to text instead
(`scrape_pdf`, using `pypdf`). A URL counts as a PDF if its path ends in `.pdf` or if a HEAD request, following
redirects, returns `Content-Type: application/pdf` (short links like `anthropic.com/<name>-system-card` redirect to a
PDF). The text is cached like any other page: a small HTML page with one `<pre>` block per PDF page. Scanned PDFs with
no text layer fail with "PDF has no extractable text" (no OCR).

## LessWrong and Alignment Forum

Both sites return 403 to the automated browser. Post URLs (`lesswrong.com/posts/<id>/...`,
`alignmentforum.org/posts/<id>/...`, matched by `FORUM_POST_RE`) are fetched from the site's GraphQL API instead
(`scrape_forum_api`), and cached like any other page: a small HTML page with the title, authors (full names where set,
otherwise display names) and date at the top, then the post body.

## Error Handling

- Network errors, timeouts: raise `RuntimeError`; nothing is cached. `classify_entries.py` marks the entry `scrape_error`
  and does not retry it until `reset_classify.py` resets it.
- HTTP errors (4xx, 5xx): the response body is saved like any page; the classifier marks it `error_detected`.
