# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..core.http_response import HttpResponse
from ..types.retrieve_location_settings_response import RetrieveLocationSettingsResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..requests.checkout_location_settings import CheckoutLocationSettingsParams
from ..types.update_location_settings_response import UpdateLocationSettingsResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.retrieve_merchant_settings_response import RetrieveMerchantSettingsResponse
from ..requests.checkout_merchant_settings import CheckoutMerchantSettingsParams
from ..types.update_merchant_settings_response import UpdateMerchantSettingsResponse
from ..core.client_wrapper import AsyncClientWrapper
from ..core.http_response import AsyncHttpResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawCheckoutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_location_settings(
        self, location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveLocationSettingsResponse]:
        """
        Retrieves the location-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        location_id : str
            The ID of the location for which to retrieve settings.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveLocationSettingsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/online-checkout/location-settings/{jsonable_encoder(location_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLocationSettingsResponse,
                    construct_type(
                        type_=RetrieveLocationSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_location_settings(
        self,
        location_id: str,
        *,
        location_settings: CheckoutLocationSettingsParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateLocationSettingsResponse]:
        """
        Updates the location-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        location_id : str
            The ID of the location for which to retrieve settings.

        location_settings : CheckoutLocationSettingsParams
            Describe your updates using the `location_settings` object. Make sure it contains only the fields that have changed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLocationSettingsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/online-checkout/location-settings/{jsonable_encoder(location_id)}",
            method="PUT",
            json={
                "location_settings": convert_and_respect_annotation_metadata(
                    object_=location_settings, annotation=CheckoutLocationSettingsParams, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLocationSettingsResponse,
                    construct_type(
                        type_=UpdateLocationSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_merchant_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveMerchantSettingsResponse]:
        """
        Retrieves the merchant-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveMerchantSettingsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/online-checkout/merchant-settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveMerchantSettingsResponse,
                    construct_type(
                        type_=RetrieveMerchantSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_merchant_settings(
        self,
        *,
        merchant_settings: CheckoutMerchantSettingsParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMerchantSettingsResponse]:
        """
        Updates the merchant-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        merchant_settings : CheckoutMerchantSettingsParams
            Describe your updates using the `merchant_settings` object. Make sure it contains only the fields that have changed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMerchantSettingsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/online-checkout/merchant-settings",
            method="PUT",
            json={
                "merchant_settings": convert_and_respect_annotation_metadata(
                    object_=merchant_settings, annotation=CheckoutMerchantSettingsParams, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateMerchantSettingsResponse,
                    construct_type(
                        type_=UpdateMerchantSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawCheckoutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_location_settings(
        self, location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveLocationSettingsResponse]:
        """
        Retrieves the location-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        location_id : str
            The ID of the location for which to retrieve settings.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveLocationSettingsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/online-checkout/location-settings/{jsonable_encoder(location_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLocationSettingsResponse,
                    construct_type(
                        type_=RetrieveLocationSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_location_settings(
        self,
        location_id: str,
        *,
        location_settings: CheckoutLocationSettingsParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateLocationSettingsResponse]:
        """
        Updates the location-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        location_id : str
            The ID of the location for which to retrieve settings.

        location_settings : CheckoutLocationSettingsParams
            Describe your updates using the `location_settings` object. Make sure it contains only the fields that have changed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLocationSettingsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/online-checkout/location-settings/{jsonable_encoder(location_id)}",
            method="PUT",
            json={
                "location_settings": convert_and_respect_annotation_metadata(
                    object_=location_settings, annotation=CheckoutLocationSettingsParams, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLocationSettingsResponse,
                    construct_type(
                        type_=UpdateLocationSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_merchant_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveMerchantSettingsResponse]:
        """
        Retrieves the merchant-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveMerchantSettingsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/online-checkout/merchant-settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveMerchantSettingsResponse,
                    construct_type(
                        type_=RetrieveMerchantSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_merchant_settings(
        self,
        *,
        merchant_settings: CheckoutMerchantSettingsParams,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMerchantSettingsResponse]:
        """
        Updates the merchant-level settings for a Square-hosted checkout page.

        Parameters
        ----------
        merchant_settings : CheckoutMerchantSettingsParams
            Describe your updates using the `merchant_settings` object. Make sure it contains only the fields that have changed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMerchantSettingsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/online-checkout/merchant-settings",
            method="PUT",
            json={
                "merchant_settings": convert_and_respect_annotation_metadata(
                    object_=merchant_settings, annotation=CheckoutMerchantSettingsParams, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateMerchantSettingsResponse,
                    construct_type(
                        type_=UpdateMerchantSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
