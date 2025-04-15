
# Catalog Custom Attribute Value

An instance of a custom attribute. Custom attributes can be defined and
added to `ITEM` and `ITEM_VARIATION` type catalog objects.
[Read more about custom attributes](https://developer.squareup.com/docs/catalog-api/add-custom-attributes).

## Structure

`Catalog Custom Attribute Value`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the custom attribute. |
| `string_value` | `str` | Optional | The string value of the custom attribute.  Populated if `type` = `STRING`. |
| `custom_attribute_definition_id` | `str` | Optional | The id of the [CatalogCustomAttributeDefinition](entity:CatalogCustomAttributeDefinition) this value belongs to. |
| `type` | [`str (Catalog Custom Attribute Definition Type)`](../../doc/models/catalog-custom-attribute-definition-type.md) | Optional | Defines the possible types for a custom attribute. |
| `number_value` | `str` | Optional | Populated if `type` = `NUMBER`. Contains a string<br>representation of a decimal number, using a `.` as the decimal separator. |
| `boolean_value` | `bool` | Optional | A `true` or `false` value. Populated if `type` = `BOOLEAN`. |
| `selection_uid_values` | `List[str]` | Optional | One or more choices from `allowed_selections`. Populated if `type` = `SELECTION`. |
| `key` | `str` | Optional | If the associated `CatalogCustomAttributeDefinition` object is defined by another application, this key is prefixed by the defining application ID.<br>For example, if the CatalogCustomAttributeDefinition has a key attribute of "cocoa_brand" and the defining application ID is "abcd1234", this key is "abcd1234:cocoa_brand"<br>when the application making the request is different from the application defining the custom attribute definition. Otherwise, the key is simply "cocoa_brand". |

## Example (as JSON)

```json
{
  "name": "name2",
  "string_value": "string_value6",
  "custom_attribute_definition_id": "custom_attribute_definition_id0",
  "type": "NUMBER",
  "number_value": "number_value2"
}
```

