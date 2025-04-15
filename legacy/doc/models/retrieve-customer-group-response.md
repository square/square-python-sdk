
# Retrieve Customer Group Response

Defines the fields that are included in the response body of
a request to the [RetrieveCustomerGroup](../../doc/api/customer-groups.md#retrieve-customer-group) endpoint.

Either `errors` or `group` is present in a given response (never both).

## Structure

`Retrieve Customer Group Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `group` | [`Customer Group`](../../doc/models/customer-group.md) | Optional | Represents a group of customer profiles.<br><br>Customer groups can be created, be modified, and have their membership defined using<br>the Customers API or within the Customer Directory in the Square Seller Dashboard or Point of Sale. |

## Example (as JSON)

```json
{
  "group": {
    "created_at": "2020-04-13T21:54:57.863Z",
    "id": "2TAT3CMH4Q0A9M87XJZED0WMR3",
    "name": "Loyal Customers",
    "updated_at": "2020-04-13T21:54:58Z"
  },
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

