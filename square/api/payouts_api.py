# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class PayoutsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(PayoutsApi, self).__init__(config, auth_managers)

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
            location_id (string, optional): The ID of the location for which
                to list the payouts.  By default, payouts are returned for the
                default (main) location associated with the seller.
            status (PayoutStatus, optional): If provided, only payouts with
                the given status are returned.
            begin_time (string, optional): The timestamp for the beginning of
                the payout creation time, in RFC 3339 format. Inclusive.
                Default: The current time minus one year.
            end_time (string, optional): The timestamp for the end of the
                payout creation time, in RFC 3339 format. Default: The current
                time.
            sort_order (SortOrder, optional): The order in which payouts are
                listed.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination). If request parameters change between requests,
                subsequent results may contain duplicates or missing records.
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

        # Prepare query URL
        _url_path = '/v2/payouts'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_id': location_id,
            'status': status,
            'begin_time': begin_time,
            'end_time': end_time,
            'sort_order': sort_order,
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

    def get_payout(self,
                   payout_id):
        """Does a GET request to /v2/payouts/{payout_id}.

        Retrieves details of a specific payout identified by a payout ID. 
        To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

        Args:
            payout_id (string): The ID of the payout to retrieve the
                information for.

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
        _url_path = '/v2/payouts/{payout_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payout_id': {'value': payout_id, 'encode': True}
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

    def list_payout_entries(self,
                            payout_id,
                            sort_order=None,
                            cursor=None,
                            limit=None):
        """Does a GET request to /v2/payouts/{payout_id}/payout-entries.

        Retrieves a list of all payout entries for a specific payout.
        To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

        Args:
            payout_id (string): The ID of the payout to retrieve the
                information for.
            sort_order (SortOrder, optional): The order in which payout
                entries are listed.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination). If request parameters change between requests,
                subsequent results may contain duplicates or missing records.
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

        # Prepare query URL
        _url_path = '/v2/payouts/{payout_id}/payout-entries'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payout_id': {'value': payout_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'sort_order': sort_order,
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
