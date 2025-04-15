
# Inventory Physical Count

Represents the quantity of an item variation that is physically present
at a specific location, verified by a seller or a seller's employee. For example,
a physical count might come from an employee counting the item variations on
hand or from syncing with an external system.

## Structure

`Inventory Physical Count`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A unique Square-generated ID for the<br>[InventoryPhysicalCount](entity:InventoryPhysicalCount).<br>**Constraints**: *Maximum Length*: `100` |
| `reference_id` | `str` | Optional | An optional ID provided by the application to tie the<br>[InventoryPhysicalCount](entity:InventoryPhysicalCount) to an external<br>system.<br>**Constraints**: *Maximum Length*: `255` |
| `catalog_object_id` | `str` | Optional | The Square-generated ID of the<br>[CatalogObject](entity:CatalogObject) being tracked.<br>**Constraints**: *Maximum Length*: `100` |
| `catalog_object_type` | `str` | Optional | The [type](entity:CatalogObjectType) of the [CatalogObject](entity:CatalogObject) being tracked.<br><br>The Inventory API supports setting and reading the `"catalog_object_type": "ITEM_VARIATION"` field value.<br>In addition, it can also read the `"catalog_object_type": "ITEM"` field value that is set by the Square Restaurants app.<br>**Constraints**: *Maximum Length*: `14` |
| `state` | [`str (Inventory State)`](../../doc/models/inventory-state.md) | Optional | Indicates the state of a tracked item quantity in the lifecycle of goods. |
| `location_id` | `str` | Optional | The Square-generated ID of the [Location](entity:Location) where the related<br>quantity of items is being tracked.<br>**Constraints**: *Maximum Length*: `100` |
| `quantity` | `str` | Optional | The number of items affected by the physical count as a decimal string.<br>The number can support up to 5 digits after the decimal point.<br>**Constraints**: *Maximum Length*: `26` |
| `source` | [`Source Application`](../../doc/models/source-application.md) | Optional | Represents information about the application used to generate a change. |
| `employee_id` | `str` | Optional | The Square-generated ID of the [Employee](entity:Employee) responsible for the<br>physical count.<br>**Constraints**: *Maximum Length*: `100` |
| `team_member_id` | `str` | Optional | The Square-generated ID of the [Team Member](entity:TeamMember) responsible for the<br>physical count.<br>**Constraints**: *Maximum Length*: `100` |
| `occurred_at` | `str` | Optional | A client-generated RFC 3339-formatted timestamp that indicates when<br>the physical count was examined. For physical count updates, the `occurred_at`<br>timestamp cannot be older than 24 hours or in the future relative to the<br>time of the request.<br>**Constraints**: *Maximum Length*: `34` |
| `created_at` | `str` | Optional | An RFC 3339-formatted timestamp that indicates when the physical count is received.<br>**Constraints**: *Maximum Length*: `34` |

## Example (as JSON)

```json
{
  "id": "id0",
  "reference_id": "reference_id8",
  "catalog_object_id": "catalog_object_id4",
  "catalog_object_type": "catalog_object_type4",
  "state": "COMPOSED"
}
```

