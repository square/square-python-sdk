## Order Line Item Applied Tax

Represents an applied portion of a tax to a line item in an order.

Order scoped taxes will automatically have applied taxes present for each line item.
Line item scoped taxes must have applied taxes added manually for any applicable line items.
The corresponding applied money will automatically be computed based on participating line
items.

### Structure

`OrderLineItemAppliedTax`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the applied tax only within this order. |
| `tax_uid` | `string` |  | The `uid` of the tax for which this applied tax represents.  Must reference<br>a tax present in the `order.taxes` field.<br><br>This field is immutable. To change which taxes apply to a line item, delete and add new<br>`OrderLineItemAppliedTax`s. |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "uid": null,
  "tax_uid": "tax_uid4",
  "applied_money": null
}
```

