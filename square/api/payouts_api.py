# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class PayoutsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(PayoutsApi, self).__init__(config)

    def list_payouts(self,
                     location_id=None,
                     status=None,
                     begin_time=None,
                     end_time=None,
                     sort_order=None,
                     cursor=None,
                     limit=None):
        """Does a GET request to /v2/payouts.

        Retrieves a list of all payouts for the default location.
        You can filter payouts by location ID, status, time range, and order
        them in ascending or descending order.
        To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

        Args:
            location_id (str, optional): The ID of the location for which to
                list the payouts. By default, payouts are returned for the
                default (main) location associated with the seller.
            status (PayoutStatus, optional): If provided, only payouts with
                the given status are returned.
            begin_time (str, optional): The timestamp for the beginning of the
                payout creation time, in RFC 3339 format. Inclusive. Default:
                The current time minus one year.
            end_time (str, optional): The timestamp for the end of the payout
                creation time, in RFC 3339 format. Default: The current time.
            sort_order (SortOrder, optional): The order in which payouts are
                listed.
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination). If request parameters change
                between requests, subsequent results may contain duplicates or
                missing records.
            limit (int, optional): The maximum number of results to be
                returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default
                value of 100 is also the maximum allowed value. If the
                provided value is greater than 100, it is ignored and the
                default value is used instead. Default: `100`

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
            .path('/v2/payouts')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
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

    def get_payout(self,
                   payout_id):
        """Does a GET request to /v2/payouts/{payout_id}.

        Retrieves details of a specific payout identified by a payout ID.
        To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

        Args:
            payout_id (str): The ID of the payout to retrieve the information
                for.

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
            .path('/v2/payouts/{payout_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('payout_id')
                            .value(payout_id)
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

    def list_payout_entries(self,
                            payout_id,
                            sort_order=None,
                            cursor=None,
                            limit=None):
        """Does a GET request to /v2/payouts/{payout_id}/payout-entries.

        Retrieves a list of all payout entries for a specific payout.
        To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

        Args:
            payout_id (str): The ID of the payout to retrieve the information
                for.
            sort_order (SortOrder, optional): The order in which payout
                entries are listed.
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination). If request parameters change
                between requests, subsequent results may contain duplicates or
                missing records.
            limit (int, optional): The maximum number of results to be
                returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default
                value of 100 is also the maximum allowed value. If the
                provided value is greater than 100, it is ignored and the
                default value is used instead. Default: `100`

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
            .path('/v2/payouts/{payout_id}/payout-entries')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('payout_id')
                            .value(payout_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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
