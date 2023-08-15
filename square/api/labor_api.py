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


class LaborApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(LaborApi, self).__init__(config)

    def list_break_types(self,
                         location_id=None,
                         limit=None,
                         cursor=None):
        """Does a GET request to /v2/labor/break-types.

        Returns a paginated list of `BreakType` instances for a business.

        Args:
            location_id (str, optional): Filter the returned `BreakType`
                results to only those that are associated with the specified
                location.
            limit (int, optional): The maximum number of `BreakType` results
                to return per page. The number can range between 1 and 200.
                The default is 200.
            cursor (str, optional): A pointer to the next page of `BreakType`
                results to fetch.

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
            .path('/v2/labor/break-types')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
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

    def create_break_type(self,
                          body):
        """Does a POST request to /v2/labor/break-types.

        Creates a new `BreakType`.
        A `BreakType` is a template for creating `Break` objects.
        You must provide the following values in your request to this
        endpoint:
        - `location_id`
        - `break_name`
        - `expected_duration`
        - `is_paid`
        You can only have three `BreakType` instances per location. If you
        attempt to add a fourth
        `BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit
        of 3 breaks per location."
        is returned.

        Args:
            body (CreateBreakTypeRequest): An object containing the fields to
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
            .path('/v2/labor/break-types')
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

    def delete_break_type(self,
                          id):
        """Does a DELETE request to /v2/labor/break-types/{id}.

        Deletes an existing `BreakType`.
        A `BreakType` can be deleted even if it is referenced from a `Shift`.

        Args:
            id (str): The UUID for the `BreakType` being deleted.

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
            .path('/v2/labor/break-types/{id}')
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

    def get_break_type(self,
                       id):
        """Does a GET request to /v2/labor/break-types/{id}.

        Returns a single `BreakType` specified by `id`.

        Args:
            id (str): The UUID for the `BreakType` being retrieved.

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
            .path('/v2/labor/break-types/{id}')
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

    def update_break_type(self,
                          id,
                          body):
        """Does a PUT request to /v2/labor/break-types/{id}.

        Updates an existing `BreakType`.

        Args:
            id (str): The UUID for the `BreakType` being updated.
            body (UpdateBreakTypeRequest): An object containing the fields to
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
            .path('/v2/labor/break-types/{id}')
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

    @deprecated()
    def list_employee_wages(self,
                            employee_id=None,
                            limit=None,
                            cursor=None):
        """Does a GET request to /v2/labor/employee-wages.

        Returns a paginated list of `EmployeeWage` instances for a business.

        Args:
            employee_id (str, optional): Filter the returned wages to only
                those that are associated with the specified employee.
            limit (int, optional): The maximum number of `EmployeeWage`
                results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor (str, optional): A pointer to the next page of
                `EmployeeWage` results to fetch.

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
            .path('/v2/labor/employee-wages')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('employee_id')
                         .value(employee_id))
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

    @deprecated()
    def get_employee_wage(self,
                          id):
        """Does a GET request to /v2/labor/employee-wages/{id}.

        Returns a single `EmployeeWage` specified by `id`.

        Args:
            id (str): The UUID for the `EmployeeWage` being retrieved.

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
            .path('/v2/labor/employee-wages/{id}')
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

    def create_shift(self,
                     body):
        """Does a POST request to /v2/labor/shifts.

        Creates a new `Shift`.
        A `Shift` represents a complete workday for a single employee.
        You must provide the following values in your request to this
        endpoint:
        - `location_id`
        - `employee_id`
        - `start_at`
        An attempt to create a new `Shift` can result in a `BAD_REQUEST` error
        when:
        - The `status` of the new `Shift` is `OPEN` and the employee has
        another
        shift with an `OPEN` status.
        - The `start_at` date is in the future.
        - The `start_at` or `end_at` date overlaps another shift for the same
        employee.
        - The `Break` instances are set in the request and a break `start_at`
        is before the `Shift.start_at`, a break `end_at` is after
        the `Shift.end_at`, or both.

        Args:
            body (CreateShiftRequest): An object containing the fields to POST
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
            .path('/v2/labor/shifts')
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

    def search_shifts(self,
                      body):
        """Does a POST request to /v2/labor/shifts/search.

        Returns a paginated list of `Shift` records for a business.
        The list to be returned can be filtered by:
        - Location IDs.
        - Employee IDs.
        - Shift status (`OPEN` and `CLOSED`).
        - Shift start.
        - Shift end.
        - Workday details.
        The list can be sorted by:
        - `start_at`.
        - `end_at`.
        - `created_at`.
        - `updated_at`.

        Args:
            body (SearchShiftsRequest): An object containing the fields to
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
            .path('/v2/labor/shifts/search')
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

    def delete_shift(self,
                     id):
        """Does a DELETE request to /v2/labor/shifts/{id}.

        Deletes a `Shift`.

        Args:
            id (str): The UUID for the `Shift` being deleted.

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
            .path('/v2/labor/shifts/{id}')
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

    def get_shift(self,
                  id):
        """Does a GET request to /v2/labor/shifts/{id}.

        Returns a single `Shift` specified by `id`.

        Args:
            id (str): The UUID for the `Shift` being retrieved.

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
            .path('/v2/labor/shifts/{id}')
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

    def update_shift(self,
                     id,
                     body):
        """Does a PUT request to /v2/labor/shifts/{id}.

        Updates an existing `Shift`.
        When adding a `Break` to a `Shift`, any earlier `Break` instances in
        the `Shift` have
        the `end_at` property set to a valid RFC-3339 datetime string.
        When closing a `Shift`, all `Break` instances in the `Shift` must be
        complete with `end_at`
        set on each `Break`.

        Args:
            id (str): The ID of the object being updated.
            body (UpdateShiftRequest): An object containing the fields to POST
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
            .path('/v2/labor/shifts/{id}')
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

    def list_team_member_wages(self,
                               team_member_id=None,
                               limit=None,
                               cursor=None):
        """Does a GET request to /v2/labor/team-member-wages.

        Returns a paginated list of `TeamMemberWage` instances for a
        business.

        Args:
            team_member_id (str, optional): Filter the returned wages to only
                those that are associated with the specified team member.
            limit (int, optional): The maximum number of `TeamMemberWage`
                results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor (str, optional): A pointer to the next page of
                `EmployeeWage` results to fetch.

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
            .path('/v2/labor/team-member-wages')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('team_member_id')
                         .value(team_member_id))
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

    def get_team_member_wage(self,
                             id):
        """Does a GET request to /v2/labor/team-member-wages/{id}.

        Returns a single `TeamMemberWage` specified by `id `.

        Args:
            id (str): The UUID for the `TeamMemberWage` being retrieved.

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
            .path('/v2/labor/team-member-wages/{id}')
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

    def list_workweek_configs(self,
                              limit=None,
                              cursor=None):
        """Does a GET request to /v2/labor/workweek-configs.

        Returns a list of `WorkweekConfig` instances for a business.

        Args:
            limit (int, optional): The maximum number of `WorkweekConfigs`
                results to return per page.
            cursor (str, optional): A pointer to the next page of
                `WorkweekConfig` results to fetch.

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
            .path('/v2/labor/workweek-configs')
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

    def update_workweek_config(self,
                               id,
                               body):
        """Does a PUT request to /v2/labor/workweek-configs/{id}.

        Updates a `WorkweekConfig`.

        Args:
            id (str): The UUID for the `WorkweekConfig` object being updated.
            body (UpdateWorkweekConfigRequest): An object containing the
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
            .path('/v2/labor/workweek-configs/{id}')
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
