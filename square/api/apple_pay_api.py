# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class ApplePayApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(ApplePayApi, self).__init__(config)

    def register_domain(self,
                        body):
        """Does a POST request to /v2/apple-pay/domains.

        Activates a domain for use with Apple Pay on the Web and Square. A
        validation
        is performed on this domain by Apple to ensure that it is properly set
        up as
        an Apple Pay enabled domain.
        This endpoint provides an easy way for platform developers to bulk
        activate
        Apple Pay on the Web with Square for merchants using their platform.
        Note: You will need to host a valid domain verification file on your
        domain to support Apple Pay.  The
        current version of this file is always available at
        https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merc
        hantid-domain-association,
        and should be hosted at
        `.well_known/apple-developer-merchantid-domain-association` on your
        domain.  This file is subject to change; we strongly recommend
        checking for updates regularly and avoiding
        long-lived caches that might not keep in sync with the correct file
        version.
        To learn more about the Web Payments SDK and how to add Apple Pay, see
        [Take an Apple Pay
        Payment](https://developer.squareup.com/docs/web-payments/apple-pay).

        Args:
            body (RegisterDomainRequest): An object containing the fields to
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
            .path('/v2/apple-pay/domains')
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
