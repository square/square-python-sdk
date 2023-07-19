
# Create Gift Card Response

A response that contains a `GiftCard`. The response might contain a set of `Error` objects if the request
resulted in errors.

## Structure

`Create Gift Card Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `gift_card` | [`Gift Card`](../../doc/models/gift-card.md) | Optional | Represents a Square gift card. |

## Example (as JSON)

```json
{
  "gift_card": {
    "balance_money": {
      "amount": 0,
      "currency": "USD"
    },
    "created_at": "2021-05-20T22:26:54.000Z",
    "gan": "7783320006753271",
    "gan_source": "SQUARE",
    "id": "gftc:6cbacbb64cf54e2ca9f573d619038059",
    "state": "PENDING",
    "type": "DIGITAL"
  },
  "errors": [
    {
      "category": "REFUND_ERROR",
      "code": "MERCHANT_SUBSCRIPTION_NOT_FOUND",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "BAD_REQUEST",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "EXTERNAL_VENDOR_ERROR",
      "code": "MISSING_REQUIRED_PARAMETER",
      "detail": "detail3",
      "field": "field1"
    }
  ]
}
```

