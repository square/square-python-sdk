
# Shift

A record of the hourly rate, start, and end times for a single work shift
for an employee. This might include a record of the start and end times for breaks
taken during the shift.

## Structure

`Shift`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The UUID for this object.<br>**Constraints**: *Maximum Length*: `255` |
| `employee_id` | `str` | Optional | The ID of the employee this shift belongs to. DEPRECATED at version 2020-08-26. Use `team_member_id` instead. |
| `location_id` | `str` | Required | The ID of the location this shift occurred at. The location should be based on<br>where the employee clocked in.<br>**Constraints**: *Minimum Length*: `1` |
| `timezone` | `str` | Optional | The read-only convenience value that is calculated from the location based<br>on the `location_id`. Format: the IANA timezone database identifier for the<br>location timezone. |
| `start_at` | `str` | Required | RFC 3339; shifted to the location timezone + offset. Precision up to the<br>minute is respected; seconds are truncated.<br>**Constraints**: *Minimum Length*: `1` |
| `end_at` | `str` | Optional | RFC 3339; shifted to the timezone + offset. Precision up to the minute is<br>respected; seconds are truncated. |
| `wage` | [`Shift Wage`](../../doc/models/shift-wage.md) | Optional | The hourly wage rate used to compensate an employee for this shift. |
| `breaks` | [`List Break`](../../doc/models/break.md) | Optional | A list of all the paid or unpaid breaks that were taken during this shift. |
| `status` | [`str (Shift Status)`](../../doc/models/shift-status.md) | Optional | Enumerates the possible status of a `Shift`. |
| `version` | `int` | Optional | Used for resolving concurrency issues. The request fails if the version<br>provided does not match the server version at the time of the request. If not provided,<br>Square executes a blind write; potentially overwriting data from another<br>write. |
| `created_at` | `str` | Optional | A read-only timestamp in RFC 3339 format; presented in UTC. |
| `updated_at` | `str` | Optional | A read-only timestamp in RFC 3339 format; presented in UTC. |
| `team_member_id` | `str` | Optional | The ID of the team member this shift belongs to. Replaced `employee_id` at version "2020-08-26". |
| `declared_cash_tip_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

## Example (as JSON)

```json
{
  "id": "id0",
  "employee_id": "employee_id0",
  "location_id": "location_id4",
  "timezone": "timezone0",
  "start_at": "start_at2",
  "end_at": "end_at0",
  "wage": {
    "title": "title8",
    "hourly_rate": {
      "amount": 172,
      "currency": "LAK"
    },
    "job_id": "job_id0",
    "tip_eligible": false
  }
}
```

