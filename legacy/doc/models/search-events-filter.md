
# Search Events Filter

Criteria to filter events by.

## Structure

`Search Events Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_types` | `List[str]` | Optional | Filter events by event types. |
| `merchant_ids` | `List[str]` | Optional | Filter events by merchant. |
| `location_ids` | `List[str]` | Optional | Filter events by location. |
| `created_at` | [`Time Range`](../../doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC 3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevant endpoint-specific documentation to determine<br>how time ranges are handled. |

## Example (as JSON)

```json
{
  "event_types": [
    "event_types6",
    "event_types7",
    "event_types8"
  ],
  "merchant_ids": [
    "merchant_ids5",
    "merchant_ids6",
    "merchant_ids7"
  ],
  "location_ids": [
    "location_ids8",
    "location_ids9"
  ],
  "created_at": {
    "start_at": "start_at4",
    "end_at": "end_at8"
  }
}
```

