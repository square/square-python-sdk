import time
import uuid
from functools import wraps

from square.core.api_error import ApiError
from square.core.request_options import RequestOptions
from square.types.break_type import BreakType

from . import helpers

# NOTE: Shift tests were removed when the Shifts API was retired (2026-05-21,
# replaced by Timecards). Break type and workweek config coverage remains.

MAX_TIMEOUT = 120
MAX_RETRIES = 5


def retry_with_backoff(max_retries=5, base_delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ApiError, Exception) as e:
                    if attempt < max_retries - 1:
                        delay = base_delay * (2 ** attempt)  # exponential backoff
                        print(f"Request failed. Retrying in {delay} seconds... Error: {str(e)}")
                        time.sleep(delay)
                        continue
                    raise
            return None
        return wrapper
    return decorator


@retry_with_backoff()
def create_break_type() -> str:
    client = helpers.test_client()

    break_response = client.labor.break_types.create(
        break_type={
            "location_id": helpers.get_default_location_id(client),
            "break_name": "Lunch_" + str(uuid.uuid4()),
            "expected_duration": "PT0H30M0S",
            "is_paid": True,
        },
        idempotency_key=str(uuid.uuid4()),
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    break_type = break_response.break_type
    assert break_type is not None
    assert isinstance(break_type, BreakType)
    assert break_type.id is not None
    return break_type.id


def delete_break_type(break_type_id: str):
    client = helpers.test_client()
    try:
        client.labor.break_types.delete(
            id=break_type_id,
            request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
        )
    except Exception as e:
        # test may have already deleted the break
        print(f"Error deleting break type: {str(e)}")
        pass


@retry_with_backoff()
def get_first_break_type_id() -> str:
    client = helpers.test_client()
    response = client.labor.break_types.list(
        location_id=helpers.get_default_location_id(client),
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    break_types = response.items
    if break_types is not None and len(break_types) > 0:
        return break_types[0].id or ""
    raise Exception("No break types found")


@retry_with_backoff()
def test_get_break_type():
    # Wait to kick off the first test to avoid being rate limited.
    time.sleep(3)

    client = helpers.test_client()
    break_type_id = create_break_type()

    response = client.labor.break_types.get(
        id=break_type_id,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response.break_type is not None
    assert isinstance(response.break_type, BreakType)
    assert break_type_id == response.break_type.id

    list_response = client.labor.break_types.list(
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert list_response.items is not None
    assert len(list_response.items) > 0

    time.sleep(2)  # Add delay before cleanup
    delete_break_type(break_type_id)


@retry_with_backoff()
def test_update_break_type():
    client = helpers.test_client()
    break_type_id = create_break_type()

    response = client.labor.break_types.update(
        id=break_type_id,
        break_type={
            "location_id": helpers.get_default_location_id(client),
            "break_name": "Lunch_" + str(uuid.uuid4()),
            "expected_duration": "PT1H0M0S",
            "is_paid": True,
        },
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response.break_type is not None
    assert isinstance(response.break_type, BreakType)
    assert break_type_id == response.break_type.id
    assert "PT1H" == response.break_type.expected_duration

    time.sleep(2)  # Add delay before cleanup
    delete_break_type(break_type_id)


@retry_with_backoff()
def test_delete_break_type():
    client = helpers.test_client()

    break_response = client.labor.break_types.create(
        break_type={
            "location_id": helpers.get_default_location_id(client),
            "break_name": "Lunch_" + str(uuid.uuid4()),
            "expected_duration": "PT0H30M0S",
            "is_paid": True,
        },
        idempotency_key=str(uuid.uuid4()),
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    break_type = break_response.break_type
    assert break_type is not None
    assert isinstance(break_type, BreakType)
    assert break_type.id is not None
    break_id = break_type.id

    time.sleep(2)  # Add delay before delete

    response = client.labor.break_types.delete(
        id=break_id,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response is not None


@retry_with_backoff()
def test_list_workweek_configs():
    client = helpers.test_client()
    response = client.labor.workweek_configs.list(
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response.items is not None
    assert len(response.items) > 0
