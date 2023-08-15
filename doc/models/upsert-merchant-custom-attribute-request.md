
# Upsert Merchant Custom Attribute Request

Represents an [UpsertMerchantCustomAttribute](../../doc/api/merchant-custom-attributes.md#upsert-merchant-custom-attribute) request.

## Structure

`Upsert Merchant Custom Attribute Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute` | [`Custom Attribute`](../../doc/models/custom-attribute.md) | Required | A custom attribute value. Each custom attribute value has a corresponding<br>`CustomAttributeDefinition` object. |
| `idempotency_key` | `str` | Optional | A unique identifier for this request, used to ensure idempotency. For more information,<br>see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).<br>**Constraints**: *Maximum Length*: `45` |

## Example (as JSON)

```json
{
  "custom_attribute": {
    "key": "key2",
    "value": {
      "key1": "val1",
      "key2": "val2"
    },
    "version": 102,
    "visibility": "VISIBILITY_READ_ONLY",
    "definition": {
      "key": "key2",
      "schema": {
        "key1": "val1",
        "key2": "val2"
      },
      "name": "name2",
      "description": "description2",
      "visibility": "VISIBILITY_READ_ONLY"
    }
  },
  "idempotency_key": "idempotency_key6"
}
```

