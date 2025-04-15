
# Update Booking Custom Attribute Definition Request

Represents an [UpdateBookingCustomAttributeDefinition](../../doc/api/booking-custom-attributes.md#update-booking-custom-attribute-definition) request.

## Structure

`Update Booking Custom Attribute Definition Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition` | [`Custom Attribute Definition`](../../doc/models/custom-attribute-definition.md) | Required | Represents a definition for custom attribute values. A custom attribute definition<br>specifies the key, visibility, schema, and other properties for a custom attribute. |
| `idempotency_key` | `str` | Optional | A unique identifier for this request, used to ensure idempotency. For more information,<br>see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).<br>**Constraints**: *Maximum Length*: `45` |

## Example (as JSON)

```json
{
  "custom_attribute_definition": {
    "key": "key2",
    "schema": {
      "key1": "val1",
      "key2": "val2"
    },
    "name": "name2",
    "description": "description8",
    "visibility": "VISIBILITY_HIDDEN"
  },
  "idempotency_key": "idempotency_key2"
}
```

