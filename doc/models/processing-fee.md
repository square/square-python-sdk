## Processing Fee

Represents Square processing fee.

### Structure

`ProcessingFee`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `effective_at` | `string` | Optional | Timestamp of when the fee takes effect, in RFC 3339 format. |
| `type` | `string` | Optional | The type of fee assessed or adjusted. Can be one of: `INITIAL`, `ADJUSTMENT`. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "effective_at": null,
  "type": null,
  "amount_money": null
}
```

