## Create Refund Request

Defines the body parameters that can be included in
a request to the [CreateRefund](#endpoint-createrefund) endpoint.

Deprecated - recommend using [RefundPayment](#endpoint-refunds-refundpayment)

### Structure

`CreateRefundRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` |  | A value you specify that uniquely identifies this<br>refund among refunds you've created for the tender.<br><br>If you're unsure whether a particular refund succeeded,<br>you can reattempt it with the same idempotency key without<br>worrying about duplicating the refund.<br><br>See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information. |
| `tender_id` | `string` |  | The ID of the tender to refund.<br><br>A [`Transaction`](#type-transaction) has one or more `tenders` (i.e., methods<br>of payment) associated with it, and you refund each tender separately with<br>the Connect API. |
| `reason` | `string` | Optional | A description of the reason for the refund.<br><br>Default value: `Refund via API` |
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "idempotency_key": "86ae1696-b1e3-4328-af6d-f1e04d947ad2",
  "tender_id": "MtZRYYdDrYNQbOvV7nbuBvMF",
  "reason": "a reason",
  "amount_money": {
    "amount": 100,
    "currency": "USD"
  }
}
```

