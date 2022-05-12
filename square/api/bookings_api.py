# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class BookingsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(BookingsApi, self).__init__(config, auth_managers)

    def list_bookings(self,
                      limit=None,
                      cursor=None,
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
            cursor (string, optional): The pagination cursor from the
                preceding response to return the next page of the results. Do
                not set this when retrieving the first page of the results.
            team_member_id (string, optional): The team member for whom to
                retrieve bookings. If this is not set, bookings of all members
                are retrieved.
            location_id (string, optional): The location for which to retrieve
                bookings. If this is not set, all locations' bookings are
                retrieved.
            start_at_min (string, optional): The RFC 3339 timestamp specifying
                the earliest of the start time. If this is not set, the
                current time is used.
            start_at_max (string, optional): The RFC 3339 timestamp specifying
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

        # Prepare query URL
        _url_path = '/v2/bookings'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'limit': limit,
            'cursor': cursor,
            'team_member_id': team_member_id,
            'location_id': location_id,
            'start_at_min': start_at_min,
            'start_at_max': start_at_max
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

    def create_booking(self,
                       body):
        """Does a POST request to /v2/bookings.

        Creates a booking.
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

        # Prepare query URL
        _url_path = '/v2/bookings'
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

        # Prepare query URL
        _url_path = '/v2/bookings/availability/search'
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

        # Prepare query URL
        _url_path = '/v2/bookings/business-booking-profile'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
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
            cursor (string, optional): The pagination cursor from the
                preceding response to return the next page of the results. Do
                not set this when retrieving the first page of the results.
            location_id (string, optional): Indicates whether to include only
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

        # Prepare query URL
        _url_path = '/v2/bookings/team-member-booking-profiles'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'bookable_only': bookable_only,
            'limit': limit,
            'cursor': cursor,
            'location_id': location_id
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

    def retrieve_team_member_booking_profile(self,
                                             team_member_id):
        """Does a GET request to /v2/bookings/team-member-booking-profiles/{team_member_id}.

        Retrieves a team member's booking profile.

        Args:
            team_member_id (string): The ID of the team member to retrieve.

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
        _url_path = '/v2/bookings/team-member-booking-profiles/{team_member_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'team_member_id': {'value': team_member_id, 'encode': True}
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

    def retrieve_booking(self,
                         booking_id):
        """Does a GET request to /v2/bookings/{booking_id}.

        Retrieves a booking.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            booking_id (string): The ID of the [Booking]($m/Booking) object
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

        # Prepare query URL
        _url_path = '/v2/bookings/{booking_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'booking_id': {'value': booking_id, 'encode': True}
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
            booking_id (string): The ID of the [Booking]($m/Booking) object
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

        # Prepare query URL
        _url_path = '/v2/bookings/{booking_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'booking_id': {'value': booking_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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
            booking_id (string): The ID of the [Booking]($m/Booking) object
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

        # Prepare query URL
        _url_path = '/v2/bookings/{booking_id}/cancel'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'booking_id': {'value': booking_id, 'encode': True}
        })
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
