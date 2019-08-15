## Item Variation Location Overrides

Price and inventory alerting overrides for a [CatalogItemVariation](./models/catalog-item-variation.md) at a specific [location](./models/location.md).

### Structure

`ItemVariationLocationOverrides`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Optional | The ID of the [location](./models/location.md). |
| `price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `pricing_type` | [`str (Catalog Pricing Type)`](/doc/models/catalog-pricing-type.md) | Optional | Indicates whether the price of a [CatalogItemVariation](./models/catalog-item-variation.md) should be entered manually at the time of sale. |
| `track_inventory` | `bool` | Optional | If `true`, inventory tracking is active for the [CatalogItemVariation](./models/catalog-item-variation.md) at this [location](./models/location.md). |
| `inventory_alert_type` | [`str (Inventory Alert Type)`](/doc/models/inventory-alert-type.md) | Optional | Indicates whether Square should alert the merchant when the inventory quantity of a [CatalogItemVariation](./models/catalog-item-variation.md) is low. |
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

