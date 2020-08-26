## Batch Retrieve Inventory Changes Request

### Structure

`BatchRetrieveInventoryChangesRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_ids` | `List of string` | Optional | The filter to return results by `CatalogObject` ID.<br>The filter is only applicable when set. The default value is null. |
| `location_ids` | `List of string` | Optional | The filter to return results by `Location` ID. <br>The filter is only applicable when set. The default value is null. |
| `types` | [`List of str (Inventory Change Type)`](/doc/models/inventory-change-type.md) | Optional | The filter to return results by `InventoryChangeType` values other than `TRANSFER`.<br>The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.<br>See [InventoryChangeType](#type-inventorychangetype) for possible values |
| `states` | [`List of str (Inventory State)`](/doc/models/inventory-state.md) | Optional | The filter to return `ADJUSTMENT` query results by<br>`InventoryState`. This filter is only applied when set.<br>The default value is null.<br>See [InventoryState](#type-inventorystate) for possible values |
| `updated_after` | `string` | Optional | The filter to return results with their `calculated_at` value  <br>after the given time as specified in an RFC 3339 timestamp. <br>The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`). |
| `updated_before` | `string` | Optional | The filter to return results with their `created_at` or `calculated_at` value  <br>strictly before the given time as specified in an RFC 3339 timestamp. <br>The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`). |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. |

### Example (as JSON)

```json
{
  "catalog_object_ids": [
    "W62UWFY35CWMYGVWK6TWJDNI"
  ],
  "location_ids": [
    "C6W5YS5QM06F5"
  ],
  "types": [
    "PHYSICAL_COUNT"
  ],
  "states": [
    "IN_STOCK"
  ],
  "updated_after": "2016-11-01T00:00:00.000Z",
  "updated_before": "2016-12-01T00:00:00.000Z"
}
```

