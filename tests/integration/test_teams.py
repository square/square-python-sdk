import uuid
from typing import List

from square.types.money import Money
from square.types.team_member import TeamMember
from square.types.wage_setting import WageSetting

from . import helpers


def create_team_member() -> str:
    client = helpers.test_client()

    member_response = client.team_members.create(
        idempotency_key=str(uuid.uuid4()),
        team_member={"given_name": "Sherlock", "family_name": "Holmes"},
    )
    member = member_response.team_member
    assert member is not None
    assert isinstance(member, TeamMember)
    assert member.id is not None
    return member.id


def create_bulk_team_members() -> List[str]:
    client = helpers.test_client()

    bulk_response = client.team_members.batch_create(
        team_members={
            "id1": {
                "team_member": {"given_name": "Donatello", "family_name": "Splinter"}
            },
            "id2": {
                "team_member": {"given_name": "Leonardo", "family_name": "Splinter"}
            },
        }
    )

    bulk_member_ids = []

    team_members = bulk_response.team_members
    assert team_members is not None
    team_members = team_members if team_members else dict()
    for value in team_members.values():
        team_member = value.team_member
        assert team_member is not None
        assert isinstance(team_member, TeamMember)
        assert team_member.id is not None
        bulk_member_ids.append(team_member.id)

    return bulk_member_ids


def test_search_team_members():
    client = helpers.test_client()
    member_id = create_team_member()
    bulk_member_ids = create_bulk_team_members()

    response = client.team_members.search(limit=1)
    assert response.team_members is not None
    assert len(response.team_members) > 0


def test_create_team_member():
    client = helpers.test_client()

    response = client.team_members.create(
        idempotency_key=str(uuid.uuid4()),
        team_member={"given_name": "John", "family_name": "Watson"},
    )

    assert response.team_member is not None
    assert isinstance(response.team_member, TeamMember)
    assert "John" == response.team_member.given_name
    assert "Watson" == response.team_member.family_name


def test_retrieve_team_member():
    client = helpers.test_client()
    member_id = create_team_member()
    bulk_member_ids = create_bulk_team_members()

    response = client.team_members.get(team_member_id=member_id)

    assert response.team_member is not None
    assert isinstance(response.team_member, TeamMember)
    assert member_id == response.team_member.id


def test_update_team_member():
    client = helpers.test_client()
    member_id = create_team_member()
    bulk_member_ids = create_bulk_team_members()

    client.team_members.update(
        team_member_id=member_id,
        team_member={"given_name": "Agent", "family_name": "Smith"},
    )
    get_response = client.team_members.get(team_member_id=member_id)

    team_member = get_response.team_member
    assert team_member is not None
    assert isinstance(team_member, TeamMember)
    assert "Agent" == team_member.given_name
    assert "Smith" == team_member.family_name


def test_update_wage_setting():
    client = helpers.test_client()
    member_id = create_team_member()
    bulk_member_ids = create_bulk_team_members()

    response = client.team_members.wage_setting.update(
        team_member_id=member_id,
        wage_setting={
            "job_assignments": [
                {
                    "pay_type": "HOURLY",
                    "hourly_rate": {"amount": 2500, "currency": "USD"},
                    "job_title": "Math tutor",
                }
            ]
        },
    )

    assert response.wage_setting is not None
    assert isinstance(response.wage_setting, WageSetting)
    job_assignments = response.wage_setting.job_assignments
    assert job_assignments is not None
    assert len(job_assignments) > 0
    assert "Math tutor" == job_assignments[0].job_title
    hourly_rate = job_assignments[0].hourly_rate
    assert hourly_rate is not None
    assert isinstance(hourly_rate, Money)
    assert 2500 == hourly_rate.amount


def test_batch_update_team_members():
    client = helpers.test_client()
    member_id = create_team_member()
    bulk_member_ids = create_bulk_team_members()

    response = client.team_members.batch_update(
        team_members={
            bulk_member_ids[0]: {
                "team_member": {"given_name": "Raphael", "family_name": "Splinter"}
            },
            bulk_member_ids[1]: {
                "team_member": {"given_name": "Leonardo", "family_name": "Splinter"}
            },
        }
    )
    assert response.team_members is not None
    assert 2 == len(response.team_members)
