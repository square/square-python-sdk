# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class CustomersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(CustomersApi, self).__init__(config, auth_managers)

    def list_customers(self,
                       cursor=None,
                       limit=None,
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
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for your original query.  For
                more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            limit (int, optional): The maximum number of results to return in
                a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less
                than 1 or greater than 100, Square returns a `400
                VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default
                value is 100.  For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            sort_field (CustomerSortField, optional): Indicates how customers
                should be sorted.  The default value is `DEFAULT`.
            sort_order (SortOrder, optional): Indicates whether customers
                should be sorted in ascending (`ASC`) or descending (`DESC`)
                order.  The default value is `ASC`.

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
            'limit': limit,
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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

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

        Creates a new customer for a business.
        You must provide at least one of the following values in your request
        to this
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
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

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
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_customer(self,
                        customer_id,
                        version=None):
        """Does a DELETE request to /v2/customers/{customer_id}.

        Deletes a customer profile from a business. This operation also
        unlinks any associated cards on file. 
        As a best practice, you should include the `version` field in the
        request to enable [optimistic
        concurrency](https://developer.squareup.com/docs/working-with-apis/opti
        mistic-concurrency) control. The value must be set to the current
        version of the customer profile. 
        To delete a customer profile that was created by merging existing
        profiles, you must use the ID of the newly created profile.

        Args:
            customer_id (string): The ID of the customer to delete.
            version (long|int, optional): The current version of the customer
                profile.  As a best practice, you should include this
                parameter to enable [optimistic
                concurrency](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/optimistic-concurrency) control.  For more
                information, see [Delete a customer
                profile](https://developer.squareup.com/docs/customers-api/use-
                the-api/keep-records#delete-customer-profile).

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
        _query_parameters = {
            'version': version
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
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

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

        Updates a customer profile. To change an attribute, specify the new
        value. To remove an attribute, specify the value as an empty string or
        empty object.
        As a best practice, you should include the `version` field in the
        request to enable [optimistic
        concurrency](https://developer.squareup.com/docs/working-with-apis/opti
        mistic-concurrency) control. The value must be set to the current
        version of the customer profile.
        To update a customer profile that was created by merging existing
        profiles, you must use the ID of the newly created profile.
        You cannot use this endpoint to change cards on file. To make changes,
        use the [Cards API]($e/Cards) or [Gift Cards API]($e/GiftCards).

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
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    @deprecated()
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
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    @deprecated()
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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
