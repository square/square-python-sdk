# -*- coding: utf-8 -*-

import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from square.api_helper import APIHelper


class LocationsApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(LocationsApiTests, cls).setUpClass()
        cls.controller = cls.client.locations
        cls.response_catcher = cls.controller.http_call_back

    # Provides details about all of the seller's [locations](https://developer.squareup.com/docs/locations-api),
    #including those with an inactive status.
    def test_list_locations(self):

        # Perform the API call through the SDK function
        result = self.controller.list_locations()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

