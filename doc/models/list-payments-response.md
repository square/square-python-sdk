## List Payments Response

Defines the fields that are included in the response body of
a request to the [ListPayments](#endpoint-payments-listpayments) endpoint.

### Structure

`ListPaymentsResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `payments` | [`List of Payment`](/doc/models/payment.md) | Optional | The requested list of `Payment`s. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request. If empty,<br>this is the final response.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |

### Example (as JSON)

```json
{
  "payments": [
    {
      "id": "6SRrImjQGn8FuzIsURiN677CwaB",
      "created_at": "2019-07-09T14:36:13.745Z",
      "updated_at": "2019-07-09T14:36:13.883Z",
      "amount_money": {
        "amount": 1000,
        "currency": "USD"
      },
      "total_money": {
        "amount": 1000,
        "currency": "USD"
      },
      "status": "APPROVED",
      "source_type": "CARD",
      "card_details": {
        "status": "AUTHORIZED",
        "card": {
          "card_brand": "VISA",
          "last_4": "1111",
          "exp_month": 2,
          "exp_year": 2022,
          "fingerprint": "sq-1-lHpUJIUyqOPQmH89b6GuQEljmc-mZmu4kSTaMlkLDkJI7NVjAl4Zirn2sk3OeyVKVA"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "auth_result_code": "NQbV3A"
      },
      "location_id": "XK3DBG77NJBFX",
      "order_id": "EM6qWxDd7RSy5udzjXktPw3PJa4F"
    },
    {
      "id": "MRWmTKxBDNRgwfNSZptAO76xuaB",
      "created_at": "2019-07-08T01:00:51.607Z",
      "updated_at": "2019-07-08T01:13:58.508Z",
      "amount_money": {
        "amount": 1000,
        "currency": "USD"
      },
      "total_money": {
        "amount": 1000,
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
        "auth_result_code": "vPIr0K"
      },
      "location_id": "XK3DBG77NJBFX",
      "order_id": "OVE4bJyb4B6bGFwMYEtVdfE4ge4F",
      "customer_id": "VDKXEEKPJN48QDG3BGGFAK05P8",
      "processing_fee": [
        {
          "effective_at": "2019-07-08T03:00:53.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 59,
            "currency": "USD"
          }
        }
      ]
    }
  ],
  "cursor": "Q2g4SUF4SWJUVkpYYlZSTGVFSkVUbEpuZDJaT1UxcHdkRUZQTnpaNGRXRkNFSmVJNVBpOExRPT0"
}
```

