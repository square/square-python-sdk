# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .wage_setting import WageSettingParams
import typing
from .error import ErrorParams


class GetWageSettingResponseParams(typing_extensions.TypedDict):
    """
    Represents a response from a retrieve request containing the specified `WageSetting` object or error messages.
    """

    wage_setting: typing_extensions.NotRequired[WageSettingParams]
    """
    The successfully retrieved `WageSetting` object.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    The errors that occurred during the request.
    """
