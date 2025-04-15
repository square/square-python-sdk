import uuid

from square.types.card import Card
from square.types.custom_attribute import CustomAttribute
from square.types.customer import Customer
from square.types.customer_group import CustomerGroup

from . import helpers


def create_customer() -> str:
    client = helpers.test_client()
    customer_response = client.customers.create(
        idempotency_key=str(uuid.uuid4()),
        given_name="Amelia",
        family_name="Earhart",
        phone_number="1-212-555-4240",
        note="a customer",
        address={
            "address_line1": "500 Electric Ave",
            "address_line2": "Suite 600",
            "locality": "New York",
            "administrative_district_level1": "NY",
            "postal_code": "10003",
            "country": "US",
        },
    )
    customer = customer_response.customer
    assert customer is not None
    assert isinstance(customer, Customer)
    assert customer.id is not None
    return customer.id


def delete_customer(customer_id: str):
    client = helpers.test_client()
    try:
        client.customers.delete(customer_id=customer_id)
    except Exception as e:
        raise RuntimeError(e)


def create_customer_group() -> str:
    client = helpers.test_client()
    create_groups_response = client.customers.groups.create(
        group={"name": "Test Group " + str(uuid.uuid4())},
        idempotency_key=str(uuid.uuid4()),
    )
    group = create_groups_response.group
    assert group is not None
    assert isinstance(group, CustomerGroup)
    assert group.id is not None
    return group.id


def delete_customer_group(customer_group_id: str):
    client = helpers.test_client()
    try:
        client.customers.groups.delete(group_id=customer_group_id)
    except Exception as e:
        raise RuntimeError(e)


def create_custom_attribute_definition() -> str:
    client = helpers.test_client()
    custom_attribute_key = "favorite-drink-" + str(uuid.uuid4())
    client.customers.custom_attribute_definitions.create(
        custom_attribute_definition={
            "key": custom_attribute_key,
            "name": "Favorite Drink" + str(uuid.uuid4()),
            "description": "A customer's favorite drink",
            "visibility": "VISIBILITY_READ_WRITE_VALUES",
            "schema": {
                "$ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.String"
            },
        }
    )
    return custom_attribute_key


def delete_custom_attribute_definition(key: str):
    client = helpers.test_client()
    try:
        client.customers.custom_attribute_definitions.delete(key=key)
    except Exception as e:
        raise RuntimeError(e)


def test_retrieve_customer():
    client = helpers.test_client()
    customer_id = create_customer()
    response = client.customers.get(customer_id=customer_id)
    assert response.customer is not None
    assert isinstance(response.customer, Customer)
    assert customer_id == response.customer.id
    delete_customer(customer_id)


def test_update_customer():
    client = helpers.test_client()
    customer_id = create_customer()
    response = client.customers.update(
        customer_id=customer_id,
        given_name="Updated Amelia",
        family_name="Updated Earhart",
    )
    customer = response.customer
    assert customer is not None
    assert isinstance(customer, Customer)
    assert "Updated Amelia" == customer.given_name
    assert "Updated Earhart" == customer.family_name
    delete_customer(customer_id)


def test_create_customer_card():
    client = helpers.test_client()
    customer_id = create_customer()
    create_card_response = client.customers.cards.create(
        customer_id=customer_id, card_nonce="cnon:card-nonce-ok"
    )
    assert create_card_response.card is not None
    assert isinstance(create_card_response.card, Card)
    customer_card_id = create_card_response.card.id
    assert customer_card_id is not None
    delete_card_response = client.customers.cards.delete(
        customer_id=customer_id, card_id=customer_card_id
    )
    assert delete_card_response is not None
    delete_customer(customer_id)


def test_add_customer_to_group():
    client = helpers.test_client()
    customer_id = create_customer()
    customer_group_id = create_customer_group()
    add_group_response = client.customers.groups.add(
        customer_id=customer_id, group_id=customer_group_id
    )
    assert add_group_response is not None

    remove_group_response = client.customers.groups.remove(
        customer_id=customer_id, group_id=customer_group_id
    )
    assert remove_group_response is not None
    delete_customer(customer_id)
    delete_customer_group(customer_group_id)


def test_create_customer_custom_attribute():
    client = helpers.test_client()
    customer_id = create_customer()
    custom_attribute_key = create_custom_attribute_definition()
    create_attr_response = client.customers.custom_attributes.upsert(
        customer_id=customer_id,
        key=custom_attribute_key,
        custom_attribute={"value": "Double-shot breve", "key": custom_attribute_key},
    )
    assert create_attr_response.custom_attribute is not None
    assert isinstance(create_attr_response.custom_attribute, CustomAttribute)
    assert "Double-shot breve" == create_attr_response.custom_attribute.value

    delete_customer(customer_id)
    delete_custom_attribute_definition(custom_attribute_key)


def test_update_customer_custom_attribute():
    client = helpers.test_client()
    customer_id = create_customer()
    custom_attribute_key = create_custom_attribute_definition()
    update_attr_response = client.customers.custom_attributes.upsert(
        customer_id=customer_id,
        key=custom_attribute_key,
        custom_attribute={"value": "Black coffee"},
    )
    custom_attribute = update_attr_response.custom_attribute
    assert custom_attribute is not None
    assert isinstance(custom_attribute, CustomAttribute)
    assert "Black coffee" == custom_attribute.value

    delete_customer(customer_id)
    delete_custom_attribute_definition(custom_attribute_key)


def test_list_customer_custom_attributes():
    client = helpers.test_client()
    customer_id = create_customer()
    custom_attribute_key = create_custom_attribute_definition()
    client.customers.custom_attributes.upsert(
        customer_id=customer_id,
        key=custom_attribute_key,
        custom_attribute={"value": "Double-shot breve"},
    )

    pager = client.customers.custom_attributes.list(
        customer_id=customer_id, with_definitions=True
    )
    assert pager is not None

    attributes = pager.items
    assert attributes is not None

    delete_attr_response = client.customers.custom_attributes.delete(
        customer_id=customer_id,
        key=custom_attribute_key,
    )
    assert delete_attr_response is not None

    delete_customer(customer_id)
    delete_custom_attribute_definition(custom_attribute_key)


def test_delete_customer_custom_attribute():
    client = helpers.test_client()
    customer_id = create_customer()
    custom_attribute_key = create_custom_attribute_definition()
    client.customers.custom_attributes.upsert(
        customer_id=customer_id,
        key=custom_attribute_key,
        custom_attribute={"value": "Double-shot breve"},
    )

    response = client.customers.custom_attributes.delete(
        customer_id=customer_id, key=custom_attribute_key
    )
    assert response is not None

    delete_customer(customer_id)
    delete_custom_attribute_definition(custom_attribute_key)
