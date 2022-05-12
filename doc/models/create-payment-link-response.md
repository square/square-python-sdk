
# Create Payment Link Response

## Structure

`Create Payment Link Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `payment_link` | [`Payment Link`](../../doc/models/payment-link.md) | Optional | - |

## Example (as JSON)

```json
{
  "payment_link": {
    "created_at": "2022-04-25T23:58:01Z",
    "id": "PKVT6XGJZXYUP3NZ",
    "order_id": "o4b7saqp4HzhNttf5AJxC0Srjd4F",
    "url": "https://square.link/u/EXAMPLE",
    "version": 1
  }
}
```

