
# Workweek Config

Sets the day of the week and hour of the day that a business starts a
workweek. This is used to calculate overtime pay.

## Structure

`Workweek Config`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The UUID for this object. |
| `start_of_week` | [`str (Weekday)`](../../doc/models/weekday.md) | Required | The days of the week. |
| `start_of_day_local_time` | `str` | Required | The local time at which a business week starts. Represented as a<br>string in `HH:MM` format (`HH:MM:SS` is also accepted, but seconds are<br>truncated).<br>**Constraints**: *Minimum Length*: `1` |
| `version` | `int` | Optional | Used for resolving concurrency issues. The request fails if the version<br>provided does not match the server version at the time of the request. If not provided,<br>Square executes a blind write; potentially overwriting data from another<br>write. |
| `created_at` | `str` | Optional | A read-only timestamp in RFC 3339 format; presented in UTC. |
| `updated_at` | `str` | Optional | A read-only timestamp in RFC 3339 format; presented in UTC. |

## Example (as JSON)

```json
{
  "id": "id4",
  "start_of_week": "SUN",
  "start_of_day_local_time": "start_of_day_local_time0",
  "version": 104,
  "created_at": "created_at2",
  "updated_at": "updated_at0"
}
```

