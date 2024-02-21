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


class CustomersApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(CustomersApi, self).__init__(config)

    def list_customers(self,
                       cursor=None,
                       limit=None,
                       sort_field=None,
                       sort_order=None,
                       count=False):
        """Does a GET request to /v2/customers.

        Lists customer profiles associated with a Square account.
        Under normal operating conditions, newly created or updated customer
        profiles become available
        for the listing operation in well under 30 seconds. Occasionally,
        propagation of the new or updated
        profiles can take closer to one minute or longer, especially during
        network incidents and outages.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for your original query.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            limit (int, optional): The maximum number of results to return in
                a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less
                than 1 or greater than 100, Square returns a `400
                VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default
                value is 100.  For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            sort_field (CustomerSortField, optional): Indicates how customers
                should be sorted.  The default value is `DEFAULT`.
            sort_order (SortOrder, optional): Indicates whether customers
                should be sorted in ascending (`ASC`) or descending (`DESC`)
                order.  The default value is `ASC`.
            count (bool, optional): Indicates whether to return the total
                count of customers in the `count` field of the response.  The
                default value is `false`.

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
            .path('/v2/customers')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('sort_field')
                         .value(sort_field))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
            .query_param(Parameter()
                         .key('count')
                         .value(count))
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

    def create_customer(self,
                        body):
        """Does a POST request to /v2/customers.

        Creates a new customer for a business.
        You must provide at least one of the following values in your request
        to this
        endpoint:
        - `given_name`
        - `family_name`
        - `company_name`
        - `email_address`
        - `phone_number`

        Args:
            body (CreateCustomerRequest): An object containing the fields to
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
            .path('/v2/customers')
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

    def bulk_create_customers(self,
                              body):
        """Does a POST request to /v2/customers/bulk-create.

        Creates multiple [customer profiles]($m/Customer) for a business.
        This endpoint takes a map of individual create requests and returns a
        map of responses.
        You must provide at least one of the following values in each create
        request:
        - `given_name`
        - `family_name`
        - `company_name`
        - `email_address`
        - `phone_number`

        Args:
            body (BulkCreateCustomersRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
            .path('/v2/customers/bulk-create')
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

    def bulk_delete_customers(self,
                              body):
        """Does a POST request to /v2/customers/bulk-delete.

        Deletes multiple customer profiles.
        The endpoint takes a list of customer IDs and returns a map of
        responses.

        Args:
            body (BulkDeleteCustomersRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
            .path('/v2/customers/bulk-delete')
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

    def bulk_retrieve_customers(self,
                                body):
        """Does a POST request to /v2/customers/bulk-retrieve.

        Retrieves multiple customer profiles.
        This endpoint takes a list of customer IDs and returns a map of
        responses.

        Args:
            body (BulkRetrieveCustomersRequest): An object containing the
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
            .path('/v2/customers/bulk-retrieve')
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

    def bulk_update_customers(self,
                              body):
        """Does a POST request to /v2/customers/bulk-update.

        Updates multiple customer profiles.
        This endpoint takes a map of individual update requests and returns a
        map of responses.
        You cannot use this endpoint to change cards on file. To make changes,
        use the [Cards API]($e/Cards) or [Gift Cards API]($e/GiftCards).

        Args:
            body (BulkUpdateCustomersRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
            .path('/v2/customers/bulk-update')
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

    def search_customers(self,
                         body):
        """Does a POST request to /v2/customers/search.

        Searches the customer profiles associated with a Square account using
        one or more supported query filters.
        Calling `SearchCustomers` without any explicit query filter returns
        all
        customer profiles ordered alphabetically based on `given_name` and
        `family_name`.
        Under normal operating conditions, newly created or updated customer
        profiles become available
        for the search operation in well under 30 seconds. Occasionally,
        propagation of the new or updated
        profiles can take closer to one minute or longer, especially during
        network incidents and outages.

        Args:
            body (SearchCustomersRequest): An object containing the fields to
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
            .path('/v2/customers/search')
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

    def delete_customer(self,
                        customer_id,
                        version=None):
        """Does a DELETE request to /v2/customers/{customer_id}.

        Deletes a customer profile from a business. This operation also
        unlinks any associated cards on file.
        To delete a customer profile that was created by merging existing
        profiles, you must use the ID of the newly created profile.

        Args:
            customer_id (str): The ID of the customer to delete.
            version (long|int, optional): The current version of the customer
                profile.  As a best practice, you should include this
                parameter to enable [optimistic
                concurrency](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/optimistic-concurrency) control.  For more
                information, see [Delete a customer
                profile](https://developer.squareup.com/docs/customers-api/use-
                the-api/keep-records#delete-customer-profile).

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
            .path('/v2/customers/{customer_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
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

    def retrieve_customer(self,
                          customer_id):
        """Does a GET request to /v2/customers/{customer_id}.

        Returns details for a single customer.

        Args:
            customer_id (str): The ID of the customer to retrieve.

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
            .path('/v2/customers/{customer_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
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

    def update_customer(self,
                        customer_id,
                        body):
        """Does a PUT request to /v2/customers/{customer_id}.

        Updates a customer profile. This endpoint supports sparse updates, so
        only new or changed fields are required in the request.
        To add or update a field, specify the new value. To remove a field,
        specify `null`.
        To update a customer profile that was created by merging existing
        profiles, you must use the ID of the newly created profile.
        You cannot use this endpoint to change cards on file. To make changes,
        use the [Cards API]($e/Cards) or [Gift Cards API]($e/GiftCards).

        Args:
            customer_id (str): The ID of the customer to update.
            body (UpdateCustomerRequest): An object containing the fields to
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
            .path('/v2/customers/{customer_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
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

    @deprecated()
    def create_customer_card(self,
                             customer_id,
                             body):
        """Does a POST request to /v2/customers/{customer_id}/cards.

        Adds a card on file to an existing customer.
        As with charges, calls to `CreateCustomerCard` are idempotent.
        Multiple
        calls with the same card nonce return the same card record that was
        created
        with the provided nonce during the _first_ call.

        Args:
            customer_id (str): The Square ID of the customer profile the card
                is linked to.
            body (CreateCustomerCardRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
            .path('/v2/customers/{customer_id}/cards')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
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

    @deprecated()
    def delete_customer_card(self,
                             customer_id,
                             card_id):
        """Does a DELETE request to /v2/customers/{customer_id}/cards/{card_id}.

        Removes a card on file from a customer.

        Args:
            customer_id (str): The ID of the customer that the card on file
                belongs to.
            card_id (str): The ID of the card on file to delete.

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
            .path('/v2/customers/{customer_id}/cards/{card_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('card_id')
                            .value(card_id)
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

    def remove_group_from_customer(self,
                                   customer_id,
                                   group_id):
        """Does a DELETE request to /v2/customers/{customer_id}/groups/{group_id}.

        Removes a group membership from a customer.
        The customer is identified by the `customer_id` value
        and the customer group is identified by the `group_id` value.

        Args:
            customer_id (str): The ID of the customer to remove from the
                group.
            group_id (str): The ID of the customer group to remove the
                customer from.

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
            .path('/v2/customers/{customer_id}/groups/{group_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('group_id')
                            .value(group_id)
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

    def add_group_to_customer(self,
                              customer_id,
                              group_id):
        """Does a PUT request to /v2/customers/{customer_id}/groups/{group_id}.

        Adds a group membership to a customer.
        The customer is identified by the `customer_id` value
        and the customer group is identified by the `group_id` value.

        Args:
            customer_id (str): The ID of the customer to add to a group.
            group_id (str): The ID of the customer group to add the customer
                to.

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
            .path('/v2/customers/{customer_id}/groups/{group_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('group_id')
                            .value(group_id)
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
