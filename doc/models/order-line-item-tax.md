## Order Line Item Tax

Represents a tax that applies to one or more line items in an order.

Fixed-amount, order-scoped taxes are distributed across all non-zero line item totals.
The amount distributed to each line item is relative to that item’s contribution to the
order subtotal.

### Structure

`OrderLineItemTax`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the tax only within this order. |
| `catalog_object_id` | `string` | Optional | The catalog object id referencing [CatalogTax](./models/catalog-tax.md). |
| `name` | `string` | Optional | The tax's name. |
| `type` | [`str (Order Line Item Tax Type)`](/doc/models/order-line-item-tax-type.md) | Optional | Indicates how the tax is applied to the associated line item or order. |
| `percentage` | `string` | Optional | The percentage of the tax, as a string representation of a decimal number.<br><br>A value of `7.25` corresponds to a percentage of 7.25%. |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `scope` | [`str (Order Line Item Tax Scope)`](/doc/models/order-line-item-tax-scope.md) | Optional | Indicates whether this is a line item or order level tax. |

### Example (as JSON)

```json
{
  "uid": null,
  "catalog_object_id": null,
  "name": null,
  "type": null,
  "percentage": null,
  "applied_money": null,
  "scope": null
}
```

