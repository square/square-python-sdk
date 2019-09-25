## Payment

Represents a payment processed by the Square API.

### Structure

`Payment`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Unique ID for the payment. |
| `created_at` | `string` | Optional | Timestamp of when the payment was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | Timestamp of when the payment was last updated, in RFC 3339 format. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `tip_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `app_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `processing_fee` | [`List of Processing Fee`](/doc/models/processing-fee.md) | Optional | Processing fees and fee adjustments assessed by Square on this payment. |
| `refunded_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `status` | `string` | Optional | Indicates whether the payment is `APPROVED`, `COMPLETED`, `CANCELED`, or `FAILED`. |
| `source_type` | `string` | Optional | The source type for this payment<br><br>Current values include:<br>`CARD` |
| `card_details` | [`Card Payment Details`](/doc/models/card-payment-details.md) | Optional | Reflects the current status of a card payment. |
| `location_id` | `string` | Optional | ID of the location associated with the payment. |
| `order_id` | `string` | Optional | ID of the order associated with this payment. |
| `reference_id` | `string` | Optional | An optional ID that associates this payment with an entity in<br>another system. |
| `customer_id` | `string` | Optional | An optional customer_id to be entered by the developer when creating a payment. |
| `employee_id` | `string` | Optional | An optional ID of the employee associated with taking this payment. |
| `refund_ids` | `List of string` | Optional | List of `refund_id`s identifying refunds for this payment. |
| `buyer_email_address` | `string` | Optional | The buyer's e-mail address |
| `billing_address` | [`Address`](/doc/models/address.md) | Optional | Represents a physical address. |
| `shipping_address` | [`Address`](/doc/models/address.md) | Optional | Represents a physical address. |
| `note` | `string` | Optional | An optional note to include when creating a payment |

### Example (as JSON)

```json
{
  "id": null,
  "created_at": null,
  "updated_at": null,
  "amount_money": null,
  "tip_money": null,
  "total_money": null,
  "app_fee_money": null,
  "processing_fee": null,
  "refunded_money": null,
  "status": null,
  "source_type": null,
  "card_details": null,
  "location_id": null,
  "order_id": null,
  "reference_id": null,
  "customer_id": null,
  "employee_id": null,
  "refund_ids": null,
  "buyer_email_address": null,
  "billing_address": null,
  "shipping_address": null,
  "note": null
}
```

