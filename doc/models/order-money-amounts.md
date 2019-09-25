## Order Money Amounts

A collection of various money amounts.

### Structure

`OrderMoneyAmounts`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `discount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `tip_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `service_charge_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "total_money": null,
  "tax_money": null,
  "discount_money": null,
  "tip_money": null,
  "service_charge_money": null
}
```

