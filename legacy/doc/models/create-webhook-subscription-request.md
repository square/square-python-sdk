
# Create Webhook Subscription Request

Creates a [Subscription](../../doc/models/webhook-subscription.md).

## Structure

`Create Webhook Subscription Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Optional | A unique string that identifies the [CreateWebhookSubscription](api-endpoint:WebhookSubscriptions-CreateWebhookSubscription) request.<br>**Constraints**: *Maximum Length*: `45` |
| `subscription` | [`Webhook Subscription`](../../doc/models/webhook-subscription.md) | Required | Represents the details of a webhook subscription, including notification URL,<br>event types, and signature key. |

## Example (as JSON)

```json
{
  "idempotency_key": "63f84c6c-2200-4c99-846c-2670a1311fbf",
  "subscription": {
    "api_version": "2021-12-15",
    "event_types": [
      "payment.created",
      "payment.updated"
    ],
    "name": "Example Webhook Subscription",
    "notification_url": "https://example-webhook-url.com",
    "id": "id4",
    "enabled": false
  }
}
```

