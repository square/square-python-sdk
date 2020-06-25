## Tender

Represents a tender (i.e., a method of payment) used in a Square transaction.

### Structure

`Tender`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The tender's unique ID. |
| `location_id` | `string` | Optional | The ID of the transaction's associated location. |
| `transaction_id` | `string` | Optional | The ID of the tender's associated transaction. |
| `created_at` | `string` | Optional | The timestamp for when the tender was created, in RFC 3339 format. |
| `note` | `string` | Optional | An optional note associated with the tender at the time of payment. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `tip_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `processing_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `customer_id` | `string` | Optional | If the tender is associated with a customer or represents a customer's card on file,<br>this is the ID of the associated customer. |
| `type` | [`str (Tender Type)`](/doc/models/tender-type.md) |  | Indicates a tender's type. |
| `card_details` | [`Tender Card Details`](/doc/models/tender-card-details.md) | Optional | Represents additional details of a tender with `type` `CARD` or `SQUARE_GIFT_CARD` |
| `cash_details` | [`Tender Cash Details`](/doc/models/tender-cash-details.md) | Optional | Represents the details of a tender with `type` `CASH`. |
| `additional_recipients` | [`List of Additional Recipient`](/doc/models/additional-recipient.md) | Optional | Additional recipients (other than the merchant) receiving a portion of this tender.<br>For example, fees assessed on the purchase by a third party integration. |
| `payment_id` | `string` | Optional | The ID of the [Payment](#type-payment) that corresponds to this tender.<br>This value is only present for payments created with the v2 Payments API. |

### Example (as JSON)

```json
{
  "id": null,
  "location_id": null,
  "transaction_id": null,
  "created_at": null,
  "note": null,
  "amount_money": null,
  "tip_money": null,
  "processing_fee_money": null,
  "customer_id": null,
  "type": "THIRD_PARTY_CARD",
  "card_details": null,
  "cash_details": null,
  "additional_recipients": null,
  "payment_id": null
}
```

