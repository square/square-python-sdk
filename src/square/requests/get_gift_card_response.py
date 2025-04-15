# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .gift_card import GiftCardParams


class GetGiftCardResponseParams(typing_extensions.TypedDict):
    """
    A response that contains a `GiftCard`. The response might contain a set of `Error` objects
    if the request resulted in errors.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    gift_card: typing_extensions.NotRequired[GiftCardParams]
    """
    The gift card retrieved.
    """
