# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .raw_client import RawSubscriptionsClient
from ...types.sort_order import SortOrder
from ...core.request_options import RequestOptions
from ...core.pagination import SyncPager
from ...types.webhook_subscription import WebhookSubscription
from ...types.list_webhook_subscriptions_response import ListWebhookSubscriptionsResponse
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...requests.webhook_subscription import WebhookSubscriptionParams
from ...types.create_webhook_subscription_response import CreateWebhookSubscriptionResponse
from ...types.get_webhook_subscription_response import GetWebhookSubscriptionResponse
from ...types.update_webhook_subscription_response import UpdateWebhookSubscriptionResponse
from ...types.delete_webhook_subscription_response import DeleteWebhookSubscriptionResponse
from ...types.update_webhook_subscription_signature_key_response import UpdateWebhookSubscriptionSignatureKeyResponse
from ...types.test_webhook_subscription_response import TestWebhookSubscriptionResponse
from ...core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawSubscriptionsClient
from ...core.pagination import AsyncPager

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_disabled: typing.Optional[bool] = None,
        sort_order: typing.Optional[SortOrder] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[WebhookSubscription]:
        """
        Lists all webhook subscriptions owned by your application.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        include_disabled : typing.Optional[bool]
            Includes disabled [Subscription](entity:WebhookSubscription)s.
            By default, all enabled [Subscription](entity:WebhookSubscription)s are returned.

        sort_order : typing.Optional[SortOrder]
            Sorts the returned list by when the [Subscription](entity:WebhookSubscription) was created with the specified order.
            This field defaults to ASC.

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page.
            It is possible to receive fewer results than the specified limit on a given page.
            The default value of 100 is also the maximum allowed value.

            Default: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[WebhookSubscription]
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        response = client.webhooks.subscriptions.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._raw_client._client_wrapper.httpx_client.request(
            "v2/webhooks/subscriptions",
            method="GET",
            params={
                "cursor": cursor,
                "include_disabled": include_disabled,
                "sort_order": sort_order,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListWebhookSubscriptionsResponse,
                    construct_type(
                        type_=ListWebhookSubscriptionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    cursor=_parsed_next,
                    include_disabled=include_disabled,
                    sort_order=sort_order,
                    limit=limit,
                    request_options=request_options,
                )
                _items = _parsed_response.subscriptions
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        subscription: WebhookSubscriptionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookSubscriptionResponse:
        """
        Creates a webhook subscription.

        Parameters
        ----------
        subscription : WebhookSubscriptionParams
            The [Subscription](entity:WebhookSubscription) to create.

        idempotency_key : typing.Optional[str]
            A unique string that identifies the [CreateWebhookSubscription](api-endpoint:WebhookSubscriptions-CreateWebhookSubscription) request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookSubscriptionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.webhooks.subscriptions.create(
            idempotency_key="63f84c6c-2200-4c99-846c-2670a1311fbf",
            subscription={
                "name": "Example Webhook Subscription",
                "event_types": ["payment.created", "payment.updated"],
                "notification_url": "https://example-webhook-url.com",
                "api_version": "2021-12-15",
            },
        )
        """
        response = self._raw_client.create(
            subscription=subscription, idempotency_key=idempotency_key, request_options=request_options
        )
        return response.data

    def get(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookSubscriptionResponse:
        """
        Retrieves a webhook subscription identified by its ID.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookSubscriptionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.webhooks.subscriptions.get(
            subscription_id="subscription_id",
        )
        """
        response = self._raw_client.get(subscription_id, request_options=request_options)
        return response.data

    def update(
        self,
        subscription_id: str,
        *,
        subscription: typing.Optional[WebhookSubscriptionParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookSubscriptionResponse:
        """
        Updates a webhook subscription.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update.

        subscription : typing.Optional[WebhookSubscriptionParams]
            The [Subscription](entity:WebhookSubscription) to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookSubscriptionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.webhooks.subscriptions.update(
            subscription_id="subscription_id",
            subscription={
                "name": "Updated Example Webhook Subscription",
                "enabled": False,
            },
        )
        """
        response = self._raw_client.update(subscription_id, subscription=subscription, request_options=request_options)
        return response.data

    def delete(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhookSubscriptionResponse:
        """
        Deletes a webhook subscription.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhookSubscriptionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.webhooks.subscriptions.delete(
            subscription_id="subscription_id",
        )
        """
        response = self._raw_client.delete(subscription_id, request_options=request_options)
        return response.data

    def update_signature_key(
        self,
        subscription_id: str,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookSubscriptionSignatureKeyResponse:
        """
        Updates a webhook subscription by replacing the existing signature key with a new one.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update.

        idempotency_key : typing.Optional[str]
            A unique string that identifies the [UpdateWebhookSubscriptionSignatureKey](api-endpoint:WebhookSubscriptions-UpdateWebhookSubscriptionSignatureKey) request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookSubscriptionSignatureKeyResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.webhooks.subscriptions.update_signature_key(
            subscription_id="subscription_id",
            idempotency_key="ed80ae6b-0654-473b-bbab-a39aee89a60d",
        )
        """
        response = self._raw_client.update_signature_key(
            subscription_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return response.data

    def test(
        self,
        subscription_id: str,
        *,
        event_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestWebhookSubscriptionResponse:
        """
        Tests a webhook subscription by sending a test event to the notification URL.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to test.

        event_type : typing.Optional[str]
            The event type that will be used to test the [Subscription](entity:WebhookSubscription). The event type must be
            contained in the list of event types in the [Subscription](entity:WebhookSubscription).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestWebhookSubscriptionResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.webhooks.subscriptions.test(
            subscription_id="subscription_id",
            event_type="payment.created",
        )
        """
        response = self._raw_client.test(subscription_id, event_type=event_type, request_options=request_options)
        return response.data


class AsyncSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_disabled: typing.Optional[bool] = None,
        sort_order: typing.Optional[SortOrder] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[WebhookSubscription]:
        """
        Lists all webhook subscriptions owned by your application.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

        include_disabled : typing.Optional[bool]
            Includes disabled [Subscription](entity:WebhookSubscription)s.
            By default, all enabled [Subscription](entity:WebhookSubscription)s are returned.

        sort_order : typing.Optional[SortOrder]
            Sorts the returned list by when the [Subscription](entity:WebhookSubscription) was created with the specified order.
            This field defaults to ASC.

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page.
            It is possible to receive fewer results than the specified limit on a given page.
            The default value of 100 is also the maximum allowed value.

            Default: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[WebhookSubscription]
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.webhooks.subscriptions.list()
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            "v2/webhooks/subscriptions",
            method="GET",
            params={
                "cursor": cursor,
                "include_disabled": include_disabled,
                "sort_order": sort_order,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListWebhookSubscriptionsResponse,
                    construct_type(
                        type_=ListWebhookSubscriptionsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _parsed_next = _parsed_response.cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    cursor=_parsed_next,
                    include_disabled=include_disabled,
                    sort_order=sort_order,
                    limit=limit,
                    request_options=request_options,
                )
                _items = _parsed_response.subscriptions
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        subscription: WebhookSubscriptionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookSubscriptionResponse:
        """
        Creates a webhook subscription.

        Parameters
        ----------
        subscription : WebhookSubscriptionParams
            The [Subscription](entity:WebhookSubscription) to create.

        idempotency_key : typing.Optional[str]
            A unique string that identifies the [CreateWebhookSubscription](api-endpoint:WebhookSubscriptions-CreateWebhookSubscription) request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookSubscriptionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.subscriptions.create(
                idempotency_key="63f84c6c-2200-4c99-846c-2670a1311fbf",
                subscription={
                    "name": "Example Webhook Subscription",
                    "event_types": ["payment.created", "payment.updated"],
                    "notification_url": "https://example-webhook-url.com",
                    "api_version": "2021-12-15",
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.create(
            subscription=subscription, idempotency_key=idempotency_key, request_options=request_options
        )
        return response.data

    async def get(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookSubscriptionResponse:
        """
        Retrieves a webhook subscription identified by its ID.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookSubscriptionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.subscriptions.get(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(subscription_id, request_options=request_options)
        return response.data

    async def update(
        self,
        subscription_id: str,
        *,
        subscription: typing.Optional[WebhookSubscriptionParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookSubscriptionResponse:
        """
        Updates a webhook subscription.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update.

        subscription : typing.Optional[WebhookSubscriptionParams]
            The [Subscription](entity:WebhookSubscription) to update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookSubscriptionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.subscriptions.update(
                subscription_id="subscription_id",
                subscription={
                    "name": "Updated Example Webhook Subscription",
                    "enabled": False,
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.update(
            subscription_id, subscription=subscription, request_options=request_options
        )
        return response.data

    async def delete(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhookSubscriptionResponse:
        """
        Deletes a webhook subscription.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhookSubscriptionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.subscriptions.delete(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.delete(subscription_id, request_options=request_options)
        return response.data

    async def update_signature_key(
        self,
        subscription_id: str,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookSubscriptionSignatureKeyResponse:
        """
        Updates a webhook subscription by replacing the existing signature key with a new one.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update.

        idempotency_key : typing.Optional[str]
            A unique string that identifies the [UpdateWebhookSubscriptionSignatureKey](api-endpoint:WebhookSubscriptions-UpdateWebhookSubscriptionSignatureKey) request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookSubscriptionSignatureKeyResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.subscriptions.update_signature_key(
                subscription_id="subscription_id",
                idempotency_key="ed80ae6b-0654-473b-bbab-a39aee89a60d",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.update_signature_key(
            subscription_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return response.data

    async def test(
        self,
        subscription_id: str,
        *,
        event_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestWebhookSubscriptionResponse:
        """
        Tests a webhook subscription by sending a test event to the notification URL.

        Parameters
        ----------
        subscription_id : str
            [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to test.

        event_type : typing.Optional[str]
            The event type that will be used to test the [Subscription](entity:WebhookSubscription). The event type must be
            contained in the list of event types in the [Subscription](entity:WebhookSubscription).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestWebhookSubscriptionResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.subscriptions.test(
                subscription_id="subscription_id",
                event_type="payment.created",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.test(subscription_id, event_type=event_type, request_options=request_options)
        return response.data
