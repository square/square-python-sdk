
# Update Merchant Settings Request

## Structure

`Update Merchant Settings Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_settings` | [`Checkout Merchant Settings`](../../doc/models/checkout-merchant-settings.md) | Required | - |

## Example (as JSON)

```json
{
  "merchant_settings": {
    "payment_methods": {
      "apple_pay": {
        "enabled": false
      },
      "google_pay": {
        "enabled": false
      },
      "cash_app": {
        "enabled": false
      },
      "afterpay_clearpay": {
        "order_eligibility_range": {
          "min": {
            "amount": 34,
            "currency": "OMR"
          },
          "max": {
            "amount": 140,
            "currency": "JPY"
          }
        },
        "item_eligibility_range": {
          "min": {
            "amount": 34,
            "currency": "OMR"
          },
          "max": {
            "amount": 140,
            "currency": "JPY"
          }
        },
        "enabled": false
      }
    },
    "updated_at": "updated_at6"
  }
}
```

