# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...requests.bulk_delete_order_custom_attributes_request_delete_custom_attribute import (
    BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams,
)
from ...core.request_options import RequestOptions
from ...core.http_response import HttpResponse
from ...types.bulk_delete_order_custom_attributes_response import BulkDeleteOrderCustomAttributesResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...requests.bulk_upsert_order_custom_attributes_request_upsert_custom_attribute import (
    BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams,
)
from ...types.bulk_upsert_order_custom_attributes_response import BulkUpsertOrderCustomAttributesResponse
from ...types.retrieve_order_custom_attribute_response import RetrieveOrderCustomAttributeResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...requests.custom_attribute import CustomAttributeParams
from ...types.upsert_order_custom_attribute_response import UpsertOrderCustomAttributeResponse
from ...types.delete_order_custom_attribute_response import DeleteOrderCustomAttributeResponse
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
        values: typing.Dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkDeleteOrderCustomAttributesResponse]:
        """
        Deletes order [custom attributes](entity:CustomAttribute) as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders.
        A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
        custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

        This `BulkDeleteOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual delete
        requests and returns a map of individual delete responses. Each delete request has a unique ID
        and provides an order ID and custom attribute. Each delete response is returned with the ID
        of the corresponding request.

        To delete a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams]
            A map of requests that correspond to individual delete operations for custom attributes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkDeleteOrderCustomAttributesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/orders/custom-attributes/bulk-delete",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams],
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
                    BulkDeleteOrderCustomAttributesResponse,
                    construct_type(
                        type_=BulkDeleteOrderCustomAttributesResponse,  # type: ignore
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
        values: typing.Dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkUpsertOrderCustomAttributesResponse]:
        """
        Creates or updates order [custom attributes](entity:CustomAttribute) as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders.
        A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
        custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

        This `BulkUpsertOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
        requests and returns a map of individual upsert responses. Each upsert request has a unique ID
        and provides an order ID and custom attribute. Each upsert response is returned with the ID
        of the corresponding request.

        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams]
            A map of requests that correspond to individual upsert operations for custom attributes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkUpsertOrderCustomAttributesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/orders/custom-attributes/bulk-upsert",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams],
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
                    BulkUpsertOrderCustomAttributesResponse,
                    construct_type(
                        type_=BulkUpsertOrderCustomAttributesResponse,  # type: ignore
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
        order_id: str,
        custom_attribute_key: str,
        *,
        version: typing.Optional[int] = None,
        with_definition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveOrderCustomAttributeResponse]:
        """
        Retrieves a [custom attribute](entity:CustomAttribute) associated with an order.

        You can use the `with_definition` query parameter to also retrieve the custom attribute definition
        in the same call.

        To retrieve a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        order_id : str
            The ID of the target [order](entity:Order).

        custom_attribute_key : str
            The key of the custom attribute to retrieve.  This key must match the key of an
            existing custom attribute definition.

        version : typing.Optional[int]
            To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            control, include this optional field and specify the current version of the custom attribute.

        with_definition : typing.Optional[bool]
            Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
            custom attribute. Set this parameter to `true` to get the name and description of each custom attribute,
            information about the data type, or other definition details. The default value is `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveOrderCustomAttributeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/orders/{jsonable_encoder(order_id)}/custom-attributes/{jsonable_encoder(custom_attribute_key)}",
            method="GET",
            params={
                "version": version,
                "with_definition": with_definition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveOrderCustomAttributeResponse,
                    construct_type(
                        type_=RetrieveOrderCustomAttributeResponse,  # type: ignore
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
        order_id: str,
        custom_attribute_key: str,
        *,
        custom_attribute: CustomAttributeParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpsertOrderCustomAttributeResponse]:
        """
        Creates or updates a [custom attribute](entity:CustomAttribute) for an order.

        Use this endpoint to set the value of a custom attribute for a specific order.
        A custom attribute is based on a custom attribute definition in a Square seller account. (To create a
        custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        order_id : str
            The ID of the target [order](entity:Order).

        custom_attribute_key : str
            The key of the custom attribute to create or update.  This key must match the key
            of an existing custom attribute definition.

        custom_attribute : CustomAttributeParams
            The custom attribute to create or update, with the following fields:

            - `value`. This value must conform to the `schema` specified by the definition.
            For more information, see [Value data types](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attributes#value-data-types).

            - `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            control, include this optional field and specify the current version of the custom attribute.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency.
            For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpsertOrderCustomAttributeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/orders/{jsonable_encoder(order_id)}/custom-attributes/{jsonable_encoder(custom_attribute_key)}",
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
                    UpsertOrderCustomAttributeResponse,
                    construct_type(
                        type_=UpsertOrderCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, order_id: str, custom_attribute_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteOrderCustomAttributeResponse]:
        """
        Deletes a [custom attribute](entity:CustomAttribute) associated with a customer profile.

        To delete a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        order_id : str
            The ID of the target [order](entity:Order).

        custom_attribute_key : str
            The key of the custom attribute to delete.  This key must match the key of an
            existing custom attribute definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteOrderCustomAttributeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/orders/{jsonable_encoder(order_id)}/custom-attributes/{jsonable_encoder(custom_attribute_key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteOrderCustomAttributeResponse,
                    construct_type(
                        type_=DeleteOrderCustomAttributeResponse,  # type: ignore
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
        values: typing.Dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkDeleteOrderCustomAttributesResponse]:
        """
        Deletes order [custom attributes](entity:CustomAttribute) as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders.
        A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
        custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

        This `BulkDeleteOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual delete
        requests and returns a map of individual delete responses. Each delete request has a unique ID
        and provides an order ID and custom attribute. Each delete response is returned with the ID
        of the corresponding request.

        To delete a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams]
            A map of requests that correspond to individual delete operations for custom attributes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkDeleteOrderCustomAttributesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/orders/custom-attributes/bulk-delete",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams],
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
                    BulkDeleteOrderCustomAttributesResponse,
                    construct_type(
                        type_=BulkDeleteOrderCustomAttributesResponse,  # type: ignore
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
        values: typing.Dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkUpsertOrderCustomAttributesResponse]:
        """
        Creates or updates order [custom attributes](entity:CustomAttribute) as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders.
        A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
        custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

        This `BulkUpsertOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
        requests and returns a map of individual upsert responses. Each upsert request has a unique ID
        and provides an order ID and custom attribute. Each upsert response is returned with the ID
        of the corresponding request.

        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        values : typing.Dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams]
            A map of requests that correspond to individual upsert operations for custom attributes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkUpsertOrderCustomAttributesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/orders/custom-attributes/bulk-upsert",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams],
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
                    BulkUpsertOrderCustomAttributesResponse,
                    construct_type(
                        type_=BulkUpsertOrderCustomAttributesResponse,  # type: ignore
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
        order_id: str,
        custom_attribute_key: str,
        *,
        version: typing.Optional[int] = None,
        with_definition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveOrderCustomAttributeResponse]:
        """
        Retrieves a [custom attribute](entity:CustomAttribute) associated with an order.

        You can use the `with_definition` query parameter to also retrieve the custom attribute definition
        in the same call.

        To retrieve a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        order_id : str
            The ID of the target [order](entity:Order).

        custom_attribute_key : str
            The key of the custom attribute to retrieve.  This key must match the key of an
            existing custom attribute definition.

        version : typing.Optional[int]
            To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            control, include this optional field and specify the current version of the custom attribute.

        with_definition : typing.Optional[bool]
            Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
            custom attribute. Set this parameter to `true` to get the name and description of each custom attribute,
            information about the data type, or other definition details. The default value is `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveOrderCustomAttributeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/orders/{jsonable_encoder(order_id)}/custom-attributes/{jsonable_encoder(custom_attribute_key)}",
            method="GET",
            params={
                "version": version,
                "with_definition": with_definition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveOrderCustomAttributeResponse,
                    construct_type(
                        type_=RetrieveOrderCustomAttributeResponse,  # type: ignore
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
        order_id: str,
        custom_attribute_key: str,
        *,
        custom_attribute: CustomAttributeParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpsertOrderCustomAttributeResponse]:
        """
        Creates or updates a [custom attribute](entity:CustomAttribute) for an order.

        Use this endpoint to set the value of a custom attribute for a specific order.
        A custom attribute is based on a custom attribute definition in a Square seller account. (To create a
        custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

        To create or update a custom attribute owned by another application, the `visibility` setting
        must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        order_id : str
            The ID of the target [order](entity:Order).

        custom_attribute_key : str
            The key of the custom attribute to create or update.  This key must match the key
            of an existing custom attribute definition.

        custom_attribute : CustomAttributeParams
            The custom attribute to create or update, with the following fields:

            - `value`. This value must conform to the `schema` specified by the definition.
            For more information, see [Value data types](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attributes#value-data-types).

            - `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
            control, include this optional field and specify the current version of the custom attribute.

        idempotency_key : typing.Optional[str]
            A unique identifier for this request, used to ensure idempotency.
            For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpsertOrderCustomAttributeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/orders/{jsonable_encoder(order_id)}/custom-attributes/{jsonable_encoder(custom_attribute_key)}",
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
                    UpsertOrderCustomAttributeResponse,
                    construct_type(
                        type_=UpsertOrderCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, order_id: str, custom_attribute_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteOrderCustomAttributeResponse]:
        """
        Deletes a [custom attribute](entity:CustomAttribute) associated with a customer profile.

        To delete a custom attribute owned by another application, the `visibility` setting must be
        `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
        (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

        Parameters
        ----------
        order_id : str
            The ID of the target [order](entity:Order).

        custom_attribute_key : str
            The key of the custom attribute to delete.  This key must match the key of an
            existing custom attribute definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteOrderCustomAttributeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/orders/{jsonable_encoder(order_id)}/custom-attributes/{jsonable_encoder(custom_attribute_key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteOrderCustomAttributeResponse,
                    construct_type(
                        type_=DeleteOrderCustomAttributeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
