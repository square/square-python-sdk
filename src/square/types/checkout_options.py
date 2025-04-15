# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .custom_field import CustomField
from .accepted_payment_methods import AcceptedPaymentMethods
from .money import Money
from .shipping_fee import ShippingFee
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CheckoutOptions(UncheckedBaseModel):
    allow_tipping: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the payment allows tipping.
    """

    custom_fields: typing.Optional[typing.List[CustomField]] = pydantic.Field(default=None)
    """
    The custom fields requesting information from the buyer.
    """

    subscription_plan_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the subscription plan for the buyer to pay and subscribe.
    For more information, see [Subscription Plan Checkout](https://developer.squareup.com/docs/checkout-api/subscription-plan-checkout).
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The confirmation page URL to redirect the buyer to after Square processes the payment.
    """

    merchant_support_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address that buyers can use to contact the seller.
    """

    ask_for_shipping_address: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether to include the address fields in the payment form.
    """

    accepted_payment_methods: typing.Optional[AcceptedPaymentMethods] = pydantic.Field(default=None)
    """
    The methods allowed for buyers during checkout.
    """

    app_fee_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of money that the developer is taking as a fee for facilitating the payment on behalf of the seller.
    
    The amount cannot be more than 90% of the total amount of the payment.
    
    The amount must be specified in the smallest denomination of the applicable currency (for example, US dollar amounts are specified in cents). For more information, see [Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/common-data-types/working-with-monetary-amounts).
    
    The fee currency code must match the currency associated with the seller that is accepting the payment. The application must be from a developer account in the same country and using the same currency code as the seller. For more information about the application fee scenario, see [Take Payments and Collect Fees](https://developer.squareup.com/docs/payments-api/take-payments-and-collect-fees).
    
    To set this field, `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission is required. For more information, see [Permissions](https://developer.squareup.com/docs/payments-api/collect-fees/additional-considerations#permissions).
    """

    shipping_fee: typing.Optional[ShippingFee] = pydantic.Field(default=None)
    """
    The fee associated with shipping to be applied to the `Order` as a service charge.
    """

    enable_coupon: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether to include the `Add coupon` section for the buyer to provide a Square marketing coupon in the payment form.
    """

    enable_loyalty: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether to include the `REWARDS` section for the buyer to opt in to loyalty, redeem rewards in the payment form, or both.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
