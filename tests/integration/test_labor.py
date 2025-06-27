import time
import uuid
from datetime import datetime, timedelta
from functools import wraps

from square.core.api_error import ApiError
from square.core.request_options import RequestOptions
from square.types.break_type import BreakType
from square.types.money import Money
from square.types.shift import Shift
from square.types.shift_wage import ShiftWage
from square.types.team_member import TeamMember

from . import helpers

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
def get_first_team_member() -> str:
    client = helpers.test_client()

    # Search for active team members at the default location
    team_response = client.team_members.search(
        query={
            "filter": {
                "location_ids": [helpers.get_default_location_id(client)],
                "status": "ACTIVE"
            }
        },
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    if not team_response.team_members or len(team_response.team_members) == 0:
        raise Exception(f"No team members available at location {helpers.get_default_location_id(client)}")
    
    team_member = team_response.team_members[0]
    assert team_member is not None
    assert isinstance(team_member, TeamMember)
    assert team_member.id is not None
    return team_member.id


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
def create_shift(team_member_id: str) -> str:
    client = helpers.test_client()

    shift_response = client.labor.shifts.create(
        shift={
            "location_id": helpers.get_default_location_id(client),
            "start_at": helpers.format_date_string(datetime.now()),
            "team_member_id": team_member_id,
        },
        idempotency_key=str(uuid.uuid4()),
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    shift = shift_response.shift
    assert shift is not None
    assert isinstance(shift, Shift)
    assert shift.id is not None
    return shift.id


def delete_shift(shift_id: str):
    client = helpers.test_client()
    try:
        client.labor.shifts.delete(
            id=shift_id,
            request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
        )
    except Exception as e:
        # test may have already deleted the shift
        print(f"Error deleting shift: {str(e)}")
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
    team_member_id = get_first_team_member()
    time.sleep(2)  # Add delay between operations
    break_type_id = create_break_type()
    time.sleep(2)  # Add delay between operations
    shift_id = create_shift(team_member_id)

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
    delete_shift(shift_id)


@retry_with_backoff()
def test_update_break_type():
    client = helpers.test_client()
    team_member_id = get_first_team_member()
    time.sleep(2)  # Add delay between operations
    break_type_id = create_break_type()
    time.sleep(2)  # Add delay between operations
    shift_id = create_shift(team_member_id)

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
    delete_shift(shift_id)


@retry_with_backoff()
def test_search_shifts():
    client = helpers.test_client()
    team_member_id = get_first_team_member()
    time.sleep(2)  # Add delay between operations
    break_type_id = create_break_type()
    time.sleep(2)  # Add delay between operations
    shift_id = create_shift(team_member_id)

    response = client.labor.shifts.search(
        limit=1,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response.shifts is not None
    assert len(response.shifts) > 0

    time.sleep(2)  # Add delay before cleanup
    delete_break_type(break_type_id)
    delete_shift(shift_id)


@retry_with_backoff()
def test_get_shift():
    client = helpers.test_client()
    team_member_id = get_first_team_member()
    time.sleep(2)  # Add delay between operations
    break_type_id = create_break_type()
    time.sleep(2)  # Add delay between operations
    shift_id = create_shift(team_member_id)

    response = client.labor.shifts.get(
        id=shift_id,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response.shift is not None
    assert isinstance(response.shift, Shift)
    assert shift_id == response.shift.id

    time.sleep(2)  # Add delay before cleanup
    delete_break_type(break_type_id)
    delete_shift(shift_id)


@retry_with_backoff()
def test_update_shift():
    client = helpers.test_client()
    team_member_id = get_first_team_member()
    time.sleep(2)  # Add delay between operations
    break_type_id = create_break_type()
    time.sleep(2)  # Add delay between operations
    shift_id = create_shift(team_member_id)

    response = client.labor.shifts.update(
        id=shift_id,
        shift={
            "location_id": helpers.get_default_location_id(client),
            "start_at": helpers.format_date_string(
                datetime.now() - timedelta(minutes=1)
            ),
            "team_member_id": team_member_id,
            "wage": {
                "title": "Manager",
                "hourly_rate": {"amount": 2500, "currency": "USD"},
            },
        },
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    shift = response.shift
    assert shift is not None
    assert isinstance(shift, Shift)
    assert shift.wage is not None
    assert isinstance(shift.wage, ShiftWage)
    assert "Manager" == shift.wage.title
    assert isinstance(shift.wage.hourly_rate, Money)
    assert 2500 == shift.wage.hourly_rate.amount
    assert "USD" == shift.wage.hourly_rate.currency

    time.sleep(2)  # Add delay before cleanup
    delete_break_type(break_type_id)
    delete_shift(shift_id)


@retry_with_backoff()
def test_delete_shift():
    client = helpers.test_client()

    # Search for existing shifts for this team member
    team_member_id = get_first_team_member()
    
    # Search for existing shifts
    existing_shifts = client.labor.shifts.search(
        query={
            "filter": {
                "team_member_ids": [team_member_id]
            }
        },
        limit=100,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    # Delete any existing shifts
    if existing_shifts.shifts:
        for shift in existing_shifts.shifts:
            if shift.id:
                delete_shift(shift.id)

    # Start the shift 10 seconds from now and end it 20 seconds from now
    start_time = datetime.now() + timedelta(seconds=10)
    end_time = start_time + timedelta(seconds=10)

    # Create shift
    shift_response = client.labor.shifts.create(
        shift={
            "location_id": helpers.get_default_location_id(client),
            "start_at": helpers.format_date_string(start_time),
            "end_at": helpers.format_date_string(end_time),
            "team_member_id": team_member_id,
        },
        idempotency_key=str(uuid.uuid4()),
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    assert shift_response.shift is not None
    assert isinstance(shift_response.shift, Shift)
    assert shift_response.shift.id is not None
    shift_id = shift_response.shift.id

    time.sleep(1)  # Add small delay to ensure the shift is fully created

    response = client.labor.shifts.delete(
        id=shift_id,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    assert response is not None


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