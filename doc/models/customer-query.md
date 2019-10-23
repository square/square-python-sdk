## Customer Query

Represents a query (filtering and sorting criteria) used to search
for customer profiles.

### Structure

`CustomerQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Customer Filter`](/doc/models/customer-filter.md) | Optional | Represents a set of `CustomerQuery` filters used<br>to limit the set of Customers returned by SearchCustomers. |
| `sort` | [`Customer Sort`](/doc/models/customer-sort.md) | Optional | Indicates the field to use for sorting customer profiles. |

### Example (as JSON)

```json
{
  "filter": null,
  "sort": null
}
```

