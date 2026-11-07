"""Web scraping utilities with playwright and selenium."""

import html
import io
import logging
import os
import re
import threading
import time
from pathlib import Path
from typing import IO, Any, Literal
from urllib.parse import urlparse

import requests
from playwright.sync_api import Browser, sync_playwright

from .common import SCRAPED_PATH
from .stats import get_stats
from .utils import normalize_url, smart_open, url_hash

logger = logging.getLogger(__name__)

# Scraping backend selection
# Set to True to use Selenium (thread-safe), False for Playwright (faster but needs workers=1)
USE_SELENIUM = True

# Global lock for Playwright operations (only used if USE_SELENIUM=False)
# Playwright's sync API uses greenlets which are not thread-safe.
# This lock ensures only ONE thread scrapes at a time, preventing
# "browser has been closed" errors from greenlet context switching.
_playwright_lock = threading.Lock()

# Lock for Selenium WebDriver creation (prevents ChromeDriver resource exhaustion)
# Creating too many WebDriver instances simultaneously can crash ChromeDriver
# Lock only driver creation, not the whole scraping (scraping can run in parallel)
_selenium_create_lock = threading.Lock()


def get_scrape_path(url: str) -> Path:
    """
    Get the file path for a scraped URL.

    Args:
        url: URL to get path for (will be normalized)

    Returns:
        Path to .html.zst file
    """
    hash_value = url_hash(url)
    return SCRAPED_PATH / f"{hash_value}.html.zst"


def open_scraped(
    url: str,
    mode: Literal["rt", "wt", "rb", "wb"],
    encoding: str | None = None,
    **kwargs: Any,
) -> IO:
    """
    Open a scraped file with automatic compression.

    Args:
        url: URL to open scraped content for
        mode: Open mode (rt/wt for text, rb/wb for binary)
        encoding: Text encoding (for text modes)
        **kwargs: Additional args passed to smart_open()

    Returns:
        File-like object
    """
    path = get_scrape_path(url)
    return smart_open(path, mode, encoding=encoding, **kwargs)


def get_browser_context(browser: Browser, **kwargs):
    """
    Create browser context with realistic settings.

    Args:
        browser: Playwright browser instance
        **kwargs: Additional context options

    Returns:
        Browser context
    """
    # Realistic user agent
    default_kwargs = {
        "user_agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "viewport": {"width": 1920, "height": 1080},
        "locale": "en-US",
        "timezone_id": "America/New_York",
    }

    # Merge with user-provided kwargs
    default_kwargs.update(kwargs)

    return browser.new_context(**default_kwargs)


def scrape_playwright(url: str, headless: bool = True, wait_for: str = "networkidle", scroll: bool = True) -> tuple[str, int]:
    """
    Scrape URL using Playwright.
    
    NOT thread-safe - caller must use _playwright_lock.
    
    Args:
        url: URL to scrape
        headless: Run browser in headless mode
        wait_for: Wait condition ("networkidle", "load", "domcontentloaded")
        scroll: Scroll page to trigger lazy loading
        
    Returns:
        Tuple of (html_content, status_code)
        
    Raises:
        Exception: If scraping fails
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = get_browser_context(browser)
        page = context.new_page()

        # Navigate to URL
        response = page.goto(url, wait_until=wait_for, timeout=60000)
        status_code = response.status if response else 0

        # Scroll to trigger lazy loading
        if scroll:
            page.evaluate(
                """
                () => {
                    window.scrollTo(0, document.body.scrollHeight / 2);
                }
                """
            )
            page.wait_for_timeout(500)
            page.evaluate("() => { window.scrollTo(0, document.body.scrollHeight); }")
            page.wait_for_timeout(500)

        # Get page content
        content = page.content()

        browser.close()
    
    return (content, status_code)


def scrape_selenium(url: str, headless: bool = True, scroll: bool = True) -> tuple[str, int]:
    """
    Scrape URL using Selenium.
    
    Thread-safe - each call creates its own WebDriver instance.
    
    Args:
        url: URL to scrape
        headless: Run browser in headless mode
        scroll: Scroll page to trigger lazy loading
        
    Returns:
        Tuple of (html_content, status_code)
        
    Raises:
        Exception: If scraping fails
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    import time
    
    # Configure Chrome options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # Realistic user agent
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    
    # Create driver with lock to prevent ChromeDriver resource exhaustion
    # Lock only creation, not the whole scraping (allows parallel scraping)
    with _selenium_create_lock:
        driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to URL
        driver.get(url)
        
        # Wait for page to be ready
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        
        # Additional wait for network idle (approximate)
        time.sleep(1)
        
        # Scroll to trigger lazy loading
        if scroll:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
        
        # Get page content
        content = driver.page_source
        
        # Selenium doesn't provide status codes directly
        # Assume 200 if we successfully loaded the page
        status_code = 200
        
        # Try to detect errors from page title/content
        title = driver.title.lower()
        if "404" in title or "not found" in title:
            status_code = 404
        elif "403" in title or "forbidden" in title:
            status_code = 403
        elif "500" in title or "error" in title:
            status_code = 500
            
        return (content, status_code)
        
    finally:
        driver.quit()


