# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac


def is_valid_webhook_event_signature(request_body: str, signature_header: str, signature_key: str,
                                     notification_url: str) -> bool:
    """
    Verifies and validates an event notification. See the `documentation`_ for more details.

    Args:
        request_body:       The JSON body of the request.
        signature_header:   The value for the `x-square-hmacsha256-signature` header.
        signature_key:      The signature key from the Square Developer portal for the webhook subscription.
        notification_url:   The notification endpoint URL as defined in the Square Developer portal for the webhook
                            subscription.

    Returns:
        bool: True if the signature is valid, indicating that the event can be trusted as it came from Square.
            False if the signature validation fails, indicating that the event did not come from Square, so it may
            be malicious and should be discarded.

    Raises:
        ValueError: if `signature_key` or `notification_url` are empty.

    .. _documentation:
        https://developer.squareup.com/docs/webhooks/step3validate
    """
    if not request_body:
        return False
    if not signature_key:
        raise ValueError('signature_key is empty')
    if not notification_url:
        raise ValueError('notification_url is empty')

    # Perform UTF-8 encoding to bytes
    payload = notification_url + request_body
    payload_bytes = payload.encode('utf-8')
    signature_header_bytes = signature_header.encode('utf-8')
    signature_key_bytes = signature_key.encode('utf-8')

    # Compute the hash value
    hashing_obj = hmac.new(key=signature_key_bytes, msg=payload_bytes, digestmod=hashlib.sha256)
    hash_bytes = hashing_obj.digest()

    # Compare the computed hash vs the value in the signature header
    hash_base64 = base64.b64encode(hash_bytes)
    return hmac.compare_digest(hash_base64, signature_header_bytes)
