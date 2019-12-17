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
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `status` | [`str (Refund Status)`]($m/RefundStatus) |  | Indicates a refund's current status. |
| `processing_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `additional_recipients` | [`List of Additional Recipient`]($m/AdditionalRecipient) | Optional | Additional recipients (other than the merchant) receiving a portion of this refund.<br>For example, fees assessed on a refund of a purchase by a third party integration. |

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

