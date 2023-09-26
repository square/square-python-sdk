
# Search Team Members Request

Represents a search request for a filtered list of `TeamMember` objects.

## Structure

`Search Team Members Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | [`Search Team Members Query`](../../doc/models/search-team-members-query.md) | Optional | Represents the parameters in a search for `TeamMember` objects. |
| `limit` | `int` | Optional | The maximum number of `TeamMember` objects in a page (100 by default).<br>**Constraints**: `>= 1`, `<= 200` |
| `cursor` | `str` | Optional | The opaque cursor for fetching the next page. For more information, see<br>[pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |

## Example (as JSON)

```json
{
  "limit": 10,
  "query": {
    "filter": {
      "location_ids": [
        "0G5P3VGACMMQZ"
      ],
      "status": "ACTIVE",
      "is_owner": false
    }
  },
  "cursor": "cursor8"
}
```

