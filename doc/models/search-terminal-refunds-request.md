
# Search Terminal Refunds Request

## Structure

`Search Terminal Refunds Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | [`Terminal Refund Query`](/doc/models/terminal-refund-query.md) | Optional | - |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query. |
| `limit` | `int` | Optional | Limit the number of results returned for a single request. |

## Example (as JSON)

```json
{
  "limit": 1,
  "query": {
    "filter": {
      "status": "COMPLETED"
    }
  }
}
```

