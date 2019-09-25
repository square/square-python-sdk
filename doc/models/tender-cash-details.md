## Tender Cash Details

Represents the details of a tender with `type` `CASH`.

### Structure

`TenderCashDetails`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buyer_tendered_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `change_back_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "buyer_tendered_money": null,
  "change_back_money": null
}
```

