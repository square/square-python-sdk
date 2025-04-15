
# Search Events Sort

Criteria to sort events by.

## Structure

`Search Events Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`str (Search Events Sort Field)`](../../doc/models/search-events-sort-field.md) | Optional | Specifies the sort key for events returned from a search. |
| `order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "field": "DEFAULT",
  "order": "DESC"
}
```

