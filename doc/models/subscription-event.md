
# Subscription Event

Describes changes to a subscription and the subscription status.

## Structure

`Subscription Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The ID of the subscription event. |
| `subscription_event_type` | [`str (Subscription Event Subscription Event Type)`](../../doc/models/subscription-event-subscription-event-type.md) | Required | Supported types of an event occurred to a subscription. |
| `effective_date` | `str` | Required | The `YYYY-MM-DD`-formatted date (for example, 2013-01-15) when the subscription event occurred. |
| `monthly_billing_anchor_date` | `int` | Optional | The day-of-the-month the billing anchor date was changed to, if applicable. |
| `info` | [`Subscription Event Info`](../../doc/models/subscription-event-info.md) | Optional | Provides information about the subscription event. |
| `phases` | [`List Phase`](../../doc/models/phase.md) | Optional | A list of Phases, to pass phase-specific information used in the swap. |
| `plan_variation_id` | `str` | Required | The ID of the subscription plan variation associated with the subscription. |

## Example (as JSON)

```json
{
  "id": "id6",
  "subscription_event_type": "RESUME_SUBSCRIPTION",
  "effective_date": "effective_date4",
  "monthly_billing_anchor_date": 54,
  "info": {
    "detail": "detail6",
    "code": "CUSTOMER_DELETED"
  },
  "phases": [
    {
      "uid": "uid0",
      "ordinal": 78,
      "order_template_id": "order_template_id2",
      "plan_phase_uid": "plan_phase_uid6"
    },
    {
      "uid": "uid0",
      "ordinal": 78,
      "order_template_id": "order_template_id2",
      "plan_phase_uid": "plan_phase_uid6"
    }
  ],
  "plan_variation_id": "plan_variation_id0"
}
```

