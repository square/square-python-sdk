## V1 Settlement

V1Settlement

### Structure

`V1Settlement`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The settlement's unique identifier. |
| `status` | [`str (V1 Settlement Status)`]($m/V1SettlementStatus) | Optional | - |
| `total_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `initiated_at` | `string` | Optional | The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format. |
| `bank_account_id` | `string` | Optional | The Square-issued unique identifier for the bank account associated with the settlement. |
| `entries` | [`List of V1 Settlement Entry`]($m/V1SettlementEntry) | Optional | The entries included in this settlement. |

### Example (as JSON)

```json
{
  "id": null,
  "status": null,
  "total_money": null,
  "initiated_at": null,
  "bank_account_id": null,
  "entries": null
}
```

