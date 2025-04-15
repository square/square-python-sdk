# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .money import MoneyParams


class TenderCashDetailsParams(typing_extensions.TypedDict):
    """
    Represents the details of a tender with `type` `CASH`.
    """

    buyer_tendered_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of cash provided by the buyer, before change is given.
    """

    change_back_money: typing_extensions.NotRequired[MoneyParams]
    """
    The amount of change returned to the buyer.
    """
