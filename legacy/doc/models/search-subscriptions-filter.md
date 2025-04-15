
# Search Subscriptions Filter

Represents a set of query expressions (filters) to narrow the scope of targeted subscriptions returned by
the [SearchSubscriptions](../../doc/api/subscriptions.md#search-subscriptions) endpoint.

## Structure

`Search Subscriptions Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_ids` | `List[str]` | Optional | A filter to select subscriptions based on the subscribing customer IDs. |
| `location_ids` | `List[str]` | Optional | A filter to select subscriptions based on the location. |
| `source_names` | `List[str]` | Optional | A filter to select subscriptions based on the source application. |

## Example (as JSON)

```json
{
  "customer_ids": [
    "customer_ids1",
    "customer_ids2"
  ],
  "location_ids": [
    "location_ids4",
    "location_ids5",
    "location_ids6"
  ],
  "source_names": [
    "source_names2",
    "source_names3",
    "source_names4"
  ]
}
```

