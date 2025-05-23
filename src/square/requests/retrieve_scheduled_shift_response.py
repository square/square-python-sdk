# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .scheduled_shift import ScheduledShiftParams
import typing
from .error import ErrorParams


class RetrieveScheduledShiftResponseParams(typing_extensions.TypedDict):
    """
    Represents a [RetrieveScheduledShift](api-endpoint:Labor-RetrieveScheduledShift) response.
    Either `scheduled_shift` or `errors` is present in the response.
    """

    scheduled_shift: typing_extensions.NotRequired[ScheduledShiftParams]
    """
    The requested scheduled shift.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
