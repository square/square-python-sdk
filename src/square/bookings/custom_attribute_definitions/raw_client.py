# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...requests.custom_attribute_definition import CustomAttributeDefinitionParams
from ...core.request_options import RequestOptions
from ...core.http_response import HttpResponse
from ...types.create_booking_custom_attribute_definition_response import CreateBookingCustomAttributeDefinitionResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.retrieve_booking_custom_attribute_definition_response import (
    RetrieveBookingCustomAttributeDefinitionResponse,
)
from ...core.jsonable_encoder import jsonable_encoder
from ...types.update_booking_custom_attribute_definition_response import UpdateBookingCustomAttributeDefinitionResponse
from ...types.delete_booking_custom_attribute_definition_response import DeleteBookingCustomAttributeDefinitionResponse
from ...core.client_wrapper import AsyncClientWrapper
from ...core.http_response import AsyncHttpResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawCustomAttributeDefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateBookingCustomAttributeDefinitionResponse]:
        """
        Creates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Parameters
        ----------
        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition to create, with the following fields:

            - `key`

            - `name`. If provided, `name` must be unique (case-sensitive) across all visible booking-related custom attribute
            definitions for the seller.

            - `description`

            - `visibility`. Note that all custom attributes are visible in exported booking data, including those set to
            `VISIBILITY_HIDDEN`.

            - `schema`. With the exception of the `Selection` data type, the `schema` is specified as a
            simple URL to the JSON schema definition hosted on the Square CDN. For more information, see
            [Specifying the schema](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attribute-definitions#specify-schema).

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bookings/custom-attribute-definitions",
            method="POST",
            json={
                "custom_attribute_definition": convert_and_respect_annotation_metadata(
                    object_=custom_attribute_definition, annotation=CustomAttributeDefinitionParams, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=CreateBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, key: str, *, version: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveBookingCustomAttributeDefinitionResponse]:
        """
        Retrieves a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

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
        HttpResponse[RetrieveBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/custom-attribute-definitions/{jsonable_encoder(key)}",
            method="GET",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=RetrieveBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        key: str,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateBookingCustomAttributeDefinitionResponse]:
        """
        Updates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to update.

        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition that contains the fields to update. Only the following fields can be updated:
            - `name`
            - `description`
            - `visibility`
            - `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
            selections are supported.

            For more information, see
            [Updatable definition fields](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attribute-definitions#updatable-definition-fields).

            To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            control, include the optional `version` field and specify the current version of the custom attribute definition.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/custom-attribute-definitions/{jsonable_encoder(key)}",
            method="PUT",
            json={
                "custom_attribute_definition": convert_and_respect_annotation_metadata(
                    object_=custom_attribute_definition, annotation=CustomAttributeDefinitionParams, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    UpdateBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=UpdateBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteBookingCustomAttributeDefinitionResponse]:
        """
        Deletes a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/custom-attribute-definitions/{jsonable_encoder(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=DeleteBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawCustomAttributeDefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateBookingCustomAttributeDefinitionResponse]:
        """
        Creates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Parameters
        ----------
        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition to create, with the following fields:

            - `key`

            - `name`. If provided, `name` must be unique (case-sensitive) across all visible booking-related custom attribute
            definitions for the seller.

            - `description`

            - `visibility`. Note that all custom attributes are visible in exported booking data, including those set to
            `VISIBILITY_HIDDEN`.

            - `schema`. With the exception of the `Selection` data type, the `schema` is specified as a
            simple URL to the JSON schema definition hosted on the Square CDN. For more information, see
            [Specifying the schema](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attribute-definitions#specify-schema).

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bookings/custom-attribute-definitions",
            method="POST",
            json={
                "custom_attribute_definition": convert_and_respect_annotation_metadata(
                    object_=custom_attribute_definition, annotation=CustomAttributeDefinitionParams, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=CreateBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, key: str, *, version: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveBookingCustomAttributeDefinitionResponse]:
        """
        Retrieves a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

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
        AsyncHttpResponse[RetrieveBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/custom-attribute-definitions/{jsonable_encoder(key)}",
            method="GET",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=RetrieveBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        key: str,
        *,
        custom_attribute_definition: CustomAttributeDefinitionParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateBookingCustomAttributeDefinitionResponse]:
        """
        Updates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to update.

        custom_attribute_definition : CustomAttributeDefinitionParams
            The custom attribute definition that contains the fields to update. Only the following fields can be updated:
            - `name`
            - `description`
            - `visibility`
            - `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
            selections are supported.

            For more information, see
            [Updatable definition fields](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attribute-definitions#updatable-definition-fields).

            To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            control, include the optional `version` field and specify the current version of the custom attribute definition.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/custom-attribute-definitions/{jsonable_encoder(key)}",
            method="PUT",
            json={
                "custom_attribute_definition": convert_and_respect_annotation_metadata(
                    object_=custom_attribute_definition, annotation=CustomAttributeDefinitionParams, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    UpdateBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=UpdateBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteBookingCustomAttributeDefinitionResponse]:
        """
        Deletes a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
        To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
        or *Appointments Premium*.

        Parameters
        ----------
        key : str
            The key of the custom attribute definition to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteBookingCustomAttributeDefinitionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/custom-attribute-definitions/{jsonable_encoder(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBookingCustomAttributeDefinitionResponse,
                    construct_type(
                        type_=DeleteBookingCustomAttributeDefinitionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
