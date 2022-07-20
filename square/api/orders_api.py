# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class OrdersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(OrdersApi, self).__init__(config, auth_managers)

    def create_order(self,
                     body):
        """Does a POST request to /v2/orders.

        Creates a new [order]($m/Order) that can include information about
        products for
        purchase and settings to apply to the purchase.
        To pay for a created order, see 
        [Pay for
        Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).
                You can modify open orders using the
        [UpdateOrder]($e/Orders/UpdateOrder) endpoint.

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

    def batch_retrieve_orders(self,
                              body):
        """Does a POST request to /v2/orders/batch-retrieve.

        Retrieves a set of [orders]($m/Order) by their IDs.
        If a given order ID does not exist, the ID is ignored instead of
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

    def calculate_order(self,
                        body):
        """Does a POST request to /v2/orders/calculate.

        Enables applications to preview order pricing without creating an
        order.

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

    def clone_order(self,
                    body):
        """Does a POST request to /v2/orders/clone.

        Creates a new order, in the `DRAFT` state, by duplicating an existing
        order. The newly created order has 
        only the core fields (such as line items, taxes, and discounts) copied
        from the original order.

        Args:
            body (CloneOrderRequest): An object containing the fields to POST
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
        _url_path = '/v2/orders/clone'
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

    def search_orders(self,
                      body):
        """Does a POST request to /v2/orders/search.

        Search all orders for one or more locations. Orders include all
        sales,
        returns, and exchanges regardless of how or when they entered the
        Square
        ecosystem (such as Point of Sale, Invoices, and Connect APIs).
        `SearchOrders` requests need to specify which locations to search and
        define a
        [SearchOrdersQuery]($m/SearchOrdersQuery) object that controls
        how to sort or filter the results. Your `SearchOrdersQuery` can:
          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete `Order` objects or
          as
        [OrderEntry]($m/OrderEntry) objects.
        Note that details for orders processed with Square Point of Sale while
        in
        offline mode might not be transmitted to Square for up to 72 hours.
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

    def retrieve_order(self,
                       order_id):
        """Does a GET request to /v2/orders/{order_id}.

        Retrieves an [Order]($m/Order) by ID.

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

    def update_order(self,
                     order_id,
                     body):
        """Does a PUT request to /v2/orders/{order_id}.

        Updates an open [order]($m/Order) by adding, replacing, or deleting
        fields. Orders with a `COMPLETED` or `CANCELED` state cannot be
        updated.
        An `UpdateOrder` request requires the following:
        - The `order_id` in the endpoint path, identifying the order to
        update.
        - The latest `version` of the order to update.
        - The [sparse
        order](https://developer.squareup.com/docs/orders-api/manage-orders/upd
        ate-orders#sparse-order-objects)
        containing only the fields to update and the version to which the
        update is
        being applied.
        - If deleting fields, the [dot notation
        paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-
        dot-notation)
        identifying the fields to clear.
        To pay for an order, see 
        [Pay for
        Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).
        
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

    def pay_order(self,
                  order_id,
                  body):
        """Does a POST request to /v2/orders/{order_id}/pay.

        Pay for an [order]($m/Order) using one or more approved
        [payments]($m/Payment)
        or settle an order with a total of `0`.
        The total of the `payment_ids` listed in the request must be equal to
        the order
        total. Orders with a total amount of `0` can be marked as paid by
        specifying an empty
        array of `payment_ids` in the request.
        To be used with `PayOrder`, a payment must:
        - Reference the order by specifying the `order_id` when [creating the
        payment]($e/Payments/CreatePayment).
        Any approved payments that reference the same `order_id` not specified
        in the
        `payment_ids` is canceled.
        - Be approved with [delayed
        capture](https://developer.squareup.com/docs/payments-api/take-payments
        /card-payments/delayed-capture).
        Using a delayed capture payment with `PayOrder` completes the approved
        payment.

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
