
# Event Type Metadata

Contains the metadata of a webhook event type.

## Structure

`Event Type Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | `str` | Optional | The event type. |
| `api_version_introduced` | `str` | Optional | The API version at which the event type was introduced. |
| `release_status` | `str` | Optional | The release status of the event type. |

## Example (as JSON)

```json
{
  "event_type": "event_type0",
  "api_version_introduced": "api_version_introduced0",
  "release_status": "release_status4"
}
```

