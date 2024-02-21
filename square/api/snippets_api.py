# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class SnippetsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(SnippetsApi, self).__init__(config)

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
            site_id (str): The ID of the site that contains the snippet.

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
            .path('/v2/sites/{site_id}/snippet')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
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
            site_id (str): The ID of the site that contains the snippet.

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
            .path('/v2/sites/{site_id}/snippet')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
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
            site_id (str): The ID of the site where you want to add or update
                the snippet.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/sites/{site_id}/snippet')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
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
