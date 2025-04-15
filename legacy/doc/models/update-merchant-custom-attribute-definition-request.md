
# Update Merchant Custom Attribute Definition Request

Represents an [UpdateMerchantCustomAttributeDefinition](../../doc/api/merchant-custom-attributes.md#update-merchant-custom-attribute-definition) request.

## Structure

`Update Merchant Custom Attribute Definition Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition` | [`Custom Attribute Definition`](../../doc/models/custom-attribute-definition.md) | Required | Represents a definition for custom attribute values. A custom attribute definition<br>specifies the key, visibility, schema, and other properties for a custom attribute. |
| `idempotency_key` | `str` | Optional | A unique identifier for this request, used to ensure idempotency. For more information,<br>see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).<br>**Constraints**: *Maximum Length*: `45` |

## Example (as JSON)

```json
{
  "custom_attribute_definition": {
    "description": "Update the description as desired.",
    "visibility": "VISIBILITY_READ_ONLY",
    "key": "key2",
    "schema": {
      "key1": "val1",
      "key2": "val2"
    },
    "name": "name2"
  },
  "idempotency_key": "idempotency_key4"
}
```

