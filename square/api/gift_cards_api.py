# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class GiftCardsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(GiftCardsApi, self).__init__(config)

    def list_gift_cards(self,
                        mtype=None,
                        state=None,
                        limit=None,
                        cursor=None,
                        customer_id=None):
        """Does a GET request to /v2/gift-cards.

        Lists all gift cards. You can specify optional filters to retrieve 
        a subset of the gift cards. Results are sorted by `created_at` in
        ascending order.

        Args:
            mtype (str, optional): If a [type](entity:GiftCardType) is
                provided, the endpoint returns gift cards of the specified
                type. Otherwise, the endpoint returns gift cards of all
                types.
            state (str, optional): If a [state](entity:GiftCardStatus) is
                provided, the endpoint returns the gift cards in the specified
                state. Otherwise, the endpoint returns the gift cards of all
                states.
            limit (int, optional): If a limit is provided, the endpoint
                returns only the specified number of results per page. The
                maximum value is 200. The default value is 30. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. If a cursor is not
                provided, the endpoint returns the first page of the results. 
                For more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            customer_id (str, optional): If a customer ID is provided, the
                endpoint returns only the gift cards linked to the specified
                customer.

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
            .path('/v2/gift-cards')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('state')
                         .value(state))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('customer_id')
                         .value(customer_id))
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

    def create_gift_card(self,
                         body):
        """Does a POST request to /v2/gift-cards.

        Creates a digital gift card or registers a physical (plastic) gift
        card. After the gift card 
        is created, you must call
        [CreateGiftCardActivity]($e/GiftCardActivities/CreateGiftCardActivity)
                to activate the card with an initial balance before it can be used for
        payment.

        Args:
            body (CreateGiftCardRequest): An object containing the fields to
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
            .path('/v2/gift-cards')
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

    def retrieve_gift_card_from_gan(self,
                                    body):
        """Does a POST request to /v2/gift-cards/from-gan.

        Retrieves a gift card using the gift card account number (GAN).

        Args:
            body (RetrieveGiftCardFromGANRequest): An object containing the
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
            .path('/v2/gift-cards/from-gan')
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

    def retrieve_gift_card_from_nonce(self,
                                      body):
        """Does a POST request to /v2/gift-cards/from-nonce.

        Retrieves a gift card using a secure payment token that represents the
        gift card.

        Args:
            body (RetrieveGiftCardFromNonceRequest): An object containing the
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
            .path('/v2/gift-cards/from-nonce')
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

    def link_customer_to_gift_card(self,
                                   gift_card_id,
                                   body):
        """Does a POST request to /v2/gift-cards/{gift_card_id}/link-customer.

        Links a customer to a gift card, which is also referred to as adding a
        card on file.

        Args:
            gift_card_id (str): The ID of the gift card to be linked.
            body (LinkCustomerToGiftCardRequest): An object containing the
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
            .path('/v2/gift-cards/{gift_card_id}/link-customer')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('gift_card_id')
                            .value(gift_card_id)
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

    def unlink_customer_from_gift_card(self,
                                       gift_card_id,
                                       body):
        """Does a POST request to /v2/gift-cards/{gift_card_id}/unlink-customer.

        Unlinks a customer from a gift card, which is also referred to as
        removing a card on file.

        Args:
            gift_card_id (str): The ID of the gift card to be unlinked.
            body (UnlinkCustomerFromGiftCardRequest): An object containing the
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
            .path('/v2/gift-cards/{gift_card_id}/unlink-customer')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('gift_card_id')
                            .value(gift_card_id)
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

    def retrieve_gift_card(self,
                           id):
        """Does a GET request to /v2/gift-cards/{id}.

        Retrieves a gift card using the gift card ID.

        Args:
            id (str): The ID of the gift card to retrieve.

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
            .path('/v2/gift-cards/{id}')
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
