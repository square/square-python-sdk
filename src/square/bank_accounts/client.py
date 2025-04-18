# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawBankAccountsClient
import typing
from ..core.request_options import RequestOptions
from ..core.pagination import SyncPager
from ..types.bank_account import BankAccount
from ..types.list_bank_accounts_response import ListBankAccountsResponse
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.get_bank_account_by_v1id_response import GetBankAccountByV1IdResponse
from ..types.get_bank_account_response import GetBankAccountResponse
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawBankAccountsClient
from ..core.pagination import AsyncPager


class BankAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBankAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBankAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBankAccountsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[BankAccount]:
        """
        Returns a list of [BankAccount](entity:BankAccount) objects linked to a Square account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned by a previous call to this endpoint.
            Use it in the next `ListBankAccounts` request to retrieve the next set
            of results.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        limit : typing.Optional[int]
            Upper limit on the number of bank accounts to return in the response.
            Currently, 1000 is the largest supported limit. You can specify a limit
            of up to 1000 bank accounts. This is also the default limit.

        location_id : typing.Optional[str]
            Location ID. You can specify this optional filter
            to retrieve only the linked bank accounts belonging to a specific location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[BankAccount]
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        response = client.bank_accounts.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._raw_client._client_wrapper.httpx_client.request(
            "v2/bank-accounts",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListBankAccountsResponse,
                    construct_type(
                        type_=ListBankAccountsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    cursor=_parsed_next,
                    limit=limit,
                    location_id=location_id,
                    request_options=request_options,
                )
                _items = _parsed_response.bank_accounts
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountByV1IdResponse:
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
        GetBankAccountByV1IdResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.bank_accounts.get_by_v1id(
            v1bank_account_id="v1_bank_account_id",
        )
        """
        response = self._raw_client.get_by_v1id(v1bank_account_id, request_options=request_options)
        return response.data

    def get(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountResponse:
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
        GetBankAccountResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.bank_accounts.get(
            bank_account_id="bank_account_id",
        )
        """
        response = self._raw_client.get(bank_account_id, request_options=request_options)
        return response.data


class AsyncBankAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBankAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBankAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBankAccountsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[BankAccount]:
        """
        Returns a list of [BankAccount](entity:BankAccount) objects linked to a Square account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned by a previous call to this endpoint.
            Use it in the next `ListBankAccounts` request to retrieve the next set
            of results.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        limit : typing.Optional[int]
            Upper limit on the number of bank accounts to return in the response.
            Currently, 1000 is the largest supported limit. You can specify a limit
            of up to 1000 bank accounts. This is also the default limit.

        location_id : typing.Optional[str]
            Location ID. You can specify this optional filter
            to retrieve only the linked bank accounts belonging to a specific location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[BankAccount]
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.bank_accounts.list()
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            "v2/bank-accounts",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListBankAccountsResponse,
                    construct_type(
                        type_=ListBankAccountsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    cursor=_parsed_next,
                    limit=limit,
                    location_id=location_id,
                    request_options=request_options,
                )
                _items = _parsed_response.bank_accounts
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountByV1IdResponse:
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
        GetBankAccountByV1IdResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bank_accounts.get_by_v1id(
                v1bank_account_id="v1_bank_account_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get_by_v1id(v1bank_account_id, request_options=request_options)
        return response.data

    async def get(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountResponse:
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
        GetBankAccountResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bank_accounts.get(
                bank_account_id="bank_account_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(bank_account_id, request_options=request_options)
        return response.data
