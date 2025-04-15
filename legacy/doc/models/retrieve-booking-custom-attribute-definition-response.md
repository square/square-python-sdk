
# Retrieve Booking Custom Attribute Definition Response

Represents a [RetrieveBookingCustomAttributeDefinition](../../doc/api/booking-custom-attributes.md#retrieve-booking-custom-attribute-definition) response.
Either `custom_attribute_definition` or `errors` is present in the response.

## Structure

`Retrieve Booking Custom Attribute Definition Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition` | [`Custom Attribute Definition`](../../doc/models/custom-attribute-definition.md) | Optional | Represents a definition for custom attribute values. A custom attribute definition<br>specifies the key, visibility, schema, and other properties for a custom attribute. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "custom_attribute_definition": {
    "created_at": "2022-11-16T15:27:30Z",
    "description": "The favorite shampoo of the customer.",
    "key": "favoriteShampoo",
    "name": "Favorite shampoo",
    "schema": {
      "key1": "val1",
      "key2": "val2"
    },
    "updated_at": "2022-11-16T15:27:30Z",
    "version": 1,
    "visibility": "VISIBILITY_READ_WRITE_VALUES"
  },
  "errors": []
}
```

