
# Update Webhook Subscription Signature Key Response

Defines the fields that are included in the response body of
a request to the [UpdateWebhookSubscriptionSignatureKey](../../doc/api/webhook-subscriptions.md#update-webhook-subscription-signature-key) endpoint.

Note: If there are errors processing the request, the [Subscription](../../doc/models/webhook-subscription.md) is not
present.

## Structure

`Update Webhook Subscription Signature Key Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `signature_key` | `str` | Optional | The new Square-generated signature key used to validate the origin of the webhook event. |

## Example (as JSON)

```json
{
  "signature_key": "1k9bIJKCeTmSQwyagtNRLg",
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

