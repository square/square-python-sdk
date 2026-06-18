import asyncio
import threading
import time
import typing

from ..core.request_options import RequestOptions
from ..requests.query import QueryParams
from ..types.cache_mode import CacheMode
from ..types.load_response import LoadResponse

if typing.TYPE_CHECKING:
    from ..client import AsyncSquare, Square

# Sentinel returned by the Reporting API on an HTTP 200 while a /v1/load query is
# still processing. It is NOT an error -- the request should be retried. See the
# Reporting API docs: https://developer.squareup.com/docs/reporting-api/overview
CONTINUE_WAIT = "Continue wait"

# Defaults for the polling loop: up to 20 attempts with exponential backoff
# starting at 2s and capped at 20s.
DEFAULT_MAX_ATTEMPTS = 20
DEFAULT_INITIAL_DELAY_S = 2.0
DEFAULT_MAX_DELAY_S = 20.0
DEFAULT_BACKOFF_FACTOR = 2.0


class ReportingPollTimeoutError(Exception):
    """Raised when a reporting query does not resolve within the allotted attempts."""


class ReportingPollCancelledError(Exception):
    """Raised when a reporting poll loop is cancelled via its ``cancel_event``."""


def _is_continue_wait(response: LoadResponse) -> bool:
    # A "Continue wait" body parses into a LoadResponse (LoadResponse is an
    # UncheckedBaseModel, so validation is skipped) with the extra ``error`` field
    # preserved (the model is configured with extra="allow") and ``data`` left as
    # None. That surviving ``error`` sentinel is the signal to retry.
    return getattr(response, "error", None) == CONTINUE_WAIT


def _build_load_kwargs(
    *,
    query_type: typing.Optional[str],
    cache: typing.Optional[CacheMode],
    query: typing.Optional[QueryParams],
    request_options: typing.Optional[RequestOptions],
) -> typing.Dict[str, typing.Any]:
    # Forward only the inputs the caller actually set; the generated ``load`` omits
    # anything we leave out (its params default to a sentinel), so a ``None`` here
    # means "don't send it" rather than "send null".
    load_kwargs: typing.Dict[str, typing.Any] = {"request_options": request_options}
    if query_type is not None:
        load_kwargs["query_type"] = query_type
    if cache is not None:
        load_kwargs["cache"] = cache
    if query is not None:
        load_kwargs["query"] = query
    return load_kwargs


def _next_delay(delay: float, backoff_factor: float, max_delay_s: float) -> float:
    return min(delay * backoff_factor, max_delay_s)


def _timeout_error(max_attempts: int) -> ReportingPollTimeoutError:
    return ReportingPollTimeoutError(
        f'Reporting query did not complete after {max_attempts} attempts ("{CONTINUE_WAIT}").'
    )


