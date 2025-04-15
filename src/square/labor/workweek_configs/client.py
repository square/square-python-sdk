# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .raw_client import RawWorkweekConfigsClient
from ...core.request_options import RequestOptions
from ...core.pagination import SyncPager
from ...types.workweek_config import WorkweekConfig
from ...types.list_workweek_configs_response import ListWorkweekConfigsResponse
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...requests.workweek_config import WorkweekConfigParams
from ...types.update_workweek_config_response import UpdateWorkweekConfigResponse
from ...core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawWorkweekConfigsClient
from ...core.pagination import AsyncPager

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WorkweekConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkweekConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkweekConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkweekConfigsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[WorkweekConfig]:
        """
        Returns a list of `WorkweekConfig` instances for a business.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of `WorkweekConfigs` results to return per page.

        cursor : typing.Optional[str]
            A pointer to the next page of `WorkweekConfig` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[WorkweekConfig]
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        response = client.labor.workweek_configs.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._raw_client._client_wrapper.httpx_client.request(
            "v2/labor/workweek-configs",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListWorkweekConfigsResponse,
                    construct_type(
                        type_=ListWorkweekConfigsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.workweek_configs
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, id: str, *, workweek_config: WorkweekConfigParams, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateWorkweekConfigResponse:
        """
        Updates a `WorkweekConfig`.

        Parameters
        ----------
        id : str
            The UUID for the `WorkweekConfig` object being updated.

        workweek_config : WorkweekConfigParams
            The updated `WorkweekConfig` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkweekConfigResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.labor.workweek_configs.get(
            id="id",
            workweek_config={
                "start_of_week": "MON",
                "start_of_day_local_time": "10:00",
                "version": 10,
            },
        )
        """
        response = self._raw_client.get(id, workweek_config=workweek_config, request_options=request_options)
        return response.data


class AsyncWorkweekConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkweekConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkweekConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkweekConfigsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[WorkweekConfig]:
        """
        Returns a list of `WorkweekConfig` instances for a business.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of `WorkweekConfigs` results to return per page.

        cursor : typing.Optional[str]
            A pointer to the next page of `WorkweekConfig` results to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[WorkweekConfig]
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.labor.workweek_configs.list()
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            "v2/labor/workweek-configs",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListWorkweekConfigsResponse,
                    construct_type(
                        type_=ListWorkweekConfigsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.workweek_configs
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: str, *, workweek_config: WorkweekConfigParams, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateWorkweekConfigResponse:
        """
        Updates a `WorkweekConfig`.

        Parameters
        ----------
        id : str
            The UUID for the `WorkweekConfig` object being updated.

        workweek_config : WorkweekConfigParams
            The updated `WorkweekConfig` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkweekConfigResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.labor.workweek_configs.get(
                id="id",
                workweek_config={
                    "start_of_week": "MON",
                    "start_of_day_local_time": "10:00",
                    "version": 10,
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(id, workweek_config=workweek_config, request_options=request_options)
        return response.data
