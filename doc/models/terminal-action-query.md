
# Terminal Action Query

## Structure

`Terminal Action Query`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Terminal Action Query Filter`](../../doc/models/terminal-action-query-filter.md) | Optional | - |
| `sort` | [`Terminal Action Query Sort`](../../doc/models/terminal-action-query-sort.md) | Optional | - |

## Example (as JSON)

```json
{
  "include": [
    "CUSTOMER"
  ],
  "limit": 2,
  "query": {
    "filter": {
      "status": "COMPLETED"
    }
  },
  "filter": {
    "device_id": "device_id0",
    "created_at": {
      "start_at": "start_at4",
      "end_at": "end_at8"
    },
    "status": "status6",
    "type": "SAVE_CARD"
  },
  "sort": {
    "sort_order": "DESC"
  }
}
```

