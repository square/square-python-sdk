# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class CustomerSegmentsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(CustomerSegmentsApi, self).__init__(config)

    def list_customer_segments(self,
                               cursor=None,
                               limit=None):
        """Does a GET request to /v2/customers/segments.

        Retrieves the list of customer segments of a business.

        Args:
            cursor (str, optional): A pagination cursor returned by previous
                calls to `ListCustomerSegments`. This cursor is used to
                retrieve the next set of query results.  For more information,
                see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            limit (int, optional): The maximum number of results to return in
                a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less
                than 1 or greater than 50, Square returns a `400
                VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default
                value is 50.  For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).

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
            .path('/v2/customers/segments')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
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

    def retrieve_customer_segment(self,
                                  segment_id):
        """Does a GET request to /v2/customers/segments/{segment_id}.

        Retrieves a specific customer segment as identified by the
        `segment_id` value.

        Args:
            segment_id (str): The Square-issued ID of the customer segment.

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
            .path('/v2/customers/segments/{segment_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('segment_id')
                            .value(segment_id)
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
