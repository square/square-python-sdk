## Inventory Change

Represents a single physical count, inventory, adjustment, or transfer
that is part of the history of inventory changes for a particular
`CatalogObject`.

### Structure

`InventoryChange`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`str (Inventory Change Type)`]($m/InventoryChangeType) | Optional | Indicates how the inventory change was applied to a tracked quantity of items. |
| `physical_count` | [`Inventory Physical Count`]($m/InventoryPhysicalCount) | Optional | Represents the quantity of an item variation that is physically present<br>at a specific location, verified by a seller or a seller's employee. For example,<br>a physical count might come from an employee counting the item variations on<br>hand or from syncing with an external system. |
| `adjustment` | [`Inventory Adjustment`]($m/InventoryAdjustment) | Optional | Represents a change in state or quantity of product inventory at a<br>particular time and location. |
| `transfer` | [`Inventory Transfer`]($m/InventoryTransfer) | Optional | Represents the transfer of a quantity of product inventory at a<br>particular time from one location to another. |

### Example (as JSON)

```json
{
  "type": null,
  "physical_count": null,
  "adjustment": null,
  "transfer": null
}
```

