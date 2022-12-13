
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
  "points": 236,
  "definition": null,
  "pricing_rule_reference": {
    "object_id": null,
    "catalog_version": null
  }
}
```

