# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class TeamApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(TeamApi, self).__init__(config, auth_managers)

    def create_team_member(self,
                           body):
        """Does a POST request to /v2/team-members.

        Creates a single `TeamMember` object. The `TeamMember` object is
        returned on successful creates.
        You must provide the following values in your request to this
        endpoint:
        - `given_name`
        - `family_name`
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#createtea
        mmember).

        Args:
            body (CreateTeamMemberRequest): An object containing the fields to
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
        _url_path = '/v2/team-members'
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

    def bulk_create_team_members(self,
                                 body):
        """Does a POST request to /v2/team-members/bulk-create.

        Creates multiple `TeamMember` objects. The created `TeamMember`
        objects are returned on successful creates.
        This process is non-transactional and processes as much of the request
        as possible. If one of the creates in
        the request cannot be successfully processed, the request is not
        marked as failed, but the body of the response
        contains explicit error information for the failed create.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#bulk-crea
        te-team-members).

        Args:
            body (BulkCreateTeamMembersRequest): An object containing the
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
        _url_path = '/v2/team-members/bulk-create'
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

    def bulk_update_team_members(self,
                                 body):
        """Does a POST request to /v2/team-members/bulk-update.

        Updates multiple `TeamMember` objects. The updated `TeamMember`
        objects are returned on successful updates.
        This process is non-transactional and processes as much of the request
        as possible. If one of the updates in
        the request cannot be successfully processed, the request is not
        marked as failed, but the body of the response
        contains explicit error information for the failed update.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#bulk-upda
        te-team-members).

        Args:
            body (BulkUpdateTeamMembersRequest): An object containing the
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
        _url_path = '/v2/team-members/bulk-update'
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

    def search_team_members(self,
                            body):
        """Does a POST request to /v2/team-members/search.

        Returns a paginated list of `TeamMember` objects for a business.
        The list can be filtered by the following:
        - location IDs
        - `status`

        Args:
            body (SearchTeamMembersRequest): An object containing the fields
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
        _url_path = '/v2/team-members/search'
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

    def retrieve_team_member(self,
                             team_member_id):
        """Does a GET request to /v2/team-members/{team_member_id}.

        Retrieves a `TeamMember` object for the given `TeamMember.id`.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-
        a-team-member).

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
        _url_path = '/v2/team-members/{team_member_id}'
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

    def update_team_member(self,
                           team_member_id,
                           body):
        """Does a PUT request to /v2/team-members/{team_member_id}.

        Updates a single `TeamMember` object. The `TeamMember` object is
        returned on successful updates.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#update-a-
        team-member).

        Args:
            team_member_id (string): The ID of the team member to update.
            body (UpdateTeamMemberRequest): An object containing the fields to
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
        _url_path = '/v2/team-members/{team_member_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'team_member_id': {'value': team_member_id, 'encode': True}
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

    def retrieve_wage_setting(self,
                              team_member_id):
        """Does a GET request to /v2/team-members/{team_member_id}/wage-setting.

        Retrieves a `WageSetting` object for a team member specified
        by `TeamMember.id`.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#retrievew
        agesetting).

        Args:
            team_member_id (string): The ID of the team member for which to
                retrieve the wage setting.

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
        _url_path = '/v2/team-members/{team_member_id}/wage-setting'
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

    def update_wage_setting(self,
                            team_member_id,
                            body):
        """Does a PUT request to /v2/team-members/{team_member_id}/wage-setting.

        Creates or updates a `WageSetting` object. The object is created if a
        `WageSetting` with the specified `team_member_id` does not exist.
        Otherwise,
        it fully replaces the `WageSetting` object for the team member.
        The `WageSetting` is returned on a successful update.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#create-or
        -update-a-wage-setting).

        Args:
            team_member_id (string): The ID of the team member for which to
                update the `WageSetting` object.
            body (UpdateWageSettingRequest): An object containing the fields
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
        _url_path = '/v2/team-members/{team_member_id}/wage-setting'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'team_member_id': {'value': team_member_id, 'encode': True}
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
