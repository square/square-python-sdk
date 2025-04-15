
# Search Terminal Checkouts Request

## Structure

`Search Terminal Checkouts Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | [`Terminal Checkout Query`](../../doc/models/terminal-checkout-query.md) | Optional | - |
| `cursor` | `str` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information. |
| `limit` | `int` | Optional | Limits the number of results returned for a single request.<br>**Constraints**: `>= 1`, `<= 100` |

## Example (as JSON)

```json
{
  "limit": 2,
  "query": {
    "filter": {
      "status": "COMPLETED",
      "device_id": "device_id0",
      "created_at": {
        "start_at": "start_at4",
        "end_at": "end_at8"
      }
    },
    "sort": {
      "sort_order": "DESC"
    }
  },
  "cursor": "cursor4"
}
```

