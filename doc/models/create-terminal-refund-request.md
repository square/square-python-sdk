
# Create Terminal Refund Request

## Structure

`Create Terminal Refund Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` |  | A unique string that identifies this `CreateRefund` request. Keys can be any valid string but<br>must be unique for every `CreateRefund` request.<br><br>See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information. |
| `refund` | [`Terminal Refund`](/doc/models/terminal-refund.md) | Optional | - |

## Example (as JSON)

```json
{
  "idempotency_key": "idempotency_key6",
  "refund": {
    "id": "id8",
    "refund_id": "refund_id2",
    "payment_id": "payment_id8",
    "order_id": "order_id2",
    "amount_money": {
      "amount": 120,
      "currency": "AUD"
    },
    "reason": "reason4",
    "device_id": "device_id4"
  }
}
```

