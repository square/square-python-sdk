
# Catalog Query Range

The query filter to return the search result whose named attribute values fall between the specified range.

## Structure

`Catalog Query Range`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attribute_name` | `str` | Required | The name of the attribute to be searched.<br>**Constraints**: *Minimum Length*: `1` |
| `attribute_min_value` | `long\|int` | Optional | The desired minimum value for the search attribute (inclusive). |
| `attribute_max_value` | `long\|int` | Optional | The desired maximum value for the search attribute (inclusive). |

## Example (as JSON)

```json
{
  "attribute_name": "attribute_name0",
  "attribute_min_value": 184,
  "attribute_max_value": 94
}
```

