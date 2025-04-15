# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.gift_card_type import GiftCardType
from ..types.gift_card_gan_source import GiftCardGanSource
from ..types.gift_card_status import GiftCardStatus
from .money import MoneyParams
import typing


class GiftCardParams(typing_extensions.TypedDict):
    """
    Represents a Square gift card.
    """

    id: typing_extensions.NotRequired[str]
    """
    The Square-assigned ID of the gift card.
    """

    type: GiftCardType
    """
    The gift card type.
    See [Type](#type-type) for possible values
    """

    gan_source: typing_extensions.NotRequired[GiftCardGanSource]
    """
    The source that generated the gift card account number (GAN). The default value is `SQUARE`.
    See [GANSource](#type-gansource) for possible values
    """

    state: typing_extensions.NotRequired[GiftCardStatus]
    """
    The current gift card state.
    See [Status](#type-status) for possible values
    """

    balance_money: typing_extensions.NotRequired[MoneyParams]
    """
    The current gift card balance. This balance is always greater than or equal to zero.
    """

    gan: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The gift card account number (GAN). Buyers can use the GAN to make purchases or check 
    the gift card balance.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the gift card was created, in RFC 3339 format. 
    In the case of a digital gift card, it is the time when you create a card 
    (using the Square Point of Sale application, Seller Dashboard, or Gift Cards API).  
    In the case of a plastic gift card, it is the time when Square associates the card with the 
    seller at the time of activation.
    """

    customer_ids: typing_extensions.NotRequired[typing.Sequence[str]]
    """
    The IDs of the [customer profiles](entity:Customer) to whom this gift card is linked.
    """
