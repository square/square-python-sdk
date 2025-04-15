# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentBalanceActivityAppFeeRefundDetail(UncheckedBaseModel):
    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the payment associated with this activity.
    """

    refund_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the refund associated with this activity.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the location of the merchant associated with the payment refund activity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
