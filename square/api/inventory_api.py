# -*- coding: utf-8 -*-

from deprecation import deprecated
from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class InventoryApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(InventoryApi, self).__init__(config)

    @deprecated()
    def deprecated_retrieve_inventory_adjustment(self,
                                                 adjustment_id):
        """Does a GET request to /v2/inventory/adjustment/{adjustment_id}.

        Deprecated version of
        [RetrieveInventoryAdjustment](api-endpoint:Inventory-RetrieveInventoryA
        djustment) after the endpoint URL
        is updated to conform to the standard convention.

        Args:
            adjustment_id (str): ID of the
                [InventoryAdjustment](entity:InventoryAdjustment) to
                retrieve.

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
            .path('/v2/inventory/adjustment/{adjustment_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('adjustment_id')
                            .value(adjustment_id)
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

    def retrieve_inventory_adjustment(self,
                                      adjustment_id):
        """Does a GET request to /v2/inventory/adjustments/{adjustment_id}.

        Returns the [InventoryAdjustment]($m/InventoryAdjustment) object
        with the provided `adjustment_id`.

        Args:
            adjustment_id (str): ID of the
                [InventoryAdjustment](entity:InventoryAdjustment) to
                retrieve.

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
            .path('/v2/inventory/adjustments/{adjustment_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('adjustment_id')
                            .value(adjustment_id)
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

    @deprecated()
    def deprecated_batch_change_inventory(self,
                                          body):
        """Does a POST request to /v2/inventory/batch-change.

        Deprecated version of
        [BatchChangeInventory](api-endpoint:Inventory-BatchChangeInventory)
        after the endpoint URL
        is updated to conform to the standard convention.

        Args:
            body (BatchChangeInventoryRequest): An object containing the
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
            .path('/v2/inventory/batch-change')
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

    @deprecated()
    def deprecated_batch_retrieve_inventory_changes(self,
                                                    body):
        """Does a POST request to /v2/inventory/batch-retrieve-changes.

        Deprecated version of
        [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInv
        entoryChanges) after the endpoint URL
        is updated to conform to the standard convention.

        Args:
            body (BatchRetrieveInventoryChangesRequest): An object containing
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
            .path('/v2/inventory/batch-retrieve-changes')
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

    @deprecated()
    def deprecated_batch_retrieve_inventory_counts(self,
                                                   body):
        """Does a POST request to /v2/inventory/batch-retrieve-counts.

        Deprecated version of
        [BatchRetrieveInventoryCounts](api-endpoint:Inventory-BatchRetrieveInve
        ntoryCounts) after the endpoint URL
        is updated to conform to the standard convention.

        Args:
            body (BatchRetrieveInventoryCountsRequest): An object containing
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
            .path('/v2/inventory/batch-retrieve-counts')
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

    def batch_change_inventory(self,
                               body):
        """Does a POST request to /v2/inventory/changes/batch-create.

        Applies adjustments and counts to the provided item quantities.
        On success: returns the current calculated counts for all objects
        referenced in the request.
        On failure: returns a list of related errors.

        Args:
            body (BatchChangeInventoryRequest): An object containing the
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
            .path('/v2/inventory/changes/batch-create')
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

    def batch_retrieve_inventory_changes(self,
                                         body):
        """Does a POST request to /v2/inventory/changes/batch-retrieve.

        Returns historical physical counts and adjustments based on the
        provided filter criteria.
        Results are paginated and sorted in ascending order according their
        `occurred_at` timestamp (oldest first).
        BatchRetrieveInventoryChanges is a catch-all query endpoint for
        queries
        that cannot be handled by other, simpler endpoints.

        Args:
            body (BatchRetrieveInventoryChangesRequest): An object containing
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
            .path('/v2/inventory/changes/batch-retrieve')
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

    def batch_retrieve_inventory_counts(self,
                                        body):
        """Does a POST request to /v2/inventory/counts/batch-retrieve.

        Returns current counts for the provided
        [CatalogObject]($m/CatalogObject)s at the requested
        [Location]($m/Location)s.
        Results are paginated and sorted in descending order according to
        their
        `calculated_at` timestamp (newest first).
        When `updated_after` is specified, only counts that have changed since
        that
        time (based on the server timestamp for the most recent change) are
        returned. This allows clients to perform a "sync" operation, for
        example
        in response to receiving a Webhook notification.

        Args:
            body (BatchRetrieveInventoryCountsRequest): An object containing
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
            .path('/v2/inventory/counts/batch-retrieve')
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

    @deprecated()
    def deprecated_retrieve_inventory_physical_count(self,
                                                     physical_count_id):
        """Does a GET request to /v2/inventory/physical-count/{physical_count_id}.

        Deprecated version of
        [RetrieveInventoryPhysicalCount](api-endpoint:Inventory-RetrieveInvento
        ryPhysicalCount) after the endpoint URL
        is updated to conform to the standard convention.

        Args:
            physical_count_id (str): ID of the
                [InventoryPhysicalCount](entity:InventoryPhysicalCount) to
                retrieve.

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
            .path('/v2/inventory/physical-count/{physical_count_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('physical_count_id')
                            .value(physical_count_id)
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

    def retrieve_inventory_physical_count(self,
                                          physical_count_id):
        """Does a GET request to /v2/inventory/physical-counts/{physical_count_id}.

        Returns the [InventoryPhysicalCount]($m/InventoryPhysicalCount)
        object with the provided `physical_count_id`.

        Args:
            physical_count_id (str): ID of the
                [InventoryPhysicalCount](entity:InventoryPhysicalCount) to
                retrieve.

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
            .path('/v2/inventory/physical-counts/{physical_count_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('physical_count_id')
                            .value(physical_count_id)
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

    def retrieve_inventory_transfer(self,
                                    transfer_id):
        """Does a GET request to /v2/inventory/transfers/{transfer_id}.

        Returns the [InventoryTransfer]($m/InventoryTransfer) object
        with the provided `transfer_id`.

        Args:
            transfer_id (str): ID of the
                [InventoryTransfer](entity:InventoryTransfer) to retrieve.

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
            .path('/v2/inventory/transfers/{transfer_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('transfer_id')
                            .value(transfer_id)
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

    def retrieve_inventory_count(self,
                                 catalog_object_id,
                                 location_ids=None,
                                 cursor=None):
        """Does a GET request to /v2/inventory/{catalog_object_id}.

        Retrieves the current calculated stock count for a given
        [CatalogObject]($m/CatalogObject) at a given set of
        [Location]($m/Location)s. Responses are paginated and unsorted.
        For more sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id (str): ID of the
                [CatalogObject](entity:CatalogObject) to retrieve.
            location_ids (str, optional): The [Location](entity:Location) IDs
                to look up as a comma-separated list. An empty list queries
                all locations.
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this to retrieve the next set
                of results for the original query.  See the
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination) guide for more information.

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
            .path('/v2/inventory/{catalog_object_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('catalog_object_id')
                            .value(catalog_object_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('location_ids')
                         .value(location_ids))
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

    @deprecated()
    def retrieve_inventory_changes(self,
                                   catalog_object_id,
                                   location_ids=None,
                                   cursor=None):
        """Does a GET request to /v2/inventory/{catalog_object_id}/changes.

        Returns a set of physical counts and inventory adjustments for the
        provided [CatalogObject](entity:CatalogObject) at the requested
        [Location](entity:Location)s.
        You can achieve the same result by calling
        [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInv
        entoryChanges)
        and having the `catalog_object_ids` list contain a single element of
        the `CatalogObject` ID.
        Results are paginated and sorted in descending order according to
        their
        `occurred_at` timestamp (newest first).
        There are no limits on how far back the caller can page. This endpoint
        can be
        used to display recent changes for a specific item. For more
        sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id (str): ID of the
                [CatalogObject](entity:CatalogObject) to retrieve.
            location_ids (str, optional): The [Location](entity:Location) IDs
                to look up as a comma-separated list. An empty list queries
                all locations.
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this to retrieve the next set
                of results for the original query.  See the
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination) guide for more information.

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
            .path('/v2/inventory/{catalog_object_id}/changes')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('catalog_object_id')
                            .value(catalog_object_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('location_ids')
                         .value(location_ids))
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
