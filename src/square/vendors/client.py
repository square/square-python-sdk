# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawVendorsClient
from ..requests.vendor import VendorParams
from ..core.request_options import RequestOptions
from ..types.batch_create_vendors_response import BatchCreateVendorsResponse
from ..types.batch_get_vendors_response import BatchGetVendorsResponse
from ..requests.update_vendor_request import UpdateVendorRequestParams
from ..types.batch_update_vendors_response import BatchUpdateVendorsResponse
from ..types.create_vendor_response import CreateVendorResponse
from ..requests.search_vendors_request_filter import SearchVendorsRequestFilterParams
from ..requests.search_vendors_request_sort import SearchVendorsRequestSortParams
from ..types.search_vendors_response import SearchVendorsResponse
from ..types.get_vendor_response import GetVendorResponse
from ..types.update_vendor_response import UpdateVendorResponse
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawVendorsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VendorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVendorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVendorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVendorsClient
        """
        return self._raw_client

    def batch_create(
        self, *, vendors: typing.Dict[str, VendorParams], request_options: typing.Optional[RequestOptions] = None
    ) -> BatchCreateVendorsResponse:
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
        BatchCreateVendorsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.batch_create(
            vendors={
                "8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe": {
                    "name": "Joe's Fresh Seafood",
                    "address": {
                        "address_line1": "505 Electric Ave",
                        "address_line2": "Suite 600",
                        "locality": "New York",
                        "administrative_district_level1": "NY",
                        "postal_code": "10003",
                        "country": "US",
                    },
                    "contacts": [
                        {
                            "name": "Joe Burrow",
                            "email_address": "joe@joesfreshseafood.com",
                            "phone_number": "1-212-555-4250",
                            "ordinal": 1,
                        }
                    ],
                    "account_number": "4025391",
                    "note": "a vendor",
                }
            },
        )
        """
        response = self._raw_client.batch_create(vendors=vendors, request_options=request_options)
        return response.data

    def batch_get(
        self,
        *,
        vendor_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchGetVendorsResponse:
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
        BatchGetVendorsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.batch_get(
            vendor_ids=["INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4"],
        )
        """
        response = self._raw_client.batch_get(vendor_ids=vendor_ids, request_options=request_options)
        return response.data

    def batch_update(
        self,
        *,
        vendors: typing.Dict[str, UpdateVendorRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchUpdateVendorsResponse:
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
        BatchUpdateVendorsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.batch_update(
            vendors={
                "FMCYHBWT1TPL8MFH52PBMEN92A": {"vendor": {}},
                "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4": {"vendor": {}},
            },
        )
        """
        response = self._raw_client.batch_update(vendors=vendors, request_options=request_options)
        return response.data

    def create(
        self,
        *,
        idempotency_key: str,
        vendor: typing.Optional[VendorParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateVendorResponse:
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
        CreateVendorResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.create(
            idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
            vendor={
                "name": "Joe's Fresh Seafood",
                "address": {
                    "address_line1": "505 Electric Ave",
                    "address_line2": "Suite 600",
                    "locality": "New York",
                    "administrative_district_level1": "NY",
                    "postal_code": "10003",
                    "country": "US",
                },
                "contacts": [
                    {
                        "name": "Joe Burrow",
                        "email_address": "joe@joesfreshseafood.com",
                        "phone_number": "1-212-555-4250",
                        "ordinal": 1,
                    }
                ],
                "account_number": "4025391",
                "note": "a vendor",
            },
        )
        """
        response = self._raw_client.create(
            idempotency_key=idempotency_key, vendor=vendor, request_options=request_options
        )
        return response.data

    def search(
        self,
        *,
        filter: typing.Optional[SearchVendorsRequestFilterParams] = OMIT,
        sort: typing.Optional[SearchVendorsRequestSortParams] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchVendorsResponse:
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
        SearchVendorsResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.search()
        """
        response = self._raw_client.search(filter=filter, sort=sort, cursor=cursor, request_options=request_options)
        return response.data

    def get(self, vendor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetVendorResponse:
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
        GetVendorResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.get(
            vendor_id="vendor_id",
        )
        """
        response = self._raw_client.get(vendor_id, request_options=request_options)
        return response.data

    def update(
        self,
        vendor_id: str,
        *,
        vendor: VendorParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateVendorResponse:
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
        UpdateVendorResponse
            Success

        Examples
        --------
        from square import Square

        client = Square(
            token="YOUR_TOKEN",
        )
        client.vendors.update(
            vendor_id="vendor_id",
            idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
            vendor={
                "id": "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4",
                "name": "Jack's Chicken Shack",
                "version": 1,
                "status": "ACTIVE",
            },
        )
        """
        response = self._raw_client.update(
            vendor_id, vendor=vendor, idempotency_key=idempotency_key, request_options=request_options
        )
        return response.data


class AsyncVendorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVendorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVendorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVendorsClient
        """
        return self._raw_client

    async def batch_create(
        self, *, vendors: typing.Dict[str, VendorParams], request_options: typing.Optional[RequestOptions] = None
    ) -> BatchCreateVendorsResponse:
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
        BatchCreateVendorsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.batch_create(
                vendors={
                    "8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe": {
                        "name": "Joe's Fresh Seafood",
                        "address": {
                            "address_line1": "505 Electric Ave",
                            "address_line2": "Suite 600",
                            "locality": "New York",
                            "administrative_district_level1": "NY",
                            "postal_code": "10003",
                            "country": "US",
                        },
                        "contacts": [
                            {
                                "name": "Joe Burrow",
                                "email_address": "joe@joesfreshseafood.com",
                                "phone_number": "1-212-555-4250",
                                "ordinal": 1,
                            }
                        ],
                        "account_number": "4025391",
                        "note": "a vendor",
                    }
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.batch_create(vendors=vendors, request_options=request_options)
        return response.data

    async def batch_get(
        self,
        *,
        vendor_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchGetVendorsResponse:
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
        BatchGetVendorsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.batch_get(
                vendor_ids=["INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4"],
            )


        asyncio.run(main())
        """
        response = await self._raw_client.batch_get(vendor_ids=vendor_ids, request_options=request_options)
        return response.data

    async def batch_update(
        self,
        *,
        vendors: typing.Dict[str, UpdateVendorRequestParams],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchUpdateVendorsResponse:
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
        BatchUpdateVendorsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.batch_update(
                vendors={
                    "FMCYHBWT1TPL8MFH52PBMEN92A": {"vendor": {}},
                    "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4": {"vendor": {}},
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.batch_update(vendors=vendors, request_options=request_options)
        return response.data

    async def create(
        self,
        *,
        idempotency_key: str,
        vendor: typing.Optional[VendorParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateVendorResponse:
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
        CreateVendorResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.create(
                idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
                vendor={
                    "name": "Joe's Fresh Seafood",
                    "address": {
                        "address_line1": "505 Electric Ave",
                        "address_line2": "Suite 600",
                        "locality": "New York",
                        "administrative_district_level1": "NY",
                        "postal_code": "10003",
                        "country": "US",
                    },
                    "contacts": [
                        {
                            "name": "Joe Burrow",
                            "email_address": "joe@joesfreshseafood.com",
                            "phone_number": "1-212-555-4250",
                            "ordinal": 1,
                        }
                    ],
                    "account_number": "4025391",
                    "note": "a vendor",
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.create(
            idempotency_key=idempotency_key, vendor=vendor, request_options=request_options
        )
        return response.data

    async def search(
        self,
        *,
        filter: typing.Optional[SearchVendorsRequestFilterParams] = OMIT,
        sort: typing.Optional[SearchVendorsRequestSortParams] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchVendorsResponse:
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
        SearchVendorsResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.search()


        asyncio.run(main())
        """
        response = await self._raw_client.search(
            filter=filter, sort=sort, cursor=cursor, request_options=request_options
        )
        return response.data

    async def get(
        self, vendor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetVendorResponse:
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
        GetVendorResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.get(
                vendor_id="vendor_id",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(vendor_id, request_options=request_options)
        return response.data

    async def update(
        self,
        vendor_id: str,
        *,
        vendor: VendorParams,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateVendorResponse:
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
        UpdateVendorResponse
            Success

        Examples
        --------
        import asyncio

        from square import AsyncSquare

        client = AsyncSquare(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vendors.update(
                vendor_id="vendor_id",
                idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
                vendor={
                    "id": "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4",
                    "name": "Jack's Chicken Shack",
                    "version": 1,
                    "status": "ACTIVE",
                },
            )


        asyncio.run(main())
        """
        response = await self._raw_client.update(
            vendor_id, vendor=vendor, idempotency_key=idempotency_key, request_options=request_options
        )
        return response.data
