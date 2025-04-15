from . import helpers


def test_customers_pagination():
    client = helpers.test_client()

    for _ in range(5):
        helpers.create_test_customer(client)

    pager = client.customers.list()
    count = 0
    for customer in pager:
        assert customer is not None
        assert customer.id is not None
        count += 1

    assert count > 4
