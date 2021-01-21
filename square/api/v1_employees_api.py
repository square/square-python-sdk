# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class V1EmployeesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(V1EmployeesApi, self).__init__(config, call_back)

    def list_employees(self,
                       order=None,
                       begin_updated_at=None,
                       end_updated_at=None,
                       begin_created_at=None,
                       end_created_at=None,
                       status=None,
                       external_id=None,
                       limit=None,
                       batch_token=None):
        """Does a GET request to /v1/me/employees.

        Provides summary information for all of a business's employees.

        Args:
            order (SortOrder, optional): The order in which employees are
                listed in the response, based on their created_at field.     
                Default value: ASC
            begin_updated_at (string, optional): If filtering results by their
                updated_at field, the beginning of the requested reporting
                period, in ISO 8601 format
            end_updated_at (string, optional): If filtering results by there
                updated_at field, the end of the requested reporting period,
                in ISO 8601 format.
            begin_created_at (string, optional): If filtering results by their
                created_at field, the beginning of the requested reporting
                period, in ISO 8601 format.
            end_created_at (string, optional): If filtering results by their
                created_at field, the end of the requested reporting period,
                in ISO 8601 format.
            status (V1ListEmployeesRequestStatus, optional): If provided, the
                endpoint returns only employee entities with the specified
                status (ACTIVE or INACTIVE).
            external_id (string, optional): If provided, the endpoint returns
                only employee entities with the specified external_id.
            limit (int, optional): The maximum integer number of employee
                entities to return in a single response. Default 100, maximum
                200.
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.

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
        _url_path = '/v1/me/employees'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'begin_updated_at': begin_updated_at,
            'end_updated_at': end_updated_at,
            'begin_created_at': begin_created_at,
            'end_created_at': end_created_at,
            'status': status,
            'external_id': external_id,
            'limit': limit,
            'batch_token': batch_token
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

    def create_employee(self,
                        body):
        """Does a POST request to /v1/me/employees.

         Use the CreateEmployee endpoint to add an employee to a Square
        account. Employees created with the Connect API have an initial
        status
        of `INACTIVE`. Inactive employees cannot sign in to Square Point of
        Sale
        until they are activated from the Square Dashboard. Employee status
        cannot be changed with the Connect API.
        Employee entities cannot be deleted. To disable employee profiles,
        set the employee's status to <code>INACTIVE</code>

        Args:
            body (V1Employee): An object containing the fields to POST for the
                request.  See the corresponding object definition for field
                details.

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
        _url_path = '/v1/me/employees'
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

    def retrieve_employee(self,
                          employee_id):
        """Does a GET request to /v1/me/employees/{employee_id}.

        Provides the details for a single employee.

        Args:
            employee_id (string): The employee's ID.

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
        _url_path = '/v1/me/employees/{employee_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'employee_id': {'value': employee_id, 'encode': True}
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

    def update_employee(self,
                        employee_id,
                        body):
        """Does a PUT request to /v1/me/employees/{employee_id}.

        UpdateEmployee

        Args:
            employee_id (string): The ID of the role to modify.
            body (V1Employee): An object containing the fields to POST for the
                request.  See the corresponding object definition for field
                details.

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
        _url_path = '/v1/me/employees/{employee_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'employee_id': {'value': employee_id, 'encode': True}
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

    def list_employee_roles(self,
                            order=None,
                            limit=None,
                            batch_token=None):
        """Does a GET request to /v1/me/roles.

        Provides summary information for all of a business's employee roles.

        Args:
            order (SortOrder, optional): The order in which employees are
                listed in the response, based on their created_at
                field.Default value: ASC
            limit (int, optional): The maximum integer number of employee
                entities to return in a single response. Default 100, maximum
                200.
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.

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
        _url_path = '/v1/me/roles'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'limit': limit,
            'batch_token': batch_token
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

    def create_employee_role(self,
                             body):
        """Does a POST request to /v1/me/roles.

        Creates an employee role you can then assign to employees.
        Square accounts can include any number of roles that can be assigned
        to
        employees. These roles define the actions and permissions granted to
        an
        employee with that role. For example, an employee with a "Shift
        Manager"
        role might be able to issue refunds in Square Point of Sale, whereas
        an
        employee with a "Clerk" role might not.
        Roles are assigned with the
        [V1UpdateEmployee](#endpoint-v1updateemployee)
        endpoint. An employee can have only one role at a time.
        If an employee has no role, they have none of the permissions
        associated
        with roles. All employees can accept payments with Square Point of
        Sale.

        Args:
            body (V1EmployeeRole): An EmployeeRole object with a name and
                permissions, and an optional owner flag.

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
        _url_path = '/v1/me/roles'
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

    def retrieve_employee_role(self,
                               role_id):
        """Does a GET request to /v1/me/roles/{role_id}.

        Provides the details for a single employee role.

        Args:
            role_id (string): The role's ID.

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
        _url_path = '/v1/me/roles/{role_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'role_id': {'value': role_id, 'encode': True}
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

    def update_employee_role(self,
                             role_id,
                             body):
        """Does a PUT request to /v1/me/roles/{role_id}.

        Modifies the details of an employee role.

        Args:
            role_id (string): The ID of the role to modify.
            body (V1EmployeeRole): An object containing the fields to POST for
                the request.  See the corresponding object definition for
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
        _url_path = '/v1/me/roles/{role_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'role_id': {'value': role_id, 'encode': True}
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
    def list_timecards(self,
                       order=None,
                       employee_id=None,
                       begin_clockin_time=None,
                       end_clockin_time=None,
                       begin_clockout_time=None,
                       end_clockout_time=None,
                       begin_updated_at=None,
                       end_updated_at=None,
                       deleted=False,
                       limit=None,
                       batch_token=None):
        """Does a GET request to /v1/me/timecards.

        Provides summary information for all of a business's employee
        timecards.

        Args:
            order (SortOrder, optional): The order in which timecards are
                listed in the response, based on their created_at field.
            employee_id (string, optional): If provided, the endpoint returns
                only timecards for the employee with the specified ID.
            begin_clockin_time (string, optional): If filtering results by
                their clockin_time field, the beginning of the requested
                reporting period, in ISO 8601 format.
            end_clockin_time (string, optional): If filtering results by their
                clockin_time field, the end of the requested reporting period,
                in ISO 8601 format.
            begin_clockout_time (string, optional): If filtering results by
                their clockout_time field, the beginning of the requested
                reporting period, in ISO 8601 format.
            end_clockout_time (string, optional): If filtering results by
                their clockout_time field, the end of the requested reporting
                period, in ISO 8601 format.
            begin_updated_at (string, optional): If filtering results by their
                updated_at field, the beginning of the requested reporting
                period, in ISO 8601 format.
            end_updated_at (string, optional): If filtering results by their
                updated_at field, the end of the requested reporting period,
                in ISO 8601 format.
            deleted (bool, optional): If true, only deleted timecards are
                returned. If false, only valid timecards are returned.If you
                don't provide this parameter, both valid and deleted timecards
                are returned.
            limit (int, optional): The maximum integer number of employee
                entities to return in a single response. Default 100, maximum
                200.
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.

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
        _url_path = '/v1/me/timecards'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'employee_id': employee_id,
            'begin_clockin_time': begin_clockin_time,
            'end_clockin_time': end_clockin_time,
            'begin_clockout_time': begin_clockout_time,
            'end_clockout_time': end_clockout_time,
            'begin_updated_at': begin_updated_at,
            'end_updated_at': end_updated_at,
            'deleted': deleted,
            'limit': limit,
            'batch_token': batch_token
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
    def create_timecard(self,
                        body):
        """Does a POST request to /v1/me/timecards.

        Creates a timecard for an employee and clocks them in with an
        `API_CREATE` event and a `clockin_time` set to the current time
        unless
        the request provides a different value.
        To import timecards from another
        system (rather than clocking someone in). Specify the `clockin_time`
        and* `clockout_time` in the request.
        Timecards correspond to exactly one shift for a given employee,
        bounded
        by the `clockin_time` and `clockout_time` fields. An employee is
        considered clocked in if they have a timecard that doesn't have a
        `clockout_time` set. An employee that is currently clocked in cannot
        be clocked in a second time.

        Args:
            body (V1Timecard): An object containing the fields to POST for the
                request.  See the corresponding object definition for field
                details.

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
        _url_path = '/v1/me/timecards'
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

    @deprecated()
    def delete_timecard(self,
                        timecard_id):
        """Does a DELETE request to /v1/me/timecards/{timecard_id}.

        Deletes a timecard. Timecards can also be deleted through the
        Square Dashboard. Deleted timecards are still accessible through
        Connect API endpoints, but cannot be modified. The `deleted` field of
        the `Timecard` object indicates whether the timecard has been
        deleted.
        __Note__: By default, deleted timecards appear alongside valid
        timecards in
        results returned by the
        [ListTimecards](#endpoint-v1employees-listtimecards)
        endpoint. To filter deleted timecards, include the `deleted` query
        parameter in the list request.
        Only approved accounts can manage their employees with Square.
        Unapproved accounts cannot use employee management features with the
        API.

        Args:
            timecard_id (string): The ID of the timecard to delete.

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
        _url_path = '/v1/me/timecards/{timecard_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'timecard_id': {'value': timecard_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = _response.text
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    @deprecated()
    def retrieve_timecard(self,
                          timecard_id):
        """Does a GET request to /v1/me/timecards/{timecard_id}.

        Provides the details for a single timecard.
        Only approved accounts can manage their employees with Square.
        Unapproved accounts cannot use employee management features with the
        API.

        Args:
            timecard_id (string): The timecard's ID.

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
        _url_path = '/v1/me/timecards/{timecard_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'timecard_id': {'value': timecard_id, 'encode': True}
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

    @deprecated()
    def update_timecard(self,
                        timecard_id,
                        body):
        """Does a PUT request to /v1/me/timecards/{timecard_id}.

        Modifies the details of a timecard with an `API_EDIT` event for
        the timecard. Updating an active timecard with a `clockout_time`
        clocks the employee out.

        Args:
            timecard_id (string): TThe ID of the timecard to modify.
            body (V1Timecard): An object containing the fields to POST for the
                request. See the corresponding object definition for field
                details.

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
        _url_path = '/v1/me/timecards/{timecard_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'timecard_id': {'value': timecard_id, 'encode': True}
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
    def list_timecard_events(self,
                             timecard_id):
        """Does a GET request to /v1/me/timecards/{timecard_id}/events.

        Provides summary information for all events associated with a
        particular timecard.
        Only approved accounts can manage their employees with Square.
        Unapproved accounts cannot use employee management features with the
        API.

        Args:
            timecard_id (string): The ID of the timecard to list events for.

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
        _url_path = '/v1/me/timecards/{timecard_id}/events'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'timecard_id': {'value': timecard_id, 'encode': True}
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

    @deprecated()
    def list_cash_drawer_shifts(self,
                                location_id,
                                order=None,
                                begin_time=None,
                                end_time=None):
        """Does a GET request to /v1/{location_id}/cash-drawer-shifts.

        Provides the details for all of a location's cash drawer shifts during
        a date range. The date range you specify cannot exceed 90 days.

        Args:
            location_id (string): The ID of the location to list cash drawer
                shifts for.
            order (SortOrder, optional): The order in which cash drawer shifts
                are listed in the response, based on their created_at field.
                Default value: ASC
            begin_time (string, optional): The beginning of the requested
                reporting period, in ISO 8601 format. Default value: The
                current time minus 90 days.
            end_time (string, optional): The beginning of the requested
                reporting period, in ISO 8601 format. Default value: The
                current time.

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
        _url_path = '/v1/{location_id}/cash-drawer-shifts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'begin_time': begin_time,
            'end_time': end_time
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
    def retrieve_cash_drawer_shift(self,
                                   location_id,
                                   shift_id):
        """Does a GET request to /v1/{location_id}/cash-drawer-shifts/{shift_id}.

        Provides the details for a single cash drawer shift, including all
        events that occurred during the shift.

        Args:
            location_id (string): The ID of the location to list cash drawer
                shifts for.
            shift_id (string): The shift's ID.

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
        _url_path = '/v1/{location_id}/cash-drawer-shifts/{shift_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': {'value': location_id, 'encode': True},
            'shift_id': {'value': shift_id, 'encode': True}
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
