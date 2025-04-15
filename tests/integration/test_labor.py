import time
import uuid
from datetime import datetime, timedelta

from square.types.break_type import BreakType
from square.types.money import Money
from square.types.shift import Shift
from square.types.shift_wage import ShiftWage
from square.types.team_member import TeamMember

from . import helpers


def create_team_member() -> str:
    client = helpers.test_client()

    team_response = client.team_members.create(
        idempotency_key=str(uuid.uuid4()),
        team_member={"given_name": "Sherlock", "family_name": "Holmes"},
    )
    team_member = team_response.team_member
    assert team_member is not None
    assert isinstance(team_member, TeamMember)
    assert team_member.id is not None
    return team_member.id


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
    )
    break_type = break_response.break_type
    assert break_type is not None
    assert isinstance(break_type, BreakType)
    assert break_type.id is not None
    return break_type.id


def delete_break_type(break_type_id: str):
    client = helpers.test_client()
    try:
        client.labor.break_types.delete(id=break_type_id)
    except Exception as e:
        # test may have already deleted the break
        pass


def create_shift(team_member_id: str) -> str:
    client = helpers.test_client()

    shift_response = client.labor.shifts.create(
        shift={
            "location_id": helpers.get_default_location_id(client),
            "start_at": helpers.format_date_string(datetime.now()),
            "team_member_id": team_member_id,
        },
        idempotency_key=str(uuid.uuid4()),
    )
    shift = shift_response.shift
    assert shift is not None
    assert isinstance(shift, Shift)
    assert shift.id is not None
    return shift.id


def delete_shift(shift_id: str):
    client = helpers.test_client()
    try:
        client.labor.shifts.delete(id=shift_id)
    except Exception as e:
        # test may have already deleted the shift
        pass


def get_first_break_type_id() -> str:
    client = helpers.test_client()
    response = client.labor.break_types.list(
        location_id=helpers.get_default_location_id(client)
    )
    break_types = response.items
    if break_types is not None and len(break_types) > 0:
        return break_types[0].id or ""
    raise Exception("No break types found")


def test_get_break_type():
    # Wait to kick off the first test to avoid being rate limited.
    time.sleep(3)

    client = helpers.test_client()
    team_member_id = create_team_member()
    break_type_id = create_break_type()
    shift_id = create_shift(team_member_id)

    response = client.labor.break_types.get(id=break_type_id)
    assert response.break_type is not None
    assert isinstance(response.break_type, BreakType)
    assert break_type_id == response.break_type.id

    list_response = client.labor.break_types.list()
    assert list_response.items is not None
    assert len(list_response.items) > 0

    delete_break_type(break_type_id)
    delete_shift(shift_id)


def test_update_break_type():
    client = helpers.test_client()
    team_member_id = create_team_member()
    break_type_id = create_break_type()
    shift_id = create_shift(team_member_id)

    response = client.labor.break_types.update(
        id=break_type_id,
        break_type={
            "location_id": helpers.get_default_location_id(client),
            "break_name": "Lunch_" + str(uuid.uuid4()),
            "expected_duration": "PT1H0M0S",
            "is_paid": True,
        },
    )
    assert response.break_type is not None
    assert isinstance(response.break_type, BreakType)
    assert break_type_id == response.break_type.id
    assert "PT1H" == response.break_type.expected_duration

    delete_break_type(break_type_id)
    delete_shift(shift_id)


def test_search_shifts():
    client = helpers.test_client()
    team_member_id = create_team_member()
    break_type_id = create_break_type()
    shift_id = create_shift(team_member_id)

    response = client.labor.shifts.search(limit=1)
    assert response.shifts is not None
    assert len(response.shifts) > 0

    delete_break_type(break_type_id)
    delete_shift(shift_id)


def test_get_shift():
    client = helpers.test_client()
    team_member_id = create_team_member()
    break_type_id = create_break_type()
    shift_id = create_shift(team_member_id)

    response = client.labor.shifts.get(id=shift_id)
    assert response.shift is not None
    assert isinstance(response.shift, Shift)
    assert shift_id == response.shift.id

    delete_break_type(break_type_id)
    delete_shift(shift_id)


def test_update_shift():
    client = helpers.test_client()
    team_member_id = create_team_member()
    break_type_id = create_break_type()
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

    delete_break_type(break_type_id)
    delete_shift(shift_id)


def test_delete_shift():
    client = helpers.test_client()

    team_member_response = client.team_members.create(
        idempotency_key=str(uuid.uuid4()),
        team_member={"given_name": "Sherlock", "family_name": "Holmes"},
    )

    assert team_member_response.team_member is not None
    assert isinstance(team_member_response.team_member, TeamMember)
    assert team_member_response.team_member.id is not None

    shift_response = client.labor.shifts.create(
        shift={
            "location_id": helpers.get_default_location_id(client),
            "start_at": helpers.format_date_string(datetime.now()),
            "team_member_id": team_member_response.team_member.id,
        },
        idempotency_key=str(uuid.uuid4()),
    )

    assert shift_response.shift is not None
    assert isinstance(shift_response.shift, Shift)
    assert shift_response.shift.id is not None
    shift_id = shift_response.shift.id
    response = client.labor.shifts.delete(id=shift_id)
    assert response is not None


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
    )

    break_type = break_response.break_type
    assert break_type is not None
    assert isinstance(break_type, BreakType)
    assert break_type.id is not None
    break_id = break_type.id

    response = client.labor.break_types.delete(id=break_id)
    assert response is not None


def test_list_workweek_configs():
    client = helpers.test_client()
    response = client.labor.workweek_configs.list()
    assert response.items is not None
    assert len(response.items) > 0
