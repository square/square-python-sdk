
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
| `reward_tiers` | [`List of Loyalty Program Reward Tier`](../../doc/models/loyalty-program-reward-tier.md) | Optional | The list of rewards for buyers, sorted by ascending points. |
| `expiration_policy` | [`Loyalty Program Expiration Policy`](../../doc/models/loyalty-program-expiration-policy.md) | Optional | Describes when the loyalty program expires. |
| `terminology` | [`Loyalty Program Terminology`](../../doc/models/loyalty-program-terminology.md) | Optional | Represents the naming used for loyalty points. |
| `location_ids` | `List of string` | Optional | The [locations](entity:Location) at which the program is active. |
| `created_at` | `string` | Optional | The timestamp when the program was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the reward was last updated, in RFC 3339 format. |
| `accrual_rules` | [`List of Loyalty Program Accrual Rule`](../../doc/models/loyalty-program-accrual-rule.md) | Optional | Defines how buyers can earn loyalty points from the base loyalty program.<br>To check for associated [loyalty promotions](entity:LoyaltyPromotion) that enable<br>buyers to earn extra points, call [ListLoyaltyPromotions](api-endpoint:Loyalty-ListLoyaltyPromotions). |

## Example (as JSON)

```json
{
  "id": "id0",
  "status": "INACTIVE",
  "reward_tiers": [
    {
      "id": "id9",
      "points": 249,
      "name": "name9",
      "definition": {
        "scope": "CATEGORY",
        "discount_type": "FIXED_PERCENTAGE",
        "percentage_discount": "percentage_discount1",
        "catalog_object_ids": [
          "catalog_object_ids3",
          "catalog_object_ids4",
          "catalog_object_ids5"
        ],
        "fixed_discount_money": {
          "amount": 119,
          "currency": "SEK"
        },
        "max_discount_money": {
          "amount": 163,
          "currency": "SEK"
        }
      },
      "created_at": "created_at7",
      "pricing_rule_reference": {
        "object_id": "object_id9",
        "catalog_version": 205
      }
    },
    {
      "id": "id0",
      "points": 248,
      "name": "name0",
      "definition": {
        "scope": "ORDER",
        "discount_type": "FIXED_AMOUNT",
        "percentage_discount": "percentage_discount2",
        "catalog_object_ids": [
          "catalog_object_ids4"
        ],
        "fixed_discount_money": {
          "amount": 120,
          "currency": "SGD"
        },
        "max_discount_money": {
          "amount": 164,
          "currency": "SGD"
        }
      },
      "created_at": "created_at8",
      "pricing_rule_reference": {
        "object_id": "object_id0",
        "catalog_version": 206
      }
    }
  ],
  "expiration_policy": {
    "expiration_duration": "expiration_duration0"
  },
  "terminology": {
    "one": "one0",
    "other": "other6"
  }
}
```

