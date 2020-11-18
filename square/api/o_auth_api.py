# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class OAuthApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(OAuthApi, self).__init__(config, call_back)

    @deprecated()
    def renew_token(self,
                    client_id,
                    body,
                    authorization):
        """Does a POST request to /oauth2/clients/{client_id}/access-token/renew.

        `RenewToken` is deprecated. For information about refreshing OAuth
        access tokens, see
        [Renew OAuth
        Token](https://developer.squareup.com/docs/oauth-api/cookbook/renew-oau
        th-tokens).
        Renews an OAuth access token before it expires.
        OAuth access tokens besides your application's personal access token
        expire after __30 days__.
        You can also renew expired tokens within __15 days__ of their
        expiration.
        You cannot renew an access token that has been expired for more than
        15 days.
        Instead, the associated user must re-complete the OAuth flow from the
        beginning.
        __Important:__ The `Authorization` header for this endpoint must have
        the
        following format:
        ```
        Authorization: Client APPLICATION_SECRET
        ```
        Replace `APPLICATION_SECRET` with the application secret on the
        Credentials
        page in the [application
        dashboard](https://connect.squareup.com/apps).

        Args:
            client_id (string): Your application ID, available from the
                [application dashboard](https://connect.squareup.com/apps).
            body (RenewTokenRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.
            authorization (string): Client APPLICATION_SECRET

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
        _url_path = '/oauth2/clients/{client_id}/access-token/renew'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'client_id': {'value': client_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def revoke_token(self,
                     body,
                     authorization):
        """Does a POST request to /oauth2/revoke.

        Revokes an access token generated with the OAuth flow.
        If an account has more than one OAuth access token for your
        application, this
        endpoint revokes all of them, regardless of which token you specify.
        When an
        OAuth access token is revoked, all of the active subscriptions
        associated
        with that OAuth token are canceled immediately.
        __Important:__ The `Authorization` header for this endpoint must have
        the
        following format:
        ```
        Authorization: Client APPLICATION_SECRET
        ```
        Replace `APPLICATION_SECRET` with the application secret on the
        Credentials
        page in the [Developer
        Dashboard](https://developer.squareup.com/apps).

        Args:
            body (RevokeTokenRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.
            authorization (string): Client APPLICATION_SECRET

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
        _url_path = '/oauth2/revoke'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def obtain_token(self,
                     body):
        """Does a POST request to /oauth2/token.

        Returns an OAuth access token.
        The endpoint supports distinct methods of obtaining OAuth access
        tokens.
        Applications specify a method by adding the `grant_type` parameter
        in the request and also provide relevant information.
        __Note:__ Regardless of the method application specified,
        the endpoint always returns two items; an OAuth access token and
        a refresh token in the response.
        __OAuth tokens should only live on secure servers. Application
        clients
        should never interact directly with OAuth tokens__.

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

        # Prepare query URL
        _url_path = '/oauth2/token'
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
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
