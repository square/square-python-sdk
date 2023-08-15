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


class GiftCardActivitiesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(GiftCardActivitiesApi, self).__init__(config)

    def list_gift_card_activities(self,
                                  gift_card_id=None,
                                  mtype=None,
                                  location_id=None,
                                  begin_time=None,
                                  end_time=None,
                                  limit=None,
                                  cursor=None,
                                  sort_order=None):
        """Does a GET request to /v2/gift-cards/activities.

        Lists gift card activities. By default, you get gift card activities
        for all
        gift cards in the seller's account. You can optionally specify query
        parameters to
        filter the list. For example, you can get a list of gift card
        activities for a gift card,
        for all gift cards in a specific region, or for activities within a
        time window.

        Args:
            gift_card_id (str, optional): If a gift card ID is provided, the
                endpoint returns activities related  to the specified gift
                card. Otherwise, the endpoint returns all gift card activities
                for  the seller.
            mtype (str, optional): If a [type](entity:GiftCardActivityType) is
                provided, the endpoint returns gift card activities of the
                specified type.  Otherwise, the endpoint returns all types of
                gift card activities.
            location_id (str, optional): If a location ID is provided, the
                endpoint returns gift card activities for the specified
                location.  Otherwise, the endpoint returns gift card
                activities for all locations.
            begin_time (str, optional): The timestamp for the beginning of the
                reporting period, in RFC 3339 format. This start time is
                inclusive. The default value is the current time minus one
                year.
            end_time (str, optional): The timestamp for the end of the
                reporting period, in RFC 3339 format. This end time is
                inclusive. The default value is the current time.
            limit (int, optional): If a limit is provided, the endpoint
                returns the specified number  of results (or fewer) per page.
                The maximum value is 100. The default value is 50. For more
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
            sort_order (str, optional): The order in which the endpoint
                returns the activities, based on `created_at`. - `ASC` -
                Oldest to newest. - `DESC` - Newest to oldest (default).

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
            .path('/v2/gift-cards/activities')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('gift_card_id')
                         .value(gift_card_id))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('begin_time')
                         .value(begin_time))
            .query_param(Parameter()
                         .key('end_time')
                         .value(end_time))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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

    def create_gift_card_activity(self,
                                  body):
        """Does a POST request to /v2/gift-cards/activities.

        Creates a gift card activity to manage the balance or state of a [gift
        card]($m/GiftCard). 
        For example, you create an `ACTIVATE` activity to activate a gift card
        with an initial balance 
        before the gift card can be used.

        Args:
            body (CreateGiftCardActivityRequest): An object containing the
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
            .path('/v2/gift-cards/activities')
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
