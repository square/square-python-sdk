# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class CustomersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(CustomersApi, self).__init__(config, call_back)

    def list_customers(self,
                       cursor=None,
                       sort_field=None,
                       sort_order=None):
        """Does a GET request to /v2/customers.

        Lists customer profiles associated with a Square account.
        Under normal operating conditions, newly created or updated customer
        profiles become available
        for the listing operation in well under 30 seconds. Occasionally,
        propagation of the new or updated
        profiles can take closer to one minute or longer, especially during
        network incidents and outages.

        Args:
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for your original query.  See the
                [Pagination
                guide](https://developer.squareup.com/docs/working-with-apis/pa
                gination) for more information.
            sort_field (CustomerSortField, optional): Indicates how Customers
                should be sorted.  Default: `DEFAULT`.
            sort_order (SortOrder, optional): Indicates whether Customers
                should be sorted in ascending (`ASC`) or descending (`DESC`)
                order.  Default: `ASC`.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'sort_field': sort_field,
            'sort_order': sort_order
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_customer(self,
                        body):
        """Does a POST request to /v2/customers.

        Creates a new customer for a business, which can have associated cards
        on file.
        You must provide __at least one__ of the following values in your
        request to this
        endpoint:
        - `given_name`
        - `family_name`
        - `company_name`
        - `email_address`
        - `phone_number`

        Args:
            body (CreateCustomerRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def search_customers(self,
                         body):
        """Does a POST request to /v2/customers/search.

        Searches the customer profiles associated with a Square account using
        a supported query filter.
        Calling `SearchCustomers` without any explicit query filter returns
        all
        customer profiles ordered alphabetically based on `given_name` and
        `family_name`.
        Under normal operating conditions, newly created or updated customer
        profiles become available
        for the search operation in well under 30 seconds. Occasionally,
        propagation of the new or updated
        profiles can take closer to one minute or longer, especially during
        network incidents and outages.

        Args:
            body (SearchCustomersRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/search'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_customer(self,
                        customer_id):
        """Does a DELETE request to /v2/customers/{customer_id}.

        Deletes a customer from a business, along with any linked cards on
        file. When two profiles
        are merged into a single profile, that profile is assigned a new
        `customer_id`. You must use the
        new `customer_id` to delete merged profiles.

        Args:
            customer_id (string): The ID of the customer to delete.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_customer(self,
                          customer_id):
        """Does a GET request to /v2/customers/{customer_id}.

        Returns details for a single customer.

        Args:
            customer_id (string): The ID of the customer to retrieve.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_customer(self,
                        customer_id,
                        body):
        """Does a PUT request to /v2/customers/{customer_id}.

        Updates the details of an existing customer. When two profiles are
        merged
        into a single profile, that profile is assigned a new `customer_id`.
        You must use
        the new `customer_id` to update merged profiles.
        You cannot edit a customer's cards on file with this endpoint. To make
        changes
        to a card on file, you must delete the existing card on file with the
        [DeleteCustomerCard](#endpoint-Customers-deletecustomercard) endpoint,
        then create a new one with the
        [CreateCustomerCard](#endpoint-Customers-createcustomercard)
        endpoint.

        Args:
            customer_id (string): The ID of the customer to update.
            body (UpdateCustomerRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_customer_card(self,
                             customer_id,
                             body):
        """Does a POST request to /v2/customers/{customer_id}/cards.

        Adds a card on file to an existing customer.
        As with charges, calls to `CreateCustomerCard` are idempotent.
        Multiple
        calls with the same card nonce return the same card record that was
        created
        with the provided nonce during the _first_ call.

        Args:
            customer_id (string): The Square ID of the customer profile the
                card is linked to.
            body (CreateCustomerCardRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/cards'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_customer_card(self,
                             customer_id,
                             card_id):
        """Does a DELETE request to /v2/customers/{customer_id}/cards/{card_id}.

        Removes a card on file from a customer.

        Args:
            customer_id (string): The ID of the customer that the card on file
                belongs to.
            card_id (string): The ID of the card on file to delete.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/cards/{card_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True},
            'card_id': {'value': card_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def remove_group_from_customer(self,
                                   customer_id,
                                   group_id):
        """Does a DELETE request to /v2/customers/{customer_id}/groups/{group_id}.

        Removes a group membership from a customer. 
        The customer is identified by the `customer_id` value 
        and the customer group is identified by the `group_id` value.

        Args:
            customer_id (string): The ID of the customer to remove from the
                group.
            group_id (string): The ID of the customer group to remove the
                customer from.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/groups/{group_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True},
            'group_id': {'value': group_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def add_group_to_customer(self,
                              customer_id,
                              group_id):
        """Does a PUT request to /v2/customers/{customer_id}/groups/{group_id}.

        Adds a group membership to a customer. 
        The customer is identified by the `customer_id` value 
        and the customer group is identified by the `group_id` value.

        Args:
            customer_id (string): The ID of the customer to add to a group.
            group_id (string): The ID of the customer group to add the
                customer to.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/groups/{group_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True},
            'group_id': {'value': group_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
