
# Delete Merchant Custom Attribute Response

Represents a [DeleteMerchantCustomAttribute](../../doc/api/merchant-custom-attributes.md#delete-merchant-custom-attribute) response.
Either an empty object `{}` (for a successful deletion) or `errors` is present in the response.

## Structure

`Delete Merchant Custom Attribute Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
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

