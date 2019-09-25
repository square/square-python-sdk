## Refund Payment Request

Refunds a payment.

### Structure

`RefundPaymentRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` |  | A unique string that identifies this RefundPayment request. Key can be any valid string but<br>must be unique for every RefundPayment request. <br>For more information, see [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency). |
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `app_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
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

