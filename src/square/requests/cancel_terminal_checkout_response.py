# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .terminal_checkout import TerminalCheckoutParams


class CancelTerminalCheckoutResponseParams(typing_extensions.TypedDict):
    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information about errors encountered during the request.
    """

    checkout: typing_extensions.NotRequired[TerminalCheckoutParams]
    """
    The canceled `TerminalCheckout`.
    """
