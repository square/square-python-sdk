# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class BookingCustomAttributeDeleteRequest(UncheckedBaseModel):
    """
    Represents an individual delete request in a [BulkDeleteBookingCustomAttributes](api-endpoint:BookingCustomAttributes-BulkDeleteBookingCustomAttributes)
    request. An individual request contains a booking ID, the custom attribute to delete, and an optional idempotency key.
    """

    booking_id: str = pydantic.Field()
    """
    The ID of the target [booking](entity:Booking).
    """

    key: str = pydantic.Field()
    """
    The key of the custom attribute to delete. This key must match the `key` of a
    custom attribute definition in the Square seller account. If the requesting application is not
    the definition owner, you must use the qualified key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
