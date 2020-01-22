## Order Fulfillment Shipment Details

Contains details necessary to fulfill a shipment order.

### Structure

`OrderFulfillmentShipmentDetails`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | [`Order Fulfillment Recipient`](/doc/models/order-fulfillment-recipient.md) | Optional | Contains information on the recipient of a fulfillment. |
| `carrier` | `string` | Optional | The shipping carrier being used to ship this fulfillment<br>e.g. UPS, FedEx, USPS, etc. |
| `shipping_note` | `string` | Optional | A note with additional information for the shipping carrier. |
| `shipping_type` | `string` | Optional | A description of the type of shipping product purchased from the carrier.<br>e.g. First Class, Priority, Express |
| `tracking_number` | `string` | Optional | The reference number provided by the carrier to track the shipment's progress. |
| `tracking_url` | `string` | Optional | A link to the tracking webpage on the carrier's website. |
| `placed_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the shipment was<br>requested. Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `in_progress_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when this fulfillment was<br>moved to the `RESERVED` state. Indicates that preparation of this shipment has begun.<br>Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `packaged_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when this fulfillment<br>was moved to the `PREPARED` state. Indicates that the fulfillment is packaged.<br>Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `expected_shipped_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the shipment is<br>expected to be delivered to the shipping carrier. Must be in RFC3339 timestamp<br>format, e.g., "2016-09-04T23:59:33.123Z". |
| `shipped_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when this fulfillment<br>was moved to the `COMPLETED`state. Indicates that the fulfillment has been given<br>to the shipping carrier. Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `canceled_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating the shipment was canceled.<br>Must be in RFC3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z". |
| `cancel_reason` | `string` | Optional | A description of why the shipment was canceled. |
| `failed_at` | `string` | Optional | The [timestamp](#workingwithdates) indicating when the shipment<br>failed to be completed. Must be in RFC3339 timestamp format, e.g.,<br>"2016-09-04T23:59:33.123Z". |
| `failure_reason` | `string` | Optional | A description of why the shipment failed to be completed. |

### Example (as JSON)

```json
{
  "recipient": null,
  "carrier": null,
  "shipping_note": null,
  "shipping_type": null,
  "tracking_number": null,
  "tracking_url": null,
  "placed_at": null,
  "in_progress_at": null,
  "packaged_at": null,
  "expected_shipped_at": null,
  "shipped_at": null,
  "canceled_at": null,
  "cancel_reason": null,
  "failed_at": null,
  "failure_reason": null
}
```

