
# Fulfillment Pickup Details

Contains details necessary to fulfill a pickup order.

## Structure

`Fulfillment Pickup Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | [`Fulfillment Recipient`](../../doc/models/fulfillment-recipient.md) | Optional | Information about the fulfillment recipient. |
| `expires_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when this fulfillment expires if it is not marked in progress. The timestamp must be<br>in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z"). The expiration time can only be set<br>up to 7 days in the future. If `expires_at` is not set, any new payments attached to the order<br>are automatically completed. |
| `auto_complete_duration` | `str` | Optional | The duration of time after which an in progress pickup fulfillment is automatically moved<br>to the `COMPLETED` state. The duration must be in RFC 3339 format (for example, "P1W3D").<br><br>If not set, this pickup fulfillment remains in progress until it is canceled or completed. |
| `schedule_type` | [`str (Fulfillment Pickup Details Schedule Type)`](../../doc/models/fulfillment-pickup-details-schedule-type.md) | Optional | The schedule type of the pickup fulfillment. |
| `pickup_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>that represents the start of the pickup window. Must be in RFC 3339 timestamp format, e.g.,<br>"2016-09-04T23:59:33.123Z".<br><br>For fulfillments with the schedule type `ASAP`, this is automatically set<br>to the current time plus the expected duration to prepare the fulfillment. |
| `pickup_window_duration` | `str` | Optional | The window of time in which the order should be picked up after the `pickup_at` timestamp.<br>Must be in RFC 3339 duration format, e.g., "P1W3D". Can be used as an<br>informational guideline for merchants. |
| `prep_time_duration` | `str` | Optional | The duration of time it takes to prepare this fulfillment.<br>The duration must be in RFC 3339 format (for example, "P1W3D"). |
| `note` | `str` | Optional | A note to provide additional instructions about the pickup<br>fulfillment displayed in the Square Point of Sale application and set by the API.<br>**Constraints**: *Maximum Length*: `500` |
| `placed_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment was placed. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `accepted_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment was marked in progress. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `rejected_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment was rejected. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `ready_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `expired_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment expired. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `picked_up_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `canceled_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the fulfillment was canceled. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `cancel_reason` | `str` | Optional | A description of why the pickup was canceled. The maximum length: 100 characters.<br>**Constraints**: *Maximum Length*: `100` |
| `is_curbside_pickup` | `bool` | Optional | If set to `true`, indicates that this pickup order is for curbside pickup, not in-store pickup. |
| `curbside_pickup_details` | [`Fulfillment Pickup Details Curbside Pickup Details`](../../doc/models/fulfillment-pickup-details-curbside-pickup-details.md) | Optional | Specific details for curbside pickup. |

## Example (as JSON)

```json
{
  "recipient": {
    "customer_id": "customer_id6",
    "display_name": "display_name8",
    "email_address": "email_address4",
    "phone_number": "phone_number4",
    "address": {
      "address_line_1": "address_line_16",
      "address_line_2": "address_line_26",
      "address_line_3": "address_line_32",
      "locality": "locality6",
      "sublocality": "sublocality6"
    }
  },
  "expires_at": "expires_at0",
  "auto_complete_duration": "auto_complete_duration0",
  "schedule_type": "SCHEDULED",
  "pickup_at": "pickup_at8"
}
```

