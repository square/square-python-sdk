# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class InventoryApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(InventoryApi, self).__init__(config, call_back)

    def retrieve_inventory_adjustment(self,
                                      adjustment_id):
        """Does a GET request to /v2/inventory/adjustment/{adjustment_id}.

        Returns the [InventoryAdjustment](#type-inventoryadjustment) object
        with the provided `adjustment_id`.

        Args:
            adjustment_id (string): ID of the
                [InventoryAdjustment](#type-inventoryadjustment) to retrieve.

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
        _url_path = '/v2/inventory/adjustment/{adjustment_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'adjustment_id': {'value': adjustment_id, 'encode': True}
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def batch_change_inventory(self,
                               body):
        """Does a POST request to /v2/inventory/batch-change.

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

        # Prepare query URL
        _url_path = '/v2/inventory/batch-change'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def batch_retrieve_inventory_changes(self,
                                         body):
        """Does a POST request to /v2/inventory/batch-retrieve-changes.

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

        # Prepare query URL
        _url_path = '/v2/inventory/batch-retrieve-changes'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def batch_retrieve_inventory_counts(self,
                                        body):
        """Does a POST request to /v2/inventory/batch-retrieve-counts.

        Returns current counts for the provided
        [CatalogObject](#type-catalogobject)s at the requested
        [Location](#type-location)s.
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

        # Prepare query URL
        _url_path = '/v2/inventory/batch-retrieve-counts'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_inventory_physical_count(self,
                                          physical_count_id):
        """Does a GET request to /v2/inventory/physical-count/{physical_count_id}.

        Returns the [InventoryPhysicalCount](#type-inventoryphysicalcount)
        object with the provided `physical_count_id`.

        Args:
            physical_count_id (string): ID of the
                [InventoryPhysicalCount](#type-inventoryphysicalcount) to
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

        # Prepare query URL
        _url_path = '/v2/inventory/physical-count/{physical_count_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'physical_count_id': {'value': physical_count_id, 'encode': True}
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_inventory_count(self,
                                 catalog_object_id,
                                 location_ids=None,
                                 cursor=None):
        """Does a GET request to /v2/inventory/{catalog_object_id}.

        Retrieves the current calculated stock count for a given
        [CatalogObject](#type-catalogobject) at a given set of
        [Location](#type-location)s. Responses are paginated and unsorted.
        For more sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id (string): ID of the
                [CatalogObject](#type-catalogobject) to retrieve.
            location_ids (string, optional): The [Location](#type-location)
                IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for the original query.  See the
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

        # Prepare query URL
        _url_path = '/v2/inventory/{catalog_object_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'catalog_object_id': {'value': catalog_object_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_ids': location_ids,
            'cursor': cursor
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
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

    def retrieve_inventory_changes(self,
                                   catalog_object_id,
                                   location_ids=None,
                                   cursor=None):
        """Does a GET request to /v2/inventory/{catalog_object_id}/changes.

        Returns a set of physical counts and inventory adjustments for the
        provided [CatalogObject](#type-catalogobject) at the requested
        [Location](#type-location)s.
        Results are paginated and sorted in descending order according to
        their
        `occurred_at` timestamp (newest first).
        There are no limits on how far back the caller can page. This endpoint
        can be 
        used to display recent changes for a specific item. For more
        sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id (string): ID of the
                [CatalogObject](#type-catalogobject) to retrieve.
            location_ids (string, optional): The [Location](#type-location)
                IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for the original query.  See the
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

        # Prepare query URL
        _url_path = '/v2/inventory/{catalog_object_id}/changes'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'catalog_object_id': {'value': catalog_object_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_ids': location_ids,
            'cursor': cursor
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
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
