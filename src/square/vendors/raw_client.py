# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..requests.vendor import VendorParams
from ..core.request_options import RequestOptions
from ..core.http_response import HttpResponse
from ..types.batch_create_vendors_response import BatchCreateVendorsResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.batch_get_vendors_response import BatchGetVendorsResponse
from ..requests.update_vendor_request import UpdateVendorRequestParams
from ..types.batch_update_vendors_response import BatchUpdateVendorsResponse
from ..types.create_vendor_response import CreateVendorResponse
from ..requests.search_vendors_request_filter import SearchVendorsRequestFilterParams
from ..requests.search_vendors_request_sort import SearchVendorsRequestSortParams
from ..types.search_vendors_response import SearchVendorsResponse
from ..types.get_vendor_response import GetVendorResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..types.update_vendor_response import UpdateVendorResponse
from ..core.client_wrapper import AsyncClientWrapper
from ..core.http_response import AsyncHttpResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawVendorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def batch_create(
        self, *, vendors: typing.Dict[str, VendorParams], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCreateVendorsResponse]:
        """
        Creates one or more [Vendor](entity:Vendor) objects to represent suppliers to a seller.

        Parameters
        ----------
        vendors : typing.Dict[str, VendorParams]
            Specifies a set of new [Vendor](entity:Vendor) objects as represented by a collection of idempotency-key/`Vendor`-object pairs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchCreateVendorsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vendors/bulk-create",
            method="POST",
            json={
                "vendors": convert_and_respect_annotation_metadata(
                    object_=vendors, annotation=typing.Dict[str, VendorParams], direction="write"
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
                    BatchCreateVendorsResponse,
                    construct_type(
                        type_=BatchCreateVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def batch_get(
        self,
        *,
        vendor_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchGetVendorsResponse]:
        """
        Retrieves one or more vendors of specified [Vendor](entity:Vendor) IDs.

        Parameters
        ----------
        vendor_ids : typing.Optional[typing.Sequence[str]]
            IDs of the [Vendor](entity:Vendor) objects to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchGetVendorsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vendors/bulk-retrieve",
            method="POST",
            json={
                "vendor_ids": vendor_ids,
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
                    BatchGetVendorsResponse,
                    construct_type(
                        type_=BatchGetVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def batch_update(
        self,
        *,
        vendors: typing.Dict[str, UpdateVendorRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchUpdateVendorsResponse]:
        """
        Updates one or more of existing [Vendor](entity:Vendor) objects as suppliers to a seller.

        Parameters
        ----------
        vendors : typing.Dict[str, UpdateVendorRequestParams]
            A set of [UpdateVendorRequest](entity:UpdateVendorRequest) objects encapsulating to-be-updated [Vendor](entity:Vendor)
            objects. The set is represented by  a collection of `Vendor`-ID/`UpdateVendorRequest`-object pairs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchUpdateVendorsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vendors/bulk-update",
            method="PUT",
            json={
                "vendors": convert_and_respect_annotation_metadata(
                    object_=vendors, annotation=typing.Dict[str, UpdateVendorRequestParams], direction="write"
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
                    BatchUpdateVendorsResponse,
                    construct_type(
                        type_=BatchUpdateVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        idempotency_key: str,
        vendor: typing.Optional[VendorParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateVendorResponse]:
        """
        Creates a single [Vendor](entity:Vendor) object to represent a supplier to a seller.

        Parameters
        ----------
        idempotency_key : str
            A client-supplied, universally unique identifier (UUID) to make this [CreateVendor](api-endpoint:Vendors-CreateVendor) call idempotent.

            See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
            information.

        vendor : typing.Optional[VendorParams]
            The requested [Vendor](entity:Vendor) to be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateVendorResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vendors/create",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "vendor": convert_and_respect_annotation_metadata(
                    object_=vendor, annotation=VendorParams, direction="write"
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
                    CreateVendorResponse,
                    construct_type(
                        type_=CreateVendorResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def search(
        self,
        *,
        filter: typing.Optional[SearchVendorsRequestFilterParams] = OMIT,
        sort: typing.Optional[SearchVendorsRequestSortParams] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchVendorsResponse]:
        """
        Searches for vendors using a filter against supported [Vendor](entity:Vendor) properties and a supported sorter.

        Parameters
        ----------
        filter : typing.Optional[SearchVendorsRequestFilterParams]
            Specifies a filter used to search for vendors.

        sort : typing.Optional[SearchVendorsRequestSortParams]
            Specifies a sorter used to sort the returned vendors.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchVendorsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vendors/search",
            method="POST",
            json={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=SearchVendorsRequestFilterParams, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=SearchVendorsRequestSortParams, direction="write"
                ),
                "cursor": cursor,
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
                    SearchVendorsResponse,
                    construct_type(
                        type_=SearchVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, vendor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetVendorResponse]:
        """
        Retrieves the vendor of a specified [Vendor](entity:Vendor) ID.

        Parameters
        ----------
        vendor_id : str
            ID of the [Vendor](entity:Vendor) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetVendorResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vendors/{jsonable_encoder(vendor_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVendorResponse,
                    construct_type(
                        type_=GetVendorResponse,  # type: ignore
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
        vendor_id: str,
        *,
        vendor: VendorParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateVendorResponse]:
        """
        Updates an existing [Vendor](entity:Vendor) object as a supplier to a seller.

        Parameters
        ----------
        vendor_id : str
            ID of the [Vendor](entity:Vendor) to retrieve.

        vendor : VendorParams
            The specified [Vendor](entity:Vendor) to be updated.

        idempotency_key : typing.Optional[str]
            A client-supplied, universally unique identifier (UUID) for the
            request.

            See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
            information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateVendorResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vendors/{jsonable_encoder(vendor_id)}",
            method="PUT",
            json={
                "idempotency_key": idempotency_key,
                "vendor": convert_and_respect_annotation_metadata(
                    object_=vendor, annotation=VendorParams, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateVendorResponse,
                    construct_type(
                        type_=UpdateVendorResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawVendorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def batch_create(
        self, *, vendors: typing.Dict[str, VendorParams], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BatchCreateVendorsResponse]:
        """
        Creates one or more [Vendor](entity:Vendor) objects to represent suppliers to a seller.

        Parameters
        ----------
        vendors : typing.Dict[str, VendorParams]
            Specifies a set of new [Vendor](entity:Vendor) objects as represented by a collection of idempotency-key/`Vendor`-object pairs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchCreateVendorsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vendors/bulk-create",
            method="POST",
            json={
                "vendors": convert_and_respect_annotation_metadata(
                    object_=vendors, annotation=typing.Dict[str, VendorParams], direction="write"
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
                    BatchCreateVendorsResponse,
                    construct_type(
                        type_=BatchCreateVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def batch_get(
        self,
        *,
        vendor_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchGetVendorsResponse]:
        """
        Retrieves one or more vendors of specified [Vendor](entity:Vendor) IDs.

        Parameters
        ----------
        vendor_ids : typing.Optional[typing.Sequence[str]]
            IDs of the [Vendor](entity:Vendor) objects to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchGetVendorsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vendors/bulk-retrieve",
            method="POST",
            json={
                "vendor_ids": vendor_ids,
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
                    BatchGetVendorsResponse,
                    construct_type(
                        type_=BatchGetVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def batch_update(
        self,
        *,
        vendors: typing.Dict[str, UpdateVendorRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchUpdateVendorsResponse]:
        """
        Updates one or more of existing [Vendor](entity:Vendor) objects as suppliers to a seller.

        Parameters
        ----------
        vendors : typing.Dict[str, UpdateVendorRequestParams]
            A set of [UpdateVendorRequest](entity:UpdateVendorRequest) objects encapsulating to-be-updated [Vendor](entity:Vendor)
            objects. The set is represented by  a collection of `Vendor`-ID/`UpdateVendorRequest`-object pairs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchUpdateVendorsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vendors/bulk-update",
            method="PUT",
            json={
                "vendors": convert_and_respect_annotation_metadata(
                    object_=vendors, annotation=typing.Dict[str, UpdateVendorRequestParams], direction="write"
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
                    BatchUpdateVendorsResponse,
                    construct_type(
                        type_=BatchUpdateVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        idempotency_key: str,
        vendor: typing.Optional[VendorParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateVendorResponse]:
        """
        Creates a single [Vendor](entity:Vendor) object to represent a supplier to a seller.

        Parameters
        ----------
        idempotency_key : str
            A client-supplied, universally unique identifier (UUID) to make this [CreateVendor](api-endpoint:Vendors-CreateVendor) call idempotent.

            See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
            information.

        vendor : typing.Optional[VendorParams]
            The requested [Vendor](entity:Vendor) to be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateVendorResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vendors/create",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "vendor": convert_and_respect_annotation_metadata(
                    object_=vendor, annotation=VendorParams, direction="write"
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
                    CreateVendorResponse,
                    construct_type(
                        type_=CreateVendorResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def search(
        self,
        *,
        filter: typing.Optional[SearchVendorsRequestFilterParams] = OMIT,
        sort: typing.Optional[SearchVendorsRequestSortParams] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchVendorsResponse]:
        """
        Searches for vendors using a filter against supported [Vendor](entity:Vendor) properties and a supported sorter.

        Parameters
        ----------
        filter : typing.Optional[SearchVendorsRequestFilterParams]
            Specifies a filter used to search for vendors.

        sort : typing.Optional[SearchVendorsRequestSortParams]
            Specifies a sorter used to sort the returned vendors.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchVendorsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vendors/search",
            method="POST",
            json={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=SearchVendorsRequestFilterParams, direction="write"
                ),
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=SearchVendorsRequestSortParams, direction="write"
                ),
                "cursor": cursor,
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
                    SearchVendorsResponse,
                    construct_type(
                        type_=SearchVendorsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, vendor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetVendorResponse]:
        """
        Retrieves the vendor of a specified [Vendor](entity:Vendor) ID.

        Parameters
        ----------
        vendor_id : str
            ID of the [Vendor](entity:Vendor) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetVendorResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vendors/{jsonable_encoder(vendor_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVendorResponse,
                    construct_type(
                        type_=GetVendorResponse,  # type: ignore
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
        vendor_id: str,
        *,
        vendor: VendorParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateVendorResponse]:
        """
        Updates an existing [Vendor](entity:Vendor) object as a supplier to a seller.

        Parameters
        ----------
        vendor_id : str
            ID of the [Vendor](entity:Vendor) to retrieve.

        vendor : VendorParams
            The specified [Vendor](entity:Vendor) to be updated.

        idempotency_key : typing.Optional[str]
            A client-supplied, universally unique identifier (UUID) for the
            request.

            See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
            [API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
            information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateVendorResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vendors/{jsonable_encoder(vendor_id)}",
            method="PUT",
            json={
                "idempotency_key": idempotency_key,
                "vendor": convert_and_respect_annotation_metadata(
                    object_=vendor, annotation=VendorParams, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateVendorResponse,
                    construct_type(
                        type_=UpdateVendorResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
