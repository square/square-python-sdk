
# Delete Customer Request

Defines the fields that are included in a request to the `DeleteCustomer`
endpoint.

## Structure

`Delete Customer Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `long\|int` | Optional | The current version of the customer profile.<br><br>As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile). |

## Example (as JSON)

```json
{
  "version": 222
}
```

