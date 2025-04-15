# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .break_type import BreakTypeParams
import typing
from .error import ErrorParams


class GetBreakTypeResponseParams(typing_extensions.TypedDict):
    """
    The response to a request to get a `BreakType`. The response contains
    the requested `BreakType` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    break_type: typing_extensions.NotRequired[BreakTypeParams]
    """
    The response object.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
