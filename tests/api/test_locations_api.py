# -*- coding: utf-8 -*-

import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.locations_api import LocationsApi


class LocationsApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(LocationsApiTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = LocationsApi(cls.config, cls.response_catcher)

    # Provides information of all locations of a business.
    #
    #Many Square API endpoints require a `location_id` parameter.
    #The `id` field of the [`Location`](#type-location) objects returned by this
    #endpoint correspond to that `location_id` parameter.
    def test_list_locations(self):

        # Perform the API call through the SDK function
        result = self.controller.list_locations()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

