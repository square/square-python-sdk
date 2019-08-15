## Customer Query

Represents a query (filtering and sorting criteria) used to search
for customer profiles.

### Structure

`CustomerQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Customer Filter`](/doc/models/customer-filter.md) | Optional | Represents a set of [`CustomerQuery`](#type-customerquery) filters used<br>to limit the set of Customers returned by [`SearchCustomers`](/doc/customers.md#seachcustomers). |
| `sort` | [`Customer Sort`](/doc/models/customer-sort.md) | Optional | Indicates the field to use for sorting customer profiles. For example,<br>by total money spent with the merchant or the date of their first purchase. |

### Example (as JSON)

```json
{
  "filter": null,
  "sort": null
}
```

