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


class CardsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(CardsApi, self).__init__(config)

    def list_cards(self,
                   cursor=None,
                   customer_id=None,
                   include_disabled=False,
                   reference_id=None,
                   sort_order=None):
        """Does a GET request to /v2/cards.

        Retrieves a list of cards owned by the account making the request.
        A max of 25 cards will be returned.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this to retrieve the next set
                of results for your original query.  See
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination) for more information.
            customer_id (str, optional): Limit results to cards associated
                with the customer supplied. By default, all cards owned by the
                merchant are returned.
            include_disabled (bool, optional): Includes disabled cards. By
                default, all enabled cards owned by the merchant are
                returned.
            reference_id (str, optional): Limit results to cards associated
                with the reference_id supplied.
            sort_order (SortOrder, optional): Sorts the returned list by when
                the card was created with the specified order. This field
                defaults to ASC.

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
            .path('/v2/cards')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('customer_id')
                         .value(customer_id))
            .query_param(Parameter()
                         .key('include_disabled')
                         .value(include_disabled))
            .query_param(Parameter()
                         .key('reference_id')
                         .value(reference_id))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
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

    def create_card(self,
                    body):
        """Does a POST request to /v2/cards.

        Adds a card on file to an existing merchant.

        Args:
            body (CreateCardRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/cards')
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

    def retrieve_card(self,
                      card_id):
        """Does a GET request to /v2/cards/{card_id}.

        Retrieves details for a specific Card.

        Args:
            card_id (str): Unique ID for the desired Card.

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
            .path('/v2/cards/{card_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('card_id')
                            .value(card_id)
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

    def disable_card(self,
                     card_id):
        """Does a POST request to /v2/cards/{card_id}/disable.

        Disables the card, preventing any further updates or charges.
        Disabling an already disabled card is allowed but has no effect.

        Args:
            card_id (str): Unique ID for the desired Card.

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
            .path('/v2/cards/{card_id}/disable')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('card_id')
                            .value(card_id)
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
