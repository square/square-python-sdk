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


class TerminalApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(TerminalApi, self).__init__(config)

    def create_terminal_action(self,
                               body):
        """Does a POST request to /v2/terminals/actions.

        Creates a Terminal action request and sends it to the specified
        device.

        Args:
            body (CreateTerminalActionRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/terminals/actions')
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

    def search_terminal_actions(self,
                                body):
        """Does a POST request to /v2/terminals/actions/search.

        Retrieves a filtered list of Terminal action requests created by the
        account making the request. Terminal action requests are available for
        30 days.

        Args:
            body (SearchTerminalActionsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/terminals/actions/search')
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

    def get_terminal_action(self,
                            action_id):
        """Does a GET request to /v2/terminals/actions/{action_id}.

        Retrieves a Terminal action request by `action_id`. Terminal action
        requests are available for 30 days.

        Args:
            action_id (str): Unique ID for the desired `TerminalAction`.

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
            .path('/v2/terminals/actions/{action_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('action_id')
                            .value(action_id)
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

    def cancel_terminal_action(self,
                               action_id):
        """Does a POST request to /v2/terminals/actions/{action_id}/cancel.

        Cancels a Terminal action request if the status of the request permits
        it.

        Args:
            action_id (str): Unique ID for the desired `TerminalAction`.

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
            .path('/v2/terminals/actions/{action_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('action_id')
                            .value(action_id)
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

    def dismiss_terminal_action(self,
                                action_id):
        """Does a POST request to /v2/terminals/actions/{action_id}/dismiss.

        Dismisses a Terminal action request if the status and type of the
        request permits it.
        See [Link and Dismiss
        Actions](https://developer.squareup.com/docs/terminal-api/advanced-feat
        ures/custom-workflows/link-and-dismiss-actions) for more details.

        Args:
            action_id (str): Unique ID for the `TerminalAction` associated
                with the action to be dismissed.

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
            .path('/v2/terminals/actions/{action_id}/dismiss')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('action_id')
                            .value(action_id)
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

    def create_terminal_checkout(self,
                                 body):
        """Does a POST request to /v2/terminals/checkouts.

        Creates a Terminal checkout request and sends it to the specified
        device to take a payment
        for the requested amount.

        Args:
            body (CreateTerminalCheckoutRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/terminals/checkouts')
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

    def search_terminal_checkouts(self,
                                  body):
        """Does a POST request to /v2/terminals/checkouts/search.

        Returns a filtered list of Terminal checkout requests created by the
        application making the request. Only Terminal checkout requests
        created for the merchant scoped to the OAuth token are returned.
        Terminal checkout requests are available for 30 days.

        Args:
            body (SearchTerminalCheckoutsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/terminals/checkouts/search')
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

    def get_terminal_checkout(self,
                              checkout_id):
        """Does a GET request to /v2/terminals/checkouts/{checkout_id}.

        Retrieves a Terminal checkout request by `checkout_id`. Terminal
        checkout requests are available for 30 days.

        Args:
            checkout_id (str): The unique ID for the desired
                `TerminalCheckout`.

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
            .path('/v2/terminals/checkouts/{checkout_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('checkout_id')
                            .value(checkout_id)
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

    def cancel_terminal_checkout(self,
                                 checkout_id):
        """Does a POST request to /v2/terminals/checkouts/{checkout_id}/cancel.

        Cancels a Terminal checkout request if the status of the request
        permits it.

        Args:
            checkout_id (str): The unique ID for the desired
                `TerminalCheckout`.

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
            .path('/v2/terminals/checkouts/{checkout_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('checkout_id')
                            .value(checkout_id)
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

    def dismiss_terminal_checkout(self,
                                  checkout_id):
        """Does a POST request to /v2/terminals/checkouts/{checkout_id}/dismiss.

        Dismisses a Terminal checkout request if the status and type of the
        request permits it.

        Args:
            checkout_id (str): Unique ID for the `TerminalCheckout` associated
                with the checkout to be dismissed.

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
            .path('/v2/terminals/checkouts/{checkout_id}/dismiss')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('checkout_id')
                            .value(checkout_id)
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

    def create_terminal_refund(self,
                               body):
        """Does a POST request to /v2/terminals/refunds.

        Creates a request to refund an Interac payment completed on a Square
        Terminal. Refunds for Interac payments on a Square Terminal are
        supported only for Interac debit cards in Canada. Other refunds for
        Terminal payments should use the Refunds API. For more information,
        see [Refunds API]($e/Refunds).

        Args:
            body (CreateTerminalRefundRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/terminals/refunds')
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

    def search_terminal_refunds(self,
                                body):
        """Does a POST request to /v2/terminals/refunds/search.

        Retrieves a filtered list of Interac Terminal refund requests created
        by the seller making the request. Terminal refund requests are
        available for 30 days.

        Args:
            body (SearchTerminalRefundsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/terminals/refunds/search')
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

    def get_terminal_refund(self,
                            terminal_refund_id):
        """Does a GET request to /v2/terminals/refunds/{terminal_refund_id}.

        Retrieves an Interac Terminal refund object by ID. Terminal refund
        objects are available for 30 days.

        Args:
            terminal_refund_id (str): The unique ID for the desired
                `TerminalRefund`.

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
            .path('/v2/terminals/refunds/{terminal_refund_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('terminal_refund_id')
                            .value(terminal_refund_id)
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

    def cancel_terminal_refund(self,
                               terminal_refund_id):
        """Does a POST request to /v2/terminals/refunds/{terminal_refund_id}/cancel.

        Cancels an Interac Terminal refund request by refund request ID if the
        status of the request permits it.

        Args:
            terminal_refund_id (str): The unique ID for the desired
                `TerminalRefund`.

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
            .path('/v2/terminals/refunds/{terminal_refund_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('terminal_refund_id')
                            .value(terminal_refund_id)
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

    def dismiss_terminal_refund(self,
                                terminal_refund_id):
        """Does a POST request to /v2/terminals/refunds/{terminal_refund_id}/dismiss.

        Dismisses a Terminal refund request if the status and type of the
        request permits it.

        Args:
            terminal_refund_id (str): Unique ID for the `TerminalRefund`
                associated with the refund to be dismissed.

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
            .path('/v2/terminals/refunds/{terminal_refund_id}/dismiss')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('terminal_refund_id')
                            .value(terminal_refund_id)
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
