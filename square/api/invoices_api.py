# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class InvoicesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(InvoicesApi, self).__init__(config, auth_managers)

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
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
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

        # Prepare query URL
        _url_path = '/v2/invoices'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'location_id': location_id,
            'cursor': cursor,
            'limit': limit
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

        # Prepare query URL
        _url_path = '/v2/invoices'
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

        # Prepare query URL
        _url_path = '/v2/invoices/search'
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
            version (int, optional): The version of the [invoice]($m/Invoice)
                to delete. If you do not know the version, you can call
                [GetInvoice]($e/Invoices/GetInvoice) or 
                [ListInvoices]($e/Invoices/ListInvoices).

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
        _url_path = '/v2/invoices/{invoice_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
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

        # Prepare query URL
        _url_path = '/v2/invoices/{invoice_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
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

        # Prepare query URL
        _url_path = '/v2/invoices/{invoice_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
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

    def cancel_invoice(self,
                       invoice_id,
                       body):
        """Does a POST request to /v2/invoices/{invoice_id}/cancel.

        Cancels an invoice. The seller cannot collect payments for 
        the canceled invoice.
        You cannot cancel an invoice in the `DRAFT` state or in a terminal
        state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.

        Args:
            invoice_id (string): The ID of the [invoice]($m/Invoice) to
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

        # Prepare query URL
        _url_path = '/v2/invoices/{invoice_id}/cancel'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
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

        # Prepare query URL
        _url_path = '/v2/invoices/{invoice_id}/publish'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
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
