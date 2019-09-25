## Delete Catalog Object Response

### Structure

`DeleteCatalogObjectResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | The set of [Error](#type-error)s encountered. |
| `deleted_object_ids` | `List of string` | Optional | The IDs of all [CatalogObject](#type-catalogobject)s deleted by this request.<br>Multiple IDs may be returned when associated objects are also deleted, for example<br>a [CatalogItemVariation](#type-catalogitemvariation) will be deleted (and its ID included in this field)<br>when its parent [CatalogItem](#type-catalogitem) is deleted. |
| `deleted_at` | `string` | Optional | The database [timestamp](#workingwithdates) of this deletion in RFC 3339 format, e.g.,<br>"2016-09-04T23:59:33.123Z". |

### Example (as JSON)

```json
{
  "deleted_object_ids": [
    "7SB3ZQYJ5GDMVFL7JK46JCHT",
    "KQLFFHA6K6J3YQAQAWDQAL57"
  ],
  "deleted_at": "2016-11-16T22:25:24.878Z"
}
```

