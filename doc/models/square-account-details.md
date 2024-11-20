
# Square Account Details

Additional details about Square Account payments.

## Structure

`Square Account Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_source_token` | `str` | Optional | Unique identifier for the payment source used for this payment.<br>**Constraints**: *Maximum Length*: `255` |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information about errors encountered during the request. |

## Example (as JSON)

```json
{
  "payment_source_token": "payment_source_token8",
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ]
}
```

