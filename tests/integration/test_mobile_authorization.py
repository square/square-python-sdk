from . import helpers


def test_create_mobile_authorization_code():
    client = helpers.test_client()
    location_id = helpers.get_default_location_id(client)

    response = client.mobile.authorization_code(location_id=location_id)
    assert response.authorization_code is not None
    assert response.expires_at is not None
