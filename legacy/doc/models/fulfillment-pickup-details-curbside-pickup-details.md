
# Fulfillment Pickup Details Curbside Pickup Details

Specific details for curbside pickup.

## Structure

`Fulfillment Pickup Details Curbside Pickup Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `curbside_details` | `str` | Optional | Specific details for curbside pickup, such as parking number and vehicle model.<br>**Constraints**: *Maximum Length*: `250` |
| `buyer_arrived_at` | `str` | Optional | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)<br>indicating when the buyer arrived and is waiting for pickup. The timestamp must be in RFC 3339 format<br>(for example, "2016-09-04T23:59:33.123Z"). |

## Example (as JSON)

```json
{
  "curbside_details": "curbside_details0",
  "buyer_arrived_at": "buyer_arrived_at6"
}
```

