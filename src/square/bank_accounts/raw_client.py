# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..core.http_response import HttpResponse
from ..types.get_bank_account_by_v1id_response import GetBankAccountByV1IdResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.get_bank_account_response import GetBankAccountResponse
from ..core.client_wrapper import AsyncClientWrapper
from ..core.http_response import AsyncHttpResponse


class RawBankAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBankAccountByV1IdResponse]:
        """
        Returns details of a [BankAccount](entity:BankAccount) identified by V1 bank account ID.

        Parameters
        ----------
        v1bank_account_id : str
            Connect V1 ID of the desired `BankAccount`. For more information, see
            [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBankAccountByV1IdResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/by-v1-id/{jsonable_encoder(v1bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountByV1IdResponse,
                    construct_type(
                        type_=GetBankAccountByV1IdResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBankAccountResponse]:
        """
        Returns details of a [BankAccount](entity:BankAccount)
        linked to a Square account.

        Parameters
        ----------
        bank_account_id : str
            Square-issued ID of the desired `BankAccount`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBankAccountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/{jsonable_encoder(bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountResponse,
                    construct_type(
                        type_=GetBankAccountResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawBankAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBankAccountByV1IdResponse]:
        """
        Returns details of a [BankAccount](entity:BankAccount) identified by V1 bank account ID.

        Parameters
        ----------
        v1bank_account_id : str
            Connect V1 ID of the desired `BankAccount`. For more information, see
            [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBankAccountByV1IdResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/by-v1-id/{jsonable_encoder(v1bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountByV1IdResponse,
                    construct_type(
                        type_=GetBankAccountByV1IdResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBankAccountResponse]:
        """
        Returns details of a [BankAccount](entity:BankAccount)
        linked to a Square account.

        Parameters
        ----------
        bank_account_id : str
            Square-issued ID of the desired `BankAccount`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBankAccountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/{jsonable_encoder(bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountResponse,
                    construct_type(
                        type_=GetBankAccountResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
