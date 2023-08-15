
# Order Reward

Represents a reward that can be applied to an order if the necessary
reward tier criteria are met. Rewards are created through the Loyalty API.

## Structure

`Order Reward`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The identifier of the reward.<br>**Constraints**: *Minimum Length*: `1` |
| `reward_tier_id` | `str` | Required | The identifier of the reward tier corresponding to this reward.<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "id": "id0",
  "reward_tier_id": "reward_tier_id6"
}
```

