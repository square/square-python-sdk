# -*- coding: utf-8 -*-

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
        [V1UpdateEmployee]($e/V1Employees/UpdateEmployeeRole)
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
