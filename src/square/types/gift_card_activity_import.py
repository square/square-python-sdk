# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .money import Money
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GiftCardActivityImport(UncheckedBaseModel):
    """
    Represents details about an `IMPORT` [gift card activity type](entity:GiftCardActivityType).
    This activity type is used when Square imports a third-party gift card, in which case the
    `gan_source` of the gift card is set to `OTHER`.
    """

    amount_money: Money = pydantic.Field()
    """
    The balance amount on the imported gift card.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
