# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .labor_shift_created_event_object import LaborShiftCreatedEventObjectParams


class LaborShiftCreatedEventDataParams(typing_extensions.TypedDict):
    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The type of object affected by the event. For this event, the value is `shift`.
    """

    id: typing_extensions.NotRequired[str]
    """
    The ID of the affected `Shift`.
    """

    object: typing_extensions.NotRequired[LaborShiftCreatedEventObjectParams]
    """
    An object containing the affected `Shift`.
    """
