# -*- coding: utf-8 -*-



import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.merchants_api import MerchantsApi


class MerchantsApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(MerchantsApiTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = MerchantsApi(cls.config, cls.response_catcher)

    # Returns `Merchant` information for a given access token.
    #
    #If you don't know a `Merchant` ID, you can use this endpoint to retrieve the merchant ID for an access token.
    #You can specify your personal access token to get your own merchant information or specify an OAuth token
    #to get the information for the  merchant that granted you access.
    #
    #If you know the merchant ID, you can also use the [RetrieveMerchant](#endpoint-merchants-retrievemerchant) 
    #endpoint to get the merchant information.
    def test_list_merchants(self):
        # Parameters for the API call
        cursor = None

        # Perform the API call through the SDK function
        result = self.controller.list_merchants(cursor)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


