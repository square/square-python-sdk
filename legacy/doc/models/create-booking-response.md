
# Create Booking Response

## Structure

`Create Booking Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking` | [`Booking`](../../doc/models/booking.md) | Optional | Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service<br>at a given location to a requesting customer in one or more appointment segments. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Errors that occurred during the request. |

## Example (as JSON)

```json
{
  "booking": {
    "appointment_segments": [
      {
        "duration_minutes": 60,
        "service_variation_id": "RU3PBTZTK7DXZDQFCJHOK2MC",
        "service_variation_version": 1599775456731,
        "team_member_id": "TMXUrsBWWcHTt79t"
      }
    ],
    "created_at": "2020-10-28T15:47:41Z",
    "customer_id": "EX2QSVGTZN4K1E5QE1CBFNVQ8M",
    "customer_note": "",
    "id": "zkras0xv0xwswx",
    "location_id": "LEQHH0YY8B42M",
    "seller_note": "",
    "start_at": "2020-11-26T13:00:00Z",
    "status": "ACCEPTED",
    "updated_at": "2020-10-28T15:47:41Z",
    "version": 0
  },
  "errors": []
}
```

