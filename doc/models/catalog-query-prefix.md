
# Catalog Query Prefix

The query filter to return the search result whose named attribute values are prefixed by the specified attribute value.

## Structure

`Catalog Query Prefix`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `attribute_name` | `string` | The name of the attribute to be searched.<br>**Constraints**: *Minimum Length*: `1` |
| `attribute_prefix` | `string` | The desired prefix of the search attribute value.<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "attribute_name": "attribute_name4",
  "attribute_prefix": "attribute_prefix0"
}
```

