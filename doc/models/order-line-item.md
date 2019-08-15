## Order Line Item

Represents a line item in an order. Each line item describes a different
product to purchase, with its own quantity and price details.

### Structure

`OrderLineItem`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the line item only within this order. |
| `name` | `string` | Optional | The name of the line item. |
| `quantity` | `string` |  | The quantity purchased, formatted as a decimal number.<br>For example: `"3"`.<br><br>Line items with a `quantity_unit` can have non-integer quantities.<br>For example: `"1.70000"`. |
| `quantity_unit` | [`Order Quantity Unit`](/doc/models/order-quantity-unit.md) | Optional | Contains the measurement unit for a quantity and a precision which<br>specifies the number of digits after the decimal point for decimal quantities. |
| `note` | `string` | Optional | The note of the line item. |
| `catalog_object_id` | `string` | Optional | The [CatalogItemVariation](./models/catalog-item-variation.md) id applied to this line item. |
| `variation_name` | `string` | Optional | The name of the variation applied to this line item. |
| `modifiers` | [`List of Order Line Item Modifier`](/doc/models/order-line-item-modifier.md) | Optional | The [CatalogModifier](./models/catalog-modifier.md)s applied to this line item. |
| `taxes` | [`List of Order Line Item Tax`](/doc/models/order-line-item-tax.md) | Optional | A list of taxes applied to this line item. On read or retrieve, this list includes both<br>item-level taxes and any order-level taxes apportioned to this item. When creating an Order,<br>set your item-level taxes in this list.<br><br>This field has been deprecated in favour of `applied_taxes`. Usage of both this field and<br>`applied_taxes` when creating an order will result in an error. Usage of this field when<br>sending requests to the UpdateOrder endpoint will result in an error. |
| `discounts` | [`List of Order Line Item Discount`](/doc/models/order-line-item-discount.md) | Optional | A list of discounts applied to this line item. On read or retrieve, this list includes<br>both item-level discounts and any order-level discounts apportioned to this item. When<br>creating an Order, set your item-level discounts in this list.<br><br>This field has been deprecated in favour of `applied_discounts`. Usage of both this field and<br>`applied_discounts` when creating an order will result in an error. Usage of this field when<br>sending requests to the UpdateOrder endpoint will result in an error. |
| `applied_taxes` | [`List of Order Line Item Applied Tax`](/doc/models/order-line-item-applied-tax.md) | Optional | The list of references to taxes applied to this line item. Each `OrderLineItemAppliedTax`<br>has a `tax_uid` that references the `uid` of a top-level `OrderLineItemTax` that is being<br>applied to this line item. On reads, the amount applied is populated.<br><br>An `OrderLineItemAppliedTax` will be automatically created on every line item for all `ORDER`<br>scoped taxes that are added to the order. `OrderLineItemAppliedTax` records for `LINE_ITEM`<br>scoped taxes must be added in requests for the tax to apply to any line items.<br><br>To change the amount of a tax, modify the referenced top-level tax. |
| `applied_discounts` | [`List of Order Line Item Applied Discount`](/doc/models/order-line-item-applied-discount.md) | Optional | The list of references to discounts applied to this line item. Each<br>`OrderLineItemAppliedDiscount` has a `discount_uid` that references the `uid` of a top-level<br>`OrderLineItemDiscounts` that is being applied to this line item. On reads, the amount<br>applied is populated.<br><br>An `OrderLineItemAppliedDiscount` will be automatically created on every line item for all<br>`ORDER` scoped discounts that are added to the order. `OrderLineItemAppliedDiscount` records<br>for `LINE_ITEM` scoped discounts must be added in requests for the discount to apply to any<br>line items.<br><br>To change the amount of a discount, modify the referenced top-level discount. |
| `base_price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `variation_total_price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `gross_sales_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_discount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "uid": null,
  "name": null,
  "quantity": "quantity6",
  "quantity_unit": null,
  "note": null,
  "catalog_object_id": null,
  "variation_name": null,
  "modifiers": null,
  "taxes": null,
  "discounts": null,
  "applied_taxes": null,
  "applied_discounts": null,
  "base_price_money": null,
  "variation_total_price_money": null,
  "gross_sales_money": null,
  "total_tax_money": null,
  "total_discount_money": null,
  "total_money": null
}
```

