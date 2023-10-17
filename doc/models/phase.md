
# Phase

Represents a phase, which can override subscription phases as defined by plan_id

## Structure

`Phase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | id of subscription phase |
| `ordinal` | `long\|int` | Optional | index of phase in total subscription plan |
| `order_template_id` | `str` | Optional | id of order to be used in billing |
| `plan_phase_uid` | `str` | Optional | the uid from the plan's phase in catalog |

## Example (as JSON)

```json
{
  "uid": "uid4",
  "ordinal": 12,
  "order_template_id": "order_template_id6",
  "plan_phase_uid": "plan_phase_uid0"
}
```

