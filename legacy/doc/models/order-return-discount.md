
# Order Return Discount

Represents a discount being returned that applies to one or more return line items in an
order.

Fixed-amount, order-scoped discounts are distributed across all non-zero return line item totals.
The amount distributed to each return line item is relative to that item’s contribution to the
order subtotal.

## Structure

`Order Return Discount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID that identifies the returned discount only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `source_discount_uid` | `str` | Optional | The discount `uid` from the order that contains the original application of this discount.<br>**Constraints**: *Maximum Length*: `60` |
| `catalog_object_id` | `str` | Optional | The catalog object ID referencing [CatalogDiscount](entity:CatalogDiscount).<br>**Constraints**: *Maximum Length*: `192` |
| `catalog_version` | `long\|int` | Optional | The version of the catalog object that this discount references. |
| `name` | `str` | Optional | The discount's name.<br>**Constraints**: *Maximum Length*: `255` |
| `type` | [`str (Order Line Item Discount Type)`](../../doc/models/order-line-item-discount-type.md) | Optional | Indicates how the discount is applied to the associated line item or order. |
| `percentage` | `str` | Optional | The percentage of the tax, as a string representation of a decimal number.<br>A value of `"7.25"` corresponds to a percentage of 7.25%.<br><br>`percentage` is not set for amount-based discounts.<br>**Constraints**: *Maximum Length*: `10` |
| `amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `applied_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `scope` | [`str (Order Line Item Discount Scope)`](../../doc/models/order-line-item-discount-scope.md) | Optional | Indicates whether this is a line-item or order-level discount. |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "source_discount_uid": "source_discount_uid2",
  "catalog_object_id": "catalog_object_id4",
  "catalog_version": 188,
  "name": "name2"
}
```

