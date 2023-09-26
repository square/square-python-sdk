
# V1 List Refunds Response

## Structure

`V1 List Refunds Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List V1 Refund`](../../doc/models/v1-refund.md) | Optional | - |

## Example (as JSON)

```json
{
  "items": [
    {
      "type": "FULL",
      "reason": "reason6",
      "refunded_money": {
        "amount": 214,
        "currency_code": "SRD"
      },
      "refunded_processing_fee_money": {
        "amount": 0,
        "currency_code": "BGN"
      },
      "refunded_tax_money": {
        "amount": 148,
        "currency_code": "SRD"
      }
    },
    {
      "type": "FULL",
      "reason": "reason6",
      "refunded_money": {
        "amount": 214,
        "currency_code": "SRD"
      },
      "refunded_processing_fee_money": {
        "amount": 0,
        "currency_code": "BGN"
      },
      "refunded_tax_money": {
        "amount": 148,
        "currency_code": "SRD"
      }
    },
    {
      "type": "FULL",
      "reason": "reason6",
      "refunded_money": {
        "amount": 214,
        "currency_code": "SRD"
      },
      "refunded_processing_fee_money": {
        "amount": 0,
        "currency_code": "BGN"
      },
      "refunded_tax_money": {
        "amount": 148,
        "currency_code": "SRD"
      }
    }
  ]
}
```

