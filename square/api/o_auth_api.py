# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum


class OAuthApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(OAuthApi, self).__init__(config)

    def revoke_token(self,
                     body,
                     authorization):
        """Does a POST request to /oauth2/revoke.

        Revokes an access token generated with the OAuth flow.
        If an account has more than one OAuth access token for your
        application, this
        endpoint revokes all of them, regardless of which token you specify. 
        __Important:__ The `Authorization` header for this endpoint must have
        the
        following format:
        ```
        Authorization: Client APPLICATION_SECRET
        ```
        Replace `APPLICATION_SECRET` with the application secret on the
        **OAuth**
        page for your application in the Developer Dashboard.

        Args:
            body (RevokeTokenRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.
            authorization (str): Client APPLICATION_SECRET

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
            .path('/oauth2/revoke')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def obtain_token(self,
                     body):
        """Does a POST request to /oauth2/token.

        Returns an OAuth access token and a refresh token unless the 
        `short_lived` parameter is set to `true`, in which case the endpoint 
        returns only an access token.
        The `grant_type` parameter specifies the type of OAuth request. If 
        `grant_type` is `authorization_code`, you must include the
        authorization 
        code you received when a seller granted you authorization. If
        `grant_type` 
        is `refresh_token`, you must provide a valid refresh token. If you're
        using 
        an old version of the Square APIs (prior to March 13, 2019),
        `grant_type` 
        can be `migration_token` and you must provide a valid migration
        token.
        You can use the `scopes` parameter to limit the set of permissions
        granted 
        to the access token and refresh token. You can use the `short_lived`
        parameter 
        to create an access token that expires in 24 hours.
        __Note:__ OAuth tokens should be encrypted and stored on a secure
        server. 
        Application clients should never interact directly with OAuth tokens.

        Args:
            body (ObtainTokenRequest): An object containing the fields to POST
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
            .path('/oauth2/token')
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
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def retrieve_token_status(self,
                              authorization):
        """Does a POST request to /oauth2/token/status.

        Returns information about an [OAuth access
        token](https://developer.squareup.com/docs/build-basics/access-tokens#g
        et-an-oauth-access-token) or an application’s [personal access
        token](https://developer.squareup.com/docs/build-basics/access-tokens#g
        et-a-personal-access-token).
        Add the access token to the Authorization header of the request.
        __Important:__ The `Authorization` header you provide to this endpoint
        must have the following format:
        ```
        Authorization: Bearer ACCESS_TOKEN
        ```
        where `ACCESS_TOKEN` is a
        [valid production authorization
        credential](https://developer.squareup.com/docs/build-basics/access-tok
        ens).
        If the access token is expired or not a valid access token, the
        endpoint returns an `UNAUTHORIZED` error.

        Args:
            authorization (str): Client APPLICATION_SECRET

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
            .path('/oauth2/token/status')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()
