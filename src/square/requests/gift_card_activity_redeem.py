# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from .money import MoneyParams
import typing_extensions
import typing
from ..types.gift_card_activity_redeem_status import GiftCardActivityRedeemStatus


class GiftCardActivityRedeemParams(typing_extensions.TypedDict):
    """
    Represents details about a `REDEEM` [gift card activity type](entity:GiftCardActivityType).
    """

    amount_money: MoneyParams
    """
    The amount deducted from the gift card for the redemption. This value is a positive integer.
    
    Applications that use a custom payment processing system must specify this amount in the 
    [CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) request.
    """

    payment_id: typing_extensions.NotRequired[str]
    """
    The ID of the payment that represents the gift card redemption. Square populates this field 
    if the payment was processed by Square.
    """

    reference_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A client-specified ID that associates the gift card activity with an entity in another system. 
    
    Applications that use a custom payment processing system can use this field to track information
    related to an order or payment.
    """

    status: typing_extensions.NotRequired[GiftCardActivityRedeemStatus]
    """
    The status of the gift card redemption. Gift cards redeemed from Square Point of Sale or the 
    Square Seller Dashboard use a two-state process: `PENDING` 
    to `COMPLETED` or `PENDING` to  `CANCELED`. Gift cards redeemed using the Gift Card Activities API 
    always have a `COMPLETED` status.
    See [Status](#type-status) for possible values
    """
