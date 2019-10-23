## Customer Sort

Indicates the field to use for sorting customer profiles.

### Structure

`CustomerSort`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`str (Customer Sort Field)`](/doc/models/customer-sort-field.md) | Optional | Indicates the sort criteria for a list of Customers. |
| `order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

### Example (as JSON)

```json
{
  "field": null,
  "order": null
}
```

