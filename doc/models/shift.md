
# Shift

A record of the hourly rate, start, and end times for a single work shift
for an employee. This might include a record of the start and end times for breaks
taken during the shift.

## Structure

`Shift`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The UUID for this object.<br>**Constraints**: *Maximum Length*: `255` |
| `employee_id` | `string` | Optional | The ID of the employee this shift belongs to. DEPRECATED at version 2020-08-26. Use `team_member_id` instead. |
| `location_id` | `string` | Optional | The ID of the location this shift occurred at. The location should be based on<br>where the employee clocked in. |
| `timezone` | `string` | Optional | The read-only convenience value that is calculated from the location based<br>on the `location_id`. Format: the IANA timezone database identifier for the<br>location timezone. |
| `start_at` | `string` | Required | RFC 3339; shifted to the location timezone + offset. Precision up to the<br>minute is respected; seconds are truncated.<br>**Constraints**: *Minimum Length*: `1` |
| `end_at` | `string` | Optional | RFC 3339; shifted to the timezone + offset. Precision up to the minute is<br>respected; seconds are truncated. |
| `wage` | [`Shift Wage`](/doc/models/shift-wage.md) | Optional | The hourly wage rate used to compensate an employee for this shift. |
| `breaks` | [`List of Break`](/doc/models/break.md) | Optional | A list of all the paid or unpaid breaks that were taken during this shift. |
| `status` | [`str (Shift Status)`](/doc/models/shift-status.md) | Optional | Enumerates the possible status of a `Shift`. |
| `version` | `int` | Optional | Used for resolving concurrency issues. The request fails if the version<br>provided does not match the server version at the time of the request. If not provided,<br>Square executes a blind write; potentially overwriting data from another<br>write. |
| `created_at` | `string` | Optional | A read-only timestamp in RFC 3339 format; presented in UTC. |
| `updated_at` | `string` | Optional | A read-only timestamp in RFC 3339 format; presented in UTC. |
| `team_member_id` | `string` | Optional | The ID of the team member this shift belongs to. Replaced `employee_id` at version "2020-08-26". |

## Example (as JSON)

```json
{
  "id": "id0",
  "employee_id": "employee_id0",
  "location_id": "location_id4",
  "timezone": "timezone0",
  "start_at": "start_at2",
  "end_at": "end_at0"
}
```

