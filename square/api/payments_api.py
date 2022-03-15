# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class PaymentsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(PaymentsApi, self).__init__(config, auth_managers)

    def list_payments(self,
                      begin_time=None,
                      end_time=None,
                      sort_order=None,
                      cursor=None,
                      location_id=None,
                      total=None,
                      last_4=None,
                      card_brand=None,
                      limit=None):
        """Does a GET request to /v2/payments.

        Retrieves a list of payments taken by the account making the request.
        Results are eventually consistent, and new payments or changes to
        payments might take several
        seconds to appear.
        The maximum results per page is 100.

        Args:
            begin_time (string, optional): The timestamp for the beginning of
                the reporting period, in RFC 3339 format. Inclusive. Default:
                The current time minus one year.
            end_time (string, optional): The timestamp for the end of the
                reporting period, in RFC 3339 format.  Default: The current
                time.
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
                supplied. By default, results are returned for the default
                (main) location associated with the seller.
            total (long|int, optional): The exact amount in the `total_money`
                for a payment.
            last_4 (string, optional): The last four digits of a payment
                card.
            card_brand (string, optional): The brand of the payment card (for
                example, VISA).
            limit (int, optional): The maximum number of results to be
                returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page.  The default
                value of 100 is also the maximum allowed value. If the
                provided value is  greater than 100, it is ignored and the
                default value is used instead.  Default: `100`

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
        _url_path = '/v2/payments'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'begin_time': begin_time,
            'end_time': end_time,
            'sort_order': sort_order,
            'cursor': cursor,
            'location_id': location_id,
            'total': total,
            'last_4': last_4,
            'card_brand': card_brand,
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

    def create_payment(self,
                       body):
        """Does a POST request to /v2/payments.

        Creates a payment using the provided source. You can use this endpoint
                to charge a card (credit/debit card or    
        Square gift card) or record a payment that the seller received outside
        of Square 
        (cash payment from a buyer or a payment that an external entity 
        processed on behalf of the seller).
        The endpoint creates a 
        `Payment` object and returns it in the response.

        Args:
            body (CreatePaymentRequest): An object containing the fields to
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
        _url_path = '/v2/payments'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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

    def cancel_payment_by_idempotency_key(self,
                                          body):
        """Does a POST request to /v2/payments/cancel.

        Cancels (voids) a payment identified by the idempotency key that is
        specified in the
        request.
        Use this method when the status of a `CreatePayment` request is
        unknown (for example, after you send a
        `CreatePayment` request, a network error occurs and you do not get a
        response). In this case, you can
        direct Square to cancel the payment using this endpoint. In the
        request, you provide the same
        idempotency key that you provided in your `CreatePayment` request that
        you want to cancel. After
        canceling the payment, you can submit your `CreatePayment` request
        again.
        Note that if no payment with the specified idempotency key is found,
        no action is taken and the endpoint
        returns successfully.

        Args:
            body (CancelPaymentByIdempotencyKeyRequest): An object containing
                the fields to POST for the request.  See the corresponding
                object definition for field details.

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
        _url_path = '/v2/payments/cancel'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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

    def get_payment(self,
                    payment_id):
        """Does a GET request to /v2/payments/{payment_id}.

        Retrieves details for a specific payment.

        Args:
            payment_id (string): A unique ID for the desired payment.

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
        _url_path = '/v2/payments/{payment_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': {'value': payment_id, 'encode': True}
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

    def update_payment(self,
                       payment_id,
                       body):
        """Does a PUT request to /v2/payments/{payment_id}.

        Updates a payment with the APPROVED status.
        You can update the `amount_money` and `tip_money` using this
        endpoint.

        Args:
            payment_id (string): The ID of the payment to update.
            body (UpdatePaymentRequest): An object containing the fields to
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
        _url_path = '/v2/payments/{payment_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': {'value': payment_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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

    def cancel_payment(self,
                       payment_id):
        """Does a POST request to /v2/payments/{payment_id}/cancel.

        Cancels (voids) a payment. You can use this endpoint to cancel a
        payment with 
        the APPROVED `status`.

        Args:
            payment_id (string): The ID of the payment to cancel.

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
        _url_path = '/v2/payments/{payment_id}/cancel'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': {'value': payment_id, 'encode': True}
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

    def complete_payment(self,
                         payment_id,
                         body):
        """Does a POST request to /v2/payments/{payment_id}/complete.

        Completes (captures) a payment.
        By default, payments are set to complete immediately after they are
        created.
        You can use this endpoint to complete a payment with the APPROVED
        `status`.

        Args:
            payment_id (string): The unique ID identifying the payment to be
                completed.
            body (CompletePaymentRequest): An object containing the fields to
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
        _url_path = '/v2/payments/{payment_id}/complete'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': {'value': payment_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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
