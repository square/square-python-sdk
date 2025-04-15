
# List Order Custom Attributes Request

Represents a list request for order custom attributes.

## Structure

`List Order Custom Attributes Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `visibility_filter` | [`str (Visibility Filter)`](../../doc/models/visibility-filter.md) | Optional | Enumeration of visibility-filter values used to set the ability to view custom attributes or custom attribute definitions. |
| `cursor` | `str` | Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Constraints**: *Minimum Length*: `1` |
| `limit` | `int` | Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Constraints**: `>= 1`, `<= 100` |
| `with_definitions` | `bool` | Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom attribute,<br>information about the data type, or other definition details. The default value is `false`. |

## Example (as JSON)

```json
{
  "visibility_filter": "READ",
  "cursor": "cursor2",
  "limit": 158,
  "with_definitions": false
}
```

