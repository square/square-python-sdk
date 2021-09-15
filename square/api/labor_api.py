# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class LaborApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(LaborApi, self).__init__(config, call_back)

    def list_break_types(self,
                         location_id=None,
                         limit=None,
                         cursor=None):
        """Does a GET request to /v2/labor/break-types.

        Returns a paginated list of `BreakType` instances for a business.

        Args:
            location_id (string, optional): Filter Break Types returned to
                only those that are associated with the specified location.
            limit (int, optional): Maximum number of Break Types to return per
                page. Can range between 1 and 200. The default is the maximum
                at 200.
            cursor (string, optional): Pointer to the next page of Break Type
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

        # Prepare query URL
        _url_path = '/v2/labor/break-types'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_id': location_id,
            'limit': limit,
            'cursor': cursor
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

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
        You can only have 3 `BreakType` instances per location. If you attempt
        to add a 4th
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

        # Prepare query URL
        _url_path = '/v2/labor/break-types'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_break_type(self,
                          id):
        """Does a DELETE request to /v2/labor/break-types/{id}.

        Deletes an existing `BreakType`.
        A `BreakType` can be deleted even if it is referenced from a `Shift`.

        Args:
            id (string): UUID for the `BreakType` being deleted.

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
        _url_path = '/v2/labor/break-types/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def get_break_type(self,
                       id):
        """Does a GET request to /v2/labor/break-types/{id}.

        Returns a single `BreakType` specified by id.

        Args:
            id (string): UUID for the `BreakType` being retrieved.

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
        _url_path = '/v2/labor/break-types/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_break_type(self,
                          id,
                          body):
        """Does a PUT request to /v2/labor/break-types/{id}.

        Updates an existing `BreakType`.

        Args:
            id (string): UUID for the `BreakType` being updated.
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

        # Prepare query URL
        _url_path = '/v2/labor/break-types/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    @deprecated()
    def list_employee_wages(self,
                            employee_id=None,
                            limit=None,
                            cursor=None):
        """Does a GET request to /v2/labor/employee-wages.

        Returns a paginated list of `EmployeeWage` instances for a business.

        Args:
            employee_id (string, optional): Filter wages returned to only
                those that are associated with the specified employee.
            limit (int, optional): Maximum number of Employee Wages to return
                per page. Can range between 1 and 200. The default is the
                maximum at 200.
            cursor (string, optional): Pointer to the next page of Employee
                Wage results to fetch.

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
        _url_path = '/v2/labor/employee-wages'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'employee_id': employee_id,
            'limit': limit,
            'cursor': cursor
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    @deprecated()
    def get_employee_wage(self,
                          id):
        """Does a GET request to /v2/labor/employee-wages/{id}.

        Returns a single `EmployeeWage` specified by id.

        Args:
            id (string): UUID for the `EmployeeWage` being retrieved.

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
        _url_path = '/v2/labor/employee-wages/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_shift(self,
                     body):
        """Does a POST request to /v2/labor/shifts.

        Creates a new `Shift`.
        A `Shift` represents a complete work day for a single employee.
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
        - The `start_at` date is in the future
        - the `start_at` or `end_at` overlaps another shift for the same
        employee
        - If `Break`s are set in the request, a break `start_at`
        must not be before the `Shift.start_at`. A break `end_at` must not be
        after
        the `Shift.end_at`

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

        # Prepare query URL
        _url_path = '/v2/labor/shifts'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def search_shifts(self,
                      body):
        """Does a POST request to /v2/labor/shifts/search.

        Returns a paginated list of `Shift` records for a business.
        The list to be returned can be filtered by:
        - Location IDs **and**
        - employee IDs **and**
        - shift status (`OPEN`, `CLOSED`) **and**
        - shift start **and**
        - shift end **and**
        - work day details
        The list can be sorted by:
        - `start_at`
        - `end_at`
        - `created_at`
        - `updated_at`

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

        # Prepare query URL
        _url_path = '/v2/labor/shifts/search'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_shift(self,
                     id):
        """Does a DELETE request to /v2/labor/shifts/{id}.

        Deletes a `Shift`.

        Args:
            id (string): UUID for the `Shift` being deleted.

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
        _url_path = '/v2/labor/shifts/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def get_shift(self,
                  id):
        """Does a GET request to /v2/labor/shifts/{id}.

        Returns a single `Shift` specified by id.

        Args:
            id (string): UUID for the `Shift` being retrieved.

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
        _url_path = '/v2/labor/shifts/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_shift(self,
                     id,
                     body):
        """Does a PUT request to /v2/labor/shifts/{id}.

        Updates an existing `Shift`.
        When adding a `Break` to a `Shift`, any earlier `Breaks` in the
        `Shift` have
        the `end_at` property set to a valid RFC-3339 datetime string.
        When closing a `Shift`, all `Break` instances in the shift must be
        complete with `end_at`
        set on each `Break`.

        Args:
            id (string): ID of the object being updated.
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

        # Prepare query URL
        _url_path = '/v2/labor/shifts/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_team_member_wages(self,
                               team_member_id=None,
                               limit=None,
                               cursor=None):
        """Does a GET request to /v2/labor/team-member-wages.

        Returns a paginated list of `TeamMemberWage` instances for a
        business.

        Args:
            team_member_id (string, optional): Filter wages returned to only
                those that are associated with the specified team member.
            limit (int, optional): Maximum number of Team Member Wages to
                return per page. Can range between 1 and 200. The default is
                the maximum at 200.
            cursor (string, optional): Pointer to the next page of Employee
                Wage results to fetch.

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
        _url_path = '/v2/labor/team-member-wages'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'team_member_id': team_member_id,
            'limit': limit,
            'cursor': cursor
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def get_team_member_wage(self,
                             id):
        """Does a GET request to /v2/labor/team-member-wages/{id}.

        Returns a single `TeamMemberWage` specified by id.

        Args:
            id (string): UUID for the `TeamMemberWage` being retrieved.

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
        _url_path = '/v2/labor/team-member-wages/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_workweek_configs(self,
                              limit=None,
                              cursor=None):
        """Does a GET request to /v2/labor/workweek-configs.

        Returns a list of `WorkweekConfig` instances for a business.

        Args:
            limit (int, optional): Maximum number of Workweek Configs to
                return per page.
            cursor (string, optional): Pointer to the next page of Workweek
                Config results to fetch.

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
        _url_path = '/v2/labor/workweek-configs'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'limit': limit,
            'cursor': cursor
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_workweek_config(self,
                               id,
                               body):
        """Does a PUT request to /v2/labor/workweek-configs/{id}.

        Updates a `WorkweekConfig`.

        Args:
            id (string): UUID for the `WorkweekConfig` object being updated.
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

        # Prepare query URL
        _url_path = '/v2/labor/workweek-configs/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
