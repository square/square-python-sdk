
# Catalog Query Set

The query filter to return the search result(s) by exact match of the specified `attribute_name` and any of
the `attribute_values`.

## Structure

`Catalog Query Set`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attribute_name` | `str` | Required | The name of the attribute to be searched. Matching of the attribute name is exact.<br>**Constraints**: *Minimum Length*: `1` |
| `attribute_values` | `List[str]` | Required | The desired values of the search attribute. Matching of the attribute values is exact and case insensitive.<br>A maximum of 250 values may be searched in a request. |

## Example (as JSON)

```json
{
  "attribute_name": "attribute_name0",
  "attribute_values": [
    "attribute_values8"
  ]
}
```

