# -*- coding: utf-8 -*-



import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.labor_api import LaborApi


class LaborApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(LaborApiTests, cls).setUpClass()
        cls.controller = cls.client.labor
        cls.response_catcher = cls.controller.http_call_back

    # Returns a paginated list of `BreakType` instances for a business.
    def test_list_break_types(self):
        # Parameters for the API call
        location_id = None
        limit = None
        cursor = None

        # Perform the API call through the SDK function
        result = self.controller.list_break_types(location_id, limit, cursor)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Returns a paginated list of `EmployeeWage` instances for a business.
    def test_list_employee_wages(self):
        # Parameters for the API call
        employee_id = None
        limit = None
        cursor = None

        # Perform the API call through the SDK function
        result = self.controller.list_employee_wages(employee_id, limit, cursor)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Returns a list of `WorkweekConfig` instances for a business.
    def test_list_workweek_configs(self):
        # Parameters for the API call
        limit = None
        cursor = None

        # Perform the API call through the SDK function
        result = self.controller.list_workweek_configs(limit, cursor)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


