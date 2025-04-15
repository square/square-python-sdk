# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CheckoutLocationSettingsTipping(UncheckedBaseModel):
    percentages: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Set three custom percentage amounts that buyers can select at checkout. If Smart Tip is enabled, this only applies to transactions totaling $10 or more.
    """

    smart_tipping_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enables Smart Tip Amounts. If Smart Tip Amounts is enabled, tipping works as follows:
    If a transaction is less than $10, the available tipping options include No Tip, $1, $2, or $3.
    If a transaction is $10 or more, the available tipping options include No Tip, 15%, 20%, or 25%. 
    You can set custom percentage amounts with the `percentages` field.
    """

    default_percent: typing.Optional[int] = pydantic.Field(default=None)
    """
    Set the pre-selected percentage amounts that appear at checkout. If Smart Tip is enabled, this only applies to transactions totaling $10 or more.
    """

    smart_tips: typing.Optional[typing.List[Money]] = pydantic.Field(default=None)
    """
    Show the Smart Tip Amounts for this location.
    """

    default_smart_tip: typing.Optional[Money] = pydantic.Field(default=None)
    """
    Set the pre-selected whole amount that appears at checkout when Smart Tip is enabled and the transaction amount is less than $10.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
