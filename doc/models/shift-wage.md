## Shift Wage

The hourly wage rate used to compensate an employee for this shift.

### Structure

`ShiftWage`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `string` | Optional | The name of the job performed during this shift. Square<br>labor-reporting UIs may group shifts together by title. |
| `hourly_rate` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "title": null,
  "hourly_rate": null
}
```

