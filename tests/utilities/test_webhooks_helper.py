from unittest import TestCase

from square.utilities.webhooks_helper import is_valid_webhook_event_signature


class TestWebhooksHelper(TestCase):
    REQUEST_BODY = "{\"merchant_id\":\"MLEFBHHSJGVHD\",\"type\":\"webhooks.test_notification\",\"event_id\":\"ac3ac95b-f97d-458c-a6e6-18981597e05f\",\"created_at\":\"2022-07-13T20:30:59.037339943Z\",\"data\":{\"type\":\"webhooks\",\"id\":\"bc368e64-01aa-407e-b46e-3231809b1129\"}}"
    SIGNATURE_HEADER = 'GF4YkrJgGBDZ9NIYbNXBnMzqb2HoL4RW/S6vkZ9/2N4='
    SIGNATURE_KEY = 'Ibxx_5AKakO-3qeNVR61Dw'
    NOTIFICATION_URL = 'https://webhook.site/679a4f3a-dcfa-49ee-bac5-9d0edad886b9'

    def test_signature_validation_pass(self):
        is_valid = is_valid_webhook_event_signature(self.REQUEST_BODY,
                                                    self.SIGNATURE_HEADER,
                                                    self.SIGNATURE_KEY,
                                                    self.NOTIFICATION_URL)
        self.assertTrue(is_valid)

    def test_signature_validation_escaped_pass(self):

        escpaedRequestBody = '{"data":{"type":"webhooks","id":">id<"}}'
        newSignatureHeader = "Cxt7+aTi4rKgcA0bC4g9EHdVtLSDWdqccmL5MvihU4U="
        signatureKey = "signature-key"
        url = "https://webhook.site/webhooks"
        
        is_valid = is_valid_webhook_event_signature(escpaedRequestBody,
                                                    newSignatureHeader,
                                                    signatureKey,
                                                    url)
        self.assertTrue(is_valid)

    def test_signature_validation_url_mismatch(self):
        is_valid = is_valid_webhook_event_signature(self.REQUEST_BODY,
                                                    self.SIGNATURE_HEADER,
                                                    self.SIGNATURE_KEY,
                                                    'https://webhook.site/79a4f3a-dcfa-49ee-bac5-9d0edad886b9')
        self.assertFalse(is_valid)

    def test_signature_validation_invalid_signature_key(self):
        is_valid = is_valid_webhook_event_signature(self.REQUEST_BODY,
                                                    self.SIGNATURE_HEADER,
                                                    'MCmhFRxGX82xMwg5FsaoQA',
                                                    self.NOTIFICATION_URL)
        self.assertFalse(is_valid)

    def test_signature_validation_invalid_signature_header(self):
        is_valid = is_valid_webhook_event_signature(self.REQUEST_BODY,
                                                    '1z2n3DEJJiUPKcPzQo1ftvbxGdw=',
                                                    self.SIGNATURE_KEY,
                                                    self.NOTIFICATION_URL)
        self.assertFalse(is_valid)

    def test_signature_validation_body_mismatch(self):
        request_body = "{\"merchant_id\":\"MLEFBHHSJGVHD\",\"type\":\"webhooks.test_notification\",\"event_id\":\"ac3ac95b-f97d-458c-a6e6-18981597e05f\",\"created_at\":\"2022-06-13T20:30:59.037339943Z\",\"data\":{\"type\":\"webhooks\",\"id\":\"bc368e64-01aa-407e-b46e-3231809b1129\"}}"
        is_valid = is_valid_webhook_event_signature(request_body,
                                                    self.SIGNATURE_HEADER,
                                                    self.SIGNATURE_KEY,
                                                    self.NOTIFICATION_URL)
        self.assertFalse(is_valid)

    def test_signature_validation_body_formatted(self):
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
        is_valid = is_valid_webhook_event_signature(request_body,
                                                    self.SIGNATURE_HEADER,
                                                    self.SIGNATURE_KEY,
                                                    self.NOTIFICATION_URL)
        self.assertFalse(is_valid)

    def test_signature_validation_empty_signature_key(self):
        with self.assertRaisesRegex(ValueError, 'signature_key is empty'):
            is_valid_webhook_event_signature(self.REQUEST_BODY,
                                             self.SIGNATURE_HEADER,
                                             '',
                                             self.NOTIFICATION_URL)

    def test_signature_validation_signature_key_not_configured(self):
        with self.assertRaisesRegex(ValueError, 'signature_key is empty'):
            is_valid_webhook_event_signature(self.REQUEST_BODY,
                                             self.SIGNATURE_HEADER,
                                             None,
                                             self.NOTIFICATION_URL)

    def test_signature_validation_empty_notification_url(self):
        with self.assertRaisesRegex(ValueError, 'notification_url is empty'):
            is_valid_webhook_event_signature(self.REQUEST_BODY,
                                             self.SIGNATURE_HEADER,
                                             self.SIGNATURE_KEY,
                                             '')

    def test_signature_validation_notification_url_not_configured(self):
        with self.assertRaisesRegex(ValueError, 'notification_url is empty'):
            is_valid_webhook_event_signature(self.REQUEST_BODY,
                                             self.SIGNATURE_HEADER,
                                             self.SIGNATURE_KEY,
                                             None)
