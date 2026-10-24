"""Claude calls with structured output, a disk cache and a running cost estimate.

Every call is cached in cache/llm/ by its full request, so rerunning a script only pays for calls that changed.
"""

import hashlib
import json
import logging
import os
import threading
from concurrent.futures import ThreadPoolExecutor

import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel

from shared.data import CACHE, REPO, ROOT

load_dotenv(ROOT / ".env")
for other in ("facets-shared", "taxonomy", "main-pipeline"):  # otherwise reuse a key another pipeline already has
    load_dotenv(REPO / other / ".env")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpx2").setLevel(logging.WARNING)
log = logging.getLogger("llm")

DEFAULT_MODEL = os.environ.get("TAXONOMY_MODEL", "claude-opus-5-5")
MAX_PARALLEL = 8
LLM_CACHE = CACHE / "llm"

# $ per million tokens: input, output, cache read, cache write (5-minute)
PRICES = {
    "claude-opus-5-5": (4.0, 20.0, 0.20, 5.0),
    "claude-sonnet-5-5": (2.0, 10.0, 0.20, 2.5),
    "claude-haiku-5-5": (0.10, 0.50, 0.01, 0.125),
}

_client = None
_lock = threading.Lock()
usage = {"calls": 0, "cached_calls": 0, "input": 0, "output": 0, "cache_read": 0, "cache_write": 0, "cost": 0.0}


def client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(timeout=900, max_retries=4)
    return _client


def _cache_key(*parts) -> str:
    return hashlib.sha256(json.dumps(parts, sort_keys=True).encode()).hexdigest()[:32]


def parse(system: str, user: str, schema: type[BaseModel], *, model: str = DEFAULT_MODEL, effort: str = "medium",
          max_tokens: int = 16000, label: str = "") -> BaseModel | None:
    """One structured-output call. The system prompt is cached (put the big, shared part there)."""
    key = _cache_key(model, effort, system, user, schema.__name__, schema.model_json_schema())
    path = LLM_CACHE / f"{key}.json"
    if path.exists():
        with _lock:
            usage["cached_calls"] += 1
        return schema.model_validate_json(path.read_text())

    try:
        response = client().beta.messages.parse(
            model=model, max_tokens=max_tokens,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user}],
            output_config={"effort": effort}, output_format=schema,
            betas=["server-side-fallback-2026-07-01"], fallbacks="default")
    except anthropic.AuthenticationError:
        raise
    except anthropic.APIError as e:
        log.error(f"{label}: error calling Claude API: {e}")
        return None

    u = response.usage
    price = PRICES.get(model, PRICES["claude-opus-5-5"])
    cache_read = u.cache_read_input_tokens or 0
    cache_write = u.cache_creation_input_tokens or 0
    with _lock:
        usage["calls"] += 1
        usage["input"] += u.input_tokens
        usage["output"] += u.output_tokens
        usage["cache_read"] += cache_read
        usage["cache_write"] += cache_write
        usage["cost"] += (u.input_tokens * price[0] + u.output_tokens * price[1] + cache_read * price[2]
                          + cache_write * price[3]) / 1e6

    if response.stop_reason in ("refusal", "max_tokens") or response.parsed_output is None:
        log.warning(f"{label}: no usable output ({response.stop_reason})")
        return None
    LLM_CACHE.mkdir(parents=True, exist_ok=True)
    path.write_text(response.parsed_output.model_dump_json())
    return response.parsed_output


def run_parallel(fn, args_list: list, max_workers: int = MAX_PARALLEL) -> list:
    """fn(*args) for each args tuple, in parallel, results in input order."""
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(lambda args: fn(*args), args_list))


def usage_report() -> str:
    return (f"Claude: {usage['calls']} calls (+{usage['cached_calls']} from disk cache), "
            f"{usage['input']:,} input / {usage['cache_read']:,} cache-read / {usage['cache_write']:,} cache-write / "
            f"{usage['output']:,} output tokens, about ${usage['cost']:.2f}")
