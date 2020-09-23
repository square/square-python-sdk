# -*- coding: utf-8 -*-



import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.customers_api import CustomersApi


class V2EndpointsTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(V2EndpointsTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = CustomersApi(cls.config, cls.response_catcher)

    def test_v2_endpoints_journey(self):
        phone_number, phone_number2 = "1-212-555-4240", "1-917-500-1000"
        postal_code, postal_code2 = "10003", "98100"
        customer = {
            "given_name": "Amelia",
            "family_name": "Earhart",
            "phone_number": phone_number,
            "note": "a customer",
            "address": {
                "address_line_1": "500 Electric Ave",
                "address_line_2": "Suite 600",
                "locality": "New York",
                "administrative_district_level_1": "NY",
                "postal_code": postal_code,
                "country": "US"
            }
        }

        # create
        response = self.controller.create_customer(customer)
        data = response.body['customer']
        self.assertEquals(data['phone_number'], phone_number)
        self.assertEquals(data['address']['postal_code'], postal_code)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.is_success(), True)
        self.assertEquals(response.is_error(), False)
        customer_id = data['id']

        # retrieve
        response = self.controller.retrieve_customer(customer_id)
        data = response.body['customer'] 
        self.assertEquals(data['phone_number'], phone_number)
        self.assertEquals(data['address']['postal_code'], postal_code)
        self.assertEquals(response.status_code, 200)

        # list
        response = self.controller.list_customers()
        data = response.body['customers'] 
        self.assertEquals(type(data), list)
        self.assertTrue(len(data) > 0)
        self.assertEquals(response.status_code, 200)

        # update
        customer['phone_number'] = phone_number2
        customer['address']['postal_code'] = postal_code2

        response = self.controller.update_customer(customer_id=customer_id, body=customer)
        data = response.body['customer'] 
        self.assertEquals(data['phone_number'], phone_number2)
        self.assertEquals(data['address']['postal_code'], postal_code2)
        self.assertEquals(response.status_code, 200)

        # retrieve
        response = self.controller.retrieve_customer(customer_id)
        data = response.body['customer'] 
        self.assertEquals(data['phone_number'], phone_number2)
        self.assertEquals(data['address']['postal_code'], postal_code2)
        self.assertEquals(response.status_code, 200)

        # delete
        response = self.controller.delete_customer(customer_id)
        self.assertEquals(response.body, {})
        self.assertEquals(response.status_code, 200)


