# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from .money import MoneyParams
import typing_extensions


class DestinationDetailsCashRefundDetailsParams(typing_extensions.TypedDict):
    """
    Stores details about a cash refund. Contains only non-confidential information.
    """

    seller_supplied_money: MoneyParams
    """
    The amount and currency of the money supplied by the seller.
    """

    change_back_money: typing_extensions.NotRequired[MoneyParams]
    """
    The amount of change due back to the seller.
    This read-only field is calculated
    from the `amount_money` and `seller_supplied_money` fields.
    """
