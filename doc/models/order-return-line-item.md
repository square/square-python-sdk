
# Order Return Line Item

The line item being returned in an order.

## Structure

`Order Return Line Item`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | A unique ID for this return line-item entry.<br>**Constraints**: *Maximum Length*: `60` |
| `source_line_item_uid` | `string` | Optional | The `uid` of the line item in the original sale order.<br>**Constraints**: *Maximum Length*: `60` |
| `name` | `string` | Optional | The name of the line item.<br>**Constraints**: *Maximum Length*: `512` |
| `quantity` | `string` | Required | The quantity returned, formatted as a decimal number.<br>For example, `"3"`.<br><br>Line items with a `quantity_unit` can have non-integer quantities.<br>For example, `"1.70000"`.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `12` |
| `quantity_unit` | [`Order Quantity Unit`](../../doc/models/order-quantity-unit.md) | Optional | Contains the measurement unit for a quantity and a precision that<br>specifies the number of digits after the decimal point for decimal quantities. |
| `note` | `string` | Optional | The note of the return line item.<br>**Constraints**: *Maximum Length*: `2000` |
| `catalog_object_id` | `string` | Optional | The [CatalogItemVariation](../../doc/models/catalog-item-variation.md) ID applied to this return line item.<br>**Constraints**: *Maximum Length*: `192` |
| `catalog_version` | `long\|int` | Optional | The version of the catalog object that this line item references. |
| `variation_name` | `string` | Optional | The name of the variation applied to this return line item.<br>**Constraints**: *Maximum Length*: `400` |
| `item_type` | [`str (Order Line Item Item Type)`](../../doc/models/order-line-item-item-type.md) | Optional | Represents the line item type. |
| `return_modifiers` | [`List of Order Return Line Item Modifier`](../../doc/models/order-return-line-item-modifier.md) | Optional | The [CatalogModifier](../../doc/models/catalog-modifier.md)s applied to this line item. |
| `applied_taxes` | [`List of Order Line Item Applied Tax`](../../doc/models/order-line-item-applied-tax.md) | Optional | The list of references to `OrderReturnTax` entities applied to the return line item. Each<br>`OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level<br>`OrderReturnTax` applied to the return line item. On reads, the applied amount<br>is populated. |
| `applied_discounts` | [`List of Order Line Item Applied Discount`](../../doc/models/order-line-item-applied-discount.md) | Optional | The list of references to `OrderReturnDiscount` entities applied to the return line item. Each<br>`OrderLineItemAppliedDiscount` has a `discount_uid` that references the `uid` of a top-level<br>`OrderReturnDiscount` applied to the return line item. On reads, the applied amount<br>is populated. |
| `base_price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `variation_total_price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `gross_return_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_tax_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_discount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

## Example (as JSON)

```json
{
  "uid": null,
  "source_line_item_uid": null,
  "name": null,
  "quantity": "quantity6",
  "quantity_unit": null,
  "note": null,
  "catalog_object_id": null,
  "catalog_version": null,
  "variation_name": null,
  "item_type": null,
  "return_modifiers": null,
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

