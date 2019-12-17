# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class CatalogApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(CatalogApi, self).__init__(config, call_back)

    def batch_delete_catalog_objects(self,
                                     body):
        """Does a POST request to /v2/catalog/batch-delete.

        Deletes a set of [CatalogItem](#type-catalogitem)s based on the
        provided list of target IDs and returns a set of successfully deleted
        IDs in
        the response. Deletion is a cascading event such that all children of
        the
        targeted object are also deleted. For example, deleting a CatalogItem
        will
        also delete all of its
        [CatalogItemVariation](#type-catalogitemvariation)
        children.
        `BatchDeleteCatalogObjects` succeeds even if only a portion of the
        targeted
        IDs can be deleted. The response will only include IDs that were
        actually deleted.

        Args:
            body (BatchDeleteCatalogObjectsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            BatchDeleteCatalogObjectsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/batch-delete'
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

    def batch_retrieve_catalog_objects(self,
                                       body):
        """Does a POST request to /v2/catalog/batch-retrieve.

        Returns a set of objects based on the provided ID.
        Each [CatalogItem](#type-catalogitem) returned in the set includes all
        of its
        child information including: all of its
        [CatalogItemVariation](#type-catalogitemvariation) objects, references
        to
        its [CatalogModifierList](#type-catalogmodifierlist) objects, and the
        ids of
        any [CatalogTax](#type-catalogtax) objects that apply to it.

        Args:
            body (BatchRetrieveCatalogObjectsRequest): An object containing
                the fields to POST for the request.  See the corresponding
                object definition for field details.

        Returns:
            BatchRetrieveCatalogObjectsResponse: Response from the API.
                Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/batch-retrieve'
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

    def batch_upsert_catalog_objects(self,
                                     body):
        """Does a POST request to /v2/catalog/batch-upsert.

        Creates or updates up to 10,000 target objects based on the provided
        list of objects. The target objects are grouped into batches and each
        batch is
        inserted/updated in an all-or-nothing manner. If an object within a
        batch is
        malformed in some way, or violates a database constraint, the entire
        batch
        containing that item will be disregarded. However, other batches in
        the same
        request may still succeed. Each batch may contain up to 1,000 objects,
        and
        batches will be processed in order as long as the total object count
        for the
        request (items, variations, modifier lists, discounts, and taxes) is
        no more
        than 10,000.

        Args:
            body (BatchUpsertCatalogObjectsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            BatchUpsertCatalogObjectsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/batch-upsert'
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

    def create_catalog_image(self,
                             request=None,
                             image_file=None):
        """Does a POST request to /v2/catalog/images.

        Upload an image file to create a new
        [CatalogImage](#type-catalogimage) for an existing
        [CatalogObject](#type-catalogobject). Images can be uploaded and
        linked in this request or created independently
        (without an object assignment) and linked to a
        [CatalogObject](#type-catalogobject) at a later time.
        CreateCatalogImage accepts HTTP multipart/form-data requests with a
        JSON part and an image file part in
        JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB. The
        following is an example of such an HTTP request:
        ```
        POST /v2/catalog/images
        Accept: application/json
        Content-Type: multipart/form-data;boundary="boundary"
        Square-Version: XXXX-XX-XX
        Authorization: Bearer {ACCESS_TOKEN}
        --boundary
        Content-Disposition: form-data; name="request"
        Content-Type: application/json
        {
        "idempotency_key":"528dea59-7bfb-43c1-bd48-4a6bba7dd61f86",
        "object_id": "ND6EA5AAJEO5WL3JNNIAQA32",
        "image":{
        "id":"#TEMP_ID",
        "type":"IMAGE",
        "image_data":{
        "caption":"A picture of a cup of coffee"
        }
        }
        }
        --boundary
        Content-Disposition: form-data; name="image"; filename="Coffee.jpg"
        Content-Type: image/jpeg
        {ACTUAL_IMAGE_BYTES}
        --boundary
        ```
        Additional information and an example cURL request can be found in the
        [Create a Catalog Image
        recipe](https://developer.squareup.com/docs/more-apis/catalog/cookbook/
        create-catalog-images).

        Args:
            request (CreateCatalogImageRequest, optional): TODO: type
                description here.
            image_file (string, optional): TODO: type description here.

        Returns:
            CreateCatalogImageResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/images'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'request': (None, APIHelper.json_serialize(request), 'application/json; charset=utf-8'),
            'image_file': (image_file.name, image_file, 'image/jpeg')
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, files=_files)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def catalog_info(self):
        """Does a GET request to /v2/catalog/info.

        Returns information about the Square Catalog API, such as batch size
        limits for `BatchUpsertCatalogObjects`.

        Returns:
            CatalogInfoResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/info'
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

    def list_catalog(self,
                     cursor=None,
                     types=None):
        """Does a GET request to /v2/catalog/list.

        Returns a list of [CatalogObject](#type-catalogobject)s that includes
        all objects of a set of desired types (for example, all
        [CatalogItem](#type-catalogitem)
        and [CatalogTax](#type-catalogtax) objects) in the catalog. The
        `types` parameter
        is specified as a comma-separated list of valid
        [CatalogObject](#type-catalogobject) types:
        `ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`,
        `DISCOUNT`, `TAX`, `IMAGE`.
        __Important:__ ListCatalog does not return deleted catalog items. To
        retrieve
        deleted catalog items, use SearchCatalogObjects and set
        `include_deleted_objects`
        to `true`.

        Args:
            cursor (string, optional): The pagination cursor returned in the
                previous response. Leave unset for an initial request. See
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination) for more information.
            types (string, optional): An optional case-insensitive,
                comma-separated list of object types to retrieve, for example
                `ITEM,ITEM_VARIATION,CATEGORY,IMAGE`.  The legal values are
                taken from the CatalogObjectType enum: `ITEM`,
                `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`, `MODIFIER`,
                `MODIFIER_LIST`, or `IMAGE`.

        Returns:
            ListCatalogResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/list'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'types': types
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

    def upsert_catalog_object(self,
                              body):
        """Does a POST request to /v2/catalog/object.

        Creates or updates the target [CatalogObject](#type-catalogobject).

        Args:
            body (UpsertCatalogObjectRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            UpsertCatalogObjectResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/object'
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

    def delete_catalog_object(self,
                              object_id):
        """Does a DELETE request to /v2/catalog/object/{object_id}.

        Deletes a single [CatalogObject](#type-catalogobject) based on the
        provided ID and returns the set of successfully deleted IDs in the
        response.
        Deletion is a cascading event such that all children of the targeted
        object
        are also deleted. For example, deleting a
        [CatalogItem](#type-catalogitem)
        will also delete all of its
        [CatalogItemVariation](#type-catalogitemvariation) children.

        Args:
            object_id (string): The ID of the catalog object to be deleted.
                When an object is deleted, other objects in the graph that
                depend on that object will be deleted as well (for example,
                deleting a catalog item will delete its catalog item
                variations).

        Returns:
            DeleteCatalogObjectResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/object/{object_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'object_id': object_id
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_catalog_object(self,
                                object_id,
                                include_related_objects=None):
        """Does a GET request to /v2/catalog/object/{object_id}.

        Returns a single [CatalogItem](#type-catalogitem) as a
        [CatalogObject](#type-catalogobject) based on the provided ID. The
        returned
        object includes all of the relevant [CatalogItem](#type-catalogitem)
        information including:
        [CatalogItemVariation](#type-catalogitemvariation)
        children, references to its
        [CatalogModifierList](#type-catalogmodifierlist) objects, and the ids
        of
        any [CatalogTax](#type-catalogtax) objects that apply to it.

        Args:
            object_id (string): The object ID of any type of catalog objects
                to be retrieved.
            include_related_objects (bool, optional): If `true`, the response
                will include additional objects that are related to the
                requested object, as follows:  If the `object` field of the
                response contains a CatalogItem, its associated
                CatalogCategory, CatalogTax objects, CatalogImages and
                CatalogModifierLists will be returned in the `related_objects`
                field of the response. If the `object` field of the response
                contains a CatalogItemVariation, its parent CatalogItem will
                be returned in the `related_objects` field of the response. 
                Default value: `false`

        Returns:
            RetrieveCatalogObjectResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/object/{object_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'object_id': object_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'include_related_objects': include_related_objects
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

    def search_catalog_objects(self,
                               body):
        """Does a POST request to /v2/catalog/search.

        Queries the targeted catalog using a variety of query types:
        [CatalogQuerySortedAttribute](#type-catalogquerysortedattribute),
        [CatalogQueryExact](#type-catalogqueryexact),
        [CatalogQueryRange](#type-catalogqueryrange),
        [CatalogQueryText](#type-catalogquerytext),
        [CatalogQueryItemsForTax](#type-catalogqueryitemsfortax), and
        [CatalogQueryItemsForModifierList](#type-catalogqueryitemsformodifierli
        st).
        --
        --
        Future end of the above comment:
        [CatalogQueryItemsForTax](#type-catalogqueryitemsfortax),
        [CatalogQueryItemsForModifierList](#type-catalogqueryitemsformodifierli
        st),
        [CatalogQueryItemsForItemOptions](#type-catalogqueryitemsforitemoptions
        ), and
        [CatalogQueryItemVariationsForItemOptionValues](#type-catalogqueryitemv
        ariationsforitemoptionvalues).

        Args:
            body (SearchCatalogObjectsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            SearchCatalogObjectsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/search'
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

    def update_item_modifier_lists(self,
                                   body):
        """Does a POST request to /v2/catalog/update-item-modifier-lists.

        Updates the [CatalogModifierList](#type-catalogmodifierlist) objects
        that apply to the targeted [CatalogItem](#type-catalogitem) without
        having
        to perform an upsert on the entire item.

        Args:
            body (UpdateItemModifierListsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            UpdateItemModifierListsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/update-item-modifier-lists'
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

    def update_item_taxes(self,
                          body):
        """Does a POST request to /v2/catalog/update-item-taxes.

        Updates the [CatalogTax](#type-catalogtax) objects that apply to the
        targeted [CatalogItem](#type-catalogitem) without having to perform
        an
        upsert on the entire item.

        Args:
            body (UpdateItemTaxesRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            UpdateItemTaxesResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/update-item-taxes'
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
