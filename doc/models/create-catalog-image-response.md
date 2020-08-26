## Create Catalog Image Response

### Structure

`CreateCatalogImageResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on any errors encountered. |
| `image` | [`Catalog Object`](/doc/models/catalog-object.md) | Optional | - |

### Example (as JSON)

```json
{
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "REQUEST_TIMEOUT",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "CONFLICT",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "GONE",
      "detail": "detail3",
      "field": "field1"
    }
  ],
  "image": {
    "type": "ITEM_OPTION",
    "id": "id6",
    "updated_at": "updated_at2",
    "version": 100,
    "is_deleted": false,
    "custom_attribute_values": {
      "key0": {
        "name": "name9",
        "string_value": "string_value3",
        "custom_attribute_definition_id": "custom_attribute_definition_id3",
        "type": "BOOLEAN",
        "number_value": "number_value9"
      },
      "key1": {
        "name": "name0",
        "string_value": "string_value4",
        "custom_attribute_definition_id": "custom_attribute_definition_id2",
        "type": "STRING",
        "number_value": "number_value0"
      }
    },
    "catalog_v1_ids": [
      {
        "catalog_v1_id": "catalog_v1_id0",
        "location_id": "location_id0"
      },
      {
        "catalog_v1_id": "catalog_v1_id1",
        "location_id": "location_id1"
      },
      {
        "catalog_v1_id": "catalog_v1_id2",
        "location_id": "location_id2"
      }
    ]
  }
}
```

