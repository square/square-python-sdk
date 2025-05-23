# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .checkout_merchant_settings_payment_methods import CheckoutMerchantSettingsPaymentMethods
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CheckoutMerchantSettings(UncheckedBaseModel):
    payment_methods: typing.Optional[CheckoutMerchantSettingsPaymentMethods] = pydantic.Field(default=None)
    """
    The set of payment methods accepted for the merchant's account.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the settings were last updated, in RFC 3339 format.
    Examples for January 25th, 2020 6:25:34pm Pacific Standard Time:
    UTC: 2020-01-26T02:25:34Z
    Pacific Standard Time with UTC offset: 2020-01-25T18:25:34-08:00
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
