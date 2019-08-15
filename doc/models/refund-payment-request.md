## Refund Payment Request

Refunds a payment.

### Structure

`RefundPaymentRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` |  | A unique string that identifies this RefundPayment request. Key can be any valid string but<br>must be unique for every RefundPayment request. <br>For more information, see [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency). |
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `app_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `payment_id` | `string` | Optional | Unique ID of the payment being refunded. |
| `reason` | `string` | Optional | A description of the reason for the refund. |

### Example (as JSON)

```json
{
  "idempotency_key": "a7e36d40-d24b-11e8-b568-0800200c9a66",
  "payment_id": "UNOE3kv2BZwqHlJ830RCt5YCuaB",
  "amount_money": {
    "amount": 100,
    "currency": "USD"
  }
}
```

