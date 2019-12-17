## V1 Adjust Inventory Request

V1AdjustInventoryRequest

### Structure

`V1AdjustInventoryRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity_delta` | `float` | Optional | The number to adjust the variation's quantity by. |
| `adjustment_type` | [`str (V1 Adjust Inventory Request Adjustment Type)`]($m/V1AdjustInventoryRequestAdjustmentType) | Optional | - |
| `memo` | `string` | Optional | A note about the inventory adjustment. |

### Example (as JSON)

```json
{
  "quantity_delta": null,
  "adjustment_type": null,
  "memo": null
}
```

