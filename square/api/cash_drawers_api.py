# -*- coding: utf-8 -*-

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


class CashDrawersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(CashDrawersApi, self).__init__(config)

    def list_cash_drawer_shifts(self,
                                location_id,
                                sort_order=None,
                                begin_time=None,
                                end_time=None,
                                limit=None,
                                cursor=None):
        """Does a GET request to /v2/cash-drawers/shifts.

        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Args:
            location_id (str): The ID of the location to query for a list of
                cash drawer shifts.
            sort_order (SortOrder, optional): The order in which cash drawer
                shifts are listed in the response, based on their opened_at
                field. Default value: ASC
            begin_time (str, optional): The inclusive start time of the query
                on opened_at, in ISO 8601 format.
            end_time (str, optional): The exclusive end date of the query on
                opened_at, in ISO 8601 format.
            limit (int, optional): Number of cash drawer shift events in a
                page of results (200 by default, 1000 max).
            cursor (str, optional): Opaque cursor for fetching the next page
                of results.

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
            .path('/v2/cash-drawers/shifts')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
            .query_param(Parameter()
                         .key('begin_time')
                         .value(begin_time))
            .query_param(Parameter()
                         .key('end_time')
                         .value(end_time))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
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

    def retrieve_cash_drawer_shift(self,
                                   location_id,
                                   shift_id):
        """Does a GET request to /v2/cash-drawers/shifts/{shift_id}.

        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents]($e/CashDrawers/ListCashDrawerShiftEvents)
        for a list of cash drawer shift events.

        Args:
            location_id (str): The ID of the location to retrieve cash drawer
                shifts from.
            shift_id (str): The shift ID.

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
            .path('/v2/cash-drawers/shifts/{shift_id}')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .template_param(Parameter()
                            .key('shift_id')
                            .value(shift_id)
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

    def list_cash_drawer_shift_events(self,
                                      location_id,
                                      shift_id,
                                      limit=None,
                                      cursor=None):
        """Does a GET request to /v2/cash-drawers/shifts/{shift_id}/events.

        Provides a paginated list of events for a single cash drawer shift.

        Args:
            location_id (str): The ID of the location to list cash drawer
                shifts for.
            shift_id (str): The shift ID.
            limit (int, optional): Number of resources to be returned in a
                page of results (200 by default, 1000 max).
            cursor (str, optional): Opaque cursor for fetching the next page
                of results.

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
            .path('/v2/cash-drawers/shifts/{shift_id}/events')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .template_param(Parameter()
                            .key('shift_id')
                            .value(shift_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
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
