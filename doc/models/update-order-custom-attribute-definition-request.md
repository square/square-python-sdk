
# Update Order Custom Attribute Definition Request

Represents an update request for an order custom attribute definition.

## Structure

`Update Order Custom Attribute Definition Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition` | [`Custom Attribute Definition`](../../doc/models/custom-attribute-definition.md) | Required | Represents a definition for custom attribute values. A custom attribute definition<br>specifies the key, visibility, schema, and other properties for a custom attribute. |
| `idempotency_key` | `string` | Optional | A unique identifier for this request, used to ensure idempotency.<br>For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `45` |

## Example (as JSON)

```json
{
  "custom_attribute_definition": {
    "key": "cover-count",
    "version": 1,
    "visibility": "VISIBILITY_READ_ONLY"
  },
  "idempotency_key": "IDEMPOTENCY_KEY"
}
```

