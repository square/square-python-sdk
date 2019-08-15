## Money

Represents an amount of money.

__Important:__ Unlike version 1 of the Connect API, __all monetary amounts
returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative
if they represent money being paid _by_ a merchant, instead of money being
paid _to_ a merchant.)

### Structure

`Money`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `long|int` | Optional | The amount of money, in the smallest denomination of the<br>currency indicated by `currency`. For example, when `currency` is `USD`,<br>`amount` is in cents. |
| `currency` | [`str (Currency)`](/doc/models/currency.md) | Optional | Indicates the associated currency for an amount of money. Values correspond<br>to [ISO 4217](https://wikipedia.org/wiki/ISO_4217). |

### Example (as JSON)

```json
{
  "amount": null,
  "currency": null
}
```

