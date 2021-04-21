
# Subscription Event

Describes changes to subscription and billing states.

## Structure

`Subscription Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | The ID of the subscription event. |
| `subscription_event_type` | [`str (Subscription Event Subscription Event Type)`](/doc/models/subscription-event-subscription-event-type.md) | Required | The possible subscription event types. |
| `effective_date` | `string` | Required | The date, in YYYY-MM-DD format (for<br>example, 2013-01-15), when the subscription event went into effect. |
| `plan_id` | `string` | Required | The ID of the subscription plan associated with the subscription. |
| `info` | [`Subscription Event Info`](/doc/models/subscription-event-info.md) | Optional | Provides information about the subscription event. |

## Example (as JSON)

```json
{
  "id": "id0",
  "subscription_event_type": "STOP_SUBSCRIPTION",
  "effective_date": "effective_date0",
  "plan_id": "plan_id8",
  "info": {
    "detail": "detail6",
    "code": "CUSTOMER_NO_EMAIL"
  }
}
```

