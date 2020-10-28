# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class OrdersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(OrdersApi, self).__init__(config, call_back)

    def create_order(self,
                     body):
        """Does a POST request to /v2/orders.

        Creates a new [Order](#type-order) which can include information on
        products for
        purchase and settings to apply to the purchase.
        To pay for a created order, please refer to the [Pay for
        Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders)
                guide.
        You can modify open orders using the
        [UpdateOrder](#endpoint-orders-updateorder) endpoint.

        Args:
            body (CreateOrderRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.

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
        _url_path = '/v2/orders'
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

    def batch_retrieve_orders(self,
                              body):
        """Does a POST request to /v2/orders/batch-retrieve.

        Retrieves a set of [Order](#type-order)s by their IDs.
        If a given Order ID does not exist, the ID is ignored instead of
        generating an error.

        Args:
            body (BatchRetrieveOrdersRequest): An object containing the fields
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
        _url_path = '/v2/orders/batch-retrieve'
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

    def calculate_order(self,
                        body):
        """Does a POST request to /v2/orders/calculate.

        Calculates an [Order](#type-order).

        Args:
            body (CalculateOrderRequest): An object containing the fields to
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
        _url_path = '/v2/orders/calculate'
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

    def search_orders(self,
                      body):
        """Does a POST request to /v2/orders/search.

        Search all orders for one or more locations. Orders include all
        sales,
        returns, and exchanges regardless of how or when they entered the
        Square
        Ecosystem (e.g. Point of Sale, Invoices, Connect APIs, etc).
        SearchOrders requests need to specify which locations to search and
        define a
        [`SearchOrdersQuery`](#type-searchordersquery) object which controls
        how to sort or filter the results. Your SearchOrdersQuery can:
          Set filter criteria.
          Set sort order.
          Determine whether to return results as complete Order objects, or
          as
        [OrderEntry](#type-orderentry) objects.
        Note that details for orders processed with Square Point of Sale while
        in
        offline mode may not be transmitted to Square for up to 72 hours.
        Offline
        orders have a `created_at` value that reflects the time the order was
        created,
        not the time it was subsequently transmitted to Square.

        Args:
            body (SearchOrdersRequest): An object containing the fields to
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
        _url_path = '/v2/orders/search'
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

    def retrieve_order(self,
                       order_id):
        """Does a GET request to /v2/orders/{order_id}.

        Retrieves an [Order](#type-order) by ID.

        Args:
            order_id (string): The ID of the order to retrieve.

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
        _url_path = '/v2/orders/{order_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'order_id': {'value': order_id, 'encode': True}
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

    def update_order(self,
                     order_id,
                     body):
        """Does a PUT request to /v2/orders/{order_id}.

        Updates an open [Order](#type-order) by adding, replacing, or
        deleting
        fields. Orders with a `COMPLETED` or `CANCELED` state cannot be
        updated.
        An UpdateOrder request requires the following:
        - The `order_id` in the endpoint path, identifying the order to
        update.
        - The latest `version` of the order to update.
        - The [sparse
        order](https://developer.squareup.com/docs/orders-api/manage-orders#spa
        rse-order-objects)
        containing only the fields to update and the version the update is
        being applied to.
        - If deleting fields, the [dot notation
        paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-
        dot-notation)
        identifying fields to clear.
        To pay for an order, please refer to the [Pay for
        Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders)
        guide.

        Args:
            order_id (string): The ID of the order to update.
            body (UpdateOrderRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.

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
        _url_path = '/v2/orders/{order_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'order_id': {'value': order_id, 'encode': True}
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

    def pay_order(self,
                  order_id,
                  body):
        """Does a POST request to /v2/orders/{order_id}/pay.

        Pay for an [order](#type-order) using one or more approved
        [payments](#type-payment),
        or settle an order with a total of `0`.
        The total of the `payment_ids` listed in the request must be equal to
        the order
        total. Orders with a total amount of `0` can be marked as paid by
        specifying an empty
        array of `payment_ids` in the request.
        To be used with PayOrder, a payment must:
        - Reference the order by specifying the `order_id` when [creating the
        payment](#endpoint-payments-createpayment).
        Any approved payments that reference the same `order_id` not specified
        in the
        `payment_ids` will be canceled.
        - Be approved with [delayed
        capture](https://developer.squareup.com/docs/payments-api/take-payments
        #delayed-capture).
        Using a delayed capture payment with PayOrder will complete the
        approved payment.

        Args:
            order_id (string): The ID of the order being paid.
            body (PayOrderRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.

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
        _url_path = '/v2/orders/{order_id}/pay'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'order_id': {'value': order_id, 'encode': True}
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
