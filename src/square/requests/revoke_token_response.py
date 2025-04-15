# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class RevokeTokenResponseParams(typing_extensions.TypedDict):
    success: typing_extensions.NotRequired[bool]
    """
    If the request is successful, this is `true`.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
