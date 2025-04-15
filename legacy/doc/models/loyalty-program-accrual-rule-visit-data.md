
# Loyalty Program Accrual Rule Visit Data

Represents additional data for rules with the `VISIT` accrual type.

## Structure

`Loyalty Program Accrual Rule Visit Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `minimum_amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `tax_mode` | [`str (Loyalty Program Accrual Rule Tax Mode)`](../../doc/models/loyalty-program-accrual-rule-tax-mode.md) | Required | Indicates how taxes should be treated when calculating the purchase amount used for loyalty points accrual.<br>This setting applies only to `SPEND` accrual rules or `VISIT` accrual rules that have a minimum spend requirement. |

## Example (as JSON)

```json
{
  "minimum_amount_money": {
    "amount": 146,
    "currency": "GHS"
  },
  "tax_mode": "BEFORE_TAX"
}
```

