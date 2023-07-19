
# Loyalty Program Reward Tier

Represents a reward tier in a loyalty program. A reward tier defines how buyers can redeem points for a reward, such as the number of points required and the value and scope of the discount. A loyalty program can offer multiple reward tiers.

## Structure

`Loyalty Program Reward Tier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-assigned ID of the reward tier.<br>**Constraints**: *Maximum Length*: `36` |
| `points` | `int` | Required | The points exchanged for the reward tier.<br>**Constraints**: `>= 1` |
| `name` | `string` | Optional | The name of the reward tier. |
| `definition` | [`Loyalty Program Reward Definition`](../../doc/models/loyalty-program-reward-definition.md) | Optional | Provides details about the reward tier discount. DEPRECATED at version 2020-12-16. Discount details<br>are now defined using a catalog pricing rule and other catalog objects. For more information, see<br>[Getting discount details for a reward tier](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards#get-discount-details). |
| `created_at` | `string` | Optional | The timestamp when the reward tier was created, in RFC 3339 format. |
| `pricing_rule_reference` | [`Catalog Object Reference`](../../doc/models/catalog-object-reference.md) | Required | A reference to a Catalog object at a specific version. In general this is<br>used as an entry point into a graph of catalog objects, where the objects exist<br>at a specific version. |

## Example (as JSON)

```json
{
  "id": "id0",
  "points": 236,
  "name": "name0",
  "definition": {
    "scope": "ORDER",
    "discount_type": "FIXED_AMOUNT",
    "percentage_discount": "percentage_discount2",
    "catalog_object_ids": [
      "catalog_object_ids6"
    ],
    "fixed_discount_money": {
      "amount": 132,
      "currency": "CUC"
    },
    "max_discount_money": {
      "amount": 176,
      "currency": "CUC"
    }
  },
  "created_at": "created_at2",
  "pricing_rule_reference": {
    "object_id": "object_id0",
    "catalog_version": 218
  }
}
```

