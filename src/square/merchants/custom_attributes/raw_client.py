# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...requests.bulk_delete_merchant_custom_attributes_request_merchant_custom_attribute_delete_request import (
    BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams,
)
from ...core.request_options import RequestOptions
from ...core.http_response import HttpResponse
from ...types.bulk_delete_merchant_custom_attributes_response import BulkDeleteMerchantCustomAttributesResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...requests.bulk_upsert_merchant_custom_attributes_request_merchant_custom_attribute_upsert_request import (
    BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams,
)
from ...types.bulk_upsert_merchant_custom_attributes_response import BulkUpsertMerchantCustomAttributesResponse
from ...types.retrieve_merchant_custom_attribute_response import RetrieveMerchantCustomAttributeResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...requests.custom_attribute import CustomAttributeParams
from ...types.upsert_merchant_custom_attribute_response import UpsertMerchantCustomAttributeResponse
from ...types.delete_merchant_custom_attribute_response import DeleteMerchantCustomAttributeResponse
from ...core.client_wrapper import AsyncClientWrapper
from ...core.http_response import AsyncHttpResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawCustomAttributesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def batch_delete(
        self,
        *,
        values: typing.Dict[str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkDeleteMerchantCustomAttributesResponse]:
        """
        Deletes [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
        To delete a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams]
            The data used to update the `CustomAttribute` objects.
            The keys must be unique and are used to map to the corresponding response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkDeleteMerchantCustomAttributesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/merchants/custom-attributes/bulk-delete",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[
                        str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams
                    ],
                    direction="write",
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
                    BulkDeleteMerchantCustomAttributesResponse,
                    construct_type(
                        type_=BulkDeleteMerchantCustomAttributesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def batch_upsert(
        self,
        *,
        values: typing.Dict[str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkUpsertMerchantCustomAttributesResponse]:
        """
        Creates or updates [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
        Use this endpoint to set the value of one or more custom attributes for a merchant.
        A custom attribute is based on a custom attribute definition in a Square seller account, which is
        created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
        This `BulkUpsertMerchantCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
        requests and returns a map of individual upsert responses. Each upsert request has a unique ID
        and provides a merchant ID and custom attribute. Each upsert response is returned with the ID
        of the corresponding request.
        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams]
            A map containing 1 to 25 individual upsert requests. For each request, provide an
            arbitrary ID that is unique for this `BulkUpsertMerchantCustomAttributes` request and the
            information needed to create or update a custom attribute.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkUpsertMerchantCustomAttributesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/merchants/custom-attributes/bulk-upsert",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[
                        str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams
                    ],
                    direction="write",
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
                    BulkUpsertMerchantCustomAttributesResponse,
                    construct_type(
                        type_=BulkUpsertMerchantCustomAttributesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        merchant_id: str,
        key: str,
        *,
        with_definition: typing.Optional[bool] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveMerchantCustomAttributeResponse]:
        """
        Retrieves a [custom attribute](entity:CustomAttribute) associated with a merchant.
        You can use the `with_definition` query parameter to also retrieve the custom attribute definition
        in the same call.
        To retrieve a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        merchant_id : str
            The ID of the target [merchant](entity:Merchant).

        key : str
            The key of the custom attribute to retrieve. This key must match the `key` of a custom
            attribute definition in the Square seller account. If the requesting application is not the
            definition owner, you must use the qualified key.

        with_definition : typing.Optional[bool]
            Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of
            the custom attribute. Set this parameter to `true` to get the name and description of the custom
            attribute, information about the data type, or other definition details. The default value is `false`.

        version : typing.Optional[int]
            The current version of the custom attribute, which is used for strongly consistent reads to
            guarantee that you receive the most up-to-date data. When included in the request, Square
            returns the specified version or a higher version if one exists. If the specified version is
            higher than the current version, Square returns a `BAD_REQUEST` error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveMerchantCustomAttributeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/merchants/{jsonable_encoder(merchant_id)}/custom-attributes/{jsonable_encoder(key)}",
            method="GET",
            params={
                "with_definition": with_definition,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveMerchantCustomAttributeResponse,
                    construct_type(
                        type_=RetrieveMerchantCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upsert(
        self,
        merchant_id: str,
        key: str,
        *,
        custom_attribute: CustomAttributeParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpsertMerchantCustomAttributeResponse]:
        """
        Creates or updates a [custom attribute](entity:CustomAttribute) for a merchant.
        Use this endpoint to set the value of a custom attribute for a specified merchant.
        A custom attribute is based on a custom attribute definition in a Square seller account, which
        is created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        merchant_id : str
            The ID of the target [merchant](entity:Merchant).

        key : str
            The key of the custom attribute to create or update. This key must match the `key` of a
            custom attribute definition in the Square seller account. If the requesting application is not
            the definition owner, you must use the qualified key.

        custom_attribute : CustomAttributeParams
            The custom attribute to create or update, with the following fields:
            - `value`. This value must conform to the `schema` specified by the definition.
            For more information, see [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
            - The version field must match the current version of the custom attribute definition to enable
            [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpsertMerchantCustomAttributeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/merchants/{jsonable_encoder(merchant_id)}/custom-attributes/{jsonable_encoder(key)}",
            method="POST",
            json={
                "custom_attribute": convert_and_respect_annotation_metadata(
                    object_=custom_attribute, annotation=CustomAttributeParams, direction="write"
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
                    UpsertMerchantCustomAttributeResponse,
                    construct_type(
                        type_=UpsertMerchantCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, merchant_id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMerchantCustomAttributeResponse]:
        """
        Deletes a [custom attribute](entity:CustomAttribute) associated with a merchant.
        To delete a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        merchant_id : str
            The ID of the target [merchant](entity:Merchant).

        key : str
            The key of the custom attribute to delete. This key must match the `key` of a custom
            attribute definition in the Square seller account. If the requesting application is not the
            definition owner, you must use the qualified key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMerchantCustomAttributeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/merchants/{jsonable_encoder(merchant_id)}/custom-attributes/{jsonable_encoder(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMerchantCustomAttributeResponse,
                    construct_type(
                        type_=DeleteMerchantCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawCustomAttributesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def batch_delete(
        self,
        *,
        values: typing.Dict[str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkDeleteMerchantCustomAttributesResponse]:
        """
        Deletes [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
        To delete a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams]
            The data used to update the `CustomAttribute` objects.
            The keys must be unique and are used to map to the corresponding response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkDeleteMerchantCustomAttributesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/merchants/custom-attributes/bulk-delete",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[
                        str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams
                    ],
                    direction="write",
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
                    BulkDeleteMerchantCustomAttributesResponse,
                    construct_type(
                        type_=BulkDeleteMerchantCustomAttributesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def batch_upsert(
        self,
        *,
        values: typing.Dict[str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkUpsertMerchantCustomAttributesResponse]:
        """
        Creates or updates [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
        Use this endpoint to set the value of one or more custom attributes for a merchant.
        A custom attribute is based on a custom attribute definition in a Square seller account, which is
        created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
        This `BulkUpsertMerchantCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
        requests and returns a map of individual upsert responses. Each upsert request has a unique ID
        and provides a merchant ID and custom attribute. Each upsert response is returned with the ID
        of the corresponding request.
        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams]
            A map containing 1 to 25 individual upsert requests. For each request, provide an
            arbitrary ID that is unique for this `BulkUpsertMerchantCustomAttributes` request and the
            information needed to create or update a custom attribute.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkUpsertMerchantCustomAttributesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/merchants/custom-attributes/bulk-upsert",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[
                        str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams
                    ],
                    direction="write",
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
                    BulkUpsertMerchantCustomAttributesResponse,
                    construct_type(
                        type_=BulkUpsertMerchantCustomAttributesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        merchant_id: str,
        key: str,
        *,
        with_definition: typing.Optional[bool] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveMerchantCustomAttributeResponse]:
        """
        Retrieves a [custom attribute](entity:CustomAttribute) associated with a merchant.
        You can use the `with_definition` query parameter to also retrieve the custom attribute definition
        in the same call.
        To retrieve a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        merchant_id : str
            The ID of the target [merchant](entity:Merchant).

        key : str
            The key of the custom attribute to retrieve. This key must match the `key` of a custom
            attribute definition in the Square seller account. If the requesting application is not the
            definition owner, you must use the qualified key.

        with_definition : typing.Optional[bool]
            Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of
            the custom attribute. Set this parameter to `true` to get the name and description of the custom
            attribute, information about the data type, or other definition details. The default value is `false`.

        version : typing.Optional[int]
            The current version of the custom attribute, which is used for strongly consistent reads to
            guarantee that you receive the most up-to-date data. When included in the request, Square
            returns the specified version or a higher version if one exists. If the specified version is
            higher than the current version, Square returns a `BAD_REQUEST` error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveMerchantCustomAttributeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/merchants/{jsonable_encoder(merchant_id)}/custom-attributes/{jsonable_encoder(key)}",
            method="GET",
            params={
                "with_definition": with_definition,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveMerchantCustomAttributeResponse,
                    construct_type(
                        type_=RetrieveMerchantCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upsert(
        self,
        merchant_id: str,
        key: str,
        *,
        custom_attribute: CustomAttributeParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpsertMerchantCustomAttributeResponse]:
        """
        Creates or updates a [custom attribute](entity:CustomAttribute) for a merchant.
        Use this endpoint to set the value of a custom attribute for a specified merchant.
        A custom attribute is based on a custom attribute definition in a Square seller account, which
        is created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        merchant_id : str
            The ID of the target [merchant](entity:Merchant).

        key : str
            The key of the custom attribute to create or update. This key must match the `key` of a
            custom attribute definition in the Square seller account. If the requesting application is not
            the definition owner, you must use the qualified key.

        custom_attribute : CustomAttributeParams
            The custom attribute to create or update, with the following fields:
            - `value`. This value must conform to the `schema` specified by the definition.
            For more information, see [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
            - The version field must match the current version of the custom attribute definition to enable
            [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency. For more information,
            see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpsertMerchantCustomAttributeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/merchants/{jsonable_encoder(merchant_id)}/custom-attributes/{jsonable_encoder(key)}",
            method="POST",
            json={
                "custom_attribute": convert_and_respect_annotation_metadata(
                    object_=custom_attribute, annotation=CustomAttributeParams, direction="write"
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
                    UpsertMerchantCustomAttributeResponse,
                    construct_type(
                        type_=UpsertMerchantCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, merchant_id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMerchantCustomAttributeResponse]:
        """
        Deletes a [custom attribute](entity:CustomAttribute) associated with a merchant.
        To delete a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        merchant_id : str
            The ID of the target [merchant](entity:Merchant).

        key : str
            The key of the custom attribute to delete. This key must match the `key` of a custom
            attribute definition in the Square seller account. If the requesting application is not the
            definition owner, you must use the qualified key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMerchantCustomAttributeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/merchants/{jsonable_encoder(merchant_id)}/custom-attributes/{jsonable_encoder(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMerchantCustomAttributeResponse,
                    construct_type(
                        type_=DeleteMerchantCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
