
# Loyalty Event Redeem Reward

Provides metadata when the event `type` is `REDEEM_REWARD`.

## Structure

`Loyalty Event Redeem Reward`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_program_id` | `str` | Required | The ID of the [loyalty program](entity:LoyaltyProgram).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `reward_id` | `str` | Optional | The ID of the redeemed [loyalty reward](entity:LoyaltyReward).<br>This field is returned only if the event source is `LOYALTY_API`.<br>**Constraints**: *Maximum Length*: `36` |
| `order_id` | `str` | Optional | The ID of the [order](entity:Order) that redeemed the reward.<br>This field is returned only if the Orders API is used to process orders. |

## Example (as JSON)

```json
{
  "loyalty_program_id": "loyalty_program_id4",
  "reward_id": "reward_id8",
  "order_id": "order_id8"
}
```

