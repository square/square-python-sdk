## Batch Retrieve Catalog Objects Request

### Structure

`BatchRetrieveCatalogObjectsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_ids` | `List of string` |  | The IDs of the [CatalogObject](#type-catalogobject)s to be retrieved. |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested objects, as follows:<br><br>If the `objects` field of the response contains a [CatalogItem](#type-catalogitem), <br>its associated [CatalogCategory](#type-catalogcategory), [CatalogTax](#type-catalogtax)es,<br>[CatalogImage](#type-catalogimage)s and [CatalogModifierList](#type-catalogmodifierlist)s<br>will be returned in the `related_objects` field of the response. If the `objects`<br>field of the response contains a [CatalogItemVariation](#type-catalogitemvariation),<br>its parent [CatalogItem](#type-catalogitem) will be returned in the `related_objects` field of<br>the response. |

### Example (as JSON)

```json
{
  "object_ids": [
    "W62UWFY35CWMYGVWK6TWJDNI",
    "AA27W3M2GGTF3H6AVPNB77CK"
  ],
  "include_related_objects": true
}
```

