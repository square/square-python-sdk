## Complete Payment Response

Return value from a [CompletePayment](#endpoint-payments-completepayment) call.

### Structure

`CompletePaymentResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request |
| `payment` | [`Payment`](/doc/models/payment.md) | Optional | Represents a payment processed by the Square API. |

### Example (as JSON)

```json
{
  "payment": {
    "id": "EdMl5lwmBxd3ZvsvinkAT5LtvaB",
    "created_at": "2019-07-10T13:39:55.317Z",
    "updated_at": "2019-07-10T13:40:05.982Z",
    "amount_money": {
      "amount": 200,
      "currency": "USD"
    },
    "app_fee_money": {
      "amount": 10,
      "currency": "USD"
    },
    "total_money": {
      "amount": 200,
      "currency": "USD"
    },
    "status": "COMPLETED",
    "source_type": "CARD",
    "card_details": {
      "status": "CAPTURED",
      "card": {
        "card_brand": "VISA",
        "last_4": "2796",
        "exp_month": 7,
        "exp_year": 2026,
        "fingerprint": "sq-1-TpmjbNBMFdibiIjpQI5LiRgNUBC7u1689i0TgHjnlyHEWYB7tnn-K4QbW4ttvtaqXw"
      },
      "entry_method": "ON_FILE",
      "cvv_status": "CVV_ACCEPTED",
      "avs_status": "AVS_ACCEPTED",
      "auth_result_code": "MhIjEN"
    },
    "location_id": "XK3DBG77NJBFX",
    "order_id": "iJbzEHMhcwydeLbN3Apg5ZAjGi4F",
    "reference_id": "123456",
    "note": "Brief description",
    "customer_id": "VDKXEEKPJN48QDG3BGGFAK05P8"
  }
}
```

