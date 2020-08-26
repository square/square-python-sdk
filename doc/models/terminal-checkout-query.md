## Terminal Checkout Query

### Structure

`TerminalCheckoutQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Terminal Checkout Query Filter`](/doc/models/terminal-checkout-query-filter.md) | Optional | - |
| `sort` | [`Terminal Checkout Query Sort`](/doc/models/terminal-checkout-query-sort.md) | Optional | - |

### Example (as JSON)

```json
{
  "filter": {
    "device_id": "device_id0",
    "created_at": {
      "start_at": "start_at4",
      "end_at": "end_at8"
    },
    "status": "status6"
  },
  "sort": {
    "sort_order": "sort_order8"
  }
}
```

