
# Create Loyalty Account Response

A response that includes loyalty account created.

## Structure

`Create Loyalty Account Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `loyalty_account` | [`Loyalty Account`](../../doc/models/loyalty-account.md) | Optional | Describes a loyalty account in a [loyalty program](../../doc/models/loyalty-program.md). For more information, see<br>[Create and Retrieve Loyalty Accounts](https://developer.squareup.com/docs/loyalty-api/loyalty-accounts). |

## Example (as JSON)

```json
{
  "loyalty_account": {
    "balance": 0,
    "created_at": "2020-05-08T21:44:32Z",
    "customer_id": "QPTXM8PQNX3Q726ZYHPMNP46XC",
    "id": "79b807d2-d786-46a9-933b-918028d7a8c5",
    "lifetime_points": 0,
    "mapping": {
      "created_at": "2020-05-08T21:44:32Z",
      "id": "66aaab3f-da99-49ed-8b19-b87f851c844f",
      "phone_number": "+14155551234"
    },
    "program_id": "d619f755-2d17-41f3-990d-c04ecedd64dd",
    "updated_at": "2020-05-08T21:44:32Z",
    "enrolled_at": "enrolled_at6"
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

