# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .raw_client import RawCustomAttributeDefinitionsClient
from ...types.visibility_filter import VisibilityFilter
from ...core.request_options import RequestOptions
from ...core.pagination import SyncPager
from ...types.custom_attribute_definition import CustomAttributeDefinition
from ...types.list_merchant_custom_attribute_definitions_response import ListMerchantCustomAttributeDefinitionsResponse
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...requests.custom_attribute_definition import CustomAttributeDefinitionParams
from ...types.create_merchant_custom_attribute_definition_response import (
    CreateMerchantCustomAttributeDefinitionResponse,
)
from ...types.retrieve_merchant_custom_attribute_definition_response import (
    RetrieveMerchantCustomAttributeDefinitionResponse,
)
from ...types.update_merchant_custom_attribute_definition_response import (
    UpdateMerchantCustomAttributeDefinitionResponse,
)
from ...types.delete_merchant_custom_attribute_definition_response import (
    DeleteMerchantCustomAttributeDefinitionResponse,
)
from ...core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawCustomAttributeDefinitionsClient
from ...core.pagination import AsyncPager

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CustomAttributeDefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomAttributeDefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomAttributeDefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomAttributeDefinitionsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        visibility_filter: typing.Optional[VisibilityFilter] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[CustomAttributeDefinition]:
        """
        Lists the merchant-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.
        When all response pages are retrieved, the results include all custom attribute definitions
        that are visible to the requesting application, including those that are created by other
        applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        visibility_filter : typing.Optional[VisibilityFilter]
            Filters the `CustomAttributeDefinition` results by their `visibility` values.

        limit : typing.Optional[int]
            The maximum number of results to return in a single paged response. This limit is advisory.
            The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
            The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        cursor : typing.Optional[str]
            The cursor returned in the paged response from the previous call to this endpoint.
            Provide this cursor to retrieve the next page of results for your original request.
            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[CustomAttributeDefinition]
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        response = client.merchants.custom_attribute_definitions.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._raw_client._client_wrapper.httpx_client.request(
            "v2/merchants/custom-attribute-definitions",
            method="GET",
            params={
                "visibility_filter": visibility_filter,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMerchantCustomAttributeDefinitionsResponse,
                    construct_type(
                        type_=ListMerchantCustomAttributeDefinitionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    visibility_filter=visibility_filter,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.custom_attribute_definitions
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMerchantCustomAttributeDefinitionResponse:
        """
        Creates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
        Use this endpoint to define a custom attribute that can be associated with a merchant connecting to your application.
        A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
        for a custom attribute. After the definition is created, you can call
        [UpsertMerchantCustomAttribute](api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute) or
        [BulkUpsertMerchantCustomAttributes](api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes)
        to set the custom attribute for a merchant.

        Parameters
        ----------
        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition to create. Note the following:
            - With the exception of the `Selection` data type, the `schema` is specified as a simple URL to the JSON schema
            definition hosted on the Square CDN. For more information, including supported values and constraints, see
            [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
            - `name` is required unless `visibility` is set to `VISIBILITY_HIDDEN`.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.merchants.custom_attribute_definitions.create(
            custom_attribute_definition={
                "key": "alternative_seller_name",
                "schema": {
                    "ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.String"
                },
                "name": "Alternative Merchant Name",
                "description": "This is the other name this merchant goes by.",
                "visibility": "VISIBILITY_READ_ONLY",
            },
        )
        """
        response = self._raw_client.create(
            custom_attribute_definition=custom_attribute_definition,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return response.data

    def get(
        self, key: str, *, version: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveMerchantCustomAttributeDefinitionResponse:
        """
        Retrieves a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
        To retrieve a custom attribute definition created by another application, the `visibility`
        setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to retrieve. If the requesting application
            is not the definition owner, you must use the qualified key.

        version : typing.Optional[int]
            The current version of the custom attribute definition, which is used for strongly consistent
            reads to guarantee that you receive the most up-to-date data. When included in the request,
            Square returns the specified version or a higher version if one exists. If the specified version
            is higher than the current version, Square returns a `BAD_REQUEST` error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.merchants.custom_attribute_definitions.get(
            key="key",
        )
        """
        response = self._raw_client.get(key, version=version, request_options=request_options)
        return response.data

    def update(
        self,
        key: str,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMerchantCustomAttributeDefinitionResponse:
        """
        Updates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
        Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
        `schema` for a `Selection` data type.
        Only the definition owner can update a custom attribute definition.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to update.

        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition that contains the fields to update. This endpoint
            supports sparse updates, so only new or changed fields need to be included in the request.
            Only the following fields can be updated:
            - `name`
            - `description`
            - `visibility`
            - `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
            selections are supported.
            For more information, see
            [Update a merchant custom attribute definition](https://developer.squareup.com/docs/merchant-custom-attributes-api/custom-attribute-definitions#update-custom-attribute-definition).
            The version field must match the current version of the custom attribute definition to enable
            [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.merchants.custom_attribute_definitions.update(
            key="key",
            custom_attribute_definition={
                "description": "Update the description as desired.",
                "visibility": "VISIBILITY_READ_ONLY",
            },
        )
        """
        response = self._raw_client.update(
            key,
            custom_attribute_definition=custom_attribute_definition,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return response.data

    def delete(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMerchantCustomAttributeDefinitionResponse:
        """
        Deletes a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
        Deleting a custom attribute definition also deletes the corresponding custom attribute from
        the merchant.
        Only the definition owner can delete a custom attribute definition.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.merchants.custom_attribute_definitions.delete(
            key="key",
        )
        """
        response = self._raw_client.delete(key, request_options=request_options)
        return response.data


class AsyncCustomAttributeDefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomAttributeDefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomAttributeDefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomAttributeDefinitionsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        visibility_filter: typing.Optional[VisibilityFilter] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[CustomAttributeDefinition]:
        """
        Lists the merchant-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.
        When all response pages are retrieved, the results include all custom attribute definitions
        that are visible to the requesting application, including those that are created by other
        applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        visibility_filter : typing.Optional[VisibilityFilter]
            Filters the `CustomAttributeDefinition` results by their `visibility` values.

        limit : typing.Optional[int]
            The maximum number of results to return in a single paged response. This limit is advisory.
            The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
            The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        cursor : typing.Optional[str]
            The cursor returned in the paged response from the previous call to this endpoint.
            Provide this cursor to retrieve the next page of results for your original request.
            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[CustomAttributeDefinition]
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.merchants.custom_attribute_definitions.list()
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            "v2/merchants/custom-attribute-definitions",
            method="GET",
            params={
                "visibility_filter": visibility_filter,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListMerchantCustomAttributeDefinitionsResponse,
                    construct_type(
                        type_=ListMerchantCustomAttributeDefinitionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    visibility_filter=visibility_filter,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                _items = _parsed_response.custom_attribute_definitions
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMerchantCustomAttributeDefinitionResponse:
        """
        Creates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
        Use this endpoint to define a custom attribute that can be associated with a merchant connecting to your application.
        A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
        for a custom attribute. After the definition is created, you can call
        [UpsertMerchantCustomAttribute](api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute) or
        [BulkUpsertMerchantCustomAttributes](api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes)
        to set the custom attribute for a merchant.

        Parameters
        ----------
        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition to create. Note the following:
            - With the exception of the `Selection` data type, the `schema` is specified as a simple URL to the JSON schema
            definition hosted on the Square CDN. For more information, including supported values and constraints, see
            [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
            - `name` is required unless `visibility` is set to `VISIBILITY_HIDDEN`.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.custom_attribute_definitions.create(
                custom_attribute_definition={
                    "key": "alternative_seller_name",
                    "schema": {
                        "ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.String"
                    },
                    "name": "Alternative Merchant Name",
                    "description": "This is the other name this merchant goes by.",
                    "visibility": "VISIBILITY_READ_ONLY",
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.create(
            custom_attribute_definition=custom_attribute_definition,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return response.data

    async def get(
        self, key: str, *, version: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveMerchantCustomAttributeDefinitionResponse:
        """
        Retrieves a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
        To retrieve a custom attribute definition created by another application, the `visibility`
        setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to retrieve. If the requesting application
            is not the definition owner, you must use the qualified key.

        version : typing.Optional[int]
            The current version of the custom attribute definition, which is used for strongly consistent
            reads to guarantee that you receive the most up-to-date data. When included in the request,
            Square returns the specified version or a higher version if one exists. If the specified version
            is higher than the current version, Square returns a `BAD_REQUEST` error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.custom_attribute_definitions.get(
                key="key",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(key, version=version, request_options=request_options)
        return response.data

    async def update(
        self,
        key: str,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMerchantCustomAttributeDefinitionResponse:
        """
        Updates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
        Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
        `schema` for a `Selection` data type.
        Only the definition owner can update a custom attribute definition.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to update.

        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition that contains the fields to update. This endpoint
            supports sparse updates, so only new or changed fields need to be included in the request.
            Only the following fields can be updated:
            - `name`
            - `description`
            - `visibility`
            - `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
            selections are supported.
            For more information, see
            [Update a merchant custom attribute definition](https://developer.squareup.com/docs/merchant-custom-attributes-api/custom-attribute-definitions#update-custom-attribute-definition).
            The version field must match the current version of the custom attribute definition to enable
            [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.custom_attribute_definitions.update(
                key="key",
                custom_attribute_definition={
                    "description": "Update the description as desired.",
                    "visibility": "VISIBILITY_READ_ONLY",
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.update(
            key,
            custom_attribute_definition=custom_attribute_definition,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return response.data

    async def delete(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMerchantCustomAttributeDefinitionResponse:
        """
        Deletes a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
        Deleting a custom attribute definition also deletes the corresponding custom attribute from
        the merchant.
        Only the definition owner can delete a custom attribute definition.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMerchantCustomAttributeDefinitionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.custom_attribute_definitions.delete(
                key="key",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.delete(key, request_options=request_options)
        return response.data
