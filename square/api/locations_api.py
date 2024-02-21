# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class LocationsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(LocationsApi, self).__init__(config)

    def list_locations(self):
        """Does a GET request to /v2/locations.

        Provides details about all of the seller's
        [locations](https://developer.squareup.com/docs/locations-api),
        including those with an inactive status. Locations are listed
        alphabetically by `name`.

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
            .path('/v2/locations')
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

    def create_location(self,
                        body):
        """Does a POST request to /v2/locations.

        Creates a
        [location](https://developer.squareup.com/docs/locations-api).
        Creating new locations allows for separate configuration of receipt
        layouts, item prices,
        and sales reports. Developers can use locations to separate sales
        activity through applications
        that integrate with Square from sales activity elsewhere in a seller's
        account.
        Locations created programmatically with the Locations API last forever
        and
        are visible to the seller for their own management. Therefore, ensure
        that
        each location has a sensible and unique name.

        Args:
            body (CreateLocationRequest): An object containing the fields to
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
            .path('/v2/locations')
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

    def retrieve_location(self,
                          location_id):
        """Does a GET request to /v2/locations/{location_id}.

        Retrieves details of a single location. Specify "main"
        as the location ID to retrieve details of the [main
        location](https://developer.squareup.com/docs/locations-api#about-the-m
        ain-location).

        Args:
            location_id (str): The ID of the location to retrieve. Specify the
                string "main" to return the main location.

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
            .path('/v2/locations/{location_id}')
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

    def update_location(self,
                        location_id,
                        body):
        """Does a PUT request to /v2/locations/{location_id}.

        Updates a
        [location](https://developer.squareup.com/docs/locations-api).

        Args:
            location_id (str): The ID of the location to update.
            body (UpdateLocationRequest): An object containing the fields to
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
            .path('/v2/locations/{location_id}')
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
