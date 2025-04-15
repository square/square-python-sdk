
# Custom Attribute Filter

Supported custom attribute query expressions for calling the
[SearchCatalogItems](../../doc/api/catalog.md#search-catalog-items)
endpoint to search for items or item variations.

## Structure

`Custom Attribute Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition_id` | `str` | Optional | A query expression to filter items or item variations by matching their custom attributes'<br>`custom_attribute_definition_id` property value against the the specified id.<br>Exactly one of `custom_attribute_definition_id` or `key` must be specified. |
| `key` | `str` | Optional | A query expression to filter items or item variations by matching their custom attributes'<br>`key` property value against the specified key.<br>Exactly one of `custom_attribute_definition_id` or `key` must be specified. |
| `string_filter` | `str` | Optional | A query expression to filter items or item variations by matching their custom attributes'<br>`string_value`  property value against the specified text.<br>Exactly one of `string_filter`, `number_filter`, `selection_uids_filter`, or `bool_filter` must be specified. |
| `number_filter` | [`Range`](../../doc/models/range.md) | Optional | The range of a number value between the specified lower and upper bounds. |
| `selection_uids_filter` | `List[str]` | Optional | A query expression to filter items or item variations by matching  their custom attributes'<br>`selection_uid_values` values against the specified selection uids.<br>Exactly one of `string_filter`, `number_filter`, `selection_uids_filter`, or `bool_filter` must be specified. |
| `bool_filter` | `bool` | Optional | A query expression to filter items or item variations by matching their custom attributes'<br>`boolean_value` property values against the specified Boolean expression.<br>Exactly one of `string_filter`, `number_filter`, `selection_uids_filter`, or `bool_filter` must be specified. |

## Example (as JSON)

```json
{
  "custom_attribute_definition_id": "custom_attribute_definition_id0",
  "key": "key2",
  "string_filter": "string_filter4",
  "number_filter": {
    "min": "min8",
    "max": "max4"
  },
  "selection_uids_filter": [
    "selection_uids_filter0",
    "selection_uids_filter9",
    "selection_uids_filter8"
  ]
}
```

