# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderReturnTip(UncheckedBaseModel):
    """
    A tip being returned.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the tip only within this order.
    """

    applied_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of tip being returned
    --
    """

    source_tender_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tender `uid` from the order that contains the original application of this tip.
    """

    source_tender_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tender `id` from the order that contains the original application of this tip.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
