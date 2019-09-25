## Order Return Line Item

The line item being returned in an Order.

### Structure

`OrderReturnLineItem`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique identifier for this return line item entry. |
| `source_line_item_uid` | `string` | Optional | `uid` of the LineItem in the original sale Order. |
| `name` | `string` | Optional | The name of the line item. |
| `quantity` | `string` |  | The quantity returned, formatted as a decimal number.<br>For example: `"3"`.<br><br>Line items with a `quantity_unit` can have non-integer quantities.<br>For example: `"1.70000"`. |
| `quantity_unit` | [`Order Quantity Unit`](/doc/models/order-quantity-unit.md) | Optional | Contains the measurement unit for a quantity and a precision which<br>specifies the number of digits after the decimal point for decimal quantities. |
| `note` | `string` | Optional | The note of the returned line item. |
| `catalog_object_id` | `string` | Optional | The [CatalogItemVariation](#type-catalogitemvariation) id applied to this returned line item. |
| `variation_name` | `string` | Optional | The name of the variation applied to this returned line item. |
| `return_modifiers` | [`List of Order Return Line Item Modifier`](/doc/models/order-return-line-item-modifier.md) | Optional | The [CatalogModifier](#type-catalogmodifier)s applied to this line item. |
| `return_taxes` | [`List of Order Return Tax`](/doc/models/order-return-tax.md) | Optional | A list of taxes applied to this line item. On read or retrieve, this list includes both<br>item-level taxes and any return-level taxes apportioned to this item.<br><br>This field has been deprecated in favour of `applied_taxes`. |
| `return_discounts` | [`List of Order Return Discount`](/doc/models/order-return-discount.md) | Optional | A list of discounts applied to this line item. On read or retrieve, this list includes<br>both item-level discounts and any return-level discounts apportioned to this item.<br><br>This field has been deprecated in favour of `applied_discounts`. |
| `applied_taxes` | [`List of Order Line Item Applied Tax`](/doc/models/order-line-item-applied-tax.md) | Optional | The list of references to `OrderReturnTax` entities applied to the returned line item. Each<br>`OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level<br>`OrderReturnTax` applied to the returned line item. On reads, the amount applied<br>is populated. |
| `applied_discounts` | [`List of Order Line Item Applied Discount`](/doc/models/order-line-item-applied-discount.md) | Optional | The list of references to `OrderReturnDiscount` entities applied to the returned line item. Each<br>`OrderLineItemAppliedDiscount` has a `discount_uid` that references the `uid` of a top-level<br>`OrderReturnDiscount` applied to the returned line item. On reads, the amount<br>applied is populated. |
| `base_price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `variation_total_price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `gross_return_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `total_tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `total_discount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "uid": null,
  "source_line_item_uid": null,
  "name": null,
  "quantity": "quantity6",
  "quantity_unit": null,
  "note": null,
  "catalog_object_id": null,
  "variation_name": null,
  "return_modifiers": null,
  "return_taxes": null,
  "return_discounts": null,
  "applied_taxes": null,
  "applied_discounts": null,
  "base_price_money": null,
  "variation_total_price_money": null,
  "gross_return_money": null,
  "total_tax_money": null,
  "total_discount_money": null,
  "total_money": null
}
```

