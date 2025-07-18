# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .checkout_merchant_settings import CheckoutMerchantSettings
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MerchantSettingsUpdatedEventObject(UncheckedBaseModel):
    merchant_settings: typing.Optional[CheckoutMerchantSettings] = pydantic.Field(default=None)
    """
    The updated merchant settings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