def load_and_wait(
    client: "Square",
    *,
    query_type: typing.Optional[str] = None,
    cache: typing.Optional[CacheMode] = None,
    query: typing.Optional[QueryParams] = None,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    initial_delay_s: float = DEFAULT_INITIAL_DELAY_S,
    max_delay_s: float = DEFAULT_MAX_DELAY_S,
    backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
    cancel_event: typing.Optional[threading.Event] = None,
    request_options: typing.Optional[RequestOptions] = None,
) -> LoadResponse:
    """
    Runs a reporting query and transparently polls until it resolves, returning the
    final ``LoadResponse``. Re-sends the identical request with exponential backoff
    while the Reporting API answers "Continue wait".

    Args:
        client:          A configured synchronous ``Square`` client.
        query_type:      Optional query type (passed through to ``client.reporting.load``).
        cache:           Optional cache strategy.
        query:           The reporting query (measures, dimensions, filters, ...).
        max_attempts:    Maximum poll attempts before giving up. Default 20.
        initial_delay_s: Delay before the first retry, in seconds. Default 2.0.
        max_delay_s:     Upper bound on the backoff delay, in seconds. Default 20.0.
        backoff_factor:  Multiplier applied to the delay after each attempt. Default 2.0.
        cancel_event:    Optional ``threading.Event``; when set, the loop stops promptly
                         (interrupting any in-flight backoff sleep) and raises
                         ``ReportingPollCancelledError``.
        request_options: Forwarded to each underlying ``client.reporting.load`` call.

    Returns:
        The resolved ``LoadResponse`` (never the "Continue wait" sentinel).

    Raises:
        ReportingPollTimeoutError:   if the query does not resolve within ``max_attempts``.
        ReportingPollCancelledError: if ``cancel_event`` is set before the query resolves.
    """
    load_kwargs = _build_load_kwargs(
        query_type=query_type, cache=cache, query=query, request_options=request_options
    )
    delay = initial_delay_s
    for attempt in range(1, max_attempts + 1):
        if cancel_event is not None and cancel_event.is_set():
            raise ReportingPollCancelledError("Reporting query polling was cancelled.")
        response = client.reporting.load(**load_kwargs)
        if not _is_continue_wait(response):
            return response
        if attempt == max_attempts:
            break
        # ``Event.wait`` doubles as an interruptible sleep: it returns True as soon as
        # the event is set, so cancellation does not wait out the remaining backoff.
        if cancel_event is not None:
            if cancel_event.wait(delay):
                raise ReportingPollCancelledError("Reporting query polling was cancelled.")
        else:
            time.sleep(delay)
        delay = _next_delay(delay, backoff_factor, max_delay_s)

    raise _timeout_error(max_attempts)


async def load_and_wait_async(
    client: "AsyncSquare",
    *,
    query_type: typing.Optional[str] = None,
    cache: typing.Optional[CacheMode] = None,
    query: typing.Optional[QueryParams] = None,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    initial_delay_s: float = DEFAULT_INITIAL_DELAY_S,
    max_delay_s: float = DEFAULT_MAX_DELAY_S,
    backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
    request_options: typing.Optional[RequestOptions] = None,
) -> LoadResponse:
    """
    Async counterpart to :func:`load_and_wait` for the ``AsyncSquare`` client. Polls
    ``client.reporting.load`` with exponential backoff while the Reporting API answers
    "Continue wait", returning the resolved ``LoadResponse``.

    Cancellation is handled the idiomatic asyncio way: cancel the awaiting task (e.g.
    via ``asyncio.wait_for`` / ``Task.cancel``) and the in-flight ``asyncio.sleep``
    raises ``asyncio.CancelledError``, which propagates out of this coroutine.

    Args:
        client:          A configured ``AsyncSquare`` client.
        query_type:      Optional query type (passed through to ``client.reporting.load``).
        cache:           Optional cache strategy.
        query:           The reporting query (measures, dimensions, filters, ...).
        max_attempts:    Maximum poll attempts before giving up. Default 20.
        initial_delay_s: Delay before the first retry, in seconds. Default 2.0.
        max_delay_s:     Upper bound on the backoff delay, in seconds. Default 20.0.
        backoff_factor:  Multiplier applied to the delay after each attempt. Default 2.0.
        request_options: Forwarded to each underlying ``client.reporting.load`` call.

    Returns:
        The resolved ``LoadResponse`` (never the "Continue wait" sentinel).

    Raises:
        ReportingPollTimeoutError: if the query does not resolve within ``max_attempts``.
    """
    load_kwargs = _build_load_kwargs(
        query_type=query_type, cache=cache, query=query, request_options=request_options
    )
    delay = initial_delay_s
    for attempt in range(1, max_attempts + 1):
        response = await client.reporting.load(**load_kwargs)
        if not _is_continue_wait(response):
            return response
        if attempt == max_attempts:
            break
        await asyncio.sleep(delay)
        delay = _next_delay(delay, backoff_factor, max_delay_s)

    raise _timeout_error(max_attempts)
