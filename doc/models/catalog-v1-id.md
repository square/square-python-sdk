## Catalog V1 Id

An Items Connect V1 object ID along with its associated location ID.

### Structure

`CatalogV1Id`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_v1_id` | `string` | Optional | The ID for an object in Connect V1, if different from its Connect V2 ID. |
| `location_id` | `string` | Optional | The ID of the `Location` this Connect V1 ID is associated with. |

### Example (as JSON)

```json
{
  "catalog_v1_id": null,
  "location_id": null
}
```

