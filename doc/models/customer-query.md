
# Customer Query

Represents filtering and sorting criteria for a [SearchCustomers](../../doc/api/customers.md#search-customers) request.

## Structure

`Customer Query`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Customer Filter`](../../doc/models/customer-filter.md) | Optional | Represents the filtering criteria in a [search query](../../doc/models/customer-query.md) that defines how to filter<br>customer profiles returned in [SearchCustomers](../../doc/api/customers.md#search-customers) results. |
| `sort` | [`Customer Sort`](../../doc/models/customer-sort.md) | Optional | Represents the sorting criteria in a [search query](../../doc/models/customer-query.md) that defines how to sort<br>customer profiles returned in [SearchCustomers](../../doc/api/customers.md#search-customers) results. |

## Example (as JSON)

```json
{
  "filter": null,
  "sort": null
}
```

