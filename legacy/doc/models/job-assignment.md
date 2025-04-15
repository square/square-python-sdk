
# Job Assignment

Represents a job assigned to a [team member](../../doc/models/team-member.md), including the compensation the team
member earns for the job. Job assignments are listed in the team member's [wage setting](../../doc/models/wage-setting.md).

## Structure

`Job Assignment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `job_title` | `str` | Optional | The title of the job. |
| `pay_type` | [`str (Job Assignment Pay Type)`](../../doc/models/job-assignment-pay-type.md) | Required | Enumerates the possible pay types that a job can be assigned. |
| `hourly_rate` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `annual_rate` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `weekly_hours` | `int` | Optional | The planned hours per week for the job. Set if the job `PayType` is `SALARY`. |
| `job_id` | `str` | Optional | The ID of the [job](../../doc/models/job.md). |

## Example (as JSON)

```json
{
  "job_title": "job_title6",
  "pay_type": "NONE",
  "hourly_rate": {
    "amount": 172,
    "currency": "LAK"
  },
  "annual_rate": {
    "amount": 232,
    "currency": "NIO"
  },
  "weekly_hours": 120,
  "job_id": "job_id8"
}
```

