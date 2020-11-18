
# Search Team Members Request

Represents a search request for a filtered list of `TeamMember` objects.

## Structure

`Search Team Members Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | [`Search Team Members Query`](/doc/models/search-team-members-query.md) | Optional | Represents the parameters in a search for `TeamMember` objects. |
| `limit` | `int` | Optional | The maximum number of `TeamMember` objects in a page (25 by default). |
| `cursor` | `string` | Optional | The opaque cursor for fetching the next page. Read about<br>[pagination](https://developer.squareup.com/docs/working-with-apis/pagination) with Square APIs for more information. |

## Example (as JSON)

```json
{
  "limit": 10,
  "query": {
    "filter": {
      "location_ids": [
        "0G5P3VGACMMQZ"
      ],
      "status": "ACTIVE"
    }
  }
}
```

