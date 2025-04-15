from . import helpers


def test_list_locations():
    client = helpers.test_client()

    response = client.locations.list()
    assert response.locations is not None
    assert len(response.locations) > 0
