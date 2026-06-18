"""Live, end-to-end tests for the Reporting API.

The Reporting API is a beta, bespoke offering served ONLY from production
(connect.squareup.com/reporting) -- it is not routed on sandbox (which 404s),
and a sandbox token 401s against prod. Validating it live therefore needs a
production, reporting-provisioned access token. CI's regular ``TEST_SQUARE_TOKEN``
is sandbox-only, so this suite is gated behind ``TEST_SQUARE_REPORTING`` -- which
is itself the prod, reporting-provisioned token -- and skips by default when it is
unset, keeping CI green. The endpoints exercised are read-only (schema
discovery + queries). The polling *logic* is covered without a live account in
``test_reporting_helper.py``.

Run it against a real prod account:

    TEST_SQUARE_REPORTING=<prod-reporting-token> \
        poetry run pytest tests/integration/test_reporting.py
    # Override the host with TEST_SQUARE_BASE_URL=<url> if reporting moves.
"""

import os

import pytest

from square import Square
from square.environment import SquareEnvironment
from square.utils.reporting_helper import load_and_wait

pytestmark = pytest.mark.skipif(
    not os.getenv("TEST_SQUARE_REPORTING"),
    reason="Set TEST_SQUARE_REPORTING to a prod, reporting-provisioned token to run the live Reporting API suite.",
)


def reporting_client() -> Square:
    token = os.getenv("TEST_SQUARE_REPORTING")
    if not token:
        raise RuntimeError("TEST_SQUARE_REPORTING must be set to a prod, reporting-provisioned token to run the reporting integration suite.")
    # Reporting only exists on production; allow overriding the host via TEST_SQUARE_BASE_URL.
    base_url = os.getenv("TEST_SQUARE_BASE_URL")
    if base_url:
        return Square(token=token, base_url=base_url)
    return Square(token=token, environment=SquareEnvironment.PRODUCTION)


def first_measure_name(client: Square) -> str:
    metadata = client.reporting.get_metadata()
    cubes = metadata.cubes or []
    for cube in cubes:
        for measure in cube.measures or []:
            if measure.name:
                return measure.name
    raise RuntimeError("No cubes/measures are available on the reporting schema for this account.")


def test_get_metadata_returns_queryable_schema() -> None:
    client = reporting_client()
    metadata = client.reporting.get_metadata()

    assert metadata.cubes is not None
    assert len(metadata.cubes) > 0


def test_load_returns_results_or_continue_wait_sentinel() -> None:
    client = reporting_client()
    measure = first_measure_name(client)

    response = client.reporting.load(query={"measures": [measure]})

    sentinel = getattr(response, "error", None)
    if sentinel is not None:
        # Documented async behavior: a still-processing query comes back as HTTP 200
        # with {"error": "Continue wait"} instead of results.
        assert sentinel == "Continue wait"
    else:
        assert response.data is not None


def test_load_and_wait_resolves_without_continue_wait() -> None:
    client = reporting_client()
    measure = first_measure_name(client)

    response = load_and_wait(
        client,
        query={"measures": [measure]},
        max_attempts=20,
        initial_delay_s=2.0,
        max_delay_s=20.0,
    )

    # The polling helper must never hand back the raw "Continue wait" sentinel.
    assert getattr(response, "error", None) is None
    assert response.data is not None
