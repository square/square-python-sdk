
# Order Return

The set of line items, service charges, taxes, discounts, tips, and other items being returned in an order.

## Structure

`Order Return`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID that identifies the return only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `source_order_id` | `str` | Optional | An order that contains the original sale of these return line items. This is unset<br>for unlinked returns. |
| `return_line_items` | [`List Order Return Line Item`](../../doc/models/order-return-line-item.md) | Optional | A collection of line items that are being returned. |
| `return_service_charges` | [`List Order Return Service Charge`](../../doc/models/order-return-service-charge.md) | Optional | A collection of service charges that are being returned. |
| `return_taxes` | [`List Order Return Tax`](../../doc/models/order-return-tax.md) | Optional | A collection of references to taxes being returned for an order, including the total<br>applied tax amount to be returned. The taxes must reference a top-level tax ID from the source<br>order. |
| `return_discounts` | [`List Order Return Discount`](../../doc/models/order-return-discount.md) | Optional | A collection of references to discounts being returned for an order, including the total<br>applied discount amount to be returned. The discounts must reference a top-level discount ID<br>from the source order. |
| `return_tips` | [`List Order Return Tip`](../../doc/models/order-return-tip.md) | Optional | A collection of references to tips being returned for an order. |
| `rounding_adjustment` | [`Order Rounding Adjustment`](../../doc/models/order-rounding-adjustment.md) | Optional | A rounding adjustment of the money being returned. Commonly used to apply cash rounding<br>when the minimum unit of the account is smaller than the lowest physical denomination of the currency. |
| `return_amounts` | [`Order Money Amounts`](../../doc/models/order-money-amounts.md) | Optional | A collection of various money amounts. |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "source_order_id": "source_order_id0",
  "return_line_items": [
    {
      "uid": "uid0",
      "source_line_item_uid": "source_line_item_uid2",
      "name": "name0",
      "quantity": "quantity6",
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
      "note": "note4"
    }
  ],
  "return_service_charges": [
    {
      "uid": "uid6",
      "source_service_charge_uid": "source_service_charge_uid0",
      "name": "name6",
      "catalog_object_id": "catalog_object_id0",
      "catalog_version": 12
    },
    {
      "uid": "uid6",
      "source_service_charge_uid": "source_service_charge_uid0",
      "name": "name6",
      "catalog_object_id": "catalog_object_id0",
      "catalog_version": 12
    }
  ],
  "return_taxes": [
    {
      "uid": "uid2",
      "source_tax_uid": "source_tax_uid0",
      "catalog_object_id": "catalog_object_id4",
      "catalog_version": 106,
      "name": "name2"
    },
    {
      "uid": "uid2",
      "source_tax_uid": "source_tax_uid0",
      "catalog_object_id": "catalog_object_id4",
      "catalog_version": 106,
      "name": "name2"
    },
    {
      "uid": "uid2",
      "source_tax_uid": "source_tax_uid0",
      "catalog_object_id": "catalog_object_id4",
      "catalog_version": 106,
      "name": "name2"
    }
  ]
}
```

