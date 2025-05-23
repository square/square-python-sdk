# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .timecard_filter_status import TimecardFilterStatus
from .time_range import TimeRange
from .timecard_workday import TimecardWorkday
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TimecardFilter(UncheckedBaseModel):
    """
    Defines a filter used in a search for `Timecard` records. `AND` logic is
    used by Square's servers to apply each filter property specified.
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fetch timecards for the specified location.
    """

    status: typing.Optional[TimecardFilterStatus] = pydantic.Field(default=None)
    """
    Fetch a `Timecard` instance by `Timecard.status`.
    See [TimecardFilterStatus](#type-timecardfilterstatus) for possible values
    """

    start: typing.Optional[TimeRange] = pydantic.Field(default=None)
    """
    Fetch `Timecard` instances that start in the time range - Inclusive.
    """

    end: typing.Optional[TimeRange] = pydantic.Field(default=None)
    """
    Fetch the `Timecard` instances that end in the time range - Inclusive.
    """

    workday: typing.Optional[TimecardWorkday] = pydantic.Field(default=None)
    """
    Fetch the `Timecard` instances based on the workday date range.
    """

    team_member_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fetch timecards for the specified team members.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
