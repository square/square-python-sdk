
# List Customer Custom Attributes Request

Represents a [ListCustomerCustomAttributes](../../doc/api/customer-custom-attributes.md#list-customer-custom-attributes) request.

## Structure

`List Customer Custom Attributes Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Constraints**: `>= 1`, `<= 100` |
| `cursor` | `str` | Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `with_definitions` | `bool` | Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`. |

## Example (as JSON)

```json
{
  "limit": 224,
  "cursor": "cursor6",
  "with_definitions": false
}
```

