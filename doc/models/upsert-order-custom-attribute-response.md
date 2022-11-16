
# Upsert Order Custom Attribute Response

Represents a response from upserting order custom attribute definitions.

## Structure

`Upsert Order Custom Attribute Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute` | [`Custom Attribute`](../../doc/models/custom-attribute.md) | Optional | A custom attribute value. Each custom attribute value has a corresponding<br>`CustomAttributeDefinition` object. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "custom_attribute": null,
  "errors": null
}
```

