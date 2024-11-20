
# Team Member Wage

The hourly wage rate that a team member earns on a `Shift` for doing the job
specified by the `title` property of this object.

## Structure

`Team Member Wage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The UUID for this object. |
| `team_member_id` | `str` | Optional | The `TeamMember` that this wage is assigned to. |
| `title` | `str` | Optional | The job title that this wage relates to. |
| `hourly_rate` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `job_id` | `str` | Optional | An identifier for the job that this wage relates to. This cannot be<br>used to retrieve the job. |
| `tip_eligible` | `bool` | Optional | Whether team members are eligible for tips when working this job. |

## Example (as JSON)

```json
{
  "id": "id2",
  "team_member_id": "team_member_id2",
  "title": "title8",
  "hourly_rate": {
    "amount": 172,
    "currency": "LAK"
  },
  "job_id": "job_id0"
}
```

