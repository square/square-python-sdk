# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from .money import MoneyParams


class GiftCardActivityImportParams(typing_extensions.TypedDict):
    """
    Represents details about an `IMPORT` [gift card activity type](entity:GiftCardActivityType).
    This activity type is used when Square imports a third-party gift card, in which case the
    `gan_source` of the gift card is set to `OTHER`.
    """

    amount_money: MoneyParams
    """
    The balance amount on the imported gift card.
    """
