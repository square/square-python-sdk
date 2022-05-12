
# Loyalty Reward

Represents a contract to redeem loyalty points for a [reward tier](../../doc/models/loyalty-program-reward-tier.md) discount. Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state.
For more information, see [Manage loyalty rewards](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards).

## Structure

`Loyalty Reward`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-assigned ID of the loyalty reward.<br>**Constraints**: *Maximum Length*: `36` |
| `status` | [`str (Loyalty Reward Status)`](../../doc/models/loyalty-reward-status.md) | Optional | The status of the loyalty reward. |
| `loyalty_account_id` | `string` | Required | The Square-assigned ID of the [loyalty account](../../doc/models/loyalty-account.md) to which the reward belongs.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `reward_tier_id` | `string` | Required | The Square-assigned ID of the [reward tier](../../doc/models/loyalty-program-reward-tier.md) used to create the reward.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `points` | `int` | Optional | The number of loyalty points used for the reward.<br>**Constraints**: `>= 1` |
| `order_id` | `string` | Optional | The Square-assigned ID of the [order](../../doc/models/order.md) to which the reward is attached. |
| `created_at` | `string` | Optional | The timestamp when the reward was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the reward was last updated, in RFC 3339 format. |
| `redeemed_at` | `string` | Optional | The timestamp when the reward was redeemed, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": null,
  "status": null,
  "loyalty_account_id": "loyalty_account_id0",
  "reward_tier_id": "reward_tier_id6",
  "points": null,
  "order_id": null,
  "created_at": null,
  "updated_at": null,
  "redeemed_at": null
}
```

