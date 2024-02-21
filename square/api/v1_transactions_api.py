# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class V1TransactionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(V1TransactionsApi, self).__init__(config)

    @deprecated()
    def v1_list_orders(self,
                       location_id,
                       order=None,
                       limit=None,
                       batch_token=None):
        """Does a GET request to /v1/{location_id}/orders.

        Provides summary information for a merchant's online store orders.

        Args:
            location_id (str): The ID of the location to list online store
                orders for.
            order (SortOrder, optional): The order in which payments are
                listed in the response.
            limit (int, optional): The maximum number of payments to return in
                a single response. This value cannot exceed 200.
            batch_token (str, optional): A pagination cursor to retrieve the
                next set of results for your original query to the endpoint.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v1/{location_id}/orders')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('order')
                         .value(order))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('batch_token')
                         .value(batch_token))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    @deprecated()
    def v1_retrieve_order(self,
                          location_id,
                          order_id):
        """Does a GET request to /v1/{location_id}/orders/{order_id}.

        Provides comprehensive information for a single online store order,
        including the order's history.

        Args:
            location_id (str): The ID of the order's associated location.
            order_id (str): The order's Square-issued ID. You obtain this
                value from Order objects returned by the List Orders endpoint

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v1/{location_id}/orders/{order_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('order_id')
                            .value(order_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    @deprecated()
    def v1_update_order(self,
                        location_id,
                        order_id,
                        body):
        """Does a PUT request to /v1/{location_id}/orders/{order_id}.

        Updates the details of an online store order. Every update you perform
        on an order corresponds to one of three actions:

        Args:
            location_id (str): The ID of the order's associated location.
            order_id (str): The order's Square-issued ID. You obtain this
                value from Order objects returned by the List Orders endpoint
            body (V1UpdateOrderRequest): An object containing the fields to
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v1/{location_id}/orders/{order_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('order_id')
                            .value(order_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()
