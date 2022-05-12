
# Search Subscriptions Filter

Represents a set of query expressions (filters) to narrow the scope of targeted subscriptions returned by
the [SearchSubscriptions](../../doc/api/subscriptions.md#search-subscriptions) endpoint.

## Structure

`Search Subscriptions Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_ids` | `List of string` | Optional | A filter to select subscriptions based on the subscribing customer IDs. |
| `location_ids` | `List of string` | Optional | A filter to select subscriptions based on the location. |
| `source_names` | `List of string` | Optional | A filter to select subscriptions based on the source application. |

## Example (as JSON)

```json
{
  "customer_ids": null,
  "location_ids": null,
  "source_names": null
}
```

