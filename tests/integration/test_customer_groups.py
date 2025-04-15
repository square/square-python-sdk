import time
import uuid

import pytest

from square.types.customer_group import CustomerGroup

from . import helpers


def create_test_customer_group() -> str:
    client = helpers.test_client()
    response = client.customers.groups.create(
        group={"name": "Default-" + str(uuid.uuid4())},
        idempotency_key=str(uuid.uuid4()),
    )
    group = response.group
    assert group is not None
    assert isinstance(group, CustomerGroup)
    assert group.id is not None
    return group.id


def delete_test_customer_group(group_id: str):
    client = helpers.test_client()
    client.customers.groups.delete(group_id=group_id)


def test_create_and_list_customer_group():
    group_id = create_test_customer_group()
    client = helpers.test_client()
    response = client.customers.groups.list()
    assert response is not None
    groups = response.items
    assert groups is not None
    assert len(groups) > 0
    delete_test_customer_group(group_id)


def test_retrieve_customer_group():
    group_id = create_test_customer_group()
    client = helpers.test_client()
    response = client.customers.groups.get(group_id=group_id)
    assert response.group is not None
    assert isinstance(response.group, CustomerGroup)
    assert group_id == response.group.id
    delete_test_customer_group(group_id)


def test_update_customer_group():
    # This test often gets rate limited; we'll wait a few
    # seconds before proceeding.
    time.sleep(3)

    group_id = create_test_customer_group()
    client = helpers.test_client()
    new_name = "Updated-" + str(uuid.uuid4())
    response = client.customers.groups.update(
        group_id=group_id, group={"name": new_name}
    )
    assert response.group is not None
    assert isinstance(response.group, CustomerGroup)
    assert new_name == response.group.name
    delete_test_customer_group(group_id)


def test_retrieve_non_existent_group():
    client = helpers.test_client()
    with pytest.raises(Exception):
        client.customers.groups.create(
            group={"name": ""}, idempotency_key=str(uuid.uuid4())
        )
