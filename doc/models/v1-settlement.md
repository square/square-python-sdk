
# V1 Settlement

V1Settlement

## Structure

`V1 Settlement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The settlement's unique identifier. |
| `status` | [`str (V1 Settlement Status)`](../../doc/models/v1-settlement-status.md) | Optional | - |
| `total_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `initiated_at` | `str` | Optional | The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format. |
| `bank_account_id` | `str` | Optional | The Square-issued unique identifier for the bank account associated with the settlement. |
| `entries` | [`List V1 Settlement Entry`](../../doc/models/v1-settlement-entry.md) | Optional | The entries included in this settlement. |

## Example (as JSON)

```json
{
  "id": "id0",
  "status": "FAILED",
  "total_money": {
    "amount": 250,
    "currency_code": "KZT"
  },
  "initiated_at": "initiated_at2",
  "bank_account_id": "bank_account_id0"
}
```

