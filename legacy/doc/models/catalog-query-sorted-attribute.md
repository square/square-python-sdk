
# Catalog Query Sorted Attribute

The query expression to specify the key to sort search results.

## Structure

`Catalog Query Sorted Attribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attribute_name` | `str` | Required | The attribute whose value is used as the sort key.<br>**Constraints**: *Minimum Length*: `1` |
| `initial_attribute_value` | `str` | Optional | The first attribute value to be returned by the query. Ascending sorts will return only<br>objects with this value or greater, while descending sorts will return only objects with this value<br>or less. If unset, start at the beginning (for ascending sorts) or end (for descending sorts). |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "attribute_name": "attribute_name2",
  "initial_attribute_value": "initial_attribute_value4",
  "sort_order": "DESC"
}
```

