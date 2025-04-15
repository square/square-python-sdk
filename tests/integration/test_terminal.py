import uuid

from square.types.device_checkout_options import DeviceCheckoutOptions
from square.types.money import Money
from square.types.terminal_checkout import TerminalCheckout

from . import helpers

sandbox_device_id = "da40d603-c2ea-4a65-8cfd-f42e36dab0c7"


def create_terminal_checkout() -> str:
    client = helpers.test_client()

    checkout_response = client.terminal.checkouts.create(
        idempotency_key=str(uuid.uuid4()),
        checkout={
            "amount_money": {"amount": 100, "currency": "USD"},
            "device_options": {"device_id": sandbox_device_id},
        },
    )
    assert checkout_response.checkout is not None
    assert isinstance(checkout_response.checkout, TerminalCheckout)
    checkout_id = checkout_response.checkout.id
    assert checkout_id is not None
    return checkout_id


def test_create_terminal_checkout():
    client = helpers.test_client()
    checkout_id = create_terminal_checkout()

    response = client.terminal.checkouts.create(
        idempotency_key=str(uuid.uuid4()),
        checkout={
            "amount_money": {"amount": 100, "currency": "USD"},
            "device_options": {"device_id": sandbox_device_id},
        },
    )

    assert response.checkout is not None
    assert isinstance(response.checkout, TerminalCheckout)
    assert response.checkout.device_options is not None
    assert isinstance(response.checkout.device_options, DeviceCheckoutOptions)
    assert sandbox_device_id == response.checkout.device_options.device_id
    assert response.checkout.amount_money is not None
    assert isinstance(response.checkout.amount_money, Money)
    assert 100 == response.checkout.amount_money.amount


def test_search_terminal_checkouts():
    client = helpers.test_client()
    checkout_id = create_terminal_checkout()

    response = client.terminal.checkouts.search(limit=1)
    assert response.checkouts is not None
    assert len(response.checkouts) > 0


def test_get_terminal_checkout():
    client = helpers.test_client()
    checkout_id = create_terminal_checkout()

    response = client.terminal.checkouts.cancel(checkout_id=checkout_id)
    assert response.checkout is not None
    assert isinstance(response.checkout, TerminalCheckout)
    assert "CANCELED" == response.checkout.status
