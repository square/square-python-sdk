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


class InvoicesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(InvoicesApi, self).__init__(config)

    def list_invoices(self,
                      location_id,
                      cursor=None,
                      limit=None):
        """Does a GET request to /v2/invoices.

        Returns a list of invoices for a given location. The response 
        is paginated. If truncated, the response includes a `cursor` that you 
                use in a subsequent request to retrieve the next set of invoices.

        Args:
            location_id (string): The ID of the location for which to list
                invoices.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint.  Provide this cursor to
                retrieve the next set of results for your original query.  For
                more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            limit (int, optional): The maximum number of invoices to return
                (200 is the maximum `limit`).  If not provided, the server
                uses a default limit of 100 invoices.

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
            .path('/v2/invoices')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
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

    def create_invoice(self,
                       body):
        """Does a POST request to /v2/invoices.

        Creates a draft [invoice]($m/Invoice) 
        for an order created using the Orders API.
        A draft invoice remains in your account and no action is taken. 
        You must publish the invoice before Square can process it (send it to
        the customer's email address or charge the customer’s card on file).

        Args:
            body (CreateInvoiceRequest): An object containing the fields to
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
            .path('/v2/invoices')
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

    def search_invoices(self,
                        body):
        """Does a POST request to /v2/invoices/search.

        Searches for invoices from a location specified in 
        the filter. You can optionally specify customers in the filter for
        whom to 
        retrieve invoices. In the current implementation, you can only specify
        one location and 
        optionally one customer.
        The response is paginated. If truncated, the response includes a
        `cursor` 
        that you use in a subsequent request to retrieve the next set of
        invoices.

        Args:
            body (SearchInvoicesRequest): An object containing the fields to
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
            .path('/v2/invoices/search')
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

    def delete_invoice(self,
                       invoice_id,
                       version=None):
        """Does a DELETE request to /v2/invoices/{invoice_id}.

        Deletes the specified invoice. When an invoice is deleted, the 
        associated order status changes to CANCELED. You can only delete a
        draft 
        invoice (you cannot delete a published invoice, including one that is
        scheduled for processing).

        Args:
            invoice_id (string): The ID of the invoice to delete.
            version (int, optional): The version of the
                [invoice](entity:Invoice) to delete. If you do not know the
                version, you can call
                [GetInvoice](api-endpoint:Invoices-GetInvoice) or 
                [ListInvoices](api-endpoint:Invoices-ListInvoices).

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
            .path('/v2/invoices/{invoice_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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

    def get_invoice(self,
                    invoice_id):
        """Does a GET request to /v2/invoices/{invoice_id}.

        Retrieves an invoice by invoice ID.

        Args:
            invoice_id (string): The ID of the invoice to retrieve.

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
            .path('/v2/invoices/{invoice_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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

    def update_invoice(self,
                       invoice_id,
                       body):
        """Does a PUT request to /v2/invoices/{invoice_id}.

        Updates an invoice by modifying fields, clearing fields, or both. For
        most updates, you can use a sparse 
        `Invoice` object to add fields or change values and use the
        `fields_to_clear` field to specify fields to clear. 
        However, some restrictions apply. For example, you cannot change the
        `order_id` or `location_id` field and you 
        must provide the complete `custom_fields` list to update a custom
        field. Published invoices have additional restrictions.

        Args:
            invoice_id (string): The ID of the invoice to update.
            body (UpdateInvoiceRequest): An object containing the fields to
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
            .path('/v2/invoices/{invoice_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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

    def cancel_invoice(self,
                       invoice_id,
                       body):
        """Does a POST request to /v2/invoices/{invoice_id}/cancel.

        Cancels an invoice. The seller cannot collect payments for 
        the canceled invoice.
        You cannot cancel an invoice in the `DRAFT` state or in a terminal
        state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.

        Args:
            invoice_id (string): The ID of the [invoice](entity:Invoice) to
                cancel.
            body (CancelInvoiceRequest): An object containing the fields to
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
            .path('/v2/invoices/{invoice_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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

    def publish_invoice(self,
                        invoice_id,
                        body):
        """Does a POST request to /v2/invoices/{invoice_id}/publish.

        Publishes the specified draft invoice. 
        After an invoice is published, Square 
        follows up based on the invoice configuration. For example, Square 
        sends the invoice to the customer's email address, charges the
        customer's card on file, or does 
        nothing. Square also makes the invoice available on a Square-hosted
        invoice page. 
        The invoice `status` also changes from `DRAFT` to a status 
        based on the invoice configuration. For example, the status changes to
        `UNPAID` if 
        Square emails the invoice or `PARTIALLY_PAID` if Square charge a card
        on file for a portion of the 
        invoice amount.

        Args:
            invoice_id (string): The ID of the invoice to publish.
            body (PublishInvoiceRequest): An object containing the fields to
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
            .path('/v2/invoices/{invoice_id}/publish')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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
