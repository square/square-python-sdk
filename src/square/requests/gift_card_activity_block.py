# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from ..types.gift_card_activity_block_reason import GiftCardActivityBlockReason


class GiftCardActivityBlockParams(typing_extensions.TypedDict):
    """
    Represents details about a `BLOCK` [gift card activity type](entity:GiftCardActivityType).
    """

    reason: GiftCardActivityBlockReason
    """
    The reason the gift card was blocked.
    See [Reason](#type-reason) for possible values
    """
