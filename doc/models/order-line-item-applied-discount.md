## Order Line Item Applied Discount

Represents an applied portion of a discount to a line item in an order.

Order scoped discounts will automatically have applied discounts present for each line item.
Line item scoped discounts must have applied discounts added manually for any applicable line
items. The corresponding applied money will automatically be computed based on participating
line items.

### Structure

`OrderLineItemAppliedDiscount`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the applied discount only within this order. |
| `discount_uid` | `string` |  | The `uid` of the discount for which this applied discount represents.  Must reference<br>a discount present in the `order.discounts` field.<br><br>This field is immutable. To change which discounts apply to a line item, delete and add new<br>`OrderLineItemAppliedDiscount`s. |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "uid": null,
  "discount_uid": "discount_uid4",
  "applied_money": null
}
```

