# -*- coding: utf-8 -*-



import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.customers_api import CustomersApi


class CustomersApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(CustomersApiTests, cls).setUpClass()
        cls.controller = cls.client.customers
        cls.response_catcher = cls.controller.http_call_back

    # Creates a new customer for a business, which can have associated cards on file.
    #
    #You must provide __at least one__ of the following values in your request to this
    #endpoint:
    #
    #- `given_name`
    #- `family_name`
    #- `company_name`
    #- `email_address`
    #- `phone_number`
    #
    #This endpoint does not accept an idempotency key. If you accidentally create
    #a duplicate customer, you can delete it with the
    #[DeleteCustomer](#endpoint-deletecustomer) endpoint.
    def test_create_customer(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            '{"given_name":"Amelia","family_name":"Earhart","email_address":"Amelia.Ear'
            'hart@example.com","address":{"address_line_1":"500 Electric Ave","address_l'
            'ine_2":"Suite 600","locality":"New York"},"phone_number":"1-212-555-4240","'
            'reference_id":"YOUR_REFERENCE_ID","note":"a customer"}'
            )

        # Perform the API call through the SDK function
        result = self.controller.create_customer(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

