# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .v1order_state import V1OrderState
from .address import Address
from .v1money import V1Money
from .v1tender import V1Tender
from .v1order_history_entry import V1OrderHistoryEntry
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1Order(UncheckedBaseModel):
    """
    V1Order
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order's unique identifier.
    """

    buyer_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the order's buyer.
    """

    recipient_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the order's buyer.
    """

    recipient_phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number to use for the order's delivery.
    """

    state: typing.Optional[V1OrderState] = pydantic.Field(default=None)
    """
    Whether the tax is an ADDITIVE tax or an INCLUSIVE tax.
    See [V1OrderState](#type-v1orderstate) for possible values
    """

    shipping_address: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The address to ship the order to.
    """

    subtotal_money: typing.Optional[V1Money] = pydantic.Field(default=None)
    """
    The amount of all items purchased in the order, before taxes and shipping.
    """

    total_shipping_money: typing.Optional[V1Money] = pydantic.Field(default=None)
    """
    The shipping cost for the order.
    """

    total_tax_money: typing.Optional[V1Money] = pydantic.Field(default=None)
    """
    The total of all taxes applied to the order.
    """

    total_price_money: typing.Optional[V1Money] = pydantic.Field(default=None)
    """
    The total cost of the order.
    """

    total_discount_money: typing.Optional[V1Money] = pydantic.Field(default=None)
    """
    The total of all discounts applied to the order.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the order was created, in ISO 8601 format.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the order was last modified, in ISO 8601 format.
    """

    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the order expires if no action is taken, in ISO 8601 format.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the payment associated with the order.
    """

    buyer_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the buyer when the order was created, if any.
    """

    completed_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the merchant when the order's state was set to COMPLETED, if any
    """

    refunded_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the merchant when the order's state was set to REFUNDED, if any.
    """

    canceled_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the merchant when the order's state was set to CANCELED, if any.
    """

    tender: typing.Optional[V1Tender] = pydantic.Field(default=None)
    """
    The tender used to pay for the order.
    """

    order_history: typing.Optional[typing.List[V1OrderHistoryEntry]] = pydantic.Field(default=None)
    """
    The history of actions associated with the order.
    """

    promo_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The promo code provided by the buyer, if any.
    """

    btc_receive_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    For Bitcoin transactions, the address that the buyer sent Bitcoin to.
    """

    btc_price_satoshi: typing.Optional[float] = pydantic.Field(default=None)
    """
    For Bitcoin transactions, the price of the buyer's order in satoshi (100 million satoshi equals 1 BTC).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
