# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BookingCustomAttributeDeleteResponse(UncheckedBaseModel):
    """
    Represents a response for an individual upsert request in a [BulkDeleteBookingCustomAttributes](api-endpoint:BookingCustomAttributes-BulkDeleteBookingCustomAttributes) operation.
    """

    booking_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [booking](entity:Booking) associated with the custom attribute.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred while processing the individual request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
