
# Loyalty Program Reward Definition

Provides details about the reward tier discount. DEPRECATED at version 2020-12-16. Discount details
are now defined using a catalog pricing rule and other catalog objects. For more information, see
[Getting discount details for a reward tier](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards#get-discount-details).

## Structure

`Loyalty Program Reward Definition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scope` | [`str (Loyalty Program Reward Definition Scope)`](../../doc/models/loyalty-program-reward-definition-scope.md) | Required | Indicates the scope of the reward tier. DEPRECATED at version 2020-12-16. Discount details<br>are now defined using a catalog pricing rule and other catalog objects. For more information, see<br>[Getting discount details for a reward tier](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards#get-discount-details). |
| `discount_type` | [`str (Loyalty Program Reward Definition Type)`](../../doc/models/loyalty-program-reward-definition-type.md) | Required | The type of discount the reward tier offers. DEPRECATED at version 2020-12-16. Discount details<br>are now defined using a catalog pricing rule and other catalog objects. For more information, see<br>[Getting discount details for a reward tier](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards#get-discount-details). |
| `percentage_discount` | `str` | Optional | The fixed percentage of the discount. Present if `discount_type` is `FIXED_PERCENTAGE`.<br>For example, a 7.25% off discount will be represented as "7.25". DEPRECATED at version 2020-12-16. You can find this<br>information in the `discount_data.percentage` field of the `DISCOUNT` catalog object referenced by the pricing rule. |
| `catalog_object_ids` | `List[str]` | Optional | The list of catalog objects to which this reward can be applied. They are either all item-variation ids or category ids, depending on the `type` field.<br>DEPRECATED at version 2020-12-16. You can find this information in the `product_set_data.product_ids_any` field<br>of the `PRODUCT_SET` catalog object referenced by the pricing rule. |
| `fixed_discount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `max_discount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

## Example (as JSON)

```json
{
  "scope": "ORDER",
  "discount_type": "FIXED_AMOUNT",
  "percentage_discount": "percentage_discount0",
  "catalog_object_ids": [
    "catalog_object_ids8"
  ],
  "fixed_discount_money": {
    "amount": 36,
    "currency": "SLL"
  },
  "max_discount_money": {
    "amount": 84,
    "currency": "BOB"
  }
}
```

