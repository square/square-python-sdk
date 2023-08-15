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


class BookingCustomAttributesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(BookingCustomAttributesApi, self).__init__(config)

    def list_booking_custom_attribute_definitions(self,
                                                  limit=None,
                                                  cursor=None):
        """Does a GET request to /v2/bookings/custom-attribute-definitions.

        Get all bookings custom attribute definitions.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            limit (int, optional): The maximum number of results to return in
                a single paged response. This limit is advisory. The response
                might contain more or fewer results. The minimum value is 1
                and the maximum value is 100. The default value is 20. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            cursor (str, optional): The cursor returned in the paged response
                from the previous call to this endpoint. Provide this cursor
                to retrieve the next page of results for your original
                request. For more information, see
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
            .path('/v2/bookings/custom-attribute-definitions')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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

    def create_booking_custom_attribute_definition(self,
                                                   body):
        """Does a POST request to /v2/bookings/custom-attribute-definitions.

        Creates a bookings custom attribute definition.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            body (CreateBookingCustomAttributeDefinitionRequest): An object
                containing the fields to POST for the request.  See the
                corresponding object definition for field details.

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
            .path('/v2/bookings/custom-attribute-definitions')
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

    def delete_booking_custom_attribute_definition(self,
                                                   key):
        """Does a DELETE request to /v2/bookings/custom-attribute-definitions/{key}.

        Deletes a bookings custom attribute definition.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            key (str): The key of the custom attribute definition to delete.

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
            .path('/v2/bookings/custom-attribute-definitions/{key}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('key')
                            .value(key)
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

    def retrieve_booking_custom_attribute_definition(self,
                                                     key,
                                                     version=None):
        """Does a GET request to /v2/bookings/custom-attribute-definitions/{key}.

        Retrieves a bookings custom attribute definition.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            key (str): The key of the custom attribute definition to retrieve.
                If the requesting application is not the definition owner, you
                must use the qualified key.
            version (int, optional): The current version of the custom
                attribute definition, which is used for strongly consistent
                reads to guarantee that you receive the most up-to-date data.
                When included in the request, Square returns the specified
                version or a higher version if one exists. If the specified
                version is higher than the current version, Square returns a
                `BAD_REQUEST` error.

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
            .path('/v2/bookings/custom-attribute-definitions/{key}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('key')
                            .value(key)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
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

    def update_booking_custom_attribute_definition(self,
                                                   key,
                                                   body):
        """Does a PUT request to /v2/bookings/custom-attribute-definitions/{key}.

        Updates a bookings custom attribute definition.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            key (str): The key of the custom attribute definition to update.
            body (UpdateBookingCustomAttributeDefinitionRequest): An object
                containing the fields to POST for the request.  See the
                corresponding object definition for field details.

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
            .path('/v2/bookings/custom-attribute-definitions/{key}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('key')
                            .value(key)
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

    def bulk_delete_booking_custom_attributes(self,
                                              body):
        """Does a POST request to /v2/bookings/custom-attributes/bulk-delete.

        Bulk deletes bookings custom attributes.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            body (BulkDeleteBookingCustomAttributesRequest): An object
                containing the fields to POST for the request.  See the
                corresponding object definition for field details.

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
            .path('/v2/bookings/custom-attributes/bulk-delete')
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

    def bulk_upsert_booking_custom_attributes(self,
                                              body):
        """Does a POST request to /v2/bookings/custom-attributes/bulk-upsert.

        Bulk upserts bookings custom attributes.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            body (BulkUpsertBookingCustomAttributesRequest): An object
                containing the fields to POST for the request.  See the
                corresponding object definition for field details.

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
            .path('/v2/bookings/custom-attributes/bulk-upsert')
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

    def list_booking_custom_attributes(self,
                                       booking_id,
                                       limit=None,
                                       cursor=None,
                                       with_definitions=False):
        """Does a GET request to /v2/bookings/{booking_id}/custom-attributes.

        Lists a booking's custom attributes.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            booking_id (str): The ID of the target [booking](entity:Booking).
            limit (int, optional): The maximum number of results to return in
                a single paged response. This limit is advisory. The response
                might contain more or fewer results. The minimum value is 1
                and the maximum value is 100. The default value is 20. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            cursor (str, optional): The cursor returned in the paged response
                from the previous call to this endpoint. Provide this cursor
                to retrieve the next page of results for your original
                request. For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            with_definitions (bool, optional): Indicates whether to return the
                [custom attribute
                definition](entity:CustomAttributeDefinition) in the
                `definition` field of each custom attribute. Set this
                parameter to `true` to get the name and description of each
                custom attribute, information about the data type, or other
                definition details. The default value is `false`.

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
            .path('/v2/bookings/{booking_id}/custom-attributes')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('with_definitions')
                         .value(with_definitions))
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

    def delete_booking_custom_attribute(self,
                                        booking_id,
                                        key):
        """Does a DELETE request to /v2/bookings/{booking_id}/custom-attributes/{key}.

        Deletes a bookings custom attribute.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            booking_id (str): The ID of the target [booking](entity:Booking).
            key (str): The key of the custom attribute to delete. This key
                must match the `key` of a custom attribute definition in the
                Square seller account. If the requesting application is not
                the definition owner, you must use the qualified key.

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
            .path('/v2/bookings/{booking_id}/custom-attributes/{key}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('key')
                            .value(key)
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

    def retrieve_booking_custom_attribute(self,
                                          booking_id,
                                          key,
                                          with_definition=False,
                                          version=None):
        """Does a GET request to /v2/bookings/{booking_id}/custom-attributes/{key}.

        Retrieves a bookings custom attribute.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

        Args:
            booking_id (str): The ID of the target [booking](entity:Booking).
            key (str): The key of the custom attribute to retrieve. This key
                must match the `key` of a custom attribute definition in the
                Square seller account. If the requesting application is not
                the definition owner, you must use the qualified key.
            with_definition (bool, optional): Indicates whether to return the
                [custom attribute
                definition](entity:CustomAttributeDefinition) in the
                `definition` field of the custom attribute. Set this parameter
                to `true` to get the name and description of the custom
                attribute, information about the data type, or other
                definition details. The default value is `false`.
            version (int, optional): The current version of the custom
                attribute, which is used for strongly consistent reads to
                guarantee that you receive the most up-to-date data. When
                included in the request, Square returns the specified version
                or a higher version if one exists. If the specified version is
                higher than the current version, Square returns a
                `BAD_REQUEST` error.

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
            .path('/v2/bookings/{booking_id}/custom-attributes/{key}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('key')
                            .value(key)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('with_definition')
                         .value(with_definition))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
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

    def upsert_booking_custom_attribute(self,
                                        booking_id,
                                        key,
                                        body):
        """Does a PUT request to /v2/bookings/{booking_id}/custom-attributes/{key}.

        Upserts a bookings custom attribute.
        To call this endpoint with buyer-level permissions, set
        `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set
        `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth
        scope.
        For calls to this endpoint with seller-level permissions to succeed,
        the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Args:
            booking_id (str): The ID of the target [booking](entity:Booking).
            key (str): The key of the custom attribute to create or update.
                This key must match the `key` of a custom attribute definition
                in the Square seller account. If the requesting application is
                not the definition owner, you must use the qualified key.
            body (UpsertBookingCustomAttributeRequest): An object containing
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
            .path('/v2/bookings/{booking_id}/custom-attributes/{key}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('booking_id')
                            .value(booking_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('key')
                            .value(key)
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
