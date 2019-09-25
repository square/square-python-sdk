## Item Variation Location Overrides

Price and inventory alerting overrides for a [CatalogItemVariation](#type-catalogitemvariation) at a specific [location](#type-location).

### Structure

`ItemVariationLocationOverrides`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Optional | The ID of the [location](#type-location). |
| `price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `pricing_type` | [`str (Catalog Pricing Type)`](/doc/models/catalog-pricing-type.md) | Optional | Indicates whether the price of a [CatalogItemVariation](#type-catalogitemvariation) should be entered manually at the time of sale. |
| `track_inventory` | `bool` | Optional | If `true`, inventory tracking is active for the [CatalogItemVariation](#type-catalogitemvariation) at this [location](#type-location). |
| `inventory_alert_type` | [`str (Inventory Alert Type)`](/doc/models/inventory-alert-type.md) | Optional | Indicates whether Square should alert the merchant when the inventory quantity of a [CatalogItemVariation](#type-catalogitemvariation) is low. |
| `inventory_alert_threshold` | `long|int` | Optional | If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type`<br>is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.<br><br>This value is always an integer. |

### Example (as JSON)

```json
{
  "location_id": null,
  "price_money": null,
  "pricing_type": null,
  "track_inventory": null,
  "inventory_alert_type": null,
  "inventory_alert_threshold": null
}
```

