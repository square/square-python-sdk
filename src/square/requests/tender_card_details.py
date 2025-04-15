# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.tender_card_details_status import TenderCardDetailsStatus
from .card import CardParams
from ..types.tender_card_details_entry_method import TenderCardDetailsEntryMethod


class TenderCardDetailsParams(typing_extensions.TypedDict):
    """
    Represents additional details of a tender with `type` `CARD` or `SQUARE_GIFT_CARD`
    """

    status: typing_extensions.NotRequired[TenderCardDetailsStatus]
    """
    The credit card payment's current state (such as `AUTHORIZED` or
    `CAPTURED`). See [TenderCardDetailsStatus](entity:TenderCardDetailsStatus)
    for possible values.
    See [TenderCardDetailsStatus](#type-tendercarddetailsstatus) for possible values
    """

    card: typing_extensions.NotRequired[CardParams]
    """
    The credit card's non-confidential details.
    """

    entry_method: typing_extensions.NotRequired[TenderCardDetailsEntryMethod]
    """
    The method used to enter the card's details for the transaction.
    See [TenderCardDetailsEntryMethod](#type-tendercarddetailsentrymethod) for possible values
    """
