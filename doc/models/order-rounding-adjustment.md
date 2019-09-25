## Order Rounding Adjustment

A rounding adjustment of the money being returned. Commonly used to apply Cash Rounding
when the minimum unit of account is smaller than the lowest physical denomination of currency.

### Structure

`OrderRoundingAdjustment`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the rounding adjustment only within this order. |
| `name` | `string` | Optional | The name of the rounding adjustment from the original sale Order. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "uid": null,
  "name": null,
  "amount_money": null
}
```

