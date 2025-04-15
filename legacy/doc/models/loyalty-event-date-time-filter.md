
# Loyalty Event Date Time Filter

Filter events by date time range.

## Structure

`Loyalty Event Date Time Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | [`Time Range`](../../doc/models/time-range.md) | Required | Represents a generic time range. The start and end values are<br>represented in RFC 3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevant endpoint-specific documentation to determine<br>how time ranges are handled. |

## Example (as JSON)

```json
{
  "created_at": {
    "start_at": "start_at4",
    "end_at": "end_at8"
  }
}
```

