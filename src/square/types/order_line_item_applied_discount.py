# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderLineItemAppliedDiscount(UncheckedBaseModel):
    """
    Represents an applied portion of a discount to a line item in an order.

    Order scoped discounts have automatically applied discounts present for each line item.
    Line-item scoped discounts must have applied discounts added manually for any applicable line
    items. The corresponding applied money is automatically computed based on participating
    line items.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the applied discount only within this order.
    """

    discount_uid: str = pydantic.Field()
    """
    The `uid` of the discount that the applied discount represents. It must
    reference a discount present in the `order.discounts` field.
    
    This field is immutable. To change which discounts apply to a line item,
    you must delete the discount and re-add it as a new `OrderLineItemAppliedDiscount`.
    """

    applied_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of money applied by the discount to the line item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
