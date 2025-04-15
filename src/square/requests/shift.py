# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .shift_wage import ShiftWageParams
from .break_ import BreakParams
from ..types.shift_status import ShiftStatus
from .money import MoneyParams


class ShiftParams(typing_extensions.TypedDict):
    """
    A record of the hourly rate, start, and end times for a single work shift
    for an employee. This might include a record of the start and end times for breaks
    taken during the shift.
    """

    id: typing_extensions.NotRequired[str]
    """
    The UUID for this object.
    """

    employee_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the employee this shift belongs to. DEPRECATED at version 2020-08-26. Use `team_member_id` instead.
    """

    location_id: str
    """
    The ID of the location this shift occurred at. The location should be based on
    where the employee clocked in.
    """

    timezone: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The read-only convenience value that is calculated from the location based
    on the `location_id`. Format: the IANA timezone database identifier for the
    location timezone.
    """

    start_at: str
    """
    RFC 3339; shifted to the location timezone + offset. Precision up to the
    minute is respected; seconds are truncated.
    """

    end_at: typing_extensions.NotRequired[typing.Optional[str]]
    """
    RFC 3339; shifted to the timezone + offset. Precision up to the minute is
    respected; seconds are truncated.
    """

    wage: typing_extensions.NotRequired[ShiftWageParams]
    """
    Job and pay related information. If the wage is not set on create, it defaults to a wage
    of zero. If the title is not set on create, it defaults to the name of the role the employee
    is assigned to, if any.
    """

    breaks: typing_extensions.NotRequired[typing.Optional[typing.Sequence[BreakParams]]]
    """
    A list of all the paid or unpaid breaks that were taken during this shift.
    """

    status: typing_extensions.NotRequired[ShiftStatus]
    """
    Describes the working state of the current `Shift`.
    See [ShiftStatus](#type-shiftstatus) for possible values
    """

    version: typing_extensions.NotRequired[int]
    """
    Used for resolving concurrency issues. The request fails if the version
    provided does not match the server version at the time of the request. If not provided,
    Square executes a blind write; potentially overwriting data from another
    write.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    A read-only timestamp in RFC 3339 format; presented in UTC.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    A read-only timestamp in RFC 3339 format; presented in UTC.
    """

    team_member_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the team member this shift belongs to. Replaced `employee_id` at version "2020-08-26".
    """

    declared_cash_tip_money: typing_extensions.NotRequired[MoneyParams]
    """
    The tips declared by the team member for the shift.
    """
