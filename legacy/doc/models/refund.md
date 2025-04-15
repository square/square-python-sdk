
# Refund

Represents a refund processed for a Square transaction.

## Structure

`Refund`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The refund's unique ID.<br>**Constraints**: *Maximum Length*: `255` |
| `location_id` | `str` | Required | The ID of the refund's associated location.<br>**Constraints**: *Maximum Length*: `50` |
| `transaction_id` | `str` | Optional | The ID of the transaction that the refunded tender is part of.<br>**Constraints**: *Maximum Length*: `192` |
| `tender_id` | `str` | Optional | The ID of the refunded tender.<br>**Constraints**: *Maximum Length*: `192` |
| `created_at` | `str` | Optional | The timestamp for when the refund was created, in RFC 3339 format.<br>**Constraints**: *Maximum Length*: `32` |
| `reason` | `str` | Required | The reason for the refund being issued.<br>**Constraints**: *Maximum Length*: `192` |
| `amount_money` | [`Money`](../../doc/models/money.md) | Required | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `status` | [`str (Refund Status)`](../../doc/models/refund-status.md) | Required | Indicates a refund's current status. |
| `processing_fee_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `additional_recipients` | [`List Additional Recipient`](../../doc/models/additional-recipient.md) | Optional | Additional recipients (other than the merchant) receiving a portion of this refund.<br>For example, fees assessed on a refund of a purchase by a third party integration. |

## Example (as JSON)

```json
{
  "id": "id6",
  "location_id": "location_id0",
  "transaction_id": "transaction_id4",
  "tender_id": "tender_id4",
  "created_at": "created_at6",
  "reason": "reason8",
  "amount_money": {
    "amount": 186,
    "currency": "AUD"
  },
  "status": "PENDING",
  "processing_fee_money": {
    "amount": 112,
    "currency": "DJF"
  },
  "additional_recipients": [
    {
      "location_id": "location_id0",
      "description": "description6",
      "amount_money": {
        "amount": 186,
        "currency": "AUD"
      },
      "receivable_id": "receivable_id6"
    },
    {
      "location_id": "location_id0",
      "description": "description6",
      "amount_money": {
        "amount": 186,
        "currency": "AUD"
      },
      "receivable_id": "receivable_id6"
    },
    {
      "location_id": "location_id0",
      "description": "description6",
      "amount_money": {
        "amount": 186,
        "currency": "AUD"
      },
      "receivable_id": "receivable_id6"
    }
  ]
}
```

