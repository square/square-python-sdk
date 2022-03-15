# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class ApplePayApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(ApplePayApi, self).__init__(config, auth_managers)

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
        To learn more about Web Apple Pay, see
        [Add the Apple Pay on the Web
        Button](https://developer.squareup.com/docs/payment-form/add-digital-wa
        llets/apple-pay).

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
