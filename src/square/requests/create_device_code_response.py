# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .device_code import DeviceCodeParams


class CreateDeviceCodeResponseParams(typing_extensions.TypedDict):
    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    device_code: typing_extensions.NotRequired[DeviceCodeParams]
    """
    The created DeviceCode object containing the device code string.
    """
