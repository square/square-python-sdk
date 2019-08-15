## Additional Recipient

Represents an additional recipient (other than the merchant) receiving a portion of this tender.

### Structure

`AdditionalRecipient`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` |  | The location ID for a recipient (other than the merchant) receiving a portion of this tender. |
| `description` | `string` |  | The description of the additional recipient. |
| `amount_money` | [`Money`](/doc/models/money.md) |  | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `receivable_id` | `string` | Optional | The unique ID for this [AdditionalRecipientReceivable](./models/additional-recipient-receivable.md), assigned by the server. |

### Example (as JSON)

```json
{
  "location_id": "location_id4",
  "description": "description0",
  "amount_money": {
    "amount": null,
    "currency": null
  },
  "receivable_id": null
}
```

