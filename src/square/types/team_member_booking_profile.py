# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TeamMemberBookingProfile(UncheckedBaseModel):
    """
    The booking profile of a seller's team member, including the team member's ID, display name, description and whether the team member can be booked as a service provider.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [TeamMember](entity:TeamMember) object for the team member associated with the booking profile.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the team member.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of the team member.
    """

    is_bookable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the team member can be booked through the Bookings API or the seller's online booking channel or site (`true`) or not (`false`).
    """

    profile_image_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the team member's image for the bookings profile.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
