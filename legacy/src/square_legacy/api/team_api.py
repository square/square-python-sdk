# -*- coding: utf-8 -*-

from square_legacy.api_helper import APIHelper
from square_legacy.http.api_response import ApiResponse
from square_legacy.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square_legacy.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class TeamApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(TeamApi, self).__init__(config)

    def create_team_member(self,
                           body):
        """Does a POST request to /v2/team-members.

        Creates a single `TeamMember` object. The `TeamMember` object is
        returned on successful creates.
        You must provide the following values in your request to this endpoint:
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members')
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members/bulk-create')
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members/bulk-update')
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

    def list_jobs(self,
                  cursor=None):
        """Does a GET request to /v2/team-members/jobs.

        Lists jobs in a seller account. Results are sorted by title in
        ascending order.

        Args:
            cursor (str, optional): The pagination cursor returned by the
                previous call to this endpoint. Provide this cursor to
                retrieve the next page of results for your original request.
                For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).

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
            .path('/v2/team-members/jobs')
            .http_method(HttpMethodEnum.GET)
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

    def create_job(self,
                   body):
        """Does a POST request to /v2/team-members/jobs.

        Creates a job in a seller account. A job defines a title and tip
        eligibility. Note that
        compensation is defined in a [job assignment]($m/JobAssignment) in a
        team member's wage setting.

        Args:
            body (CreateJobRequest): An object containing the fields to POST
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
            .path('/v2/team-members/jobs')
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

    def retrieve_job(self,
                     job_id):
        """Does a GET request to /v2/team-members/jobs/{job_id}.

        Retrieves a specified job.

        Args:
            job_id (str): The ID of the job to retrieve.

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
            .path('/v2/team-members/jobs/{job_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('job_id')
                            .value(job_id)
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

    def update_job(self,
                   job_id,
                   body):
        """Does a PUT request to /v2/team-members/jobs/{job_id}.

        Updates the title or tip eligibility of a job. Changes to the title
        propagate to all
        `JobAssignment`, `Shift`, and `TeamMemberWage` objects that reference
        the job ID. Changes to
        tip eligibility propagate to all `TeamMemberWage` objects that
        reference the job ID.

        Args:
            job_id (str): The ID of the job to update.
            body (UpdateJobRequest): An object containing the fields to POST
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
            .path('/v2/team-members/jobs/{job_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('job_id')
                            .value(job_id)
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

    def search_team_members(self,
                            body):
        """Does a POST request to /v2/team-members/search.

        Returns a paginated list of `TeamMember` objects for a business. 
        The list can be filtered by location IDs, `ACTIVE` or `INACTIVE`
        status, or whether
        the team member is the Square account owner.

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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members/search')
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

    def retrieve_team_member(self,
                             team_member_id):
        """Does a GET request to /v2/team-members/{team_member_id}.

        Retrieves a `TeamMember` object for the given `TeamMember.id`.
        Learn about [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-
        a-team-member).

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
            .path('/v2/team-members/{team_member_id}')
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
            team_member_id (str): The ID of the team member to update.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members/{team_member_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('team_member_id')
                            .value(team_member_id)
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

    def retrieve_wage_setting(self,
                              team_member_id):
        """Does a GET request to /v2/team-members/{team_member_id}/wage-setting.

        Retrieves a `WageSetting` object for a team member specified
        by `TeamMember.id`. For more information, see
        [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#retrievew
        agesetting).
        Square recommends using
        [RetrieveTeamMember]($e/Team/RetrieveTeamMember) or
        [SearchTeamMembers]($e/Team/SearchTeamMembers)
        to get this information directly from the `TeamMember.wage_setting`
        field.

        Args:
            team_member_id (str): The ID of the team member for which to
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members/{team_member_id}/wage-setting')
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

    def update_wage_setting(self,
                            team_member_id,
                            body):
        """Does a PUT request to /v2/team-members/{team_member_id}/wage-setting.

        Creates or updates a `WageSetting` object. The object is created if a
        `WageSetting` with the specified `team_member_id` doesn't exist.
        Otherwise,
        it fully replaces the `WageSetting` object for the team member.
        The `WageSetting` is returned on a successful update. For more
        information, see
        [Troubleshooting the Team
        API](https://developer.squareup.com/docs/team/troubleshooting#create-or
        -update-a-wage-setting).
        Square recommends using [CreateTeamMember]($e/Team/CreateTeamMember)
        or [UpdateTeamMember]($e/Team/UpdateTeamMember)
        to manage the `TeamMember.wage_setting` field directly.

        Args:
            team_member_id (str): The ID of the team member for which to
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/team-members/{team_member_id}/wage-setting')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('team_member_id')
                            .value(team_member_id)
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
