"""Offline unit tests for the Reporting API polling helper.

The Reporting API answers a still-processing ``/v1/load`` query with an HTTP 200
whose body is ``{"error": "Continue wait"}``. ``load_and_wait`` /
``load_and_wait_async`` own the retry loop around that sentinel. These tests
exercise that loop without a network by scripting ``client.reporting.load``, plus
one test that proves the sentinel actually survives the generated client's
deserialization. They run offline, so they stay green in CI.

The live, end-to-end suite lives in ``test_reporting.py`` (gated behind
``TEST_SQUARE_REPORTING``).
"""

import threading
import typing

import pytest

from square.core.unchecked_base_model import construct_type
from square.types.load_response import LoadResponse
from square.utils.reporting_helper import (
    CONTINUE_WAIT,
    ReportingPollCancelledError,
    ReportingPollTimeoutError,
    load_and_wait,
    load_and_wait_async,
)

if typing.TYPE_CHECKING:
    from square.client import AsyncSquare, Square


def _continue_wait() -> LoadResponse:
    # Build the sentinel the same way the generated client does, so the tests
    # exercise the real type rather than a hand-rolled stand-in.
    return typing.cast(LoadResponse, construct_type(type_=LoadResponse, object_={"error": CONTINUE_WAIT}))


def _resolved() -> LoadResponse:
    return typing.cast(
        LoadResponse,
        construct_type(type_=LoadResponse, object_={"data": [{"Orders.count": "128"}]}),
    )


class _FakeReporting:
    """A ``reporting`` stub whose ``load`` returns a scripted sequence of responses."""

    def __init__(
        self,
        sequence: typing.List[LoadResponse],
        on_call: typing.Optional[typing.Callable[[int], None]] = None,
    ) -> None:
        self._sequence = sequence
        self._on_call = on_call
        self.calls = 0

    def load(self, **_kwargs: typing.Any) -> LoadResponse:
        response = self._sequence[min(self.calls, len(self._sequence) - 1)]
        self.calls += 1
        if self._on_call is not None:
            self._on_call(self.calls)
        return response


class _FakeAsyncReporting:
    def __init__(self, sequence: typing.List[LoadResponse]) -> None:
        self._sequence = sequence
        self.calls = 0

    async def load(self, **_kwargs: typing.Any) -> LoadResponse:
        response = self._sequence[min(self.calls, len(self._sequence) - 1)]
        self.calls += 1
        return response


def _fake_client(reporting: typing.Any) -> "Square":
    class _FakeClient:
        pass

    client = _FakeClient()
    client.reporting = reporting  # type: ignore[attr-defined]
    return typing.cast("Square", client)


def test_polls_past_continue_wait_and_returns_resolved_result() -> None:
    reporting = _FakeReporting([_continue_wait(), _continue_wait(), _resolved()])
    client = _fake_client(reporting)

    response = load_and_wait(
        client,
        query={"measures": ["Orders.count"]},
        initial_delay_s=0.001,
        max_delay_s=0.001,
        max_attempts=5,
    )

    # The helper must never hand back the raw sentinel.
    assert getattr(response, "error", None) is None
    assert response.data is not None
    assert reporting.calls == 3


def test_returns_immediately_when_first_response_has_results() -> None:
    reporting = _FakeReporting([_resolved()])
    client = _fake_client(reporting)

    response = load_and_wait(client, initial_delay_s=0.001)

    assert response.data is not None
    assert reporting.calls == 1


def test_raises_timeout_once_max_attempts_exhausted() -> None:
    reporting = _FakeReporting([_continue_wait()])  # never resolves
    client = _fake_client(reporting)

    with pytest.raises(ReportingPollTimeoutError, match="did not complete after 3 attempts"):
        load_and_wait(client, initial_delay_s=0.001, max_delay_s=0.001, max_attempts=3)

    assert reporting.calls == 3


def test_cancel_event_set_before_start_aborts_without_calling() -> None:
    reporting = _FakeReporting([_continue_wait()])
    client = _fake_client(reporting)
    cancel_event = threading.Event()
    cancel_event.set()

    with pytest.raises(ReportingPollCancelledError):
        load_and_wait(client, initial_delay_s=10, max_attempts=10, cancel_event=cancel_event)

    assert reporting.calls == 0


def test_cancel_event_interrupts_backoff_sleep() -> None:
    cancel_event = threading.Event()

    # Trip the event after the first poll; the helper's interruptible backoff sleep
    # must then return promptly and raise rather than waiting out the delay.
    def on_call(_count: int) -> None:
        cancel_event.set()

    reporting = _FakeReporting([_continue_wait()], on_call=on_call)
    client = _fake_client(reporting)

    with pytest.raises(ReportingPollCancelledError):
        load_and_wait(client, initial_delay_s=30, max_attempts=10, cancel_event=cancel_event)

    assert reporting.calls == 1


def test_continue_wait_body_survives_real_deserialization_as_sentinel() -> None:
    # The crux of the design: the generated ``reporting.load`` parses the body with
    # ``construct_type`` (skip-validation + extra="allow"), so the ``error`` sentinel
    # survives onto a LoadResponse-shaped object while ``data`` stays None. If this
    # ever stops being true, load_and_wait would mistake "Continue wait" for a result.
    parsed = typing.cast(
        typing.Any, construct_type(type_=LoadResponse, object_={"error": CONTINUE_WAIT})
    )

    assert parsed.error == CONTINUE_WAIT
    assert parsed.data is None


async def test_async_polls_past_continue_wait_and_resolves() -> None:
    reporting = _FakeAsyncReporting([_continue_wait(), _continue_wait(), _resolved()])
    client = typing.cast("AsyncSquare", _fake_client(reporting))

    response = await load_and_wait_async(
        client,
        query={"measures": ["Orders.count"]},
        initial_delay_s=0.001,
        max_delay_s=0.001,
        max_attempts=5,
    )

    assert getattr(response, "error", None) is None
    assert response.data is not None
    assert reporting.calls == 3


async def test_async_raises_timeout_once_max_attempts_exhausted() -> None:
    reporting = _FakeAsyncReporting([_continue_wait()])  # never resolves
    client = typing.cast("AsyncSquare", _fake_client(reporting))

    with pytest.raises(ReportingPollTimeoutError, match="did not complete after 3 attempts"):
        await load_and_wait_async(client, initial_delay_s=0.001, max_delay_s=0.001, max_attempts=3)

    assert reporting.calls == 3
