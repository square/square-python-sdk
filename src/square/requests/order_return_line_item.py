# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .order_quantity_unit import OrderQuantityUnitParams
from ..types.order_line_item_item_type import OrderLineItemItemType
from .order_return_line_item_modifier import OrderReturnLineItemModifierParams
from .order_line_item_applied_tax import OrderLineItemAppliedTaxParams
from .order_line_item_applied_discount import OrderLineItemAppliedDiscountParams
from .money import MoneyParams
from .order_line_item_applied_service_charge import OrderLineItemAppliedServiceChargeParams


class OrderReturnLineItemParams(typing_extensions.TypedDict):
    """
    The line item being returned in an order.
    """

    uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID for this return line-item entry.
    """

    source_line_item_uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The `uid` of the line item in the original sale order.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the line item.
    """

    quantity: str
    """
    The quantity returned, formatted as a decimal number.
    For example, `"3"`.
    
    Line items with a `quantity_unit` can have non-integer quantities.
    For example, `"1.70000"`.
    """

    quantity_unit: typing_extensions.NotRequired[OrderQuantityUnitParams]
    """
    The unit and precision that this return line item's quantity is measured in.
    """

    note: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The note of the return line item.
    """

    catalog_object_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The [CatalogItemVariation](entity:CatalogItemVariation) ID applied to this return line item.
    """

    catalog_version: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The version of the catalog object that this line item references.
    """

    variation_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the variation applied to this return line item.
    """

    item_type: typing_extensions.NotRequired[OrderLineItemItemType]
    """
    The type of line item: an itemized return, a non-itemized return (custom amount),
    or the return of an unactivated gift card sale.
    See [OrderLineItemItemType](#type-orderlineitemitemtype) for possible values
    """

    return_modifiers: typing_extensions.NotRequired[typing.Optional[typing.Sequence[OrderReturnLineItemModifierParams]]]
    """
    The [CatalogModifier](entity:CatalogModifier)s applied to this line item.
    """

    applied_taxes: typing_extensions.NotRequired[typing.Optional[typing.Sequence[OrderLineItemAppliedTaxParams]]]
    """
    The list of references to `OrderReturnTax` entities applied to the return line item. Each
    `OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level
    `OrderReturnTax` applied to the return line item. On reads, the applied amount
    is populated.
    """

    applied_discounts: typing_extensions.NotRequired[
        typing.Optional[typing.Sequence[OrderLineItemAppliedDiscountParams]]
    ]
    """
    The list of references to `OrderReturnDiscount` entities applied to the return line item. Each
    `OrderLineItemAppliedDiscount` has a `discount_uid` that references the `uid` of a top-level
    `OrderReturnDiscount` applied to the return line item. On reads, the applied amount
    is populated.
    """

    base_price_money: typing_extensions.NotRequired[MoneyParams]
    """
    The base price for a single unit of the line item.
    """

    variation_total_price_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total price of all item variations returned in this line item.
    The price is calculated as `base_price_money` multiplied by `quantity` and
    does not include modifiers.
    """

    gross_return_money: typing_extensions.NotRequired[MoneyParams]
    """
    The gross return amount of money calculated as (item base price + modifiers price) * quantity.
    """

    total_tax_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of tax money to return for the line item.
    """

    total_discount_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of discount money to return for the line item.
    """

    total_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of money to return for this line item.
    """

    applied_service_charges: typing_extensions.NotRequired[
        typing.Optional[typing.Sequence[OrderLineItemAppliedServiceChargeParams]]
    ]
    """
    The list of references to `OrderReturnServiceCharge` entities applied to the return
    line item. Each `OrderLineItemAppliedServiceCharge` has a `service_charge_uid` that
    references the `uid` of a top-level `OrderReturnServiceCharge` applied to the return line
    item. On reads, the applied amount is populated.
    """

    total_service_charge_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of apportioned service charge money to return for the line item.
    """
