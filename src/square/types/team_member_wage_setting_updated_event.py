# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .team_member_wage_setting_updated_event_data import TeamMemberWageSettingUpdatedEventData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TeamMemberWageSettingUpdatedEvent(UncheckedBaseModel):
    """
    Published when a Wage Setting is updated.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the target merchant associated with the event.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of event this represents, `"team_member.wage_setting.updated"`.
    """

    event_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for the event.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timestamp of when the event was created, in RFC 3339 format.
    """

    data: typing.Optional[TeamMemberWageSettingUpdatedEventData] = pydantic.Field(default=None)
    """
    Data associated with the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
