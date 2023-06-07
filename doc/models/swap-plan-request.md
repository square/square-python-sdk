
# Swap Plan Request

Defines input parameters in a call to the
[SwapPlan](../../doc/api/subscriptions.md#swap-plan) endpoint.

## Structure

`Swap Plan Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_plan_variation_id` | `string` | Optional | The ID of the new subscription plan variation.<br><br>This field is required. |
| `phases` | [`List of Phase Input`](../../doc/models/phase-input.md) | Optional | A list of PhaseInputs, to pass phase-specific information used in the swap. |

## Example (as JSON)

```json
{
  "new_plan_variation_id": "new_plan_variation_id0",
  "phases": [
    {
      "ordinal": 207,
      "order_template_id": "order_template_id7"
    },
    {
      "ordinal": 208,
      "order_template_id": "order_template_id8"
    }
  ]
}
```

