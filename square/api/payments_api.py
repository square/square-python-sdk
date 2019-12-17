# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class PaymentsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(PaymentsApi, self).__init__(config, call_back)

    def list_payments(self,
                      begin_time=None,
                      end_time=None,
                      sort_order=None,
                      cursor=None,
                      location_id=None,
                      total=None,
                      last_4=None,
                      card_brand=None):
        """Does a GET request to /v2/payments.

        Retrieves a list of payments taken by the account making the request.
        Max results per page: 100

        Args:
            begin_time (string, optional): Timestamp for the beginning of the
                reporting period, in RFC 3339 format. Inclusive. Default: The
                current time minus one year.
            end_time (string, optional): Timestamp for the end of the
                requested reporting period, in RFC 3339 format.  Default: The
                current time.
            sort_order (string, optional): The order in which results are
                listed. - `ASC` - oldest to newest - `DESC` - newest to oldest
                (default).
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for the original query.  See
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination) for more information.
            location_id (string, optional): ID of location associated with
                payment
            total (long|int, optional): The exact amount in the total_money
                for a `Payment`.
            last_4 (string, optional): The last 4 digits of `Payment` card.
            card_brand (string, optional): The brand of `Payment` card. For
                example, `VISA`

        Returns:
            ListPaymentsResponse: Response from the API. Success

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
            'card_brand': card_brand
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

    def create_payment(self,
                       body):
        """Does a POST request to /v2/payments.

        Charges a payment source, for example, a card 
        represented by customer's card on file or a card nonce. In addition 
        to the payment source, the request must also include the 
        amount to accept for the payment.
        There are several optional parameters that you can include in the
        request. 
        For example, tip money, whether to autocomplete the payment, or a
        reference ID
        to correlate this payment with another system. 
        For more information about these 
        payment options, see [Take
        Payments](https://developer.squareup.com/docs/payments-api/take-payment
        s).
        The `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission is
        required
        to enable application fees.

        Args:
            body (CreatePaymentRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            CreatePaymentResponse: Response from the API. Success

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

    def cancel_payment_by_idempotency_key(self,
                                          body):
        """Does a POST request to /v2/payments/cancel.

        Cancels (voids) a payment identified by the idempotency key that is
        specified in the request. 
        Use this method when status of a CreatePayment request is unknown. 
        For example, after you send a CreatePayment 
        request a network error occurs and you don't get a response. In this
        case, you can direct 
        Square to cancel the payment using this endpoint. In the request, you
        provide the same idempotency 
        key that you provided in your CreatePayment request you want  to
        cancel. After cancelling the 
        payment, you can submit your CreatePayment request again. 
        Note that if no payment with the specified idempotency key is found,
        no action is taken, the end 
        point returns successfully.

        Args:
            body (CancelPaymentByIdempotencyKeyRequest): An object containing
                the fields to POST for the request.  See the corresponding
                object definition for field details.

        Returns:
            CancelPaymentByIdempotencyKeyResponse: Response from the API.
                Success

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

    def get_payment(self,
                    payment_id):
        """Does a GET request to /v2/payments/{payment_id}.

        Retrieves details for a specific Payment.

        Args:
            payment_id (string): Unique ID for the desired `Payment`.

        Returns:
            GetPaymentResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/payments/{payment_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': payment_id
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

    def cancel_payment(self,
                       payment_id):
        """Does a POST request to /v2/payments/{payment_id}/cancel.

        Cancels (voids) a payment. If you set `autocomplete` to false when
        creating a payment, 
        you can cancel the payment using this endpoint. For more information,
        see 
        [Delayed
        Payments](https://developer.squareup.com/docs/payments-api/take-payment
        s#delayed-payments).

        Args:
            payment_id (string): `payment_id` identifying the payment to be
                canceled.

        Returns:
            CancelPaymentResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/payments/{payment_id}/cancel'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': payment_id
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

    def complete_payment(self,
                         payment_id):
        """Does a POST request to /v2/payments/{payment_id}/complete.

        Completes (captures) a payment.
        By default, payments are set to complete immediately after they are
        created. 
        If you set autocomplete to false when creating a payment, you can
        complete (capture) 
        the payment using this endpoint. For more information, see
        [Delayed
        Payments](https://developer.squareup.com/docs/payments-api/take-payment
        s#delayed-payments).

        Args:
            payment_id (string): Unique ID identifying the payment to be
                completed.

        Returns:
            CompletePaymentResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/payments/{payment_id}/complete'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'payment_id': payment_id
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
