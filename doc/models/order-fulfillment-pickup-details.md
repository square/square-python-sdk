## Order Fulfillment Pickup Details

Contains details necessary to fulfill a pickup order.

### Structure

`OrderFulfillmentPickupDetails`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | [`Order Fulfillment Recipient`](/doc/models/order-fulfillment-recipient.md) | Optional | The recipient of a fulfillment. |
| `expires_at` | `string` | Optional | The expiry [timestamp](#workingwithdates) in RFC 3339 format, e.g.,<br>"2016-09-04T23:59:33.123Z". This timestamp indicates when the pickup fulfillment will<br>expire if it is not accepted by the merchant. Expiration time can only be set up to 7 days in<br>the future. If not set, this pickup fulfillment will be automatically accepted when placed. |
| `auto_complete_duration` | `string` | Optional | The auto completion duration in RFC3339 duration format, e.g., "P1W3D". If set, an open<br>and accepted pickup fulfillment will automatically move to the `COMPLETED` state after this<br>period of time. If not set, this pickup fulfillment will remain accepted until it is canceled<br>or completed. |
| `schedule_type` | [`str (Order Fulfillment Pickup Details Schedule Type)`](/doc/models/order-fulfillment-pickup-details-schedule-type.md) | Optional | The schedule type of the pickup fulfillment. |
| `pickup_at` | `string` | Optional | The pickup [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z".<br>For fulfillments with the schedule type `ASAP`, this is automatically set to the current time<br>plus the expected duration to prepare the fulfillment. This represents the start of the<br>pickup window. |
| `pickup_window_duration` | `string` | Optional | The pickup window duration in RFC3339 duration format, e.g., "P1W3D". This duration<br>represents the window of time for which the order should be picked up after the `pickup_at`<br>time. Can be used as an informational guideline for merchants. |
| `prep_time_duration` | `string` | Optional | The preparation time duration in RFC3339 duration format, e.g., "P1W3D". This duration<br>indicates how long it takes the merchant to prepare this fulfillment. |
| `note` | `string` | Optional | A general note about the pickup fulfillment.<br><br>Notes are useful for providing additional instructions and are displayed in Square apps. |
| `placed_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment was placed. |
| `accepted_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment was accepted by the merchant. |
| `rejected_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment was rejected. |
| `ready_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the merchant set the fulfillment as ready for pickup. |
| `expired_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment expired. |
| `picked_up_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment was picked up by the recipient. |
| `canceled_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment was canceled by the merchant or buyer. |
| `cancel_reason` | `string` | Optional | A description of why the pickup was canceled. Max length is 100 characters. |

### Example (as JSON)

```json
{
  "recipient": null,
  "expires_at": null,
  "auto_complete_duration": null,
  "schedule_type": null,
  "pickup_at": null,
  "pickup_window_duration": null,
  "prep_time_duration": null,
  "note": null,
  "placed_at": null,
  "accepted_at": null,
  "rejected_at": null,
  "ready_at": null,
  "expired_at": null,
  "picked_up_at": null,
  "canceled_at": null,
  "cancel_reason": null
}
```

