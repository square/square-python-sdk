# -*- coding: utf-8 -*-



import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.refunds_api import RefundsApi


class RefundsApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(RefundsApiTests, cls).setUpClass()
        cls.controller = cls.client.refunds
        cls.response_catcher = cls.controller.http_call_back

    # Retrieves a list of refunds for the account making the request.
    #
    #Max results per page: 100
    def test_test_list_payment_refunds(self):
        # Parameters for the API call
        begin_time = None
        end_time = None
        sort_order = None
        cursor = None
        location_id = None
        status = None
        source_type = None

        # Perform the API call through the SDK function
        result = self.controller.list_payment_refunds(begin_time, end_time, sort_order, cursor, location_id, status, source_type)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


