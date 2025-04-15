
# Item Variation Location Overrides

Price and inventory alerting overrides for a `CatalogItemVariation` at a specific `Location`.

## Structure

`Item Variation Location Overrides`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | The ID of the `Location`. This can include locations that are deactivated. |
| `price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `pricing_type` | [`str (Catalog Pricing Type)`](../../doc/models/catalog-pricing-type.md) | Optional | Indicates whether the price of a CatalogItemVariation should be entered manually at the time of sale. |
| `track_inventory` | `bool` | Optional | If `true`, inventory tracking is active for the `CatalogItemVariation` at this `Location`. |
| `inventory_alert_type` | [`str (Inventory Alert Type)`](../../doc/models/inventory-alert-type.md) | Optional | Indicates whether Square should alert the merchant when the inventory quantity of a CatalogItemVariation is low. |
| `inventory_alert_threshold` | `long\|int` | Optional | If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type`<br>is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.<br><br>This value is always an integer. |
| `sold_out` | `bool` | Optional | Indicates whether the overridden item variation is sold out at the specified location.<br><br>When inventory tracking is enabled on the item variation either globally or at the specified location,<br>the item variation is automatically marked as sold out when its inventory count reaches zero. The seller<br>can manually set the item variation as sold out even when the inventory count is greater than zero.<br>Attempts by an application to set this attribute are ignored. Regardless how the sold-out status is set,<br>applications should treat its inventory count as zero when this attribute value is `true`. |
| `sold_out_valid_until` | `str` | Optional | The seller-assigned timestamp, of the RFC 3339 format, to indicate when this sold-out variation<br>becomes available again at the specified location. Attempts by an application to set this attribute are ignored.<br>When the current time is later than this attribute value, the affected item variation is no longer sold out. |

## Example (as JSON)

```json
{
  "location_id": "location_id6",
  "price_money": {
    "amount": 202,
    "currency": "GTQ"
  },
  "pricing_type": "FIXED_PRICING",
  "track_inventory": false,
  "inventory_alert_type": "NONE"
}
```

