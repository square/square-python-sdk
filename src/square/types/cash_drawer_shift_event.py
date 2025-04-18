# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .cash_drawer_event_type import CashDrawerEventType
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CashDrawerShiftEvent(UncheckedBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the event.
    """

    event_type: typing.Optional[CashDrawerEventType] = pydantic.Field(default=None)
    """
    The type of cash drawer shift event.
    See [CashDrawerEventType](#type-cashdrawereventtype) for possible values
    """

    event_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of money that was added to or removed from the cash drawer
    in the event. The amount can be positive (for added money)
    or zero (for other tender type payments). The addition or removal of money can be determined by
    by the event type.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event time in RFC 3339 format.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the event, entered by the employee that
    created the event.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the team member that created the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
