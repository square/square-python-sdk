
# Inventory Change

Represents a single physical count, inventory, adjustment, or transfer
that is part of the history of inventory changes for a particular
[CatalogObject](../../doc/models/catalog-object.md) instance.

## Structure

`Inventory Change`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`str (Inventory Change Type)`](../../doc/models/inventory-change-type.md) | Optional | Indicates how the inventory change was applied to a tracked product quantity. |
| `physical_count` | [`Inventory Physical Count`](../../doc/models/inventory-physical-count.md) | Optional | Represents the quantity of an item variation that is physically present<br>at a specific location, verified by a seller or a seller's employee. For example,<br>a physical count might come from an employee counting the item variations on<br>hand or from syncing with an external system. |
| `adjustment` | [`Inventory Adjustment`](../../doc/models/inventory-adjustment.md) | Optional | Represents a change in state or quantity of product inventory at a<br>particular time and location. |
| `transfer` | [`Inventory Transfer`](../../doc/models/inventory-transfer.md) | Optional | Represents the transfer of a quantity of product inventory at a<br>particular time from one location to another. |
| `measurement_unit` | [`Catalog Measurement Unit`](../../doc/models/catalog-measurement-unit.md) | Optional | Represents the unit used to measure a `CatalogItemVariation` and<br>specifies the precision for decimal quantities. |
| `measurement_unit_id` | `string` | Optional | The ID of the [CatalogMeasurementUnit](../../doc/models/catalog-measurement-unit.md) object representing the catalog measurement unit associated with the inventory change. |

## Example (as JSON)

```json
{
  "type": null,
  "physical_count": null,
  "adjustment": null,
  "transfer": null,
  "measurement_unit": null,
  "measurement_unit_id": null
}
```

