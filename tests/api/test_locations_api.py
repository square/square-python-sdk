# -*- coding: utf-8 -*-

import json

from tests.api.api_test_base import ApiTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from square.api_helper import APIHelper


class LocationsApiTests(ApiTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(LocationsApiTests, cls).setUpClass()
        cls.controller = cls.client.locations
        cls.response_catcher = cls.controller.http_call_back

    # Provides details about all of the seller's [locations](https://developer.squareup.com/docs/locations-api),
    #including those with an inactive status. Locations are listed alphabetically by `name`.
    def test_list_locations(self):

        # Perform the API call through the SDK function
        result = self.controller.list_locations()

        # Test response code
        assert self.response_catcher.response.status_code == 200

