
# Catalog Query Set

The query filter to return the search result(s) by exact match of the specified `attribute_name` and any of
the `attribute_values`.

## Structure

`Catalog Query Set`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `attribute_name` | `string` | The name of the attribute to be searched. Matching of the attribute name is exact. |
| `attribute_values` | `List of string` | The desired values of the search attribute. Matching of the attribute values is exact and case insensitive.<br>A maximum of 250 values may be searched in a request. |

## Example (as JSON)

```json
{
  "attribute_name": "attribute_name4",
  "attribute_values": [
    "attribute_values2",
    "attribute_values3",
    "attribute_values4"
  ]
}
```

