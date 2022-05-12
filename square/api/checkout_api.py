# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class CheckoutApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(CheckoutApi, self).__init__(config, auth_managers)

    def create_checkout(self,
                        location_id,
                        body):
        """Does a POST request to /v2/locations/{location_id}/checkouts.

        Links a `checkoutId` to a `checkout_page_url` that customers are
        directed to in order to provide their payment information using a
        payment processing workflow hosted on connect.squareup.com. 
        NOTE: The Checkout API has been updated with new features. 
        For more information, see [Checkout API
        highlights](https://developer.squareup.com/docs/checkout-api#checkout-a
        pi-highlights).
        We recommend that you use the
        new [CreatePaymentLink]($e/Checkout/CreatePaymentLink) 
        endpoint in place of this previously released endpoint.

        Args:
            location_id (string): The ID of the business location to associate
                the checkout with.
            body (CreateCheckoutRequest): An object containing the fields to
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
        _url_path = '/v2/locations/{location_id}/checkouts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True}
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

    def list_payment_links(self,
                           cursor=None,
                           limit=None):
        """Does a GET request to /v2/online-checkout/payment-links.

        Lists all payment links.

        Args:
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint.  Provide this cursor to
                retrieve the next set of results for the original query.  If a
                cursor is not provided, the endpoint returns the first page of
                the results.  For more  information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination).
            limit (int, optional): A limit on the number of results to return
                per page. The limit is advisory and  the implementation might
                return more or less results. If the supplied limit is
                negative, zero, or greater than the maximum limit of 1000, it
                is ignored.  Default value: `100`

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
        _url_path = '/v2/online-checkout/payment-links'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'limit': limit
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

    def create_payment_link(self,
                            body):
        """Does a POST request to /v2/online-checkout/payment-links.

        Creates a Square-hosted checkout page. Applications can share the
        resulting payment link with their buyer to pay for goods and
        services.

        Args:
            body (CreatePaymentLinkRequest): An object containing the fields
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
        _url_path = '/v2/online-checkout/payment-links'
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

    def delete_payment_link(self,
                            id):
        """Does a DELETE request to /v2/online-checkout/payment-links/{id}.

        Deletes a payment link.

        Args:
            id (string): The ID of the payment link to delete.

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
        _url_path = '/v2/online-checkout/payment-links/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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

    def retrieve_payment_link(self,
                              id):
        """Does a GET request to /v2/online-checkout/payment-links/{id}.

        Retrieves a payment link.

        Args:
            id (string): The ID of link to retrieve.

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
        _url_path = '/v2/online-checkout/payment-links/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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

    def update_payment_link(self,
                            id,
                            body):
        """Does a PUT request to /v2/online-checkout/payment-links/{id}.

        Updates a payment link. You can update the `payment_link` fields such
        as 
        `description`, `checkout_options`, and  `pre_populated_data`. 
        You cannot update other fields such as the `order_id`, `version`,
        `URL`, or `timestamp` field.

        Args:
            id (string): The ID of the payment link to update.
            body (UpdatePaymentLinkRequest): An object containing the fields
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
        _url_path = '/v2/online-checkout/payment-links/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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
