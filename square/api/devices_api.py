# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or


class DevicesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(DevicesApi, self).__init__(config)

    def list_devices(self,
                     cursor=None,
                     sort_order=None,
                     limit=None,
                     location_id=None):
        """Does a GET request to /v2/devices.

        List devices associated with the merchant. Currently, only Terminal
        API
        devices are supported.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. See
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination) for more information.
            sort_order (SortOrder, optional): The order in which results are
                listed. - `ASC` - Oldest to newest. - `DESC` - Newest to
                oldest (default).
            limit (int, optional): The number of results to return in a single
                page.
            location_id (str, optional): If present, only returns devices at
                the target location.

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
            .path('/v2/devices')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
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

    def list_device_codes(self,
                          cursor=None,
                          location_id=None,
                          product_type=None,
                          status=None):
        """Does a GET request to /v2/devices/codes.

        Lists all DeviceCodes associated with the merchant.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this to retrieve the next set
                of results for your original query.  See [Paginating
                results](https://developer.squareup.com/docs/working-with-apis/
                pagination) for more information.
            location_id (str, optional): If specified, only returns
                DeviceCodes of the specified location. Returns DeviceCodes of
                all locations if empty.
            product_type (ProductType, optional): If specified, only returns
                DeviceCodes targeting the specified product type. Returns
                DeviceCodes of all product types if empty.
            status (DeviceCodeStatus, optional): If specified, returns
                DeviceCodes with the specified statuses. Returns DeviceCodes
                of status `PAIRED` and `UNPAIRED` if empty.

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
            .path('/v2/devices/codes')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
            .query_param(Parameter()
                         .key('product_type')
                         .value(product_type))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
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

    def create_device_code(self,
                           body):
        """Does a POST request to /v2/devices/codes.

        Creates a DeviceCode that can be used to login to a Square Terminal
        device to enter the connected
        terminal mode.

        Args:
            body (CreateDeviceCodeRequest): An object containing the fields to
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
            .path('/v2/devices/codes')
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

    def get_device_code(self,
                        id):
        """Does a GET request to /v2/devices/codes/{id}.

        Retrieves DeviceCode with the associated ID.

        Args:
            id (str): The unique identifier for the device code.

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
            .path('/v2/devices/codes/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
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

    def get_device(self,
                   device_id):
        """Does a GET request to /v2/devices/{device_id}.

        Retrieves Device with the associated `device_id`.

        Args:
            device_id (str): The unique ID for the desired `Device`.

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
            .path('/v2/devices/{device_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
