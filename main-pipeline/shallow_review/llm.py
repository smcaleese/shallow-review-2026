"""LLM calls through the Anthropic SDK: prompt templates, structured outputs, a disk cache and token/cost stats."""

import hashlib
import json
import logging
import threading
from pathlib import Path
from typing import Any, Type, TypeVar

import anthropic
from diskcache import Cache
from jinja2 import Template
from pydantic import BaseModel, ValidationError

from .common import DATA_PATH, is_shutdown_requested
from .stats import get_stats

T = TypeVar("T", bound=BaseModel)
logger = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-sonnet-5-5"

# USD per million tokens: (input, output). Cache reads cost 0.1x the input price, cache writes 1.25x (5 minute TTL)
# or 2x (1 hour TTL).
PRICES = {
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-opus-5-5": (4.0, 20.0),
    "claude-haiku-5-5": (0.1, 0.5),
}

# Validation failures (the model's JSON doesn't fit the schema) are retried this many times in total, skipping the cache
VALIDATION_ATTEMPTS = 3

_client: anthropic.Anthropic | None = None
_cache: Cache | None = None
_setup_lock = threading.Lock()


def _get_client() -> anthropic.Anthropic:
    """The shared client. The SDK retries rate limits, connection errors and 5xx responses with backoff."""
    global _client
    with _setup_lock:
        if _client is None:
            _client = anthropic.Anthropic(max_retries=5, timeout=300.0)
        return _client


def _get_cache() -> Cache:
    """Disk cache of responses, in <data>/.llm_cache."""
    global _cache
    with _setup_lock:
        if _cache is None:
            cache_dir = DATA_PATH / ".llm_cache"
            cache_dir.mkdir(exist_ok=True, parents=True)
            _cache = Cache(str(cache_dir))
        return _cache


def _read_template(template: str | None, path: Path | str | None, what: str) -> str:
    if template is not None:
        return template
    if path is not None:
        return Path(path).read_text()
    raise ValueError(f"Either {what}_prompt_path or {what}_prompt_template must be provided")


def _cost(model: str, usage: Any) -> float:
    """Cost in USD of one response; 0 for a model without a known price."""
    if model not in PRICES:
        return 0.0
    input_price, output_price = PRICES[model]
    cache_read = usage.cache_read_input_tokens or 0
    cache_write = usage.cache_creation_input_tokens or 0
    return (
        usage.input_tokens * input_price
        + cache_read * input_price * 0.1
        + cache_write * input_price * 1.25
        + usage.output_tokens * output_price
    ) / 1_000_000


def _update_stats(model: str, usage: Any, stats_subtree: str | None) -> None:
    if not stats_subtree:
        return
    try:
        stats = get_stats()
        with stats.lock:
            tokens = getattr(stats, stats_subtree, None)
            if tokens is not None:
                tokens.update(
                    cache_read=usage.cache_read_input_tokens or 0,
                    cache_write=usage.cache_creation_input_tokens or 0,
                    uncached=usage.input_tokens,
                    output=usage.output_tokens,  # includes the thinking tokens, which the API doesn't report separately
                    cost=_cost(model, usage),
                )
    except RuntimeError:
        pass  # No active stats context
    except Exception as e:
        logger.warning(f"Failed to update stats: {e}")


def get_completion(
    template_vars: dict[str, Any],
    model: str = DEFAULT_MODEL,
    stats_subtree: str | None = None,
    response_type: Type[T] | None = None,
    effort: str = "medium",
    system_cache_ttl: str | None = "5m",
    max_tokens: int = 16000,
    system_prompt_path: Path | str | None = None,
    user_prompt_path: Path | str | None = None,
    system_prompt_template: str | None = None,
    user_prompt_template: str | None = None,
) -> T | str:
    """
    Render the prompts, call Claude and return the answer.

    With `response_type` the API is asked for JSON matching that Pydantic model (structured outputs) and the validated
    model is returned; otherwise the text. Responses are cached on disk by request. Thinking is adaptive; `effort`
    ("low" to "max") sets how much of it to use.

    Args:
        template_vars: Variables for rendering both Jinja2 prompt templates
        model: Model ID (default claude-sonnet-5-5)
        stats_subtree: Name of the stats entry to add token counts and cost to (e.g. "classify_tokens")
        response_type: Pydantic model for structured output; None returns the raw text
        effort: Thinking effort: low, medium, high, xhigh or max
        system_cache_ttl: Prompt-cache TTL of the system prompt ("5m", "1h"), or None to not cache it
        max_tokens: Limit on the response, thinking included
        system_prompt_path / system_prompt_template: the system prompt (a file or a string, Jinja2)
        user_prompt_path / user_prompt_template: the user prompt (a file or a string, Jinja2)

    Raises:
        ValueError: if a prompt is missing, or the response is cut off at max_tokens
        RuntimeError: if the model refuses
        pydantic.ValidationError: if the response doesn't fit response_type after VALIDATION_ATTEMPTS
        anthropic.APIError: if the API call fails after the SDK's retries
    """
    system_prompt = Template(_read_template(system_prompt_template, system_prompt_path, "system")).render(**template_vars)
    user_prompt = Template(_read_template(user_prompt_template, user_prompt_path, "user")).render(**template_vars)

    system_block: dict[str, Any] = {"type": "text", "text": system_prompt}
    if system_cache_ttl:
        system_block["cache_control"] = {"type": "ephemeral", "ttl": system_cache_ttl}
    request: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "system": [system_block],
        "messages": [{"role": "user", "content": user_prompt}],
        "output_config": {"effort": effort},
    }
    cache_key = hashlib.sha256(
        json.dumps([request, response_type.model_json_schema() if response_type else None], sort_keys=True).encode()
    ).hexdigest()

    for attempt in range(VALIDATION_ATTEMPTS):
        if is_shutdown_requested():
            raise KeyboardInterrupt("Shutdown requested before API call")

        text = _get_cache().get(cache_key) if attempt == 0 else None
        if text is None:
            text = _call_api(request, response_type, stats_subtree)
            _get_cache().set(cache_key, text)
        else:
            logger.info(f"LLM call ({model}): cache hit")

        if response_type is None:
            return text
        try:
            return response_type.model_validate_json(text)
        except ValidationError as e:
            # Structured outputs make this rare. Forget the cached answer and ask again.
            logger.warning(f"Response didn't fit {response_type.__name__} (attempt {attempt + 1}): {e}\n{text}")
            _get_cache().delete(cache_key)
            if attempt == VALIDATION_ATTEMPTS - 1:
                raise
    raise AssertionError("unreachable")


def _call_api(request: dict[str, Any], response_type: Type[T] | None, stats_subtree: str | None) -> str:
    """One API call. Returns the text of the answer (JSON when response_type is given)."""
    client = _get_client()
    if response_type is not None:
        response = client.messages.parse(**request, output_format=response_type)
    else:
        response = client.messages.create(**request)

    usage = response.usage
    logger.info(
        f"LLM call ({request['model']}): {usage.input_tokens + (usage.cache_read_input_tokens or 0)} input tokens "
        f"({usage.cache_read_input_tokens or 0} cached), {usage.output_tokens} output tokens"
    )
    _update_stats(request["model"], usage, stats_subtree)

    if response.stop_reason == "refusal":
        raise RuntimeError(f"The model refused: {response.stop_details}")
    if response.stop_reason == "max_tokens":
        raise ValueError(f"The response was cut off at max_tokens={request['max_tokens']}")
    return next(block.text for block in response.content if block.type == "text")
