# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class BankAccountsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(BankAccountsApi, self).__init__(config, auth_managers)

    def list_bank_accounts(self,
                           cursor=None,
                           limit=None,
                           location_id=None):
        """Does a GET request to /v2/bank-accounts.

        Returns a list of [BankAccount]($m/BankAccount) objects linked to a
        Square account.

        Args:
            cursor (string, optional): The pagination cursor returned by a
                previous call to this endpoint. Use it in the next
                `ListBankAccounts` request to retrieve the next set  of
                results.  See the
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination) guide for more information.
            limit (int, optional): Upper limit on the number of bank accounts
                to return in the response.  Currently, 1000 is the largest
                supported limit. You can specify a limit  of up to 1000 bank
                accounts. This is also the default limit.
            location_id (string, optional): Location ID. You can specify this
                optional filter  to retrieve only the linked bank accounts
                belonging to a specific location.

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
        _url_path = '/v2/bank-accounts'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'limit': limit,
            'location_id': location_id
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

    def get_bank_account_by_v1_id(self,
                                  v1_bank_account_id):
        """Does a GET request to /v2/bank-accounts/by-v1-id/{v1_bank_account_id}.

        Returns details of a [BankAccount]($m/BankAccount) identified by V1
        bank account ID.

        Args:
            v1_bank_account_id (string): Connect V1 ID of the desired
                `BankAccount`. For more information, see  [Retrieve a bank
                account by using an ID issued by V1 Bank Accounts
                API](https://developer.squareup.com/docs/bank-accounts-api#retr
                ieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-a
                pi).

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
        _url_path = '/v2/bank-accounts/by-v1-id/{v1_bank_account_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'v1_bank_account_id': {'value': v1_bank_account_id, 'encode': True}
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

    def get_bank_account(self,
                         bank_account_id):
        """Does a GET request to /v2/bank-accounts/{bank_account_id}.

        Returns details of a [BankAccount]($m/BankAccount)
        linked to a Square account.

        Args:
            bank_account_id (string): Square-issued ID of the desired
                `BankAccount`.

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
        _url_path = '/v2/bank-accounts/{bank_account_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'bank_account_id': {'value': bank_account_id, 'encode': True}
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
