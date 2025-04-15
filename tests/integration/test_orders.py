import uuid

from square.types.order import Order

from . import helpers


def create_order() -> str:
    client = helpers.test_client()
    location_id = helpers.get_default_location_id(client)

    order_response = client.orders.create(
        idempotency_key=str(uuid.uuid4()),
        order={
            "location_id": location_id,
            "line_items": [
                {
                    "quantity": "1",
                    "name": "New Item",
                    "base_price_money": {"amount": 100, "currency": "USD"},
                }
            ],
        },
    )
    order = order_response.order
    assert order is not None
    assert isinstance(order, Order)
    assert order.id is not None
    return order.id


def get_line_item_id(order_id: str) -> str:
    client = helpers.test_client()

    order_response = client.orders.get(order_id=order_id)
    order = order_response.order
    assert order is not None
    assert isinstance(order, Order)
    line_items = order.line_items
    assert line_items is not None
    assert len(line_items) > 0
    line_item = line_items[0]
    assert line_item.uid is not None
    return line_item.uid


def test_create_order():
    client = helpers.test_client()

    response = client.orders.create(
        order={
            "location_id": helpers.get_default_location_id(client),
            "line_items": [
                {
                    "quantity": "1",
                    "name": "New Item",
                    "base_price_money": {"amount": 100, "currency": "USD"},
                }
            ],
        }
    )

    order = response.order
    assert order is not None
    assert isinstance(order, Order)
    line_items = order.line_items
    assert line_items is not None
    assert len(line_items) > 0
    assert "New Item" == line_items[0].name


def test_batch_retrieve_orders():
    client = helpers.test_client()
    order_id = create_order()
    line_item_id = get_line_item_id(order_id)

    response = client.orders.batch_get(order_ids=[order_id])
    orders = response.orders
    assert orders is not None
    assert len(orders) > 0
    order = orders[0]
    assert order_id == order.id


def test_search_orders():
    client = helpers.test_client()
    order_id = create_order()
    line_item_id = get_line_item_id(order_id)

    response = client.orders.search(
        limit=1, location_ids=[helpers.get_default_location_id(client)]
    )
    assert response.orders is not None
    assert len(response.orders) > 0


def test_update_order():
    client = helpers.test_client()
    order_id = create_order()
    line_item_id = get_line_item_id(order_id)

    response = client.orders.update(
        order_id=order_id,
        idempotency_key=str(uuid.uuid4()),
        order={
            "location_id": helpers.get_default_location_id(client),
            "line_items": [
                {
                    "quantity": "1",
                    "name": "Updated Item",
                    "base_price_money": {"amount": 0, "currency": "USD"},
                }
            ],
            "version": 1,
        },
        fields_to_clear=["line_items[" + line_item_id + "]"],
    )

    assert response.order is not None
    assert isinstance(response.order, Order)
    assert order_id == response.order.id
    line_items = response.order.line_items
    assert line_items is not None
    assert len(line_items) > 0
    assert "Updated Item" == line_items[0].name

    response = client.orders.pay(
        order_id=order_id,
        idempotency_key=str(uuid.uuid4()),
        order_version=2,
        payment_ids=[],
    )
    assert response.order is not None
    assert isinstance(response.order, Order)
    assert order_id == response.order.id


def test_calculate_order():
    client = helpers.test_client()
    order_id = create_order()
    line_item_id = get_line_item_id(order_id)

    response = client.orders.calculate(
        order={
            "location_id": helpers.get_default_location_id(client),
            "line_items": [
                {
                    "quantity": "1",
                    "name": "New Item",
                    "base_price_money": {"amount": 100, "currency": "USD"},
                }
            ],
        }
    )

    assert response.order is not None
    assert isinstance(response.order, Order)
    assert response.order.total_money is not None
