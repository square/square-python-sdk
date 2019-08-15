## Search Orders Query

Contains query criteria for the search.

### Structure

`SearchOrdersQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Search Orders Filter`](/doc/models/search-orders-filter.md) | Optional | Filter options to use for a query. Multiple filters will be ANDed together. |
| `sort` | [`Search Orders Sort`](/doc/models/search-orders-sort.md) | Optional | Sorting options for a query. Returned Orders will always be sorted on a timestamp. |

### Example (as JSON)

```json
{
  "filter": null,
  "sort": null
}
```

