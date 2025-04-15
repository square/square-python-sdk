
# Order Return Line Item

The line item being returned in an order.

## Structure

`Order Return Line Item`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID for this return line-item entry.<br>**Constraints**: *Maximum Length*: `60` |
| `source_line_item_uid` | `str` | Optional | The `uid` of the line item in the original sale order.<br>**Constraints**: *Maximum Length*: `60` |
| `name` | `str` | Optional | The name of the line item.<br>**Constraints**: *Maximum Length*: `512` |
| `quantity` | `str` | Required | The quantity returned, formatted as a decimal number.<br>For example, `"3"`.<br><br>Line items with a `quantity_unit` can have non-integer quantities.<br>For example, `"1.70000"`.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `12` |
| `quantity_unit` | [`Order Quantity Unit`](../../doc/models/order-quantity-unit.md) | Optional | Contains the measurement unit for a quantity and a precision that<br>specifies the number of digits after the decimal point for decimal quantities. |
| `note` | `str` | Optional | The note of the return line item.<br>**Constraints**: *Maximum Length*: `2000` |
| `catalog_object_id` | `str` | Optional | The [CatalogItemVariation](entity:CatalogItemVariation) ID applied to this return line item.<br>**Constraints**: *Maximum Length*: `192` |
| `catalog_version` | `long\|int` | Optional | The version of the catalog object that this line item references. |
| `variation_name` | `str` | Optional | The name of the variation applied to this return line item.<br>**Constraints**: *Maximum Length*: `400` |
| `item_type` | [`str (Order Line Item Item Type)`](../../doc/models/order-line-item-item-type.md) | Optional | Represents the line item type. |
| `return_modifiers` | [`List Order Return Line Item Modifier`](../../doc/models/order-return-line-item-modifier.md) | Optional | The [CatalogModifier](entity:CatalogModifier)s applied to this line item. |
| `applied_taxes` | [`List Order Line Item Applied Tax`](../../doc/models/order-line-item-applied-tax.md) | Optional | The list of references to `OrderReturnTax` entities applied to the return line item. Each<br>`OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level<br>`OrderReturnTax` applied to the return line item. On reads, the applied amount<br>is populated. |
| `applied_discounts` | [`List Order Line Item Applied Discount`](../../doc/models/order-line-item-applied-discount.md) | Optional | The list of references to `OrderReturnDiscount` entities applied to the return line item. Each<br>`OrderLineItemAppliedDiscount` has a `discount_uid` that references the `uid` of a top-level<br>`OrderReturnDiscount` applied to the return line item. On reads, the applied amount<br>is populated. |
| `base_price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `variation_total_price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `gross_return_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_tax_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_discount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `applied_service_charges` | [`List Order Line Item Applied Service Charge`](../../doc/models/order-line-item-applied-service-charge.md) | Optional | The list of references to `OrderReturnServiceCharge` entities applied to the return<br>line item. Each `OrderLineItemAppliedServiceCharge` has a `service_charge_uid` that<br>references the `uid` of a top-level `OrderReturnServiceCharge` applied to the return line<br>item. On reads, the applied amount is populated. |
| `total_service_charge_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "source_line_item_uid": "source_line_item_uid0",
  "name": "name2",
  "quantity": "quantity8",
  "quantity_unit": {
    "measurement_unit": {
      "custom_unit": {
        "name": "name2",
        "abbreviation": "abbreviation4"
      },
      "area_unit": "IMPERIAL_ACRE",
      "length_unit": "IMPERIAL_INCH",
      "volume_unit": "METRIC_LITER",
      "weight_unit": "IMPERIAL_WEIGHT_OUNCE"
    },
    "precision": 54,
    "catalog_object_id": "catalog_object_id0",
    "catalog_version": 12
  },
  "note": "note8"
}
```

