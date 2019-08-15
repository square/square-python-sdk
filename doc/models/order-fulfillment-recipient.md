## Order Fulfillment Recipient

The recipient of a fulfillment.

### Structure

`OrderFulfillmentRecipient`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Optional | The Customer ID of the customer associated with the fulfillment.<br><br>If customer_id is provided, the corresponding recipient information fields<br>(`display_name`, `email_address`, and `phone_number`) are automatically populated from the relevant<br>customer profile. If the targeted profile information does not contain the necessary required<br>information, the request will result in an error. |
| `display_name` | `string` | Optional | The display name of the fulfillment recipient.<br><br>If provided, overrides the value from customer profile indicated by customer_id. |
| `email_address` | `string` | Optional | The email address of the fulfillment recipient.<br><br>If provided, overrides the value from customer profile indicated by customer_id. |
| `phone_number` | `string` | Optional | The phone number of the fulfillment recipient.<br><br>If provided, overrides the value from customer profile indicated by customer_id. |
| `address` | [`Address`](/doc/models/address.md) | Optional | Represents a physical address. |

### Example (as JSON)

```json
{
  "customer_id": null,
  "display_name": null,
  "email_address": null,
  "phone_number": null,
  "address": null
}
```

