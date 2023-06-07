
# Subscription Action

Represents an action as a pending change to a subscription.

## Structure

`Subscription Action`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The ID of an action scoped to a subscription. |
| `type` | [`str (Subscription Action Type)`](../../doc/models/subscription-action-type.md) | Optional | Supported types of an action as a pending change to a subscription. |
| `effective_date` | `string` | Optional | The `YYYY-MM-DD`-formatted date when the action occurs on the subscription. |
| `phases` | [`List of Phase`](../../doc/models/phase.md) | Optional | A list of Phases, to pass phase-specific information used in the swap. |
| `new_plan_variation_id` | `string` | Optional | The target subscription plan variation that a subscription switches to, for a `SWAP_PLAN` action. |

## Example (as JSON)

```json
{
  "id": "id0",
  "type": "RESUME",
  "effective_date": "effective_date0",
  "phases": [
    {
      "uid": "uid5",
      "ordinal": 207,
      "order_template_id": "order_template_id7",
      "plan_phase_uid": "plan_phase_uid1"
    },
    {
      "uid": "uid6",
      "ordinal": 208,
      "order_template_id": "order_template_id8",
      "plan_phase_uid": "plan_phase_uid2"
    }
  ],
  "new_plan_variation_id": "new_plan_variation_id0"
}
```

