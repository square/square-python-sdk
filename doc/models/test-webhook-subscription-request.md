
# Test Webhook Subscription Request

Tests a [Subscription](../../doc/models/webhook-subscription.md) by sending a test event to its notification URL.

## Structure

`Test Webhook Subscription Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | `str` | Optional | The event type that will be used to test the [Subscription](entity:WebhookSubscription). The event type must be<br>contained in the list of event types in the [Subscription](entity:WebhookSubscription). |

## Example (as JSON)

```json
{
  "event_type": "payment.created"
}
```

