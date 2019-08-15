## Shift Wage

The hourly wage rate used to compensate an employee for this shift.

### Structure

`ShiftWage`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `string` | Optional | The name of the job performed during this shift. Square<br>labor-reporting UIs may group shifts together by title. |
| `hourly_rate` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "title": null,
  "hourly_rate": null
}
```

