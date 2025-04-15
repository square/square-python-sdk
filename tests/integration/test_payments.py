import uuid

from square.types.money import Money
from square.types.payment import Payment

from . import helpers


def create_payment() -> str:
    client = helpers.test_client()
    payment_response = client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        app_fee_money={"amount": 10, "currency": "USD"},
        autocomplete=False,
    )
    payment = payment_response.payment
    assert payment is not None
    assert isinstance(payment, Payment)
    assert payment.id is not None
    return payment.id


def test_list_payments():
    client = helpers.test_client()

    response = client.payments.list()
    page = response.next_page()
    payments = page.items
    assert payments is not None
    assert len(payments) > 0


def test_create_payment():
    client = helpers.test_client()

    response = client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        app_fee_money={"amount": 10, "currency": "USD"},
        autocomplete=False,
    )
    payment = response.payment
    assert payment is not None
    assert isinstance(payment, Payment)
    assert payment.app_fee_money is not None
    assert isinstance(payment.app_fee_money, Money)
    assert 10 == payment.app_fee_money.amount
    assert "USD" == payment.app_fee_money.currency
    assert payment.amount_money is not None
    assert isinstance(payment.amount_money, Money)
    assert 200 == payment.amount_money.amount
    assert "USD" == payment.amount_money.currency


def test_get_payment():
    client = helpers.test_client()
    payment_id = create_payment()

    response = client.payments.get(payment_id=payment_id)

    assert response.payment is not None
    assert isinstance(response.payment, Payment)
    assert payment_id == response.payment.id


def test_cancel_payment():
    client = helpers.test_client()
    payment_id = create_payment()

    response = client.payments.cancel(payment_id=payment_id)

    assert response.payment is not None
    assert isinstance(response.payment, Payment)
    assert payment_id == response.payment.id


def test_cancel_payment_by_idempotency_key():
    client = helpers.test_client()

    idempotency_key = str(uuid.uuid4())

    client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=idempotency_key,
        amount_money={"amount": 200, "currency": "USD"},
        app_fee_money={"amount": 10, "currency": "USD"},
        autocomplete=False,
    )

    response = client.payments.cancel_by_idempotency_key(
        idempotency_key=idempotency_key
    )
    assert response is not None


def test_complete_payment():
    client = helpers.test_client()
    payment_id = create_payment()

    create_response = client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        app_fee_money={"amount": 10, "currency": "USD"},
        autocomplete=False,
    )

    payment = create_response.payment
    assert payment is not None
    assert isinstance(payment, Payment)

    payment_id = payment.id
    response = client.payments.complete(payment_id=payment_id)

    assert response.payment is not None
    assert isinstance(response.payment, Payment)
    assert "COMPLETED" == response.payment.status
