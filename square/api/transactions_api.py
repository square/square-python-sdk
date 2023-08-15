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
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or


class TransactionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(TransactionsApi, self).__init__(config)

    @deprecated()
    def list_transactions(self,
                          location_id,
                          begin_time=None,
                          end_time=None,
                          sort_order=None,
                          cursor=None):
        """Does a GET request to /v2/locations/{location_id}/transactions.

        Lists transactions for a particular location.
        Transactions include payment information from sales and exchanges and
        refund
        information from returns and exchanges.
        Max results per
        [page](https://developer.squareup.com/docs/working-with-apis/pagination
        ): 50

        Args:
            location_id (str): The ID of the location to list transactions
                for.
            begin_time (str, optional): The beginning of the requested
                reporting period, in RFC 3339 format.  See [Date
                ranges](https://developer.squareup.com/docs/build-basics/workin
                g-with-dates) for details on date inclusivity/exclusivity. 
                Default value: The current time minus one year.
            end_time (str, optional): The end of the requested reporting
                period, in RFC 3339 format.  See [Date
                ranges](https://developer.squareup.com/docs/build-basics/workin
                g-with-dates) for details on date inclusivity/exclusivity. 
                Default value: The current time.
            sort_order (SortOrder, optional): The order in which results are
                listed in the response (`ASC` for oldest first, `DESC` for
                newest first).  Default value: `DESC`
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this to retrieve the next set
                of results for your original query.  See [Paginating
                results](https://developer.squareup.com/docs/working-with-apis/
                pagination) for more information.

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
            .path('/v2/locations/{location_id}/transactions')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('begin_time')
                         .value(begin_time))
            .query_param(Parameter()
                         .key('end_time')
                         .value(end_time))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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
    def retrieve_transaction(self,
                             location_id,
                             transaction_id):
        """Does a GET request to /v2/locations/{location_id}/transactions/{transaction_id}.

        Retrieves details for a single transaction.

        Args:
            location_id (str): The ID of the transaction's associated
                location.
            transaction_id (str): The ID of the transaction to retrieve.

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
            .path('/v2/locations/{location_id}/transactions/{transaction_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('transaction_id')
                            .value(transaction_id)
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
    def capture_transaction(self,
                            location_id,
                            transaction_id):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/capture.

        Captures a transaction that was created with the
        [Charge](api-endpoint:Transactions-Charge)
        endpoint with a `delay_capture` value of `true`.
        See [Delayed capture
        transactions](https://developer.squareup.com/docs/payments/transactions
        /overview#delayed-capture)
        for more information.

        Args:
            location_id (str): TODO: type description here.
            transaction_id (str): TODO: type description here.

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
            .path('/v2/locations/{location_id}/transactions/{transaction_id}/capture')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('transaction_id')
                            .value(transaction_id)
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
    def void_transaction(self,
                         location_id,
                         transaction_id):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/void.

        Cancels a transaction that was created with the
        [Charge](api-endpoint:Transactions-Charge)
        endpoint with a `delay_capture` value of `true`.
        See [Delayed capture
        transactions](https://developer.squareup.com/docs/payments/transactions
        /overview#delayed-capture)
        for more information.

        Args:
            location_id (str): TODO: type description here.
            transaction_id (str): TODO: type description here.

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
            .path('/v2/locations/{location_id}/transactions/{transaction_id}/void')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('transaction_id')
                            .value(transaction_id)
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
