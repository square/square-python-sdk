# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams


class OrderLineItemAppliedTaxParams(typing_extensions.TypedDict):
    """
    Represents an applied portion of a tax to a line item in an order.

    Order-scoped taxes automatically include the applied taxes in each line item.
    Line item taxes must be referenced from any applicable line items.
    The corresponding applied money is automatically computed, based on the
    set of participating line items.
    """

    uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID that identifies the applied tax only within this order.
    """

    tax_uid: str
    """
    The `uid` of the tax for which this applied tax represents. It must reference
    a tax present in the `order.taxes` field.
    
    This field is immutable. To change which taxes apply to a line item, delete and add a new
    `OrderLineItemAppliedTax`.
    """

    applied_money: typing_extensions.NotRequired[MoneyParams]
    """
    The amount of money applied by the tax to the line item.
    """