# LessWrong and the Alignment Forum block browser scraping (403), so their posts are fetched from the GraphQL API
FORUM_POST_RE = re.compile(r"^https?://(?:www\.)?(lesswrong\.com|alignmentforum\.org)/posts/([A-Za-z0-9]+)")

FORUM_POST_QUERY = """
query Post($id: String!) {
  post(input: {selector: {_id: $id}}) {
    result {
      title
      pageUrl
      postedAt
      user { displayName fullName }
      coauthors { displayName fullName }
      contents { html }
    }
  }
}
"""


def scrape_forum_api(url: str) -> tuple[str, int]:
    """Fetch a LessWrong / Alignment Forum post from the GraphQL API as a simple HTML page.

    The page has the title, authors (full names where set) and date at the top, then the post body.
    Returns (html, status_code); 404 if the API has no such post.
    """
    match = FORUM_POST_RE.match(url)
    assert match, f"Not a forum post URL: {url}"
    site, post_id = match.groups()
    response = requests.post(
        f"https://www.{site}/graphql",
        json={"query": FORUM_POST_QUERY, "variables": {"id": post_id}},
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        timeout=60,
    )
    response.raise_for_status()
    post = ((response.json().get("data") or {}).get("post") or {}).get("result")
    if not post:
        return (f"<html><body>No post {post_id} on {site}</body></html>", 404)

    people = [post.get("user") or {}] + (post.get("coauthors") or [])
    authors = [p.get("fullName") or p.get("displayName") for p in people if p.get("fullName") or p.get("displayName")]
    title = html.escape(post.get("title") or "")
    body = (post.get("contents") or {}).get("html") or ""
    page = f"""<html><head><title>{title}</title></head><body>
<h1>{title}</h1>
<p>By {html.escape(", ".join(authors))}</p>
<p>Posted {(post.get("postedAt") or "")[:10]} on {site}</p>
<article>
{body}
</article>
</body></html>"""
    return (page, 200)


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def is_pdf_url(url: str) -> bool:
    """Whether the URL serves a PDF, judged by the file name or, failing that, by the Content-Type after redirects.

    The browser backends cannot read PDFs (they return an empty viewer page), so PDFs are downloaded and converted to
    text instead. Short links such as anthropic.com/<name>-system-card redirect to a PDF, hence the HEAD request.
    """
    if urlparse(url).path.lower().endswith(".pdf"):
        return True
    try:
        response = requests.head(url, allow_redirects=True, timeout=15, headers={"User-Agent": USER_AGENT})
        return "application/pdf" in response.headers.get("Content-Type", "").lower()
    except requests.RequestException:
        return False  # Let the browser backend try


def pdf_to_html(content: bytes, header: str = "") -> str:
    """Convert PDF bytes to a simple HTML page: optional header HTML, then one <pre> block per PDF page.

    Raises if the PDF has no extractable text (e.g. scanned images).
    """
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(content))
    pages = [(page.extract_text() or "").strip() for page in reader.pages]
    if not any(pages):
        raise RuntimeError("PDF has no extractable text")
    title = html.escape((reader.metadata.title if reader.metadata else None) or "")
    body = "\n".join(f"<pre>{html.escape(text)}</pre>" for text in pages if text)
    return f"<html><head><title>{title}</title></head><body>\n{header}{body}\n</body></html>"


