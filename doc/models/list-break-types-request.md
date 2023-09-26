
# List Break Types Request

A request for a filtered set of `BreakType` objects.

## Structure

`List Break Types Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | Filter the returned `BreakType` results to only those that are associated with the<br>specified location. |
| `limit` | `int` | Optional | The maximum number of `BreakType` results to return per page. The number can range between 1<br>and 200. The default is 200.<br>**Constraints**: `>= 1`, `<= 200` |
| `cursor` | `str` | Optional | A pointer to the next page of `BreakType` results to fetch. |

## Example (as JSON)

```json
{
  "location_id": "location_id6",
  "limit": 244,
  "cursor": "cursor4"
}
```

