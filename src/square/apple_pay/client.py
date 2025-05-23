# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawApplePayClient
from ..core.request_options import RequestOptions
from ..types.register_domain_response import RegisterDomainResponse
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawApplePayClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ApplePayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplePayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplePayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplePayClient
        """
        return self._raw_client

    def register_domain(
        self, *, domain_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterDomainResponse:
        """
        Activates a domain for use with Apple Pay on the Web and Square. A validation
        is performed on this domain by Apple to ensure that it is properly set up as
        an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate
        Apple Pay on the Web with Square for merchants using their platform.

        Note: You will need to host a valid domain verification file on your domain to support Apple Pay.  The
        current version of this file is always available at https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association,
        and should be hosted at `.well_known/apple-developer-merchantid-domain-association` on your
        domain.  This file is subject to change; we strongly recommend checking for updates regularly and avoiding
        long-lived caches that might not keep in sync with the correct file version.

        To learn more about the Web Payments SDK and how to add Apple Pay, see [Take an Apple Pay Payment](https://developer.squareup.com/docs/web-payments/apple-pay).

        Parameters
        ----------
        domain_name : str
            A domain name as described in RFC-1034 that will be registered with ApplePay.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterDomainResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.apple_pay.register_domain(
            domain_name="example.com",
        )
        """
        response = self._raw_client.register_domain(domain_name=domain_name, request_options=request_options)
        return response.data


class AsyncApplePayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplePayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplePayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplePayClient
        """
        return self._raw_client

    async def register_domain(
        self, *, domain_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterDomainResponse:
        """
        Activates a domain for use with Apple Pay on the Web and Square. A validation
        is performed on this domain by Apple to ensure that it is properly set up as
        an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate
        Apple Pay on the Web with Square for merchants using their platform.

        Note: You will need to host a valid domain verification file on your domain to support Apple Pay.  The
        current version of this file is always available at https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association,
        and should be hosted at `.well_known/apple-developer-merchantid-domain-association` on your
        domain.  This file is subject to change; we strongly recommend checking for updates regularly and avoiding
        long-lived caches that might not keep in sync with the correct file version.

        To learn more about the Web Payments SDK and how to add Apple Pay, see [Take an Apple Pay Payment](https://developer.squareup.com/docs/web-payments/apple-pay).

        Parameters
        ----------
        domain_name : str
            A domain name as described in RFC-1034 that will be registered with ApplePay.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterDomainResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.apple_pay.register_domain(
                domain_name="example.com",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.register_domain(domain_name=domain_name, request_options=request_options)
        return response.data
