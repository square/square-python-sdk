## Processing Fee

Represents Square processing fee.

### Structure

`ProcessingFee`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `effective_at` | `string` | Optional | Timestamp of when the fee takes effect, in RFC 3339 format. |
| `type` | `string` | Optional | The type of fee assessed or adjusted. Can be one of: `INITIAL`, `ADJUSTMENT`. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "effective_at": null,
  "type": null,
  "amount_money": null
}
```

