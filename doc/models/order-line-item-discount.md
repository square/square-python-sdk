## Order Line Item Discount

Represents a discount that applies to one or more line items in an
order.

Fixed-amount, order-scoped discounts are distributed across all non-zero line item totals.
The amount distributed to each line item is relative to that item’s contribution to the order subtotal.

### Structure

`OrderLineItemDiscount`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the discount only within this order. |
| `catalog_object_id` | `string` | Optional | The catalog object id referencing [CatalogDiscount](./models/catalog-discount.md). |
| `name` | `string` | Optional | The discount's name. |
| `type` | [`str (Order Line Item Discount Type)`](/doc/models/order-line-item-discount-type.md) | Optional | Indicates how the discount is applied to the associated line item or order. |
| `percentage` | `string` | Optional | The percentage of the discount, as a string representation of a decimal number.<br>A value of `7.25` corresponds to a percentage of 7.25%.<br><br>The percentage won't be set for an amount-based discount. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `scope` | [`str (Order Line Item Discount Scope)`](/doc/models/order-line-item-discount-scope.md) | Optional | Indicates whether this is a line item or order level discount. |

### Example (as JSON)

```json
{
  "uid": null,
  "catalog_object_id": null,
  "name": null,
  "type": null,
  "percentage": null,
  "amount_money": null,
  "applied_money": null,
  "scope": null
}
```

