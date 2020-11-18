# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class MobileAuthorizationApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(MobileAuthorizationApi, self).__init__(config, call_back)

    def create_mobile_authorization_code(self,
                                         body):
        """Does a POST request to /mobile/authorization-code.

        Generates code to authorize a mobile application to connect to a
        Square card reader
        Authorization codes are one-time-use and expire __60 minutes__ after
        being issued.
        __Important:__ The `Authorization` header you provide to this endpoint
        must have the following format:
        ```
        Authorization: Bearer ACCESS_TOKEN
        ```
        Replace `ACCESS_TOKEN` with a
        [valid production authorization
        credential](https://developer.squareup.com/docs/build-basics/access-tok
        ens).

        Args:
            body (CreateMobileAuthorizationCodeRequest): An object containing
                the fields to POST for the request.  See the corresponding
                object definition for field details.

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
        _url_path = '/mobile/authorization-code'
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
