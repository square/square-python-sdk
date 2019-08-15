## Refund

Represents a refund processed for a Square transaction.

### Structure

`Refund`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` |  | The refund's unique ID. |
| `location_id` | `string` |  | The ID of the refund's associated location. |
| `transaction_id` | `string` |  | The ID of the transaction that the refunded tender is part of. |
| `tender_id` | `string` |  | The ID of the refunded tender. |
| `created_at` | `string` | Optional | The time when the refund was created, in RFC 3339 format. |
| `reason` | `string` |  | The reason for the refund being issued. |
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `status` | [`str (Refund Status)`](/doc/models/refund-status.md) |  | Indicates a refund's current status. |
| `processing_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `additional_recipients` | [`List of Additional Recipient`](/doc/models/additional-recipient.md) | Optional | Additional recipients (other than the merchant) receiving a portion of this refund.<br>For example, fees assessed on a refund of a purchase by a third party integration. |

### Example (as JSON)

```json
{
  "id": "id0",
  "location_id": "location_id4",
  "transaction_id": "transaction_id8",
  "tender_id": "tender_id8",
  "created_at": null,
  "reason": "reason4",
  "amount_money": {
    "amount": null,
    "currency": null
  },
  "status": "PENDING",
  "processing_fee_money": null,
  "additional_recipients": null
}
```

