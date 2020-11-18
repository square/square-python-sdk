
# List Team Member Booking Profiles Request

## Structure

`List Team Member Booking Profiles Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bookable_only` | `bool` | Optional | Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`). |
| `limit` | `int` | Optional | The maximum number of results to return. |
| `cursor` | `string` | Optional | The cursor for paginating through the results. |
| `location_id` | `string` | Optional | Indicates whether to include only team members enabled at the given location in the returned result. |

## Example (as JSON)

```json
{
  "bookable_only": false,
  "limit": 172,
  "cursor": "cursor6",
  "location_id": "location_id4"
}
```

