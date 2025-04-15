
# Search Orders Sort

Sorting criteria for a `SearchOrders` request. Results can only be sorted
by a timestamp field.

## Structure

`Search Orders Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sort_field` | [`str (Search Orders Sort Field)`](../../doc/models/search-orders-sort-field.md) | Required | Specifies which timestamp to use to sort `SearchOrder` results. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "sort_field": "CREATED_AT",
  "sort_order": "DESC"
}
```

