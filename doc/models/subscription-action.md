
# Subscription Action

Represents an action as a pending change to a subscription.

## Structure

`Subscription Action`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of an action scoped to a subscription. |
| `type` | [`str (Subscription Action Type)`](../../doc/models/subscription-action-type.md) | Optional | Supported types of an action as a pending change to a subscription. |
| `effective_date` | `str` | Optional | The `YYYY-MM-DD`-formatted date when the action occurs on the subscription. |
| `phases` | [`List Phase`](../../doc/models/phase.md) | Optional | A list of Phases, to pass phase-specific information used in the swap. |
| `new_plan_variation_id` | `str` | Optional | The target subscription plan variation that a subscription switches to, for a `SWAP_PLAN` action. |

## Example (as JSON)

```json
{
  "id": "id2",
  "type": "CANCEL",
  "effective_date": "effective_date2",
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
  "new_plan_variation_id": "new_plan_variation_id2"
}
```

