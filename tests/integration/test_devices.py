import uuid

from square.types.device_code import DeviceCode

from . import helpers


def create_device_code():
    client = helpers.test_client()
    create_response = client.devices.codes.create(
        idempotency_key=str(uuid.uuid4()), device_code={"product_type": "TERMINAL_API"}
    )
    device_code = create_response.device_code
    assert device_code is not None
    assert isinstance(device_code, DeviceCode)
    assert device_code.id is not None
    return device_code.id


def test_list_device_codes():
    client = helpers.test_client()
    create_device_code()
    response = client.devices.codes.list()
    assert response.items is not None
    assert len(response.items) > 0


def test_create_device_code():
    client = helpers.test_client()
    response = client.devices.codes.create(
        idempotency_key=str(uuid.uuid4()), device_code={"product_type": "TERMINAL_API"}
    )
    assert response.device_code is not None
    assert isinstance(response.device_code, DeviceCode)
    assert "TERMINAL_API" == response.device_code.product_type


def test_get_device_code():
    client = helpers.test_client()
    device_code_id = create_device_code()
    response = client.devices.codes.get(id=device_code_id)
    assert response.device_code is not None
    assert isinstance(response.device_code, DeviceCode)
    assert response.device_code.id
    assert "TERMINAL_API" == response.device_code.product_type
