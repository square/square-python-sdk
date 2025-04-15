# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class SquareAccountDetailsParams(typing_extensions.TypedDict):
    """
    Additional details about Square Account payments.
    """

    payment_source_token: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Unique identifier for the payment source used for this payment.
    """

    errors: typing_extensions.NotRequired[typing.Optional[typing.Sequence[ErrorParams]]]
    """
    Information about errors encountered during the request.
    """
