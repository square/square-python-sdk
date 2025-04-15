
# Create Catalog Image Request

## Structure

`Create Catalog Image Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Required | A unique string that identifies this CreateCatalogImage request.<br>Keys can be any valid string but must be unique for every CreateCatalogImage request.<br><br>See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.<br>**Constraints**: *Minimum Length*: `1` |
| `object_id` | `str` | Optional | Unique ID of the `CatalogObject` to attach this `CatalogImage` object to. Leave this<br>field empty to create unattached images, for example if you are building an integration<br>where an image can be attached to catalog items at a later time. |
| `image` | [`Catalog Object`](../../doc/models/catalog-object.md) | Required | The wrapper object for the catalog entries of a given object type.<br><br>Depending on the `type` attribute value, a `CatalogObject` instance assumes a type-specific data to yield the corresponding type of catalog object.<br><br>For example, if `type=ITEM`, the `CatalogObject` instance must have the ITEM-specific data set on the `item_data` attribute. The resulting `CatalogObject` instance is also a `CatalogItem` instance.<br><br>In general, if `type=<OBJECT_TYPE>`, the `CatalogObject` instance must have the `<OBJECT_TYPE>`-specific data set on the `<object_type>_data` attribute. The resulting `CatalogObject` instance is also a `Catalog<ObjectType>` instance.<br><br>For a more detailed discussion of the Catalog data model, please see the<br>[Design a Catalog](https://developer.squareup.com/docs/catalog-api/design-a-catalog) guide. |
| `is_primary` | `bool` | Optional | If this is set to `true`, the image created will be the primary, or first image of the object referenced by `object_id`.<br>If the `CatalogObject` already has a primary `CatalogImage`, setting this field to `true` will replace the primary image.<br>If this is set to `false` and you use the Square API version 2021-12-15 or later, the image id will be appended to the list of `image_ids` on the object.<br><br>With Square API version 2021-12-15 or later, the default value is `false`. Otherwise, the effective default value is `true`. |

## Example (as JSON)

```json
{
  "idempotency_key": "528dea59-7bfb-43c1-bd48-4a6bba7dd61f86",
  "image": {
    "id": "#TEMP_ID",
    "image_data": {
      "caption": "A picture of a cup of coffee"
    },
    "type": "IMAGE",
    "updated_at": "updated_at2",
    "version": 100,
    "is_deleted": false,
    "custom_attribute_values": {
      "key0": {
        "name": "name8",
        "string_value": "string_value2",
        "custom_attribute_definition_id": "custom_attribute_definition_id4",
        "type": "STRING",
        "number_value": "number_value8"
      },
      "key1": {
        "name": "name8",
        "string_value": "string_value2",
        "custom_attribute_definition_id": "custom_attribute_definition_id4",
        "type": "STRING",
        "number_value": "number_value8"
      }
    },
    "catalog_v1_ids": [
      {
        "catalog_v1_id": "catalog_v1_id4",
        "location_id": "location_id4"
      },
      {
        "catalog_v1_id": "catalog_v1_id4",
        "location_id": "location_id4"
      },
      {
        "catalog_v1_id": "catalog_v1_id4",
        "location_id": "location_id4"
      }
    ]
  },
  "object_id": "ND6EA5AAJEO5WL3JNNIAQA32",
  "is_primary": false
}
```

