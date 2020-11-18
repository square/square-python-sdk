# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class ApplePayApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(ApplePayApi, self).__init__(config, call_back)

    def register_domain(self,
                        body):
        """Does a POST request to /v2/apple-pay/domains.

        Activates a domain for use with Web Apple Pay and Square. A
        validation
        will be performed on this domain by Apple to ensure is it properly set
        up as
        an Apple Pay enabled domain.
        This endpoint provides an easy way for platform developers to bulk
        activate
        Web Apple Pay with Square for merchants using their platform.
        To learn more about Apple Pay on Web see the Apple Pay section in the
        [Square Payment Form
        Walkthrough](https://developer.squareup.com/docs/payment-form/payment-f
        orm-walkthrough).

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

        # Prepare query URL
        _url_path = '/v2/apple-pay/domains'
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
