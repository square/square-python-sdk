# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class ReportingApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(ReportingApi, self).__init__(config, call_back)

    @deprecated()
    def list_additional_recipient_receivable_refunds(self,
                                                     location_id,
                                                     begin_time=None,
                                                     end_time=None,
                                                     sort_order=None,
                                                     cursor=None):
        """Does a GET request to /v2/locations/{location_id}/additional-recipient-receivable-refunds.

        Returns a list of refunded transactions (across all possible
        originating locations) relating to monies
        credited to the provided location ID by another Square account using
        the `additional_recipients` field in a transaction.
        Max results per [page](#paginatingresults): 50

        Args:
            location_id (string): The ID of the location to list
                AdditionalRecipientReceivableRefunds for.
            begin_time (string, optional): The beginning of the requested
                reporting period, in RFC 3339 format.  See [Date
                ranges](#dateranges) for details on date
                inclusivity/exclusivity.  Default value: The current time
                minus one year.
            end_time (string, optional): The end of the requested reporting
                period, in RFC 3339 format.  See [Date ranges](#dateranges)
                for details on date inclusivity/exclusivity.  Default value:
                The current time.
            sort_order (SortOrder, optional): The order in which results are
                listed in the response (`ASC` for oldest first, `DESC` for
                newest first).  Default value: `DESC`
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for your original query.  See [Paginating
                results](#paginatingresults) for more information.

        Returns:
            ListAdditionalRecipientReceivableRefundsResponse: Response from
                the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations/{location_id}/additional-recipient-receivable-refunds'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'begin_time': begin_time,
            'end_time': end_time,
            'sort_order': sort_order,
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

    @deprecated()
    def list_additional_recipient_receivables(self,
                                              location_id,
                                              begin_time=None,
                                              end_time=None,
                                              sort_order=None,
                                              cursor=None):
        """Does a GET request to /v2/locations/{location_id}/additional-recipient-receivables.

        Returns a list of receivables (across all possible sending locations)
        representing monies credited
        to the provided location ID by another Square account using the
        `additional_recipients` field in a transaction.
        Max results per [page](#paginatingresults): 50

        Args:
            location_id (string): The ID of the location to list
                AdditionalRecipientReceivables for.
            begin_time (string, optional): The beginning of the requested
                reporting period, in RFC 3339 format.  See [Date
                ranges](#dateranges) for details on date
                inclusivity/exclusivity.  Default value: The current time
                minus one year.
            end_time (string, optional): The end of the requested reporting
                period, in RFC 3339 format.  See [Date ranges](#dateranges)
                for details on date inclusivity/exclusivity.  Default value:
                The current time.
            sort_order (SortOrder, optional): The order in which results are
                listed in the response (`ASC` for oldest first, `DESC` for
                newest first).  Default value: `DESC`
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for your original query.  See [Paginating
                results](#paginatingresults) for more information.

        Returns:
            ListAdditionalRecipientReceivablesResponse: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations/{location_id}/additional-recipient-receivables'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'begin_time': begin_time,
            'end_time': end_time,
            'sort_order': sort_order,
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
