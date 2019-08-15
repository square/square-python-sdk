## Charge Request Additional Recipient

Represents an additional recipient (other than the merchant) entitled to a portion of the tender.
Support is currently limited to USD, CAD and GBP currencies

### Structure

`ChargeRequestAdditionalRecipient`

### Fields

| Name | Type | Description |
|  --- | --- | --- |
| `location_id` | `string` | The location ID for a recipient (other than the merchant) receiving a portion of the tender. |
| `description` | `string` | The description of the additional recipient. |
| `amount_money` | [`Money`](/doc/models/money.md) | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "location_id": "location_id4",
  "description": "description0",
  "amount_money": {
    "amount": null,
    "currency": null
  }
}
```

