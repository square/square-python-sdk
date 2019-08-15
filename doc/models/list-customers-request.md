## List Customers Request

Defines the query parameters that can be provided in a request to the
ListCustomers endpoint.

### Structure

`ListCustomersRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `sort_field` | [`str (Customer Sort Field)`](/doc/models/customer-sort-field.md) | Optional | Indicates the sort criteria for a list of Customers. |
| `sort_order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

### Example (as JSON)

```json
{
  "cursor": null,
  "sort_field": null,
  "sort_order": null
}
```

