## Additional Recipient Receivable Refund

A refund of an [AdditionalRecipientReceivable](./models/additional-recipient-receivable.md). This includes the ID of the additional recipient receivable associated to this object, as well as a reference to the [Refund](./models/refund.md) that created this receivable refund.

### Structure

`AdditionalRecipientReceivableRefund`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` |  | The receivable refund's unique ID, issued by Square payments servers. |
| `receivable_id` | `string` |  | The ID of the receivable that the refund was applied to. |
| `refund_id` | `string` |  | The ID of the refund that is associated to this receivable refund. |
| `transaction_location_id` | `string` |  | The ID of the location that created the receivable. This is the location ID on the associated transaction. |
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `created_at` | `string` | Optional | The time when the refund was created, in RFC 3339 format. |

### Example (as JSON)

```json
{
  "id": "id0",
  "receivable_id": "receivable_id0",
  "refund_id": "refund_id4",
  "transaction_location_id": "transaction_location_id6",
  "amount_money": {
    "amount": null,
    "currency": null
  },
  "created_at": null
}
```

