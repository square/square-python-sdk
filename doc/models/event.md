
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Optional | The ID of the target merchant associated with the event. |
| `location_id` | `str` | Optional | The ID of the location associated with the event. |
| `type` | `str` | Optional | The type of event this represents. |
| `event_id` | `str` | Optional | A unique ID for the event. |
| `created_at` | `str` | Optional | Timestamp of when the event was created, in RFC 3339 format. |
| `data` | [`Event Data`](../../doc/models/event-data.md) | Optional | - |

## Example (as JSON)

```json
{
  "merchant_id": "merchant_id0",
  "location_id": "location_id4",
  "type": "type0",
  "event_id": "event_id6",
  "created_at": "created_at2"
}
```

