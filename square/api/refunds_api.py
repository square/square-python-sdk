# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class RefundsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(RefundsApi, self).__init__(config)

    def list_payment_refunds(self,
                             begin_time=None,
                             end_time=None,
                             sort_order=None,
                             cursor=None,
                             location_id=None,
                             status=None,
                             source_type=None,
                             limit=None):
        """Does a GET request to /v2/refunds.

        Retrieves a list of refunds for the account making the request.
        Results are eventually consistent, and new refunds or changes to
        refunds might take several
        seconds to appear.
        The maximum results per page is 100.

        Args:
            begin_time (str, optional): Indicates the start of the time range
                to retrieve each `PaymentRefund` for, in RFC 3339  format. 
                The range is determined using the `created_at` field for each
                `PaymentRefund`.   Default: The current time minus one year.
            end_time (str, optional): Indicates the end of the time range to
                retrieve each `PaymentRefund` for, in RFC 3339  format.  The
                range is determined using the `created_at` field for each
                `PaymentRefund`.  Default: The current time.
            sort_order (str, optional): The order in which results are listed
                by `PaymentRefund.created_at`: - `ASC` - Oldest to newest. -
                `DESC` - Newest to oldest (default).
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            location_id (str, optional): Limit results to the location
                supplied. By default, results are returned for all locations
                associated with the seller.
            status (str, optional): If provided, only refunds with the given
                status are returned. For a list of refund status values, see
                [PaymentRefund](entity:PaymentRefund).  Default: If omitted,
                refunds are returned regardless of their status.
            source_type (str, optional): If provided, only returns refunds
                whose payments have the indicated source type. Current values
                include `CARD`, `BANK_ACCOUNT`, `WALLET`, `CASH`, and
                `EXTERNAL`. For information about these payment source types,
                see [Take
                Payments](https://developer.squareup.com/docs/payments-api/take
                -payments).  Default: If omitted, refunds are returned
                regardless of the source type.
            limit (int, optional): The maximum number of results to be
                returned in a single page.  It is possible to receive fewer
                results than the specified limit on a given page.  If the
                supplied value is greater than 100, no more than 100 results
                are returned.  Default: 100

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
            .path('/v2/refunds')
            .http_method(HttpMethodEnum.GET)
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
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('source_type')
                         .value(source_type))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
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

    def refund_payment(self,
                       body):
        """Does a POST request to /v2/refunds.

        Refunds a payment. You can refund the entire payment amount or a
        portion of it. You can use this endpoint to refund a card payment or
        record a 
        refund of a cash or external payment. For more information, see
        [Refund
        Payment](https://developer.squareup.com/docs/payments-api/refund-paymen
        ts).

        Args:
            body (RefundPaymentRequest): An object containing the fields to
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
            .path('/v2/refunds')
            .http_method(HttpMethodEnum.POST)
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

    def get_payment_refund(self,
                           refund_id):
        """Does a GET request to /v2/refunds/{refund_id}.

        Retrieves a specific refund using the `refund_id`.

        Args:
            refund_id (str): The unique ID for the desired `PaymentRefund`.

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
            .path('/v2/refunds/{refund_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('refund_id')
                            .value(refund_id)
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
