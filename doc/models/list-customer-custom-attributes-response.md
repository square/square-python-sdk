
# List Customer Custom Attributes Response

Represents a [ListCustomerCustomAttributes](../../doc/api/customer-custom-attributes.md#list-customer-custom-attributes) response.
Either `custom_attributes`, an empty object, or `errors` is present in the response. If additional
results are available, the `cursor` field is also present along with `custom_attributes`.

## Structure

`List Customer Custom Attributes Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attributes` | [`List of Custom Attribute`](../../doc/models/custom-attribute.md) | Optional | The retrieved custom attributes. If `with_definitions` was set to `true` in the request,<br>the custom attribute definition is returned in the `definition` field of each custom attribute.<br><br>If no custom attributes are found, Square returns an empty object (`{}`). |
| `cursor` | `string` | Optional | The cursor to use in your next call to this endpoint to retrieve the next page of results<br>for your original request. This field is present only if the request succeeded and additional<br>results are available. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "custom_attributes": [
    {
      "created_at": "2022-04-26T15:50:27Z",
      "key": "favoritemovie",
      "updated_at": "2022-04-26T15:50:27Z",
      "value": "Dune",
      "version": 1,
      "visibility": "VISIBILITY_READ_ONLY"
    },
    {
      "created_at": "2022-04-26T15:51:53Z",
      "key": "ownsmovie",
      "updated_at": "2022-04-26T15:51:53Z",
      "value": false,
      "version": 1,
      "visibility": "VISIBILITY_HIDDEN"
    }
  ]
}
```

