
# Loyalty Program

Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for rewards.
Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.
For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

## Structure

`Loyalty Program`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-assigned ID of the loyalty program. Updates to<br>the loyalty program do not modify the identifier.<br>**Constraints**: *Maximum Length*: `36` |
| `status` | [`str (Loyalty Program Status)`](../../doc/models/loyalty-program-status.md) | Optional | Indicates whether the program is currently active. |
| `reward_tiers` | [`List of Loyalty Program Reward Tier`](../../doc/models/loyalty-program-reward-tier.md) | Required | The list of rewards for buyers, sorted by ascending points. |
| `expiration_policy` | [`Loyalty Program Expiration Policy`](../../doc/models/loyalty-program-expiration-policy.md) | Optional | Describes when the loyalty program expires. |
| `terminology` | [`Loyalty Program Terminology`](../../doc/models/loyalty-program-terminology.md) | Required | Represents the naming used for loyalty points. |
| `location_ids` | `List of string` | Optional | The [locations](../../doc/models/location.md) at which the program is active. |
| `created_at` | `string` | Optional | The timestamp when the program was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the reward was last updated, in RFC 3339 format. |
| `accrual_rules` | [`List of Loyalty Program Accrual Rule`](../../doc/models/loyalty-program-accrual-rule.md) | Required | Defines how buyers can earn loyalty points from the base loyalty program.<br>To check for associated [loyalty promotions](../../doc/models/loyalty-promotion.md) that enable<br>buyers to earn extra points, call [ListLoyaltyPromotions](../../doc/api/loyalty.md#list-loyalty-promotions). |

## Example (as JSON)

```json
{
  "status": null,
  "reward_tiers": [
    {
      "points": 249,
      "definition": null,
      "pricing_rule_reference": null
    },
    {
      "points": 248,
      "definition": null,
      "pricing_rule_reference": null
    }
  ],
  "expiration_policy": null,
  "terminology": {
    "one": "one0",
    "other": "other6"
  },
  "location_ids": null,
  "accrual_rules": [
    {
      "accrual_type": "ITEM_VARIATION",
      "points": null,
      "visit_data": null,
      "spend_data": null,
      "item_variation_data": null,
      "category_data": null
    },
    {
      "accrual_type": "SPEND",
      "points": null,
      "visit_data": null,
      "spend_data": null,
      "item_variation_data": null,
      "category_data": null
    }
  ]
}
```

