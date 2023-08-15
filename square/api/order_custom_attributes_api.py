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


class OrderCustomAttributesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(OrderCustomAttributesApi, self).__init__(config)

    def list_order_custom_attribute_definitions(self,
                                                visibility_filter=None,
                                                cursor=None,
                                                limit=None):
        """Does a GET request to /v2/orders/custom-attribute-definitions.

        Lists the order-related [custom attribute
        definitions]($m/CustomAttributeDefinition) that belong to a Square
        seller account.
        When all response pages are retrieved, the results include all custom
        attribute definitions
        that are visible to the requesting application, including those that
        are created by other
        applications and set to `VISIBILITY_READ_ONLY` or
        `VISIBILITY_READ_WRITE_VALUES`. Note that
        seller-defined custom attributes (also known as custom fields) are
        always set to `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            visibility_filter (VisibilityFilter, optional): Requests that all
                of the custom attributes be returned, or only those that are
                read-only or read-write.
            cursor (str, optional): The cursor returned in the paged response
                from the previous call to this endpoint.  Provide this cursor
                to retrieve the next page of results for your original
                request.  For more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            limit (int, optional): The maximum number of results to return in
                a single paged response. This limit is advisory.  The response
                might contain more or fewer results. The minimum value is 1
                and the maximum value is 100.  The default value is 20. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).

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
            .path('/v2/orders/custom-attribute-definitions')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('visibility_filter')
                         .value(visibility_filter))
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

    def create_order_custom_attribute_definition(self,
                                                 body):
        """Does a POST request to /v2/orders/custom-attribute-definitions.

        Creates an order-related custom attribute definition.  Use this
        endpoint to
        define a custom attribute that can be associated with orders.
        After creating a custom attribute definition, you can set the custom
        attribute for orders
        in the Square seller account.

        Args:
            body (CreateOrderCustomAttributeDefinitionRequest): An object
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
            .path('/v2/orders/custom-attribute-definitions')
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

    def delete_order_custom_attribute_definition(self,
                                                 key):
        """Does a DELETE request to /v2/orders/custom-attribute-definitions/{key}.

        Deletes an order-related [custom attribute
        definition]($m/CustomAttributeDefinition) from a Square seller
        account.
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
            .path('/v2/orders/custom-attribute-definitions/{key}')
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

    def retrieve_order_custom_attribute_definition(self,
                                                   key,
                                                   version=None):
        """Does a GET request to /v2/orders/custom-attribute-definitions/{key}.

        Retrieves an order-related [custom attribute
        definition]($m/CustomAttributeDefinition) from a Square seller
        account.
        To retrieve a custom attribute definition created by another
        application, the `visibility`
        setting must be `VISIBILITY_READ_ONLY` or
        `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom
        attributes
        (also known as custom fields) are always set to
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            key (str): The key of the custom attribute definition to
                retrieve.
            version (int, optional): To enable [optimistic
                concurrency](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/optimistic-concurrency) control, include
                this optional field and specify the current version of the
                custom attribute.

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
            .path('/v2/orders/custom-attribute-definitions/{key}')
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

    def update_order_custom_attribute_definition(self,
                                                 key,
                                                 body):
        """Does a PUT request to /v2/orders/custom-attribute-definitions/{key}.

        Updates an order-related custom attribute definition for a Square
        seller account.
        Only the definition owner can update a custom attribute definition.
        Note that sellers can view all custom attributes in exported customer
        data, including those set to `VISIBILITY_HIDDEN`.

        Args:
            key (str): The key of the custom attribute definition to update.
            body (UpdateOrderCustomAttributeDefinitionRequest): An object
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
            .path('/v2/orders/custom-attribute-definitions/{key}')
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

    def bulk_delete_order_custom_attributes(self,
                                            body):
        """Does a POST request to /v2/orders/custom-attributes/bulk-delete.

        Deletes order [custom attributes]($m/CustomAttribute) as a bulk
        operation.
        Use this endpoint to delete one or more custom attributes from one or
        more orders.
        A custom attribute is based on a custom attribute definition in a
        Square seller account.  (To create a
        custom attribute definition, use the
        [CreateOrderCustomAttributeDefinition]($e/OrderCustomAttributes/CreateO
        rderCustomAttributeDefinition) endpoint.)
        This `BulkDeleteOrderCustomAttributes` endpoint accepts a map of 1 to
        25 individual delete
        requests and returns a map of individual delete responses. Each delete
        request has a unique ID
        and provides an order ID and custom attribute. Each delete response is
        returned with the ID
        of the corresponding request.
        To delete a custom attribute owned by another application, the
        `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined
        custom attributes
        (also known as custom fields) are always set to
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            body (BulkDeleteOrderCustomAttributesRequest): An object
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
            .path('/v2/orders/custom-attributes/bulk-delete')
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

    def bulk_upsert_order_custom_attributes(self,
                                            body):
        """Does a POST request to /v2/orders/custom-attributes/bulk-upsert.

        Creates or updates order [custom attributes]($m/CustomAttribute) as a
        bulk operation.
        Use this endpoint to delete one or more custom attributes from one or
        more orders.
        A custom attribute is based on a custom attribute definition in a
        Square seller account.  (To create a
        custom attribute definition, use the
        [CreateOrderCustomAttributeDefinition]($e/OrderCustomAttributes/CreateO
        rderCustomAttributeDefinition) endpoint.)
        This `BulkUpsertOrderCustomAttributes` endpoint accepts a map of 1 to
        25 individual upsert
        requests and returns a map of individual upsert responses. Each upsert
        request has a unique ID
        and provides an order ID and custom attribute. Each upsert response is
        returned with the ID
        of the corresponding request.
        To create or update a custom attribute owned by another application,
        the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined
        custom attributes
        (also known as custom fields) are always set to
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            body (BulkUpsertOrderCustomAttributesRequest): An object
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
            .path('/v2/orders/custom-attributes/bulk-upsert')
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

    def list_order_custom_attributes(self,
                                     order_id,
                                     visibility_filter=None,
                                     cursor=None,
                                     limit=None,
                                     with_definitions=False):
        """Does a GET request to /v2/orders/{order_id}/custom-attributes.

        Lists the [custom attributes]($m/CustomAttribute) associated with an
        order.
        You can use the `with_definitions` query parameter to also retrieve
        custom attribute definitions
        in the same call.
        When all response pages are retrieved, the results include all custom
        attributes that are
        visible to the requesting application, including those that are owned
        by other applications
        and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            order_id (str): The ID of the target [order](entity:Order).
            visibility_filter (VisibilityFilter, optional): Requests that all
                of the custom attributes be returned, or only those that are
                read-only or read-write.
            cursor (str, optional): The cursor returned in the paged response
                from the previous call to this endpoint.  Provide this cursor
                to retrieve the next page of results for your original
                request.  For more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            limit (int, optional): The maximum number of results to return in
                a single paged response. This limit is advisory.  The response
                might contain more or fewer results. The minimum value is 1
                and the maximum value is 100.  The default value is 20. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            with_definitions (bool, optional): Indicates whether to return the
                [custom attribute
                definition](entity:CustomAttributeDefinition) in the
                `definition` field of each custom attribute. Set this
                parameter to `true` to get the name and description of each
                custom attribute,  information about the data type, or other
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
            .path('/v2/orders/{order_id}/custom-attributes')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('order_id')
                            .value(order_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('visibility_filter')
                         .value(visibility_filter))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
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

    def delete_order_custom_attribute(self,
                                      order_id,
                                      custom_attribute_key):
        """Does a DELETE request to /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}.

        Deletes a [custom attribute]($m/CustomAttribute) associated with a
        customer profile.
        To delete a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom
        attributes
        (also known as custom fields) are always set to
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            order_id (str): The ID of the target [order](entity:Order).
            custom_attribute_key (str): The key of the custom attribute to
                delete.  This key must match the key of an existing custom
                attribute definition.

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
            .path('/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('order_id')
                            .value(order_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('custom_attribute_key')
                            .value(custom_attribute_key)
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

    def retrieve_order_custom_attribute(self,
                                        order_id,
                                        custom_attribute_key,
                                        version=None,
                                        with_definition=False):
        """Does a GET request to /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}.

        Retrieves a [custom attribute]($m/CustomAttribute) associated with an
        order.
        You can use the `with_definition` query parameter to also retrieve the
        custom attribute definition
        in the same call.
        To retrieve a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that
        seller-defined custom attributes
        also known as custom fields) are always set to
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            order_id (str): The ID of the target [order](entity:Order).
            custom_attribute_key (str): The key of the custom attribute to
                retrieve.  This key must match the key of an existing custom
                attribute definition.
            version (int, optional): To enable [optimistic
                concurrency](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/optimistic-concurrency) control, include
                this optional field and specify the current version of the
                custom attribute.
            with_definition (bool, optional): Indicates whether to return the
                [custom attribute
                definition](entity:CustomAttributeDefinition) in the
                `definition` field of each  custom attribute. Set this
                parameter to `true` to get the name and description of each
                custom attribute,  information about the data type, or other
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
            .path('/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('order_id')
                            .value(order_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('custom_attribute_key')
                            .value(custom_attribute_key)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
            .query_param(Parameter()
                         .key('with_definition')
                         .value(with_definition))
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

    def upsert_order_custom_attribute(self,
                                      order_id,
                                      custom_attribute_key,
                                      body):
        """Does a POST request to /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}.

        Creates or updates a [custom attribute]($m/CustomAttribute) for an
        order.
        Use this endpoint to set the value of a custom attribute for a
        specific order.
        A custom attribute is based on a custom attribute definition in a
        Square seller account. (To create a
        custom attribute definition, use the
        [CreateOrderCustomAttributeDefinition]($e/OrderCustomAttributes/CreateO
        rderCustomAttributeDefinition) endpoint.)
        To create or update a custom attribute owned by another application,
        the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined
        custom attributes
        (also known as custom fields) are always set to
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            order_id (str): The ID of the target [order](entity:Order).
            custom_attribute_key (str): The key of the custom attribute to
                create or update.  This key must match the key  of an existing
                custom attribute definition.
            body (UpsertOrderCustomAttributeRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

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
            .path('/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('order_id')
                            .value(order_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('custom_attribute_key')
                            .value(custom_attribute_key)
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
