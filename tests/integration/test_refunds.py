import uuid

import pytest

from square.types.payment import Payment
from square.types.payment_refund import PaymentRefund

from . import helpers


def create_payment() -> str:
    client = helpers.test_client()

    payment_response = client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        app_fee_money={"amount": 10, "currency": "USD"},
        autocomplete=True,
    )
    payment = payment_response.payment
    assert payment is not None
    assert isinstance(payment, Payment)
    assert payment.id is not None
    return payment.id


def create_refund(payment_id: str) -> str:
    client = helpers.test_client()

    refund_response = client.refunds.refund_payment(
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        payment_id=payment_id,
    )
    refund = refund_response.refund
    assert refund is not None
    assert isinstance(refund, PaymentRefund)
    assert refund.id is not None
    return refund.id


def test_refund_payment():
    client = helpers.test_client()

    payment_response = client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        app_fee_money={"amount": 10, "currency": "USD"},
        autocomplete=True,
    )
    payment = payment_response.payment
    assert payment is not None
    assert isinstance(payment, Payment)
    assert payment.id is not None
    payment_id = payment.id

    response = client.refunds.refund_payment(
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 200, "currency": "USD"},
        payment_id=payment_id,
    )
    refund = response.refund
    assert refund is not None
    assert isinstance(refund, PaymentRefund)
    assert payment_id == refund.payment_id


def test_get_payment_refund():
    client = helpers.test_client()
    payment_id = create_payment()
    refund_id = create_refund(payment_id)

    response = client.refunds.get(refund_id=refund_id)
    assert response.refund is not None
    assert isinstance(response.refund, PaymentRefund)
    assert payment_id == response.refund.payment_id


def test_handle_invalid_refund_id():
    client = helpers.test_client()
    with pytest.raises(Exception):
        client.refunds.get(refund_id="invalid-id")
