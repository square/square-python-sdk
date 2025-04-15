# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .gift_card_activity_block_reason import GiftCardActivityBlockReason
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GiftCardActivityBlock(UncheckedBaseModel):
    """
    Represents details about a `BLOCK` [gift card activity type](entity:GiftCardActivityType).
    """

    reason: GiftCardActivityBlockReason = pydantic.Field(default="CHARGEBACK_BLOCK")
    """
    The reason the gift card was blocked.
    See [Reason](#type-reason) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
