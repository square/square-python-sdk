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


class BankAccountsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(BankAccountsApi, self).__init__(config)

    def list_bank_accounts(self,
                           cursor=None,
                           limit=None,
                           location_id=None):
        """Does a GET request to /v2/bank-accounts.

        Returns a list of [BankAccount]($m/BankAccount) objects linked to a
        Square account.

        Args:
            cursor (str, optional): The pagination cursor returned by a
                previous call to this endpoint. Use it in the next
                `ListBankAccounts` request to retrieve the next set  of
                results.  See the
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination) guide for more information.
            limit (int, optional): Upper limit on the number of bank accounts
                to return in the response.  Currently, 1000 is the largest
                supported limit. You can specify a limit  of up to 1000 bank
                accounts. This is also the default limit.
            location_id (str, optional): Location ID. You can specify this
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/bank-accounts')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
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

    def get_bank_account_by_v1_id(self,
                                  v1_bank_account_id):
        """Does a GET request to /v2/bank-accounts/by-v1-id/{v1_bank_account_id}.

        Returns details of a [BankAccount]($m/BankAccount) identified by V1
        bank account ID.

        Args:
            v1_bank_account_id (str): Connect V1 ID of the desired
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/bank-accounts/by-v1-id/{v1_bank_account_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('v1_bank_account_id')
                            .value(v1_bank_account_id)
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

    def get_bank_account(self,
                         bank_account_id):
        """Does a GET request to /v2/bank-accounts/{bank_account_id}.

        Returns details of a [BankAccount]($m/BankAccount)
        linked to a Square account.

        Args:
            bank_account_id (str): Square-issued ID of the desired
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/bank-accounts/{bank_account_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('bank_account_id')
                            .value(bank_account_id)
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
