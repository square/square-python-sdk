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


class BookingsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(BookingsApi, self).__init__(config)

    def list_bookings(self,
                      limit=None,
                      cursor=None,
                      customer_id=None,
                      team_member_id=None,
                      location_id=None,
                      start_at_min=None,
                      start_at_max=None):
        """Does a GET request to /v2/bookings.

        Retrieve a collection of bookings.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            limit (int, optional): The maximum number of results per page to
                return in a paged response.
            cursor (str, optional): The pagination cursor from the preceding
                response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            customer_id (str, optional): The [customer](entity:Customer) for
                whom to retrieve bookings. If this is not set, bookings for
                all customers are retrieved.
            team_member_id (str, optional): The team member for whom to
                retrieve bookings. If this is not set, bookings of all members
                are retrieved.
            location_id (str, optional): The location for which to retrieve
                bookings. If this is not set, all locations' bookings are
                retrieved.
            start_at_min (str, optional): The RFC 3339 timestamp specifying
                the earliest of the start time. If this is not set, the
                current time is used.
            start_at_max (str, optional): The RFC 3339 timestamp specifying
                the latest of the start time. If this is not set, the time of
                31 days after `start_at_min` is used.

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
            .path('/v2/bookings')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('customer_id')
                         .value(customer_id))
            .query_param(Parameter()
                         .key('team_member_id')
                         .value(team_member_id))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('start_at_min')
                         .value(start_at_min))
            .query_param(Parameter()
                         .key('start_at_max')
                         .value(start_at_max))
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

    def create_booking(self,
                       body):
        """Does a POST request to /v2/bookings.

        Creates a booking.
        The required input must include the following:
        - `Booking.location_id`
        - `Booking.start_at`
        - `Booking.team_member_id`
        - `Booking.AppointmentSegment.service_variation_id`
        - `Booking.AppointmentSegment.service_variation_version`
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            body (CreateBookingRequest): An object containing the fields to
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
            .path('/v2/bookings')
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

    def search_availability(self,
                            body):
        """Does a POST request to /v2/bookings/availability/search.

        Searches for availabilities for booking.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            body (SearchAvailabilityRequest): An object containing the fields
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
            .path('/v2/bookings/availability/search')
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

    def bulk_retrieve_bookings(self,
                               body):
        """Does a POST request to /v2/bookings/bulk-retrieve.

        Bulk-Retrieves a list of bookings by booking IDs.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            body (BulkRetrieveBookingsRequest): An object containing the
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
            .path('/v2/bookings/bulk-retrieve')
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

    def retrieve_business_booking_profile(self):
        """Does a GET request to /v2/bookings/business-booking-profile.

        Retrieves a seller's booking profile.

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
            .path('/v2/bookings/business-booking-profile')
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

    def list_location_booking_profiles(self,
                                       limit=None,
                                       cursor=None):
        """Does a GET request to /v2/bookings/location-booking-profiles.

        Lists location booking profiles of a seller.

        Args:
            limit (int, optional): The maximum number of results to return in
                a paged response.
            cursor (str, optional): The pagination cursor from the preceding
                response to return the next page of the results. Do not set
                this when retrieving the first page of the results.

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
            .path('/v2/bookings/location-booking-profiles')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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

    def retrieve_location_booking_profile(self,
                                          location_id):
        """Does a GET request to /v2/bookings/location-booking-profiles/{location_id}.

        Retrieves a seller's location booking profile.

        Args:
            location_id (str): The ID of the location to retrieve the booking
                profile.

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
            .path('/v2/bookings/location-booking-profiles/{location_id}')
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

    def list_team_member_booking_profiles(self,
                                          bookable_only=False,
                                          limit=None,
                                          cursor=None,
                                          location_id=None):
        """Does a GET request to /v2/bookings/team-member-booking-profiles.

        Lists booking profiles for team members.

        Args:
            bookable_only (bool, optional): Indicates whether to include only
                bookable team members in the returned result (`true`) or not
                (`false`).
            limit (int, optional): The maximum number of results to return in
                a paged response.
            cursor (str, optional): The pagination cursor from the preceding
                response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            location_id (str, optional): Indicates whether to include only
                team members enabled at the given location in the returned
                result.

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
            .path('/v2/bookings/team-member-booking-profiles')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('bookable_only')
                         .value(bookable_only))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
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

    def bulk_retrieve_team_member_booking_profiles(self,
                                                   body):
        """Does a POST request to /v2/bookings/team-member-booking-profiles/bulk-retrieve.

        Retrieves one or more team members' booking profiles.

        Args:
            body (BulkRetrieveTeamMemberBookingProfilesRequest): An object
                containing the fields to POST for the request.  See the
                corresponding object definition for field details.

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
            .path('/v2/bookings/team-member-booking-profiles/bulk-retrieve')
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

    def retrieve_team_member_booking_profile(self,
                                             team_member_id):
        """Does a GET request to /v2/bookings/team-member-booking-profiles/{team_member_id}.

        Retrieves a team member's booking profile.

        Args:
            team_member_id (str): The ID of the team member to retrieve.

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
            .path('/v2/bookings/team-member-booking-profiles/{team_member_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('team_member_id')
                            .value(team_member_id)
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

    def retrieve_booking(self,
                         booking_id):
        """Does a GET request to /v2/bookings/{booking_id}.

        Retrieves a booking.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            booking_id (str): The ID of the [Booking](entity:Booking) object
                representing the to-be-retrieved booking.

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
            .path('/v2/bookings/{booking_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
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

    def update_booking(self,
                       booking_id,
                       body):
        """Does a PUT request to /v2/bookings/{booking_id}.

        Updates a booking.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            booking_id (str): The ID of the [Booking](entity:Booking) object
                representing the to-be-updated booking.
            body (UpdateBookingRequest): An object containing the fields to
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
            .path('/v2/bookings/{booking_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
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

    def cancel_booking(self,
                       booking_id,
                       body):
        """Does a POST request to /v2/bookings/{booking_id}/cancel.

        Cancels an existing booking.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            booking_id (str): The ID of the [Booking](entity:Booking) object
                representing the to-be-cancelled booking.
            body (CancelBookingRequest): An object containing the fields to
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
            .path('/v2/bookings/{booking_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
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
