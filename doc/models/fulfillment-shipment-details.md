
# Fulfillment Shipment Details

Contains the details necessary to fulfill a shipment order.

## Structure

`Fulfillment Shipment Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient` | [`Fulfillment Recipient`](../../doc/models/fulfillment-recipient.md) | Optional | Information about the fulfillment recipient. |
| `carrier` | `string` | Optional | The shipping carrier being used to ship this fulfillment (such as UPS, FedEx, or USPS).<br>**Constraints**: *Maximum Length*: `50` |
| `shipping_note` | `string` | Optional | A note with additional information for the shipping carrier.<br>**Constraints**: *Maximum Length*: `500` |
| `shipping_type` | `string` | Optional | A description of the type of shipping product purchased from the carrier<br>(such as First Class, Priority, or Express).<br>**Constraints**: *Maximum Length*: `50` |
| `tracking_number` | `string` | Optional | The reference number provided by the carrier to track the shipment's progress.<br>**Constraints**: *Maximum Length*: `100` |
| `tracking_url` | `string` | Optional | A link to the tracking webpage on the carrier's website.<br>**Constraints**: *Maximum Length*: `2000` |
| `placed_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the shipment was requested. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `in_progress_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when this fulfillment was moved to the `RESERVED` state, which  indicates that preparation<br>of this shipment has begun. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z"). |
| `packaged_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when this fulfillment was moved to the `PREPARED` state, which indicates that the<br>fulfillment is packaged. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z"). |
| `expected_shipped_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the shipment is expected to be delivered to the shipping carrier.<br>The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z"). |
| `shipped_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when this fulfillment was moved to the `COMPLETED` state, which indicates that<br>the fulfillment has been given to the shipping carrier. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `canceled_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating the shipment was canceled.<br>The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z"). |
| `cancel_reason` | `string` | Optional | A description of why the shipment was canceled.<br>**Constraints**: *Maximum Length*: `100` |
| `failed_at` | `string` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the shipment failed to be completed. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |
| `failure_reason` | `string` | Optional | A description of why the shipment failed to be completed.<br>**Constraints**: *Maximum Length*: `100` |

## Example (as JSON)

```json
{
  "recipient": {
    "customer_id": "customer_id6",
    "display_name": "display_name8",
    "email_address": "email_address4",
    "phone_number": "phone_number4",
    "address": {
      "address_line_1": "address_line_14",
      "address_line_2": "address_line_24",
      "address_line_3": "address_line_30",
      "locality": "locality4",
      "sublocality": "sublocality4",
      "sublocality_2": "sublocality_22",
      "sublocality_3": "sublocality_34",
      "administrative_district_level_1": "administrative_district_level_18",
      "administrative_district_level_2": "administrative_district_level_20",
      "administrative_district_level_3": "administrative_district_level_32",
      "postal_code": "postal_code6",
      "country": "PK",
      "first_name": "first_name4",
      "last_name": "last_name2"
    }
  },
  "carrier": "carrier2",
  "shipping_note": "shipping_note6",
  "shipping_type": "shipping_type6",
  "tracking_number": "tracking_number8",
  "tracking_url": "tracking_url0",
  "placed_at": "placed_at0",
  "in_progress_at": "in_progress_at4",
  "packaged_at": "packaged_at4",
  "expected_shipped_at": "expected_shipped_at4",
  "shipped_at": "shipped_at8",
  "canceled_at": "canceled_at4",
  "cancel_reason": "cancel_reason4",
  "failed_at": "failed_at4",
  "failure_reason": "failure_reason0"
}
```

