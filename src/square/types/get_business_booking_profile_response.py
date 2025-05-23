# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .business_booking_profile import BusinessBookingProfile
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetBusinessBookingProfileResponse(UncheckedBaseModel):
    business_booking_profile: typing.Optional[BusinessBookingProfile] = pydantic.Field(default=None)
    """
    The seller's booking profile.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
