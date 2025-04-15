
# Catalog Query Exact

The query filter to return the search result by exact match of the specified attribute name and value.

## Structure

`Catalog Query Exact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attribute_name` | `str` | Required | The name of the attribute to be searched. Matching of the attribute name is exact.<br>**Constraints**: *Minimum Length*: `1` |
| `attribute_value` | `str` | Required | The desired value of the search attribute. Matching of the attribute value is case insensitive and can be partial.<br>For example, if a specified value of "sma", objects with the named attribute value of "Small", "small" are both matched. |

## Example (as JSON)

```json
{
  "attribute_name": "attribute_name4",
  "attribute_value": "attribute_value6"
}
```

