# -*- coding: utf-8 -*-

from tests.test_helper import TestHelper
from tests.api.api_test_base import ApiTestBase

class EmployeesApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(EmployeesApiTests, cls).setUpClass()
        cls.controller = cls.client.employees
        cls.response_catcher = cls.controller.http_call_back

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
