# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .terminal_action import TerminalActionParams


class CancelTerminalActionResponseParams(typing_extensions.TypedDict):
    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information on errors encountered during the request.
    """

    action: typing_extensions.NotRequired[TerminalActionParams]
    """
    The canceled `TerminalAction`
    """
