# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from .money import MoneyParams
from ..types.gift_card_activity_adjust_increment_reason import GiftCardActivityAdjustIncrementReason


class GiftCardActivityAdjustIncrementParams(typing_extensions.TypedDict):
    """
    Represents details about an `ADJUST_INCREMENT` [gift card activity type](entity:GiftCardActivityType).
    """

    amount_money: MoneyParams
    """
    The amount added to the gift card balance. This value is a positive integer.
    """

    reason: GiftCardActivityAdjustIncrementReason
    """
    The reason the gift card balance was adjusted.
    See [Reason](#type-reason) for possible values
    """
