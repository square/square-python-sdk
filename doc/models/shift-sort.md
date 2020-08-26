## Shift Sort

Sets the sort order of search results.

### Structure

`ShiftSort`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`str (Shift Sort Field)`](/doc/models/shift-sort-field.md) | Optional | Enumerates the `Shift` fields to sort on. |
| `order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

### Example (as JSON)

```json
{
  "field": "START_AT",
  "order": "DESC"
}
```

