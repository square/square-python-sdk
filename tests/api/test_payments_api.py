# -*- coding: utf-8 -*-

from tests.test_helper import TestHelper
from tests.api.api_test_base import ApiTestBase

class PaymentsApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(PaymentsApiTests, cls).setUpClass()
        cls.controller = cls.client.payments
        cls.response_catcher = cls.controller.http_call_back

    # Retrieves a list of payments taken by the account making the request.
    #
    #Max results per page: 100
    def test_test_list_payments(self):
        # Parameters for the API call
        begin_time = None
        end_time = None
        sort_order = None
        cursor = None
        location_id = None
        total = None
        last_4 = None
        card_brand = None

        # Perform the API call through the SDK function
        result = self.controller.list_payments(begin_time, end_time, sort_order, cursor, location_id, total, last_4, card_brand)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))
