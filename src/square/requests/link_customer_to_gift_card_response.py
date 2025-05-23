# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .gift_card import GiftCardParams


class LinkCustomerToGiftCardResponseParams(typing_extensions.TypedDict):
    """
    A response that contains the linked `GiftCard` object. If the request resulted in errors,
    the response contains a set of `Error` objects.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    gift_card: typing_extensions.NotRequired[GiftCardParams]
    """
    The gift card with the ID of the linked customer listed in the `customer_ids` field.
    """
