# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class CustomerCustomAttributesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(CustomerCustomAttributesApi, self).__init__(config, auth_managers)

    def list_customer_custom_attribute_definitions(self,
                                                   limit=None,
                                                   cursor=None):
        """Does a GET request to /v2/customers/custom-attribute-definitions.

        Lists the customer-related custom attribute definitions that belong to
        a Square seller account.
        When all response pages are retrieved, the results include all custom
        attribute definitions
        that are visible to the requesting application, including those that
        are created by other
        applications and set to `VISIBILITY_READ_ONLY` or
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            limit (int, optional): The maximum number of results to return in
                a single paged response. This limit is advisory. The response
                might contain more or fewer results. The minimum value is 1
                and the maximum value is 100. The default value is 20. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            cursor (string, optional): The cursor returned in the paged
                response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original
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

        # Prepare query URL
        _url_path = '/v2/customers/custom-attribute-definitions'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'limit': limit,
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

    def create_customer_custom_attribute_definition(self,
                                                    body):
        """Does a POST request to /v2/customers/custom-attribute-definitions.

        Creates a customer-related custom attribute definition for a Square
        seller account. Use this
        endpoint to define a custom attribute that can be associated with
        customer profiles.
        A custom attribute definition specifies the `key`, `visibility`,
        `schema`, and other properties
        for a custom attribute. After the definition is created, you can call
        [UpsertCustomerCustomAttribute]($e/CustomerCustomAttributes/UpsertCusto
        merCustomAttribute) or
        [BulkUpsertCustomerCustomAttributes]($e/CustomerCustomAttributes/BulkUp
        sertCustomerCustomAttributes)
        to set the custom attribute for customer profiles in the seller's
        Customer Directory.
        Sellers can view all custom attributes in exported customer data,
        including those set to
        `VISIBILITY_HIDDEN`.

        Args:
            body (CreateCustomerCustomAttributeDefinitionRequest): An object
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

        # Prepare query URL
        _url_path = '/v2/customers/custom-attribute-definitions'
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

    def delete_customer_custom_attribute_definition(self,
                                                    key):
        """Does a DELETE request to /v2/customers/custom-attribute-definitions/{key}.

        Deletes a customer-related custom attribute definition from a Square
        seller account.
        Deleting a custom attribute definition also deletes the corresponding
        custom attribute from
        all customer profiles in the seller's Customer Directory.
        Only the definition owner can delete a custom attribute definition.

        Args:
            key (string): The key of the custom attribute definition to
                delete.

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
        _url_path = '/v2/customers/custom-attribute-definitions/{key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'key': {'value': key, 'encode': True}
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

    def retrieve_customer_custom_attribute_definition(self,
                                                      key,
                                                      version=None):
        """Does a GET request to /v2/customers/custom-attribute-definitions/{key}.

        Retrieves a customer-related custom attribute definition from a Square
        seller account.
        To retrieve a custom attribute definition created by another
        application, the `visibility`
        setting must be `VISIBILITY_READ_ONLY` or
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            key (string): The key of the custom attribute definition to
                retrieve. If the requesting application is not the definition
                owner, you must use the qualified key.
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

        # Prepare query URL
        _url_path = '/v2/customers/custom-attribute-definitions/{key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'key': {'value': key, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'version': version
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

    def update_customer_custom_attribute_definition(self,
                                                    key,
                                                    body):
        """Does a PUT request to /v2/customers/custom-attribute-definitions/{key}.

        Updates a customer-related custom attribute definition for a Square
        seller account.
        Use this endpoint to update the following fields: `name`,
        `description`, `visibility`, or the
        `schema` for a `Selection` data type.
        Only the definition owner can update a custom attribute definition.
        Note that sellers can view
        all custom attributes in exported customer data, including those set
        to `VISIBILITY_HIDDEN`.

        Args:
            key (string): The key of the custom attribute definition to
                update.
            body (UpdateCustomerCustomAttributeDefinitionRequest): An object
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

        # Prepare query URL
        _url_path = '/v2/customers/custom-attribute-definitions/{key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'key': {'value': key, 'encode': True}
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
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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

    def bulk_upsert_customer_custom_attributes(self,
                                               body):
        """Does a POST request to /v2/customers/custom-attributes/bulk-upsert.

        Creates or updates custom attributes for customer profiles as a bulk
        operation.
        Use this endpoint to set the value of one or more custom attributes
        for one or more customer profiles.
        A custom attribute is based on a custom attribute definition in a
        Square seller account, which is
        created using the
        [CreateCustomerCustomAttributeDefinition]($e/CustomerCustomAttributes/C
        reateCustomerCustomAttributeDefinition) endpoint.
        This `BulkUpsertCustomerCustomAttributes` endpoint accepts a map of 1
        to 25 individual upsert 
        requests and returns a map of individual upsert responses. Each upsert
        request has a unique ID 
        and provides a customer ID and custom attribute. Each upsert response
        is returned with the ID 
        of the corresponding request.
        To create or update a custom attribute owned by another application,
        the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            body (BulkUpsertCustomerCustomAttributesRequest): An object
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

        # Prepare query URL
        _url_path = '/v2/customers/custom-attributes/bulk-upsert'
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

    def list_customer_custom_attributes(self,
                                        customer_id,
                                        limit=None,
                                        cursor=None,
                                        with_definitions=False):
        """Does a GET request to /v2/customers/{customer_id}/custom-attributes.

        Lists the custom attributes associated with a customer profile.
        You can use the `with_definitions` query parameter to also retrieve
        custom attribute definitions
        in the same call.
        When all response pages are retrieved, the results include all custom
        attributes that are
        visible to the requesting application, including those that are owned
        by other applications
        and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            customer_id (string): The ID of the target [customer
                profile]($m/Customer).
            limit (int, optional): The maximum number of results to return in
                a single paged response. This limit is advisory. The response
                might contain more or fewer results. The minimum value is 1
                and the maximum value is 100. The default value is 20. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            cursor (string, optional): The cursor returned in the paged
                response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original
                request. For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            with_definitions (bool, optional): Indicates whether to return the
                [custom attribute definition]($m/CustomAttributeDefinition) in
                the `definition` field of each custom attribute. Set this
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

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/custom-attributes'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'limit': limit,
            'cursor': cursor,
            'with_definitions': with_definitions
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

    def delete_customer_custom_attribute(self,
                                         customer_id,
                                         key):
        """Does a DELETE request to /v2/customers/{customer_id}/custom-attributes/{key}.

        Deletes a custom attribute associated with a customer profile.
        To delete a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            customer_id (string): The ID of the target [customer
                profile]($m/Customer).
            key (string): The key of the custom attribute to delete. This key
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

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/custom-attributes/{key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True},
            'key': {'value': key, 'encode': True}
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

    def retrieve_customer_custom_attribute(self,
                                           customer_id,
                                           key,
                                           with_definition=False,
                                           version=None):
        """Does a GET request to /v2/customers/{customer_id}/custom-attributes/{key}.

        Retrieves a custom attribute associated with a customer profile.
        You can use the `with_definition` query parameter to also retrieve the
        custom attribute definition
        in the same call.
        To retrieve a custom attribute owned by another application, the
        `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            customer_id (string): The ID of the target [customer
                profile]($m/Customer).
            key (string): The key of the custom attribute to retrieve. This
                key must match the `key` of a custom attribute definition in
                the Square seller account. If the requesting application is
                not the definition owner, you must use the qualified key.
            with_definition (bool, optional): Indicates whether to return the
                [custom attribute definition]($m/CustomAttributeDefinition) in
                the `definition` field of the custom attribute. Set this
                parameter to `true` to get the name and description of the
                custom attribute, information about the data type, or other
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

        # Prepare query URL
        _url_path = '/v2/customers/{customer_id}/custom-attributes/{key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True},
            'key': {'value': key, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'with_definition': with_definition,
            'version': version
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

    def upsert_customer_custom_attribute(self,
                                         customer_id,
                                         key,
                                         body):
        """Does a POST request to /v2/customers/{customer_id}/custom-attributes/{key}.

        Creates or updates a custom attribute for a customer profile.
        Use this endpoint to set the value of a custom attribute for a
        specified customer profile.
        A custom attribute is based on a custom attribute definition in a
        Square seller account, which
        is created using the
        [CreateCustomerCustomAttributeDefinition]($e/CustomerCustomAttributes/C
        reateCustomerCustomAttributeDefinition) endpoint.
        To create or update a custom attribute owned by another application,
        the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Args:
            customer_id (string): The ID of the target [customer
                profile]($m/Customer).
            key (string): The key of the custom attribute to create or update.
                This key must match the `key` of a custom attribute definition
                in the Square seller account. If the requesting application is
                not the definition owner, you must use the qualified key.
            body (UpsertCustomerCustomAttributeRequest): An object containing
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
        _url_path = '/v2/customers/{customer_id}/custom-attributes/{key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'customer_id': {'value': customer_id, 'encode': True},
            'key': {'value': key, 'encode': True}
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
