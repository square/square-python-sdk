# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .raw_client import RawActionsClient
from ...requests.terminal_action import TerminalActionParams
from ...core.request_options import RequestOptions
from ...types.create_terminal_action_response import CreateTerminalActionResponse
from ...requests.terminal_action_query import TerminalActionQueryParams
from ...types.search_terminal_actions_response import SearchTerminalActionsResponse
from ...types.get_terminal_action_response import GetTerminalActionResponse
from ...types.cancel_terminal_action_response import CancelTerminalActionResponse
from ...core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawActionsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActionsClient
        """
        return self._raw_client

    def create(
        self,
        *,
        idempotency_key: str,
        action: TerminalActionParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTerminalActionResponse:
        """
        Creates a Terminal action request and sends it to the specified device.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateAction` request. Keys can be any valid string
            but must be unique for every `CreateAction` request.

            See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more
            information.

        action : TerminalActionParams
            The Action to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTerminalActionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.terminal.actions.create(
            idempotency_key="thahn-70e75c10-47f7-4ab6-88cc-aaa4076d065e",
            action={
                "device_id": "{{DEVICE_ID}}",
                "deadline_duration": "PT5M",
                "type": "SAVE_CARD",
                "save_card_options": {
                    "customer_id": "{{CUSTOMER_ID}}",
                    "reference_id": "user-id-1",
                },
            },
        )
        """
        response = self._raw_client.create(
            idempotency_key=idempotency_key, action=action, request_options=request_options
        )
        return response.data

    def search(
        self,
        *,
        query: typing.Optional[TerminalActionQueryParams] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTerminalActionsResponse:
        """
        Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal action requests are available for 30 days.

        Parameters
        ----------
        query : typing.Optional[TerminalActionQueryParams]
            Queries terminal actions based on given conditions and sort order.
            Leaving this unset will return all actions with the default sort order.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.
            See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more
            information.

        limit : typing.Optional[int]
            Limit the number of results returned for a single request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchTerminalActionsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.terminal.actions.search(
            query={
                "filter": {"created_at": {"start_at": "2022-04-01T00:00:00.000Z"}},
                "sort": {"sort_order": "DESC"},
            },
            limit=2,
        )
        """
        response = self._raw_client.search(query=query, cursor=cursor, limit=limit, request_options=request_options)
        return response.data

    def get(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTerminalActionResponse:
        """
        Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.

        Parameters
        ----------
        action_id : str
            Unique ID for the desired `TerminalAction`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTerminalActionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.terminal.actions.get(
            action_id="action_id",
        )
        """
        response = self._raw_client.get(action_id, request_options=request_options)
        return response.data

    def cancel(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelTerminalActionResponse:
        """
        Cancels a Terminal action request if the status of the request permits it.

        Parameters
        ----------
        action_id : str
            Unique ID for the desired `TerminalAction`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelTerminalActionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.terminal.actions.cancel(
            action_id="action_id",
        )
        """
        response = self._raw_client.cancel(action_id, request_options=request_options)
        return response.data


class AsyncActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActionsClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        idempotency_key: str,
        action: TerminalActionParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTerminalActionResponse:
        """
        Creates a Terminal action request and sends it to the specified device.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateAction` request. Keys can be any valid string
            but must be unique for every `CreateAction` request.

            See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more
            information.

        action : TerminalActionParams
            The Action to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTerminalActionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.actions.create(
                idempotency_key="thahn-70e75c10-47f7-4ab6-88cc-aaa4076d065e",
                action={
                    "device_id": "{{DEVICE_ID}}",
                    "deadline_duration": "PT5M",
                    "type": "SAVE_CARD",
                    "save_card_options": {
                        "customer_id": "{{CUSTOMER_ID}}",
                        "reference_id": "user-id-1",
                    },
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.create(
            idempotency_key=idempotency_key, action=action, request_options=request_options
        )
        return response.data

    async def search(
        self,
        *,
        query: typing.Optional[TerminalActionQueryParams] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTerminalActionsResponse:
        """
        Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal action requests are available for 30 days.

        Parameters
        ----------
        query : typing.Optional[TerminalActionQueryParams]
            Queries terminal actions based on given conditions and sort order.
            Leaving this unset will return all actions with the default sort order.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.
            See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more
            information.

        limit : typing.Optional[int]
            Limit the number of results returned for a single request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchTerminalActionsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.actions.search(
                query={
                    "filter": {"created_at": {"start_at": "2022-04-01T00:00:00.000Z"}},
                    "sort": {"sort_order": "DESC"},
                },
                limit=2,
            )


        asyncio.run(main())
        """
        response = await self._raw_client.search(
            query=query, cursor=cursor, limit=limit, request_options=request_options
        )
        return response.data

    async def get(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTerminalActionResponse:
        """
        Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.

        Parameters
        ----------
        action_id : str
            Unique ID for the desired `TerminalAction`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTerminalActionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.actions.get(
                action_id="action_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(action_id, request_options=request_options)
        return response.data

    async def cancel(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelTerminalActionResponse:
        """
        Cancels a Terminal action request if the status of the request permits it.

        Parameters
        ----------
        action_id : str
            Unique ID for the desired `TerminalAction`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelTerminalActionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.actions.cancel(
                action_id="action_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.cancel(action_id, request_options=request_options)
        return response.data
