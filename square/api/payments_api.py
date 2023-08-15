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


class PaymentsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(PaymentsApi, self).__init__(config)

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
            begin_time (str, optional): Indicates the start of the time range
                to retrieve payments for, in RFC 3339 format.   The range is
                determined using the `created_at` field for each Payment.
                Inclusive. Default: The current time minus one year.
            end_time (str, optional): Indicates the end of the time range to
                retrieve payments for, in RFC 3339 format.  The  range is
                determined using the `created_at` field for each Payment. 
                Default: The current time.
            sort_order (str, optional): The order in which results are listed
                by `Payment.created_at`: - `ASC` - Oldest to newest. - `DESC`
                - Newest to oldest (default).
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            location_id (str, optional): Limit results to the location
                supplied. By default, results are returned for the default
                (main) location associated with the seller.
            total (long|int, optional): The exact amount in the `total_money`
                for a payment.
            last_4 (str, optional): The last four digits of a payment card.
            card_brand (str, optional): The brand of the payment card (for
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/payments')
            .http_method(HttpMethodEnum.GET)
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
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('total')
                         .value(total))
            .query_param(Parameter()
                         .key('last_4')
                         .value(last_4))
            .query_param(Parameter()
                         .key('card_brand')
                         .value(card_brand))
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/payments')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/payments/cancel')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def get_payment(self,
                    payment_id):
        """Does a GET request to /v2/payments/{payment_id}.

        Retrieves details for a specific payment.

        Args:
            payment_id (str): A unique ID for the desired payment.

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
            .path('/v2/payments/{payment_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('payment_id')
                            .value(payment_id)
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

    def update_payment(self,
                       payment_id,
                       body):
        """Does a PUT request to /v2/payments/{payment_id}.

        Updates a payment with the APPROVED status.
        You can update the `amount_money` and `tip_money` using this
        endpoint.

        Args:
            payment_id (str): The ID of the payment to update.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/payments/{payment_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('payment_id')
                            .value(payment_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def cancel_payment(self,
                       payment_id):
        """Does a POST request to /v2/payments/{payment_id}/cancel.

        Cancels (voids) a payment. You can use this endpoint to cancel a
        payment with 
        the APPROVED `status`.

        Args:
            payment_id (str): The ID of the payment to cancel.

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
            .path('/v2/payments/{payment_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('payment_id')
                            .value(payment_id)
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
            payment_id (str): The unique ID identifying the payment to be
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/payments/{payment_id}/complete')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('payment_id')
                            .value(payment_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()
