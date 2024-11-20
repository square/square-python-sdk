
# Payout Fee

Represents a payout fee that can incur as part of a payout.

## Structure

`Payout Fee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `effective_at` | `str` | Optional | The timestamp of when the fee takes effect, in RFC 3339 format. |
| `type` | [`str (Payout Fee Type)`](../../doc/models/payout-fee-type.md) | Optional | Represents the type of payout fee that can incur as part of a payout. |

## Example (as JSON)

```json
{
  "amount_money": {
    "amount": 186,
    "currency": "AUD"
  },
  "effective_at": "effective_at0",
  "type": "TRANSFER_FEE"
}
```

