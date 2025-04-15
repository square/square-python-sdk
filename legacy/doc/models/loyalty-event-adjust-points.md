
# Loyalty Event Adjust Points

Provides metadata when the event `type` is `ADJUST_POINTS`.

## Structure

`Loyalty Event Adjust Points`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_program_id` | `str` | Optional | The Square-assigned ID of the [loyalty program](entity:LoyaltyProgram).<br>**Constraints**: *Maximum Length*: `36` |
| `points` | `int` | Required | The number of points added or removed. |
| `reason` | `str` | Optional | The reason for the adjustment of points. |

## Example (as JSON)

```json
{
  "loyalty_program_id": "loyalty_program_id4",
  "points": 98,
  "reason": "reason0"
}
```

