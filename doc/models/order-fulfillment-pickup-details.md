## Order Fulfillment Pickup Details

Contains details necessary to fulfill a pickup order.

### Structure

`OrderFulfillmentPickupDetails`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | [`Order Fulfillment Recipient`]($m/OrderFulfillmentRecipient) | Optional | Contains information on the recipient of a fulfillment. |
| `expires_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when this fulfillment<br>will expire if it is not accepted. Must be in RFC 3339 format<br>e.g., "2016-09-04T23:59:33.123Z". Expiration time can only be set up to 7<br>days in the future. If `expires_at` is not set, this pickup fulfillment<br>will be automatically accepted when placed. |
| `auto_complete_duration` | `string` | Optional | The duration of time after which an open and accepted pickup fulfillment<br>will automatically move to the `COMPLETED` state. Must be in RFC3339<br>duration format e.g., "P1W3D".<br><br>If not set, this pickup fulfillment will remain accepted until it is canceled or completed. |
| `schedule_type` | [`str (Order Fulfillment Pickup Details Schedule Type)`]($m/OrderFulfillmentPickupDetailsScheduleType) | Optional | The schedule type of the pickup fulfillment. |
| `pickup_at` | `string` | Optional | The [timestamp](#workingwithdates) that represents the start of the pickup window.<br>Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z".<br>For fulfillments with the schedule type `ASAP`, this is automatically set<br>to the current time plus the expected duration to prepare the fulfillment. |
| `pickup_window_duration` | `string` | Optional | The window of time in which the order should be picked up after the `pickup_at` timestamp.<br>Must be in RFC3339 duration format, e.g., "P1W3D". Can be used as an<br>informational guideline for merchants. |
| `prep_time_duration` | `string` | Optional | The duration of time it takes to prepare this fulfillment.<br>Must be in RFC3339 duration format, e.g., "P1W3D". |
| `note` | `string` | Optional | A note meant to provide additional instructions about the pickup<br>fulfillment displayed in the Square Point of Sale and set by the API. |
| `placed_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the fulfillment<br>was placed. Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `accepted_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the fulfillment<br>was accepted. In RFC3339 timestamp format,<br>e.g., "2016-09-04T23:59:33.123Z". |
| `rejected_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the fulfillment<br>was rejected. In RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `ready_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the fulfillment is<br>marked as ready for pickup. In RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `expired_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the fulfillment expired.<br>In RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `picked_up_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the fulfillment<br>was picked up by the recipient. In RFC3339 timestamp format,<br>e.g., "2016-09-04T23:59:33.123Z". |
| `canceled_at` | `string` | Optional | The [timestamp](#workingwithdates) in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z",<br>indicating when the fulfillment was canceled. |
| `cancel_reason` | `string` | Optional | A description of why the pickup was canceled. Max length: 100 characters. |

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

