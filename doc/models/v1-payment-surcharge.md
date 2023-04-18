
# V1 Payment Surcharge

V1PaymentSurcharge

## Structure

`V1 Payment Surcharge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The name of the surcharge. |
| `applied_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `rate` | `string` | Optional | The amount of the surcharge as a percentage. The percentage is provided as a string representing the decimal equivalent of the percentage. For example, "0.7" corresponds to a 7% surcharge. Exactly one of rate or amount_money should be set. |
| `amount_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `type` | [`str (V1 Payment Surcharge Type)`](../../doc/models/v1-payment-surcharge-type.md) | Optional | - |
| `taxable` | `bool` | Optional | Indicates whether the surcharge is taxable. |
| `taxes` | [`List of V1 Payment Tax`](../../doc/models/v1-payment-tax.md) | Optional | The list of taxes that should be applied to the surcharge. |
| `surcharge_id` | `string` | Optional | A Square-issued unique identifier associated with the surcharge. |

## Example (as JSON)

```json
{
  "name": "name0",
  "applied_money": {
    "amount": 196,
    "currency_code": "LYD"
  },
  "rate": "rate0",
  "amount_money": {
    "amount": 186,
    "currency_code": "KRW"
  },
  "type": "CUSTOM",
  "taxable": false,
  "taxes": [
    {
      "errors": [
        {
          "category": "RATE_LIMIT_ERROR",
          "code": "MAP_KEY_LENGTH_TOO_SHORT",
          "detail": "detail6",
          "field": "field4"
        },
        {
          "category": "PAYMENT_METHOD_ERROR",
          "code": "MAP_KEY_LENGTH_TOO_LONG",
          "detail": "detail7",
          "field": "field5"
        }
      ],
      "name": "name5",
      "applied_money": {
        "amount": 109,
        "currency_code": "USN"
      },
      "rate": "rate5",
      "inclusion_type": "INCLUSIVE",
      "fee_id": "fee_id3"
    },
    {
      "errors": [
        {
          "category": "PAYMENT_METHOD_ERROR",
          "code": "MAP_KEY_LENGTH_TOO_LONG",
          "detail": "detail7",
          "field": "field5"
        },
        {
          "category": "REFUND_ERROR",
          "code": "CUSTOMER_MISSING_NAME",
          "detail": "detail8",
          "field": "field6"
        },
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "CUSTOMER_MISSING_EMAIL",
          "detail": "detail9",
          "field": "field7"
        }
      ],
      "name": "name6",
      "applied_money": {
        "amount": 108,
        "currency_code": "USD"
      },
      "rate": "rate4",
      "inclusion_type": "ADDITIVE",
      "fee_id": "fee_id4"
    }
  ],
  "surcharge_id": "surcharge_id4"
}
```

