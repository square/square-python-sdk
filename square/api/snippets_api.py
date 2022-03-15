# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class SnippetsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(SnippetsApi, self).__init__(config, auth_managers)

    def delete_snippet(self,
                       site_id):
        """Does a DELETE request to /v2/sites/{site_id}/snippet.

        Removes your snippet from a Square Online site.
        You can call [ListSites]($e/Sites/ListSites) to get the IDs of the
        sites that belong to a seller.
        __Note:__ Square Online APIs are publicly available as part of an
        early access program. For more information, see [Early access program
        for Square Online
        APIs](https://developer.squareup.com/docs/online-api#early-access-progr
        am-for-square-online-apis).

        Args:
            site_id (string): The ID of the site that contains the snippet.

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
        _url_path = '/v2/sites/{site_id}/snippet'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'site_id': {'value': site_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
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

    def retrieve_snippet(self,
                         site_id):
        """Does a GET request to /v2/sites/{site_id}/snippet.

        Retrieves your snippet from a Square Online site. A site can contain
        snippets from multiple snippet applications, but you can retrieve only
        the snippet that was added by your application.
        You can call [ListSites]($e/Sites/ListSites) to get the IDs of the
        sites that belong to a seller.
        __Note:__ Square Online APIs are publicly available as part of an
        early access program. For more information, see [Early access program
        for Square Online
        APIs](https://developer.squareup.com/docs/online-api#early-access-progr
        am-for-square-online-apis).

        Args:
            site_id (string): The ID of the site that contains the snippet.

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
        _url_path = '/v2/sites/{site_id}/snippet'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'site_id': {'value': site_id, 'encode': True}
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

    def upsert_snippet(self,
                       site_id,
                       body):
        """Does a POST request to /v2/sites/{site_id}/snippet.

        Adds a snippet to a Square Online site or updates the existing snippet
        on the site. 
        The snippet code is appended to the end of the `head` element on every
        page of the site, except checkout pages. A snippet application can add
        one snippet to a given site. 
        You can call [ListSites]($e/Sites/ListSites) to get the IDs of the
        sites that belong to a seller.
        __Note:__ Square Online APIs are publicly available as part of an
        early access program. For more information, see [Early access program
        for Square Online
        APIs](https://developer.squareup.com/docs/online-api#early-access-progr
        am-for-square-online-apis).

        Args:
            site_id (string): The ID of the site where you want to add or
                update the snippet.
            body (UpsertSnippetRequest): An object containing the fields to
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
        _url_path = '/v2/sites/{site_id}/snippet'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'site_id': {'value': site_id, 'encode': True}
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
