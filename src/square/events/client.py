# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawEventsClient
from ..requests.search_events_query import SearchEventsQueryParams
from ..core.request_options import RequestOptions
from ..types.search_events_response import SearchEventsResponse
from ..types.disable_events_response import DisableEventsResponse
from ..types.enable_events_response import EnableEventsResponse
from ..types.list_event_types_response import ListEventTypesResponse
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawEventsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def search_events(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchEventsQueryParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchEventsResponse:
        """
        Search for Square API events that occur within a 28-day timeframe.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of events for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        limit : typing.Optional[int]
            The maximum number of events to return in a single page. The response might contain fewer events. The default value is 100, which is also the maximum allowed value.

            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

            Default: 100

        query : typing.Optional[SearchEventsQueryParams]
            The filtering and sorting criteria for the search request. To retrieve additional pages using a cursor, you must use the original query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchEventsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.events.search_events()
        """
        response = self._raw_client.search_events(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return response.data

    def disable_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> DisableEventsResponse:
        """
        Disables events to prevent them from being searchable.
        All events are disabled by default. You must enable events to make them searchable.
        Disabling events for a specific time period prevents them from being searchable, even if you re-enable them later.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DisableEventsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.events.disable_events()
        """
        response = self._raw_client.disable_events(request_options=request_options)
        return response.data

    def enable_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnableEventsResponse:
        """
        Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnableEventsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.events.enable_events()
        """
        response = self._raw_client.enable_events(request_options=request_options)
        return response.data

    def list_event_types(
        self, *, api_version: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEventTypesResponse:
        """
        Lists all event types that you can subscribe to as webhooks or query using the Events API.

        Parameters
        ----------
        api_version : typing.Optional[str]
            The API version for which to list event types. Setting this field overrides the default version used by the application.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEventTypesResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.events.list_event_types()
        """
        response = self._raw_client.list_event_types(api_version=api_version, request_options=request_options)
        return response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def search_events(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchEventsQueryParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchEventsResponse:
        """
        Search for Square API events that occur within a 28-day timeframe.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of events for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        limit : typing.Optional[int]
            The maximum number of events to return in a single page. The response might contain fewer events. The default value is 100, which is also the maximum allowed value.

            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

            Default: 100

        query : typing.Optional[SearchEventsQueryParams]
            The filtering and sorting criteria for the search request. To retrieve additional pages using a cursor, you must use the original query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchEventsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.search_events()


        asyncio.run(main())
        """
        response = await self._raw_client.search_events(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return response.data

    async def disable_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> DisableEventsResponse:
        """
        Disables events to prevent them from being searchable.
        All events are disabled by default. You must enable events to make them searchable.
        Disabling events for a specific time period prevents them from being searchable, even if you re-enable them later.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DisableEventsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.disable_events()


        asyncio.run(main())
        """
        response = await self._raw_client.disable_events(request_options=request_options)
        return response.data

    async def enable_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnableEventsResponse:
        """
        Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnableEventsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.enable_events()


        asyncio.run(main())
        """
        response = await self._raw_client.enable_events(request_options=request_options)
        return response.data

    async def list_event_types(
        self, *, api_version: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListEventTypesResponse:
        """
        Lists all event types that you can subscribe to as webhooks or query using the Events API.

        Parameters
        ----------
        api_version : typing.Optional[str]
            The API version for which to list event types. Setting this field overrides the default version used by the application.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEventTypesResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.list_event_types()


        asyncio.run(main())
        """
        response = await self._raw_client.list_event_types(api_version=api_version, request_options=request_options)
        return response.data
