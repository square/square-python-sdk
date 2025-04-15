import pytest

from square.utils.webhooks_helper import verify_signature

REQUEST_BODY = '{"merchant_id":"MLEFBHHSJGVHD","type":"webhooks.test_notification","event_id":"ac3ac95b-f97d-458c-a6e6-18981597e05f","created_at":"2022-07-13T20:30:59.037339943Z","data":{"type":"webhooks","id":"bc368e64-01aa-407e-b46e-3231809b1129"}}'
SIGNATURE_HEADER = "GF4YkrJgGBDZ9NIYbNXBnMzqb2HoL4RW/S6vkZ9/2N4="
SIGNATURE_KEY = "Ibxx_5AKakO-3qeNVR61Dw"
NOTIFICATION_URL = "https://webhook.site/679a4f3a-dcfa-49ee-bac5-9d0edad886b9"


def test_signature_validation_pass():
    is_valid = verify_signature(
        request_body=REQUEST_BODY,
        signature_header=SIGNATURE_HEADER,
        signature_key=SIGNATURE_KEY,
        notification_url=NOTIFICATION_URL,
    )
    assert is_valid


def test_signature_validation_escaped_pass():
    escaped_request_body = '{"data":{"type":"webhooks","id":">id<"}}'
    new_signature_header = "Cxt7+aTi4rKgcA0bC4g9EHdVtLSDWdqccmL5MvihU4U="
    signature_key = "signature-key"
    url = "https://webhook.site/webhooks"

    is_valid = verify_signature(
        request_body=escaped_request_body,
        signature_header=new_signature_header,
        signature_key=signature_key,
        notification_url=url,
    )
    assert is_valid


def test_signature_validation_url_mismatch():
    is_valid = verify_signature(
        request_body=REQUEST_BODY,
        signature_header=SIGNATURE_HEADER,
        signature_key=SIGNATURE_KEY,
        notification_url="https://webhook.site/79a4f3a-dcfa-49ee-bac5-9d0edad886b9",
    )
    assert not is_valid


def test_signature_validation_invalid_signature_key():
    is_valid = verify_signature(
        request_body=REQUEST_BODY,
        signature_header=SIGNATURE_HEADER,
        signature_key="MCmhFRxGX82xMwg5FsaoQA",
        notification_url=NOTIFICATION_URL,
    )
    assert not is_valid


def test_signature_validation_invalid_signature_header():
    is_valid = verify_signature(
        request_body=REQUEST_BODY,
        signature_header="1z2n3DEJJiUPKcPzQo1ftvbxGdw=",
        signature_key=SIGNATURE_KEY,
        notification_url=NOTIFICATION_URL,
    )
    assert not is_valid


def test_signature_validation_body_mismatch():
    request_body = """
        {
            "merchant_id": "MLEFBHHSJGVHD",
            "type": "webhooks.test_notification",
            "event_id": "ac3ac95b-f97d-458c-a6e6-18981597e05f",
            "created_at": "2022-06-13T20:30:59.037339943Z",
            "data": {"type": "webhooks", "id": "bc368e64-01aa-407e-b46e-3231809b1129"}
        }
    """
    is_valid = verify_signature(
        request_body=request_body,
        signature_header=SIGNATURE_HEADER,
        signature_key=SIGNATURE_KEY,
        notification_url=NOTIFICATION_URL,
    )
    assert not is_valid


def test_signature_validation_body_formatted():
    request_body = """
        {
            "merchant_id": "MLEFBHHSJGVHD",
            "type": "webhooks.test_notification",
            "event_id": "ac3ac95b-f97d-458c-a6e6-18981597e05f",
            "created_at": "2022-07-13T20:30:59.037339943Z",
            "data": {
              "type": "webhooks",
              "id": "bc368e64-01aa-407e-b46e-3231809b1129"
            }
        }
        """
    is_valid = verify_signature(
        request_body=request_body,
        signature_header=SIGNATURE_HEADER,
        signature_key=SIGNATURE_KEY,
        notification_url=NOTIFICATION_URL,
    )
    assert not is_valid


def test_signature_validation_empty_signature_key():
    with pytest.raises(ValueError, match="signature_key is empty"):
        verify_signature(
            request_body=REQUEST_BODY,
            signature_header=SIGNATURE_HEADER,
            signature_key="",
            notification_url=NOTIFICATION_URL,
        )


def test_signature_validation_signature_key_not_configured():
    with pytest.raises(ValueError, match="signature_key is empty"):
        verify_signature(
            request_body=REQUEST_BODY,
            signature_header=SIGNATURE_HEADER,
            signature_key=None,
            notification_url=NOTIFICATION_URL,
        )


def test_signature_validation_empty_notification_url():
    with pytest.raises(ValueError, match="notification_url is empty"):
        verify_signature(
            request_body=REQUEST_BODY,
            signature_header=SIGNATURE_HEADER,
            signature_key=SIGNATURE_KEY,
            notification_url="",
        )


def test_signature_validation_notification_url_not_configured():
    with pytest.raises(ValueError, match="notification_url is empty"):
        verify_signature(
            request_body=REQUEST_BODY,
            signature_header=SIGNATURE_HEADER,
            signature_key=SIGNATURE_KEY,
            notification_url=None,
        )
