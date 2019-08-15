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
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "uid": null,
  "name": null,
  "amount_money": null
}
```