def scrape_pdf(url: str) -> tuple[str, int]:
    """Download a PDF and return its text as a simple HTML page. Returns (html, status_code)."""
    response = requests.get(url, timeout=120, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    return (pdf_to_html(response.content), 200)


# arXiv papers: the metadata comes from the arXiv API and the text from the PDF (always available, unlike the HTML
# version). Requests are spaced out to respect arXiv's rate limit (one request per 3 seconds for the API).
ARXIV_RE = re.compile(r"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?/?$")
ARXIV_DELAY_SECONDS = 3.0
_arxiv_lock = threading.Lock()
_arxiv_last_request = 0.0


def _arxiv_wait() -> None:
    """Sleep until ARXIV_DELAY_SECONDS have passed since the last arXiv request. Call with _arxiv_lock held."""
    global _arxiv_last_request
    time.sleep(max(0.0, _arxiv_last_request + ARXIV_DELAY_SECONDS - time.monotonic()))
    _arxiv_last_request = time.monotonic()


def scrape_arxiv(url: str) -> tuple[str, int]:
    """Get an arXiv paper as a simple HTML page: title, authors, date and abstract from the API, then the PDF text.

    Returns (html, status_code); 404 if the API has no such paper. Raises if the download or text extraction fails.
    """
    import arxiv

    match = ARXIV_RE.match(url)
    assert match, f"Not an arXiv URL: {url}"
    arxiv_id = match.group(1)

    with _arxiv_lock:  # One arXiv request at a time, so the delay holds with several workers
        _arxiv_wait()
        results = list(arxiv.Client(num_retries=3).results(arxiv.Search(id_list=[arxiv_id])))
        if not results:
            return (f"<html><body>No paper {arxiv_id} on arXiv</body></html>", 404)
        paper = results[0]
        _arxiv_wait()
        response = requests.get(f"https://arxiv.org/pdf/{arxiv_id}", timeout=120, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()

    header = (
        f"<h1>{html.escape(paper.title)}</h1>\n"
        f"<p>By {html.escape(', '.join(a.name for a in paper.authors))}</p>\n"
        f"<p>Submitted {paper.published:%Y-%m-%d} to arXiv ({html.escape(paper.primary_category)})</p>\n"
        f"<p>Abstract: {html.escape(' '.join((paper.summary or '').split()))}</p>\n"
    )
    return (pdf_to_html(response.content, header), 200)


# Firecrawl: last-resort fallback when the browser gets a blocked, empty or error page. It needs FIRECRAWL_API_KEY in
# .env; without it the fallback is skipped. Costs credits, so it only runs for pages that look bad.
FIRECRAWL_URL = "https://api.firecrawl.dev/v2/scrape"
MIN_VISIBLE_CHARS = 3000  # Browser pages with less visible text than this are retried with Firecrawl


def visible_text_length(content: str) -> int:
    """Number of characters of visible text in the HTML (scripts and styles excluded)."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(content, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    return len(" ".join(soup.get_text(" ").split()))


def scrape_firecrawl(url: str) -> tuple[str, int]:
    """Fetch the page with Firecrawl as markdown, wrapped in a simple HTML page. Returns (html, status_code).

    Raises if there is no API key or the request fails.
    """
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        raise RuntimeError("FIRECRAWL_API_KEY is not set")
    response = requests.post(
        FIRECRAWL_URL,
        json={"url": url, "formats": ["markdown"], "onlyMainContent": True},
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=120,
    )
    response.raise_for_status()
    data = response.json().get("data") or {}
    markdown = data.get("markdown") or ""
    metadata = data.get("metadata") or {}
    title = html.escape(metadata.get("title") or "")
    status_code = metadata.get("statusCode") or 200
    return (f"<html><head><title>{title}</title></head><body>\n<pre>{html.escape(markdown)}</pre>\n</body></html>", status_code)


def scrape_browser(url: str, headless: bool, wait_for: str, scroll: bool) -> tuple[str, int]:
    """Scrape with the browser backend, falling back to Firecrawl if the page is an error page or has little text.

    The Firecrawl result replaces the browser's only if it has more visible text.
    """
    if USE_SELENIUM:
        content, status_code = scrape_selenium(url, headless=headless, scroll=scroll)
    else:
        with _playwright_lock:
            content, status_code = scrape_playwright(url, headless=headless, wait_for=wait_for, scroll=scroll)

    if status_code < 400 and visible_text_length(content) >= MIN_VISIBLE_CHARS:
        return (content, status_code)
    if not os.environ.get("FIRECRAWL_API_KEY"):
        logger.warning(f"{url} looks blocked or empty (status={status_code}); set FIRECRAWL_API_KEY to retry with Firecrawl")
        return (content, status_code)
    logger.info(f"{url} looks blocked or empty (status={status_code}); trying Firecrawl")
    try:
        fc_content, fc_status = scrape_firecrawl(url)
    except Exception as e:
        logger.warning(f"Firecrawl failed for {url}: {e}")
        return (content, status_code)
    if visible_text_length(fc_content) > visible_text_length(content):
        return (fc_content, fc_status)
    return (content, status_code)


def compute_scrape(
    url: str,
    headless: bool = True,
    wait_for: str = "networkidle",
    scroll: bool = True,
) -> Path:
    """
    Scrape URL and cache the page to data/scraped/<hash>.html.zst

    Backend selection via USE_SELENIUM constant:
    - Selenium: Thread-safe, slower, realistic browser (USE_SELENIUM=True)
    - Playwright: Faster, needs workers=1 due to greenlets (USE_SELENIUM=False)

    The cache is the file: if it exists the page is not scraped again. Failures are not cached (the caller records
    them, e.g. as a scrape_error entry).

    Args:
        url: URL to scrape
        headless: Run browser in headless mode
        wait_for: Wait condition for Playwright ("networkidle", "load", "domcontentloaded")
        scroll: Scroll page to trigger lazy loading

    Returns:
        Path to the cached .html.zst file

    Raises:
        RuntimeError: If scraping fails
    """
    url = normalize_url(url)
    scrape_path = get_scrape_path(url)

    if scrape_path.exists():
        logger.debug(f"Using cached scrape for {url}")
        _count_page(url, "cached")
        return scrape_path

    backend = "selenium" if USE_SELENIUM else "playwright"
    logger.info(f"Scraping {url} (backend={backend})")

    try:
        if FORUM_POST_RE.match(url):
            # LessWrong / Alignment Forum: API instead of the browser (which gets 403)
            content, status_code = scrape_forum_api(url)
        elif ARXIV_RE.match(url):
            content, status_code = scrape_arxiv(url)
        elif is_pdf_url(url):
            # PDFs: download and extract the text, as browsers cannot read them
            content, status_code = scrape_pdf(url)
        else:
            content, status_code = scrape_browser(url, headless=headless, wait_for=wait_for, scroll=scroll)

        # Write to a temporary file first: a half-written file would count as a cache hit
        tmp_path = scrape_path.with_name(f"{scrape_path.name[: -len('.html.zst')]}.tmp.html.zst")
        with smart_open(tmp_path, "wt", encoding="utf-8") as f:
            f.write(content)
        tmp_path.replace(scrape_path)
    except Exception as e:
        logger.error(f"Failed to scrape {url}: {e}")
        _count_page(url, "errors", str(e))
        raise RuntimeError(f"Scraping failed: {e}") from e

    _count_page(url, "new")
    logger.info(f"Successfully scraped {url} (status={status_code})")
    return scrape_path


def _count_page(url: str, outcome: str, error: str | None = None) -> None:
    """Record the outcome (new, cached or errors) of a scrape in the run's stats, if there is one."""
    try:
        stats = get_stats()
        with stats.lock:
            if outcome == "errors":
                stats.scraped_pages.errors[url] = error
            else:
                getattr(stats.scraped_pages, outcome).add(url)
    except RuntimeError:
        pass  # No active stats context
