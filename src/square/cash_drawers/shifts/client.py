# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
from .raw_client import RawShiftsClient
import typing
from ...types.sort_order import SortOrder
from ...core.request_options import RequestOptions
from ...core.pagination import SyncPager
from ...types.cash_drawer_shift_summary import CashDrawerShiftSummary
from ...types.list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.get_cash_drawer_shift_response import GetCashDrawerShiftResponse
from ...types.cash_drawer_shift_event import CashDrawerShiftEvent
from ...core.jsonable_encoder import jsonable_encoder
from ...types.list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
from ...core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawShiftsClient
from ...core.pagination import AsyncPager


class ShiftsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShiftsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShiftsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShiftsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        location_id: str,
        sort_order: typing.Optional[SortOrder] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[CashDrawerShiftSummary]:
        """
        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Parameters
        ----------
        location_id : str
            The ID of the location to query for a list of cash drawer shifts.

        sort_order : typing.Optional[SortOrder]
            The order in which cash drawer shifts are listed in the response,
            based on their opened_at field. Default value: ASC

        begin_time : typing.Optional[str]
            The inclusive start time of the query on opened_at, in ISO 8601 format.

        end_time : typing.Optional[str]
            The exclusive end date of the query on opened_at, in ISO 8601 format.

        limit : typing.Optional[int]
            Number of cash drawer shift events in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[CashDrawerShiftSummary]
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        response = client.cash_drawers.shifts.list(
            location_id="location_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._raw_client._client_wrapper.httpx_client.request(
            "v2/cash-drawers/shifts",
            method="GET",
            params={
                "location_id": location_id,
                "sort_order": sort_order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListCashDrawerShiftsResponse,
                    construct_type(
                        type_=ListCashDrawerShiftsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    location_id=location_id,
                    sort_order=sort_order,
                    begin_time=begin_time,
                    end_time=end_time,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.cash_drawer_shifts
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, shift_id: str, *, location_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCashDrawerShiftResponse:
        """
        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](api-endpoint:CashDrawers-ListCashDrawerShiftEvents) for a list of cash drawer shift events.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to retrieve cash drawer shifts from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCashDrawerShiftResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.cash_drawers.shifts.get(
            shift_id="shift_id",
            location_id="location_id",
        )
        """
        response = self._raw_client.get(shift_id, location_id=location_id, request_options=request_options)
        return response.data

    def list_events(
        self,
        shift_id: str,
        *,
        location_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[CashDrawerShiftEvent]:
        """
        Provides a paginated list of events for a single cash drawer shift.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to list cash drawer shifts for.

        limit : typing.Optional[int]
            Number of resources to be returned in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[CashDrawerShiftEvent]
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        response = client.cash_drawers.shifts.list_events(
            shift_id="shift_id",
            location_id="location_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._raw_client._client_wrapper.httpx_client.request(
            f"v2/cash-drawers/shifts/{jsonable_encoder(shift_id)}/events",
            method="GET",
            params={
                "location_id": location_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListCashDrawerShiftEventsResponse,
                    construct_type(
                        type_=ListCashDrawerShiftEventsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list_events(
                    shift_id,
                    location_id=location_id,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.cash_drawer_shift_events
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncShiftsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShiftsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShiftsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShiftsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        location_id: str,
        sort_order: typing.Optional[SortOrder] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[CashDrawerShiftSummary]:
        """
        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Parameters
        ----------
        location_id : str
            The ID of the location to query for a list of cash drawer shifts.

        sort_order : typing.Optional[SortOrder]
            The order in which cash drawer shifts are listed in the response,
            based on their opened_at field. Default value: ASC

        begin_time : typing.Optional[str]
            The inclusive start time of the query on opened_at, in ISO 8601 format.

        end_time : typing.Optional[str]
            The exclusive end date of the query on opened_at, in ISO 8601 format.

        limit : typing.Optional[int]
            Number of cash drawer shift events in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[CashDrawerShiftSummary]
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.cash_drawers.shifts.list(
                location_id="location_id",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            "v2/cash-drawers/shifts",
            method="GET",
            params={
                "location_id": location_id,
                "sort_order": sort_order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListCashDrawerShiftsResponse,
                    construct_type(
                        type_=ListCashDrawerShiftsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    location_id=location_id,
                    sort_order=sort_order,
                    begin_time=begin_time,
                    end_time=end_time,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.cash_drawer_shifts
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, shift_id: str, *, location_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCashDrawerShiftResponse:
        """
        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](api-endpoint:CashDrawers-ListCashDrawerShiftEvents) for a list of cash drawer shift events.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to retrieve cash drawer shifts from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCashDrawerShiftResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cash_drawers.shifts.get(
                shift_id="shift_id",
                location_id="location_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(shift_id, location_id=location_id, request_options=request_options)
        return response.data

    async def list_events(
        self,
        shift_id: str,
        *,
        location_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[CashDrawerShiftEvent]:
        """
        Provides a paginated list of events for a single cash drawer shift.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to list cash drawer shifts for.

        limit : typing.Optional[int]
            Number of resources to be returned in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[CashDrawerShiftEvent]
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.cash_drawers.shifts.list_events(
                shift_id="shift_id",
                location_id="location_id",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            f"v2/cash-drawers/shifts/{jsonable_encoder(shift_id)}/events",
            method="GET",
            params={
                "location_id": location_id,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListCashDrawerShiftEventsResponse,
                    construct_type(
                        type_=ListCashDrawerShiftEventsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list_events(
                    shift_id,
                    location_id=location_id,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.cash_drawer_shift_events
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
