
# Add Group to Customer Response

Defines the fields that are included in the response body of
a request to the [AddGroupToCustomer](../../doc/api/customers.md#add-group-to-customer) endpoint.

## Structure

`Add Group to Customer Response`

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
    }
  ]
}
```

