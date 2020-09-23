# -*- coding: utf-8 -*-



import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.employees_api import EmployeesApi


class EmployeesApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(EmployeesApiTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = EmployeesApi(cls.config, cls.response_catcher)

    # Gets a list of `Employee` objects for a business.
    def test_test_list_employees(self):
        # Parameters for the API call
        location_id = None
        status = None
        limit = None
        cursor = None

        # Perform the API call through the SDK function
        result = self.controller.list_employees(location_id, status, limit, cursor)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


