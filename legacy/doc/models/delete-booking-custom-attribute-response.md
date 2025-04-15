
# Delete Booking Custom Attribute Response

Represents a [DeleteBookingCustomAttribute](../../doc/api/booking-custom-attributes.md#delete-booking-custom-attribute) response.
Either an empty object `{}` (for a successful deletion) or `errors` is present in the response.

## Structure

`Delete Booking Custom Attribute Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "errors": []
}
```

