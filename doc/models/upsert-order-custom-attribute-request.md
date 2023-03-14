
# Upsert Order Custom Attribute Request

Represents an upsert request for an order custom attribute.

## Structure

`Upsert Order Custom Attribute Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute` | [`Custom Attribute`](../../doc/models/custom-attribute.md) | Required | A custom attribute value. Each custom attribute value has a corresponding<br>`CustomAttributeDefinition` object. |
| `idempotency_key` | `string` | Optional | A unique identifier for this request, used to ensure idempotency.<br>For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).<br>**Constraints**: *Maximum Length*: `45` |

## Example (as JSON)

```json
{
  "custom_attribute": {
    "key": null,
    "value": null,
    "version": null,
    "visibility": null,
    "definition": null,
    "updated_at": null,
    "created_at": null
  },
  "idempotency_key": null
}
```

