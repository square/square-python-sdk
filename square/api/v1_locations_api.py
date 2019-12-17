# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class V1LocationsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(V1LocationsApi, self).__init__(config, call_back)

    @deprecated()
    def retrieve_business(self):
        """Does a GET request to /v1/me.

        Get the general information for a business.
        ---
        - __Deprecation date__: 2019-11-20
        - [__Retirement
        date__](https://developer.squareup.com/docs/build-basics/api-lifecycle#
        deprecated): 2020-11-18
        - [Migration
        guide](https://developer.squareup.com/docs/migrate-from-v1/guides/v1-lo
        cations)
        ---

        Returns:
            V1Merchant: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/me'
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

    @deprecated()
    def list_locations(self):
        """Does a GET request to /v1/me/locations.

        Provides details for all business locations associated with a Square
        account, including the Square-assigned object ID for the location.
        ---
        - __Deprecation date__: 2019-11-20
        - [__Retirement
        date__](https://developer.squareup.com/docs/build-basics/api-lifecycle#
        deprecated): 2020-11-18
        - [Migration
        guide](https://developer.squareup.com/docs/migrate-from-v1/guides/v1-lo
        cations)
        ---

        Returns:
            list of V1Merchant: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/me/locations'
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
