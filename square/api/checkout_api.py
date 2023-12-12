# -*- coding: utf-8 -*-

from deprecation import deprecated
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


class CheckoutApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(CheckoutApi, self).__init__(config)

    @deprecated()
    def create_checkout(self,
                        location_id,
                        body):
        """Does a POST request to /v2/locations/{location_id}/checkouts.

        Links a `checkoutId` to a `checkout_page_url` that customers are
        directed to in order to provide their payment information using a
        payment processing workflow hosted on connect.squareup.com. 
        NOTE: The Checkout API has been updated with new features. 
        For more information, see [Checkout API
        highlights](https://developer.squareup.com/docs/checkout-api#checkout-a
        pi-highlights).

        Args:
            location_id (str): The ID of the business location to associate
                the checkout with.
            body (CreateCheckoutRequest): An object containing the fields to
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
            .path('/v2/locations/{location_id}/checkouts')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
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

    def retrieve_location_settings(self,
                                   location_id):
        """Does a GET request to /v2/online-checkout/location-settings/{location_id}.

        Retrieves the location-level settings for a Square-hosted checkout
        page.

        Args:
            location_id (str): The ID of the location for which to retrieve
                settings.

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
            .path('/v2/online-checkout/location-settings/{location_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
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

    def update_location_settings(self,
                                 location_id,
                                 body):
        """Does a PUT request to /v2/online-checkout/location-settings/{location_id}.

        Updates the location-level settings for a Square-hosted checkout
        page.

        Args:
            location_id (str): The ID of the location for which to retrieve
                settings.
            body (UpdateLocationSettingsRequest): An object containing the
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
            .path('/v2/online-checkout/location-settings/{location_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('location_id')
                            .value(location_id)
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

    def retrieve_merchant_settings(self):
        """Does a GET request to /v2/online-checkout/merchant-settings.

        Retrieves the merchant-level settings for a Square-hosted checkout
        page.

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
            .path('/v2/online-checkout/merchant-settings')
            .http_method(HttpMethodEnum.GET)
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

    def update_merchant_settings(self,
                                 body):
        """Does a PUT request to /v2/online-checkout/merchant-settings.

        Updates the merchant-level settings for a Square-hosted checkout
        page.

        Args:
            body (UpdateMerchantSettingsRequest): An object containing the
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
            .path('/v2/online-checkout/merchant-settings')
            .http_method(HttpMethodEnum.PUT)
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

    def list_payment_links(self,
                           cursor=None,
                           limit=None):
        """Does a GET request to /v2/online-checkout/payment-links.

        Lists all payment links.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. If a cursor is not
                provided, the endpoint returns the first page of the results.
                For more  information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination).
            limit (int, optional): A limit on the number of results to return
                per page. The limit is advisory and the implementation might
                return more or less results. If the supplied limit is
                negative, zero, or greater than the maximum limit of 1000, it
                is ignored.  Default value: `100`

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
            .path('/v2/online-checkout/payment-links')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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

    def create_payment_link(self,
                            body):
        """Does a POST request to /v2/online-checkout/payment-links.

        Creates a Square-hosted checkout page. Applications can share the
        resulting payment link with their buyer to pay for goods and
        services.

        Args:
            body (CreatePaymentLinkRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
            .path('/v2/online-checkout/payment-links')
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

    def delete_payment_link(self,
                            id):
        """Does a DELETE request to /v2/online-checkout/payment-links/{id}.

        Deletes a payment link.

        Args:
            id (str): The ID of the payment link to delete.

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
            .path('/v2/online-checkout/payment-links/{id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
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

    def retrieve_payment_link(self,
                              id):
        """Does a GET request to /v2/online-checkout/payment-links/{id}.

        Retrieves a payment link.

        Args:
            id (str): The ID of link to retrieve.

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
            .path('/v2/online-checkout/payment-links/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
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

    def update_payment_link(self,
                            id,
                            body):
        """Does a PUT request to /v2/online-checkout/payment-links/{id}.

        Updates a payment link. You can update the `payment_link` fields such
        as
        `description`, `checkout_options`, and  `pre_populated_data`.
        You cannot update other fields such as the `order_id`, `version`,
        `URL`, or `timestamp` field.

        Args:
            id (str): The ID of the payment link to update.
            body (UpdatePaymentLinkRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
            .path('/v2/online-checkout/payment-links/{id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
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
