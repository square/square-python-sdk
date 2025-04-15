
# Swap Plan Request

Defines input parameters in a call to the
[SwapPlan](../../doc/api/subscriptions.md#swap-plan) endpoint.

## Structure

`Swap Plan Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_plan_variation_id` | `str` | Optional | The ID of the new subscription plan variation.<br><br>This field is required. |
| `phases` | [`List Phase Input`](../../doc/models/phase-input.md) | Optional | A list of PhaseInputs, to pass phase-specific information used in the swap. |

## Example (as JSON)

```json
{
  "new_plan_variation_id": "FQ7CDXXWSLUJRPM3GFJSJGZ7",
  "phases": [
    {
      "order_template_id": "uhhnjH9osVv3shUADwaC0b3hNxQZY",
      "ordinal": 0
    }
  ]
}
```

