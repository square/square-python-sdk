
# Loyalty Program Accrual Rule Spend Data

Represents additional data for rules with the `SPEND` accrual type.

## Structure

`Loyalty Program Accrual Rule Spend Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_money` | [`Money`](../../doc/models/money.md) | Required | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `excluded_category_ids` | `List[str]` | Optional | The IDs of any `CATEGORY` catalog objects that are excluded from points accrual.<br><br>You can use the [BatchRetrieveCatalogObjects](api-endpoint:Catalog-BatchRetrieveCatalogObjects)<br>endpoint to retrieve information about the excluded categories. |
| `excluded_item_variation_ids` | `List[str]` | Optional | The IDs of any `ITEM_VARIATION` catalog objects that are excluded from points accrual.<br><br>You can use the [BatchRetrieveCatalogObjects](api-endpoint:Catalog-BatchRetrieveCatalogObjects)<br>endpoint to retrieve information about the excluded item variations. |
| `tax_mode` | [`str (Loyalty Program Accrual Rule Tax Mode)`](../../doc/models/loyalty-program-accrual-rule-tax-mode.md) | Required | Indicates how taxes should be treated when calculating the purchase amount used for loyalty points accrual.<br>This setting applies only to `SPEND` accrual rules or `VISIT` accrual rules that have a minimum spend requirement. |

## Example (as JSON)

```json
{
  "amount_money": {
    "amount": 186,
    "currency": "AUD"
  },
  "excluded_category_ids": [
    "excluded_category_ids4"
  ],
  "excluded_item_variation_ids": [
    "excluded_item_variation_ids7",
    "excluded_item_variation_ids6"
  ],
  "tax_mode": "BEFORE_TAX"
}
```

