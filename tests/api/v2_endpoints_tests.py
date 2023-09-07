# -*- coding: utf-8 -*-

from tests.api.api_test_base import ApiTestBase


class V2EndpointsTests(ApiTestBase):
    @classmethod
    def setUpClass(cls):
        super(V2EndpointsTests, cls).setUpClass()
        cls.controller = cls.client.customers
        cls.response_catcher = cls.controller.http_call_back

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

        # Create a customer
        response = self.controller.create_customer(customer)
        data = response.body['customer']
        self.assertEqual(data['phone_number'], phone_number)
        self.assertEqual(data['address']['postal_code'], postal_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.is_success(), True)
        self.assertEqual(response.is_error(), False)
        customer_id = data['id']

        # Retrieve a customer
        response = self.controller.retrieve_customer(customer_id)
        data = response.body['customer'] 
        self.assertEqual(data['phone_number'], phone_number)
        self.assertEqual(data['address']['postal_code'], postal_code)
        self.assertEqual(response.status_code, 200)

        # Get list of customers
        response = self.controller.list_customers()
        data = response.body['customers'] 
        self.assertEqual(type(data), list)
        self.assertTrue(len(data) > 0)
        self.assertEqual(response.status_code, 200)

        # Update a customer record
        customer['phone_number'] = phone_number2
        customer['address']['postal_code'] = postal_code2

        response = self.controller.update_customer(customer_id=customer_id, body=customer)
        data = response.body['customer'] 
        self.assertEqual(data['phone_number'], phone_number2)
        self.assertEqual(data['address']['postal_code'], postal_code2)
        self.assertEqual(response.status_code, 200)

        # Retrieve a customer
        response = self.controller.retrieve_customer(customer_id)
        data = response.body['customer'] 
        self.assertEqual(data['phone_number'], phone_number2)
        self.assertEqual(data['address']['postal_code'], postal_code2)
        self.assertEqual(response.status_code, 200)

        # Delete the customer record
        response = self.controller.delete_customer(customer_id)
        self.assertEqual(response.body, {})
        self.assertEqual(response.status_code, 200)
