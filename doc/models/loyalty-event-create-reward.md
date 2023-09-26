
# Loyalty Event Create Reward

Provides metadata when the event `type` is `CREATE_REWARD`.

## Structure

`Loyalty Event Create Reward`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_program_id` | `str` | Required | The ID of the [loyalty program](entity:LoyaltyProgram).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `reward_id` | `str` | Optional | The Square-assigned ID of the created [loyalty reward](entity:LoyaltyReward).<br>This field is returned only if the event source is `LOYALTY_API`.<br>**Constraints**: *Maximum Length*: `36` |
| `points` | `int` | Required | The loyalty points used to create the reward. |

## Example (as JSON)

```json
{
  "loyalty_program_id": "loyalty_program_id4",
  "reward_id": "reward_id8",
  "points": 198
}
```

