# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class TransactionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(TransactionsApi, self).__init__(config, auth_managers)

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
            location_id (string): The ID of the location to list transactions
                for.
            begin_time (string, optional): The beginning of the requested
                reporting period, in RFC 3339 format.  See [Date
                ranges](https://developer.squareup.com/docs/build-basics/workin
                g-with-dates) for details on date inclusivity/exclusivity. 
                Default value: The current time minus one year.
            end_time (string, optional): The end of the requested reporting
                period, in RFC 3339 format.  See [Date
                ranges](https://developer.squareup.com/docs/build-basics/workin
                g-with-dates) for details on date inclusivity/exclusivity. 
                Default value: The current time.
            sort_order (SortOrder, optional): The order in which results are
                listed in the response (`ASC` for oldest first, `DESC` for
                newest first).  Default value: `DESC`
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for your original query.  See [Paginating
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

        # Prepare query URL
        _url_path = '/v2/locations/{location_id}/transactions'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True}
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

    @deprecated()
    def retrieve_transaction(self,
                             location_id,
                             transaction_id):
        """Does a GET request to /v2/locations/{location_id}/transactions/{transaction_id}.

        Retrieves details for a single transaction.

        Args:
            location_id (string): The ID of the transaction's associated
                location.
            transaction_id (string): The ID of the transaction to retrieve.

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
        _url_path = '/v2/locations/{location_id}/transactions/{transaction_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True},
            'transaction_id': {'value': transaction_id, 'encode': True}
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

    @deprecated()
    def capture_transaction(self,
                            location_id,
                            transaction_id):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/capture.

        Captures a transaction that was created with the
        [Charge]($e/Transactions/Charge)
        endpoint with a `delay_capture` value of `true`.
        See [Delayed capture
        transactions](https://developer.squareup.com/docs/payments/transactions
        /overview#delayed-capture)
        for more information.

        Args:
            location_id (string): TODO: type description here.
            transaction_id (string): TODO: type description here.

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
        _url_path = '/v2/locations/{location_id}/transactions/{transaction_id}/capture'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True},
            'transaction_id': {'value': transaction_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers)
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

    @deprecated()
    def void_transaction(self,
                         location_id,
                         transaction_id):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/void.

        Cancels a transaction that was created with the
        [Charge]($e/Transactions/Charge)
        endpoint with a `delay_capture` value of `true`.
        See [Delayed capture
        transactions](https://developer.squareup.com/docs/payments/transactions
        /overview#delayed-capture)
        for more information.

        Args:
            location_id (string): TODO: type description here.
            transaction_id (string): TODO: type description here.

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
        _url_path = '/v2/locations/{location_id}/transactions/{transaction_id}/void'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True},
            'transaction_id': {'value': transaction_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers)
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
