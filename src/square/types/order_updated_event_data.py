# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .order_updated_object import OrderUpdatedObject
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderUpdatedEventData(UncheckedBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the affected object’s type, `"order_updated"`.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the affected order.
    """

    object: typing.Optional[OrderUpdatedObject] = pydantic.Field(default=None)
    """
    An object containing information about the updated Order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
