
# Retrieve Catalog Object Request

## Structure

`Retrieve Catalog Object Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested object, as follows:<br><br>If the `object` field of the response contains a `CatalogItem`, its associated<br>`CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will<br>be returned in the `related_objects` field of the response. If the `object` field of<br>the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned<br>in the `related_objects` field of the response.<br><br>Default value: `false` |

## Example (as JSON)

```json
{
  "include_related_objects": false
}
```

