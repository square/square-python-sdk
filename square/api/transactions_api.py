# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class TransactionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(TransactionsApi, self).__init__(config, call_back)

    @deprecated()
    def list_refunds(self,
                     location_id,
                     begin_time=None,
                     end_time=None,
                     sort_order=None,
                     cursor=None):
        """Does a GET request to /v2/locations/{location_id}/refunds.

        Lists refunds for one of a business's locations.
        In addition to full or partial tender refunds processed through Square
        APIs,
        refunds may result from itemized returns or exchanges through
        Square's
        Point of Sale applications.
        Refunds with a `status` of `PENDING` are not currently included in
        this
        endpoint's response.
        Max results per [page](#paginatingresults): 50

        Args:
            location_id (string): The ID of the location to list refunds for.
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
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations/{location_id}/refunds'
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
        Max results per [page](#paginatingresults): 50

        Args:
            location_id (string): The ID of the location to list transactions
                for.
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
    def charge(self,
               location_id,
               body):
        """Does a POST request to /v2/locations/{location_id}/transactions.

        Charges a card represented by a card nonce or a customer's card on
        file.
        Your request to this endpoint must include _either_:
        - A value for the `card_nonce` parameter (to charge a card nonce
        generated
        with the `SqPaymentForm`)
        - Values for the `customer_card_id` and `customer_id` parameters (to
        charge
        a customer's card on file)
        In order for an eCommerce payment to potentially qualify for
        [Square chargeback
        protection](https://squareup.com/help/article/5394), you
        _must_ provide values for the following parameters in your request:
        - `buyer_email_address`
        - At least one of `billing_address` or `shipping_address`
        When this response is returned, the amount of Square's processing fee
        might not yet be
        calculated. To obtain the processing fee, wait about ten seconds and
        call
        [RetrieveTransaction](#endpoint-retrievetransaction). See the
        `processing_fee_money`
        field of each [Tender included](#type-tender) in the transaction.

        Args:
            location_id (string): The ID of the location to associate the
                created transaction with.
            body (ChargeRequest): An object containing the fields to POST for
                the request.  See the corresponding object definition for
                field details.

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
    def capture_transaction(self,
                            location_id,
                            transaction_id):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/capture.

        Captures a transaction that was created with the
        [Charge](#endpoint-charge)
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
    def create_refund(self,
                      location_id,
                      transaction_id,
                      body):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/refund.

        Initiates a refund for a previously charged tender.
        You must issue a refund within 120 days of the associated payment.
        See
        [this article](https://squareup.com/help/us/en/article/5060) for more
        information
        on refund behavior.
        NOTE: Card-present transactions with Interac credit cards **cannot be
        refunded using the Connect API**. Interac transactions must refunded
        in-person (e.g., dipping the card using POS app).

        Args:
            location_id (string): The ID of the original transaction's
                associated location.
            transaction_id (string): The ID of the original transaction that
                includes the tender to refund.
            body (CreateRefundRequest): An object containing the fields to
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
        _url_path = '/v2/locations/{location_id}/transactions/{transaction_id}/refund'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True},
            'transaction_id': {'value': transaction_id, 'encode': True}
        })
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

    @deprecated()
    def void_transaction(self,
                         location_id,
                         transaction_id):
        """Does a POST request to /v2/locations/{location_id}/transactions/{transaction_id}/void.

        Cancels a transaction that was created with the
        [Charge](#endpoint-charge)
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
