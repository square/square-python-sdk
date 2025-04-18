# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from .custom_attribute import CustomAttributeParams
import typing_extensions
import typing


class BookingCustomAttributeUpsertRequestParams(typing_extensions.TypedDict):
    """
    Represents an individual upsert request in a [BulkUpsertBookingCustomAttributes](api-endpoint:BookingCustomAttributes-BulkUpsertBookingCustomAttributes)
    request. An individual request contains a booking ID, the custom attribute to create or update,
    and an optional idempotency key.
    """

    booking_id: str
    """
    The ID of the target [booking](entity:Booking).
    """

    custom_attribute: CustomAttributeParams
    """
    The custom attribute to create or update, with following fields:
    
    - `key`. This key must match the `key` of a custom attribute definition in the Square seller
    account. If the requesting application is not the definition owner, you must provide the qualified key.
    
    - `value`. This value must conform to the `schema` specified by the definition.
    For more information, see [Value data types](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attributes#value-data-types).
    
    - `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
    control for update operations, include this optional field in the request and set the
    value to the current version of the custom attribute.
    """

    idempotency_key: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique identifier for this individual upsert request, used to ensure idempotency.
    For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    """
