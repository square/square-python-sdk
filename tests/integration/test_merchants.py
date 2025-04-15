from square.types.merchant import Merchant

from . import helpers


def get_merchant_id() -> str:
    client = helpers.test_client()

    merchants_response = client.merchants.list()
    assert merchants_response.items is not None
    assert len(merchants_response.items) > 0
    merchant = merchants_response.items[0]
    assert merchant.id is not None
    return merchant.id


def test_list_merchants():
    client = helpers.test_client()
    response = client.merchants.list()
    assert response.items is not None
    assert len(response.items) > 0


def test_retrieve_merchant():
    client = helpers.test_client()
    merchant_id = get_merchant_id()

    response = client.merchants.get(merchant_id=merchant_id)
    assert response.merchant is not None
    assert isinstance(response.merchant, Merchant)
    assert merchant_id == response.merchant.id
