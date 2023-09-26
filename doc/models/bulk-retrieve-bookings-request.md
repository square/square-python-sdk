
# Bulk Retrieve Bookings Request

Request payload for bulk retrieval of bookings.

## Structure

`Bulk Retrieve Bookings Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_ids` | `List[str]` | Required | A non-empty list of [Booking](entity:Booking) IDs specifying bookings to retrieve. |

## Example (as JSON)

```json
{
  "booking_ids": [
    "booking_ids8",
    "booking_ids9",
    "booking_ids0"
  ]
}
```

