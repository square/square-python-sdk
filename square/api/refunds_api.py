# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class RefundsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(RefundsApi, self).__init__(config, call_back)

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
        The maximum results per page is 100.

        Args:
            begin_time (string, optional): The timestamp for the beginning of
                the requested reporting period, in RFC 3339 format.  Default:
                The current time minus one year.
            end_time (string, optional): The timestamp for the end of the
                requested reporting period, in RFC 3339 format.  Default: The
                current time.
            sort_order (string, optional): The order in which results are
                listed: - `ASC` - Oldest to newest. - `DESC` - Newest to
                oldest (default).
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query.  For
                more information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination).
            location_id (string, optional): Limit results to the location
                supplied. By default, results are returned for all locations
                associated with the seller.
            status (string, optional): If provided, only refunds with the
                given status are returned. For a list of refund status values,
                see [PaymentRefund](#type-paymentrefund).  Default: If
                omitted, refunds are returned regardless of their status.
            source_type (string, optional): If provided, only refunds with the
                given source type are returned. - `CARD` - List refunds only
                for payments where `CARD` was specified as the payment source.
                Default: If omitted, refunds are returned regardless of the
                source type.
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

        # Prepare query URL
        _url_path = '/v2/refunds'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'begin_time': begin_time,
            'end_time': end_time,
            'sort_order': sort_order,
            'cursor': cursor,
            'location_id': location_id,
            'status': status,
            'source_type': source_type,
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def refund_payment(self,
                       body):
        """Does a POST request to /v2/refunds.

        Refunds a payment. You can refund the entire payment amount or a 
        portion of it.

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

        # Prepare query URL
        _url_path = '/v2/refunds'
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

    def get_payment_refund(self,
                           refund_id):
        """Does a GET request to /v2/refunds/{refund_id}.

        Retrieves a specific refund using the `refund_id`.

        Args:
            refund_id (string): The unique ID for the desired
                `PaymentRefund`.

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
        _url_path = '/v2/refunds/{refund_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'refund_id': {'value': refund_id, 'encode': True}
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
