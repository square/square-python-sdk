
# Invoice Sort

Identifies the sort field and sort order.

## Structure

`Invoice Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | `str` | Required, Constant | The field to use for sorting.<br>**Default**: `'INVOICE_SORT_DATE'` |
| `order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "field": "INVOICE_SORT_DATE",
  "order": "DESC"
}
```

