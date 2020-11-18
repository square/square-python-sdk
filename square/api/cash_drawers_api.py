# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class CashDrawersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(CashDrawersApi, self).__init__(config, call_back)

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
            location_id (string): The ID of the location to query for a list
                of cash drawer shifts.
            sort_order (SortOrder, optional): The order in which cash drawer
                shifts are listed in the response, based on their opened_at
                field. Default value: ASC
            begin_time (string, optional): The inclusive start time of the
                query on opened_at, in ISO 8601 format.
            end_time (string, optional): The exclusive end date of the query
                on opened_at, in ISO 8601 format.
            limit (int, optional): Number of cash drawer shift events in a
                page of results (200 by default, 1000 max).
            cursor (string, optional): Opaque cursor for fetching the next
                page of results.

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
        _url_path = '/v2/cash-drawers/shifts'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_id': location_id,
            'sort_order': sort_order,
            'begin_time': begin_time,
            'end_time': end_time,
            'limit': limit,
            'cursor': cursor
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

    def retrieve_cash_drawer_shift(self,
                                   location_id,
                                   shift_id):
        """Does a GET request to /v2/cash-drawers/shifts/{shift_id}.

        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](#endpoint-CashDrawers-ListCashDrawerShiftEv
        ents) for a list of cash drawer shift events.

        Args:
            location_id (string): The ID of the location to retrieve cash
                drawer shifts from.
            shift_id (string): The shift ID.

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
        _url_path = '/v2/cash-drawers/shifts/{shift_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'shift_id': {'value': shift_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_id': location_id
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

    def list_cash_drawer_shift_events(self,
                                      location_id,
                                      shift_id,
                                      limit=None,
                                      cursor=None):
        """Does a GET request to /v2/cash-drawers/shifts/{shift_id}/events.

        Provides a paginated list of events for a single cash drawer shift.

        Args:
            location_id (string): The ID of the location to list cash drawer
                shifts for.
            shift_id (string): The shift ID.
            limit (int, optional): Number of resources to be returned in a
                page of results (200 by default, 1000 max).
            cursor (string, optional): Opaque cursor for fetching the next
                page of results.

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
        _url_path = '/v2/cash-drawers/shifts/{shift_id}/events'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'shift_id': {'value': shift_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_id': location_id,
            'limit': limit,
            'cursor': cursor
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
