# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .money import Money
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GiftCardActivityLoad(UncheckedBaseModel):
    """
    Represents details about a `LOAD` [gift card activity type](entity:GiftCardActivityType).
    """

    amount_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount added to the gift card. This value is a positive integer.
    
    Applications that use a custom order processing system must specify this amount in the 
    [CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) request.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [order](entity:Order) that contains the `GIFT_CARD` line item.
    
    Applications that use the Square Orders API to process orders must specify the order ID in the 
    [CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) request.
    """

    line_item_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UID of the `GIFT_CARD` line item in the order that represents the additional funds for the gift card.
    
    Applications that use the Square Orders API to process orders must specify the line item UID
    in the [CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) request.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client-specified ID that associates the gift card activity with an entity in another system. 
    
    Applications that use a custom order processing system can use this field to track information related to 
    an order or payment.
    """

    buyer_payment_instrument_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The payment instrument IDs used to process the order for the additional funds, such as a credit card ID 
    or bank account ID. 
    
    Applications that use a custom order processing system must specify payment instrument IDs in 
    the [CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) request.
    Square uses this information to perform compliance checks. 
    
    For applications that use the Square Orders API to process payments, Square has the necessary 
    instrument IDs to perform compliance checks.
    
    Each buyer payment instrument ID can contain a maximum of 255 characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
