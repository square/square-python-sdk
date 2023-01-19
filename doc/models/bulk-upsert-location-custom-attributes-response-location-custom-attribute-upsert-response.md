
# Bulk Upsert Location Custom Attributes Response Location Custom Attribute Upsert Response

Represents a response for an individual upsert request in a [BulkUpsertLocationCustomAttributes](../../doc/api/location-custom-attributes.md#bulk-upsert-location-custom-attributes) operation.

## Structure

`Bulk Upsert Location Custom Attributes Response Location Custom Attribute Upsert Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Optional | The ID of the location associated with the custom attribute. |
| `custom_attribute` | [`Custom Attribute`](../../doc/models/custom-attribute.md) | Optional | A custom attribute value. Each custom attribute value has a corresponding<br>`CustomAttributeDefinition` object. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred while processing the individual request. |

## Example (as JSON)

```json
{
  "location_id": null,
  "custom_attribute": null,
  "errors": null
}
```

