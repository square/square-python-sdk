# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class GiftCardActivitiesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(GiftCardActivitiesApi, self).__init__(config, auth_managers)

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
            gift_card_id (string, optional): If a gift card ID is provided,
                the endpoint returns activities related  to the specified gift
                card. Otherwise, the endpoint returns all gift card activities
                for  the seller.
            mtype (string, optional): If a [type]($m/GiftCardActivityType) is
                provided, the endpoint returns gift card activities of the
                specified type.  Otherwise, the endpoint returns all types of
                gift card activities.
            location_id (string, optional): If a location ID is provided, the
                endpoint returns gift card activities for the specified
                location.  Otherwise, the endpoint returns gift card
                activities for all locations.
            begin_time (string, optional): The timestamp for the beginning of
                the reporting period, in RFC 3339 format. This start time is
                inclusive. The default value is the current time minus one
                year.
            end_time (string, optional): The timestamp for the end of the
                reporting period, in RFC 3339 format. This end time is
                inclusive. The default value is the current time.
            limit (int, optional): If a limit is provided, the endpoint
                returns the specified number  of results (or fewer) per page.
                The maximum value is 100. The default value is 50. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query. If a
                cursor is not provided, the endpoint returns the first page of
                the results. For more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            sort_order (string, optional): The order in which the endpoint
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

        # Prepare query URL
        _url_path = '/v2/gift-cards/activities'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'gift_card_id': gift_card_id,
            'type': mtype,
            'location_id': location_id,
            'begin_time': begin_time,
            'end_time': end_time,
            'limit': limit,
            'cursor': cursor,
            'sort_order': sort_order
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

        # Prepare query URL
        _url_path = '/v2/gift-cards/activities'
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
