# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..types.order_line_item_tax_type import OrderLineItemTaxType
from .money import MoneyParams
from ..types.order_line_item_tax_scope import OrderLineItemTaxScope


class OrderReturnTaxParams(typing_extensions.TypedDict):
    """
    Represents a tax being returned that applies to one or more return line items in an order.

    Fixed-amount, order-scoped taxes are distributed across all non-zero return line item totals.
    The amount distributed to each return line item is relative to that item’s contribution to the
    order subtotal.
    """

    uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID that identifies the returned tax only within this order.
    """

    source_tax_uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The tax `uid` from the order that contains the original tax charge.
    """

    catalog_object_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The catalog object ID referencing [CatalogTax](entity:CatalogTax).
    """

    catalog_version: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The version of the catalog object that this tax references.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The tax's name.
    """

    type: typing_extensions.NotRequired[OrderLineItemTaxType]
    """
    Indicates the calculation method used to apply the tax.
    See [OrderLineItemTaxType](#type-orderlineitemtaxtype) for possible values
    """

    percentage: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The percentage of the tax, as a string representation of a decimal number.
    For example, a value of `"7.25"` corresponds to a percentage of 7.25%.
    """

    applied_money: typing_extensions.NotRequired[MoneyParams]
    """
    The amount of money applied by the tax in an order.
    """

    scope: typing_extensions.NotRequired[OrderLineItemTaxScope]
    """
    Indicates the level at which the `OrderReturnTax` applies. For `ORDER` scoped
    taxes, Square generates references in `applied_taxes` on all
    `OrderReturnLineItem`s. For `LINE_ITEM` scoped taxes, the tax is only applied to
    `OrderReturnLineItem`s with references in their `applied_discounts` field.
    See [OrderLineItemTaxScope](#type-orderlineitemtaxscope) for possible values
    """
