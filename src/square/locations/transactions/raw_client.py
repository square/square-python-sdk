# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...types.sort_order import SortOrder
from ...core.request_options import RequestOptions
from ...core.http_response import HttpResponse
from ...types.list_transactions_response import ListTransactionsResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.get_transaction_response import GetTransactionResponse
from ...types.capture_transaction_response import CaptureTransactionResponse
from ...types.void_transaction_response import VoidTransactionResponse
from ...core.client_wrapper import AsyncClientWrapper
from ...core.http_response import AsyncHttpResponse


class RawTransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[SortOrder] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTransactionsResponse]:
        """
        Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund
        information from returns and exchanges.

        Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

        Parameters
        ----------
        location_id : str
            The ID of the location to list transactions for.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time.

        sort_order : typing.Optional[SortOrder]
            The order in which results are listed in the response (`ASC` for
            oldest first, `DESC` for newest first).

            Default value: `DESC`

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTransactionsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsResponse,
                    construct_type(
                        type_=ListTransactionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTransactionResponse]:
        """
        Retrieves details for a single transaction.

        Parameters
        ----------
        location_id : str
            The ID of the transaction's associated location.

        transaction_id : str
            The ID of the transaction to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTransactionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions/{jsonable_encoder(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTransactionResponse,
                    construct_type(
                        type_=GetTransactionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def capture(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaptureTransactionResponse]:
        """
        Captures a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaptureTransactionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions/{jsonable_encoder(transaction_id)}/capture",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaptureTransactionResponse,
                    construct_type(
                        type_=CaptureTransactionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def void(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoidTransactionResponse]:
        """
        Cancels a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoidTransactionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions/{jsonable_encoder(transaction_id)}/void",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoidTransactionResponse,
                    construct_type(
                        type_=VoidTransactionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[SortOrder] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTransactionsResponse]:
        """
        Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund
        information from returns and exchanges.

        Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

        Parameters
        ----------
        location_id : str
            The ID of the location to list transactions for.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time.

        sort_order : typing.Optional[SortOrder]
            The order in which results are listed in the response (`ASC` for
            oldest first, `DESC` for newest first).

            Default value: `DESC`

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTransactionsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsResponse,
                    construct_type(
                        type_=ListTransactionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTransactionResponse]:
        """
        Retrieves details for a single transaction.

        Parameters
        ----------
        location_id : str
            The ID of the transaction's associated location.

        transaction_id : str
            The ID of the transaction to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTransactionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions/{jsonable_encoder(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTransactionResponse,
                    construct_type(
                        type_=GetTransactionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def capture(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaptureTransactionResponse]:
        """
        Captures a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaptureTransactionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions/{jsonable_encoder(transaction_id)}/capture",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaptureTransactionResponse,
                    construct_type(
                        type_=CaptureTransactionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def void(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoidTransactionResponse]:
        """
        Cancels a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoidTransactionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{jsonable_encoder(location_id)}/transactions/{jsonable_encoder(transaction_id)}/void",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoidTransactionResponse,
                    construct_type(
                        type_=VoidTransactionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
