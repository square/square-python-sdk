# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .cash_app_details import CashAppDetails
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DigitalWalletDetails(UncheckedBaseModel):
    """
    Additional details about `WALLET` type payments. Contains only non-confidential information.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the `WALLET` payment. The status can be `AUTHORIZED`, `CAPTURED`, `VOIDED`, or
    `FAILED`.
    """

    brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    The brand used for the `WALLET` payment. The brand can be `CASH_APP`, `PAYPAY`, `ALIPAY`,
    `RAKUTEN_PAY`, `AU_PAY`, `D_BARAI`, `MERPAY`, `WECHAT_PAY` or `UNKNOWN`.
    """

    cash_app_details: typing.Optional[CashAppDetails] = pydantic.Field(default=None)
    """
    Brand-specific details for payments with the `brand` of `CASH_APP`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
