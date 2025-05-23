# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .time_range import TimeRange
from .terminal_action_action_type import TerminalActionActionType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TerminalActionQueryFilter(UncheckedBaseModel):
    device_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    `TerminalAction`s associated with a specific device. If no device is specified then all
    `TerminalAction`s for the merchant will be displayed.
    """

    created_at: typing.Optional[TimeRange] = pydantic.Field(default=None)
    """
    Time range for the beginning of the reporting period. Inclusive.
    Default value: The current time minus one day.
    Note that `TerminalAction`s are available for 30 days after creation.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter results with the desired status of the `TerminalAction`
    Options: `PENDING`, `IN_PROGRESS`, `CANCEL_REQUESTED`, `CANCELED`, `COMPLETED`
    """

    type: typing.Optional[TerminalActionActionType] = pydantic.Field(default=None)
    """
    Filter results with the requested ActionType.
    See [TerminalActionActionType](#type-terminalactionactiontype) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
