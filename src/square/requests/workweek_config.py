# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.weekday import Weekday


class WorkweekConfigParams(typing_extensions.TypedDict):
    """
    Sets the day of the week and hour of the day that a business starts a
    workweek. This is used to calculate overtime pay.
    """

    id: typing_extensions.NotRequired[str]
    """
    The UUID for this object.
    """

    start_of_week: Weekday
    """
    The day of the week on which a business week starts for
    compensation purposes.
    See [Weekday](#type-weekday) for possible values
    """

    start_of_day_local_time: str
    """
    The local time at which a business week starts. Represented as a
    string in `HH:MM` format (`HH:MM:SS` is also accepted, but seconds are
    truncated).
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
