# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class MerchantCustomAttributesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(MerchantCustomAttributesApi, self).__init__(config)

    def list_merchant_custom_attribute_definitions(self,
                                                   visibility_filter=None,
                                                   limit=None,
                                                   cursor=None):
        """Does a GET request to /v2/merchants/custom-attribute-definitions.

        Lists the merchant-related [custom attribute
        definitions]($m/CustomAttributeDefinition) that belong to a Square
        seller account.
        When all response pages are retrieved, the results include all custom
        attribute definitions
        that are visible to the requesting application, including those that
        are created by other
        applications and set to `VISIBILITY_READ_ONLY` or
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            visibility_filter (VisibilityFilter, optional): Filters the
                `CustomAttributeDefinition` results by their `visibility`
                values.
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
            .path('/v2/merchants/custom-attribute-definitions')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('visibility_filter')
                         .value(visibility_filter))
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

    def create_merchant_custom_attribute_definition(self,
                                                    body):
        """Does a POST request to /v2/merchants/custom-attribute-definitions.

        Creates a merchant-related [custom attribute
        definition]($m/CustomAttributeDefinition) for a Square seller
        account.
        Use this endpoint to define a custom attribute that can be associated
        with a merchant connecting to your application.
        A custom attribute definition specifies the `key`, `visibility`,
        `schema`, and other properties
        for a custom attribute. After the definition is created, you can call
        [UpsertMerchantCustomAttribute]($e/MerchantCustomAttributes/UpsertMerch
        antCustomAttribute) or
        [BulkUpsertMerchantCustomAttributes]($e/MerchantCustomAttributes/BulkUp
        sertMerchantCustomAttributes)
        to set the custom attribute for a merchant.

        Args:
            body (CreateMerchantCustomAttributeDefinitionRequest): An object
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
            .path('/v2/merchants/custom-attribute-definitions')
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

    def delete_merchant_custom_attribute_definition(self,
                                                    key):
        """Does a DELETE request to /v2/merchants/custom-attribute-definitions/{key}.

        Deletes a merchant-related [custom attribute
        definition]($m/CustomAttributeDefinition) from a Square seller
        account.
        Deleting a custom attribute definition also deletes the corresponding
        custom attribute from
        the merchant.
        Only the definition owner can delete a custom attribute definition.

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
            .path('/v2/merchants/custom-attribute-definitions/{key}')
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

    def retrieve_merchant_custom_attribute_definition(self,
                                                      key,
                                                      version=None):
        """Does a GET request to /v2/merchants/custom-attribute-definitions/{key}.

        Retrieves a merchant-related [custom attribute
        definition]($m/CustomAttributeDefinition) from a Square seller
        account.
        To retrieve a custom attribute definition created by another
        application, the `visibility`
        setting must be `VISIBILITY_READ_ONLY` or
        `VISIBILITY_READ_WRITE_VALUES`.

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
            .path('/v2/merchants/custom-attribute-definitions/{key}')
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

    def update_merchant_custom_attribute_definition(self,
                                                    key,
                                                    body):
        """Does a PUT request to /v2/merchants/custom-attribute-definitions/{key}.

        Updates a merchant-related [custom attribute
        definition]($m/CustomAttributeDefinition) for a Square seller
        account.
        Use this endpoint to update the following fields: `name`,
        `description`, `visibility`, or the
        `schema` for a `Selection` data type.
        Only the definition owner can update a custom attribute definition.

        Args:
            key (str): The key of the custom attribute definition to update.
            body (UpdateMerchantCustomAttributeDefinitionRequest): An object
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
            .path('/v2/merchants/custom-attribute-definitions/{key}')
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

    def bulk_delete_merchant_custom_attributes(self,
                                               body):
        """Does a POST request to /v2/merchants/custom-attributes/bulk-delete.

        Deletes [custom attributes]($m/CustomAttribute) for a merchant as a
        bulk operation.
        To delete a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            body (BulkDeleteMerchantCustomAttributesRequest): An object
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
            .path('/v2/merchants/custom-attributes/bulk-delete')
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

    def bulk_upsert_merchant_custom_attributes(self,
                                               body):
        """Does a POST request to /v2/merchants/custom-attributes/bulk-upsert.

        Creates or updates [custom attributes]($m/CustomAttribute) for a
        merchant as a bulk operation.
        Use this endpoint to set the value of one or more custom attributes
        for a merchant.
        A custom attribute is based on a custom attribute definition in a
        Square seller account, which is
        created using the
        [CreateMerchantCustomAttributeDefinition]($e/MerchantCustomAttributes/C
        reateMerchantCustomAttributeDefinition) endpoint.
        This `BulkUpsertMerchantCustomAttributes` endpoint accepts a map of 1
        to 25 individual upsert
        requests and returns a map of individual upsert responses. Each upsert
        request has a unique ID
        and provides a merchant ID and custom attribute. Each upsert response
        is returned with the ID
        of the corresponding request.
        To create or update a custom attribute owned by another application,
        the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            body (BulkUpsertMerchantCustomAttributesRequest): An object
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
            .path('/v2/merchants/custom-attributes/bulk-upsert')
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

    def list_merchant_custom_attributes(self,
                                        merchant_id,
                                        visibility_filter=None,
                                        limit=None,
                                        cursor=None,
                                        with_definitions=False):
        """Does a GET request to /v2/merchants/{merchant_id}/custom-attributes.

        Lists the [custom attributes]($m/CustomAttribute) associated with a
        merchant.
        You can use the `with_definitions` query parameter to also retrieve
        custom attribute definitions
        in the same call.
        When all response pages are retrieved, the results include all custom
        attributes that are
        visible to the requesting application, including those that are owned
        by other applications
        and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            merchant_id (str): The ID of the target
                [merchant](entity:Merchant).
            visibility_filter (VisibilityFilter, optional): Filters the
                `CustomAttributeDefinition` results by their `visibility`
                values.
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
            .path('/v2/merchants/{merchant_id}/custom-attributes')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('merchant_id')
                            .value(merchant_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('visibility_filter')
                         .value(visibility_filter))
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

    def delete_merchant_custom_attribute(self,
                                         merchant_id,
                                         key):
        """Does a DELETE request to /v2/merchants/{merchant_id}/custom-attributes/{key}.

        Deletes a [custom attribute]($m/CustomAttribute) associated with a
        merchant.
        To delete a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            merchant_id (str): The ID of the target
                [merchant](entity:Merchant).
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
            .path('/v2/merchants/{merchant_id}/custom-attributes/{key}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('merchant_id')
                            .value(merchant_id)
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

    def retrieve_merchant_custom_attribute(self,
                                           merchant_id,
                                           key,
                                           with_definition=False,
                                           version=None):
        """Does a GET request to /v2/merchants/{merchant_id}/custom-attributes/{key}.

        Retrieves a [custom attribute]($m/CustomAttribute) associated with a
        merchant.
        You can use the `with_definition` query parameter to also retrieve the
        custom attribute definition
        in the same call.
        To retrieve a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            merchant_id (str): The ID of the target
                [merchant](entity:Merchant).
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
            .path('/v2/merchants/{merchant_id}/custom-attributes/{key}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('merchant_id')
                            .value(merchant_id)
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

    def upsert_merchant_custom_attribute(self,
                                         merchant_id,
                                         key,
                                         body):
        """Does a POST request to /v2/merchants/{merchant_id}/custom-attributes/{key}.

        Creates or updates a [custom attribute]($m/CustomAttribute) for a
        merchant.
        Use this endpoint to set the value of a custom attribute for a
        specified merchant.
        A custom attribute is based on a custom attribute definition in a
        Square seller account, which
        is created using the
        [CreateMerchantCustomAttributeDefinition]($e/MerchantCustomAttributes/C
        reateMerchantCustomAttributeDefinition) endpoint.
        To create or update a custom attribute owned by another application,
        the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            merchant_id (str): The ID of the target
                [merchant](entity:Merchant).
            key (str): The key of the custom attribute to create or update.
                This key must match the `key` of a custom attribute definition
                in the Square seller account. If the requesting application is
                not the definition owner, you must use the qualified key.
            body (UpsertMerchantCustomAttributeRequest): An object containing
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
            .path('/v2/merchants/{merchant_id}/custom-attributes/{key}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('merchant_id')
                            .value(merchant_id)
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
