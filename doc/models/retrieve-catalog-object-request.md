## Retrieve Catalog Object Request

### Structure

`RetrieveCatalogObjectRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested object, as follows:<br><br>If the `object` field of the response contains a [CatalogItem](#type-catalogitem),<br>its associated [CatalogCategory](#type-catalogcategory), [CatalogTax](#type-catalogtax)es,<br>[CatalogImage](#type-catalogimage)s and [CatalogModifierList](#type-catalogmodifierlist)s<br>will be returned in the `related_objects` field of the response. If the `object`<br>field of the response contains a [CatalogItemVariation](#type-catalogitemvariation),<br>its parent [CatalogItem](#type-catalogitem) will be returned in the `related_objects` field of <br>the response.<br><br>Default value: `false` |

### Example (as JSON)

```json
{
  "include_related_objects": null
}
```

