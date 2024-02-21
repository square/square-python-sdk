# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class MobileAuthorizationApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(MobileAuthorizationApi, self).__init__(config)

    def create_mobile_authorization_code(self,
                                         body):
        """Does a POST request to /mobile/authorization-code.

        Generates code to authorize a mobile application to connect to a
        Square card reader.
        Authorization codes are one-time-use codes and expire 60 minutes after
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/mobile/authorization-code')
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
