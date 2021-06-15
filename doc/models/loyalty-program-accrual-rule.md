
# Loyalty Program Accrual Rule

Defines an accrual rule, which is how buyers can earn points.

## Structure

`Loyalty Program Accrual Rule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accrual_type` | [`str (Loyalty Program Accrual Rule Type)`](/doc/models/loyalty-program-accrual-rule-type.md) | Required | The type of the accrual rule that defines how buyers can earn points. |
| `points` | `int` | Optional | The number of points that<br>buyers earn based on the `accrual_type`.<br>**Constraints**: `>= 1` |
| `visit_minimum_amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `spend_amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `catalog_object_id` | `string` | Optional | When the accrual rule is item-based or category-based, this field specifies the ID<br>of the [catalog object](/doc/models/catalog-object.md) that buyers can purchase to earn points.<br>If `accrual_type` is `ITEM_VARIATION`, the object is an item variation.<br>If `accrual_type` is `CATEGORY`, the object is a category. |
| `excluded_category_ids` | `List of string` | Optional | When the accrual rule is spend-based (`accrual_type` is `SPEND`), this field<br>lists the IDs of any `CATEGORY` catalog objects that are excluded from points accrual.<br><br>You can use the [BatchRetrieveCatalogObjects](/doc/api/catalog.md#batch-retrieve-catalog-objects)<br>endpoint to retrieve information about the excluded categories. |
| `excluded_item_variation_ids` | `List of string` | Optional | When the accrual rule is spend-based (`accrual_type` is `SPEND`), this field<br>lists the IDs of any `ITEM_VARIATION` catalog objects that are excluded from points accrual.<br><br>You can use the [BatchRetrieveCatalogObjects](/doc/api/catalog.md#batch-retrieve-catalog-objects)<br>endpoint to retrieve information about the excluded item variations. |

## Example (as JSON)

```json
{
  "accrual_type": "ITEM_VARIATION",
  "points": 236,
  "visit_minimum_amount_money": {
    "amount": 118,
    "currency": "BTN"
  },
  "spend_amount_money": {
    "amount": 218,
    "currency": "GNF"
  },
  "catalog_object_id": "catalog_object_id6",
  "excluded_category_ids": [
    "excluded_category_ids8",
    "excluded_category_ids9"
  ]
}
```

