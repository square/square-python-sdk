
# Catalog Tax

A tax applicable to an item.

## Structure

`Catalog Tax`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The tax's name. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.<br>**Constraints**: *Maximum Length*: `255` |
| `calculation_phase` | [`str (Tax Calculation Phase)`](../../doc/models/tax-calculation-phase.md) | Optional | When to calculate the taxes due on a cart. |
| `inclusion_type` | [`str (Tax Inclusion Type)`](../../doc/models/tax-inclusion-type.md) | Optional | Whether to the tax amount should be additional to or included in the CatalogItem price. |
| `percentage` | `str` | Optional | The percentage of the tax in decimal form, using a `'.'` as the decimal separator and without a `'%'` sign.<br>A value of `7.5` corresponds to 7.5%. For a location-specific tax rate, contact the tax authority of the location or a tax consultant. |
| `applies_to_custom_amounts` | `bool` | Optional | If `true`, the fee applies to custom amounts entered into the Square Point of Sale<br>app that are not associated with a particular `CatalogItem`. |
| `enabled` | `bool` | Optional | A Boolean flag to indicate whether the tax is displayed as enabled (`true`) in the Square Point of Sale app or not (`false`). |
| `applies_to_product_set_id` | `str` | Optional | The ID of a `CatalogProductSet` object. If set, the tax is applicable to all products in the product set. |

## Example (as JSON)

```json
{
  "object": {
    "id": "#SalesTax",
    "present_at_all_locations": true,
    "tax_data": {
      "calculation_phase": "TAX_SUBTOTAL_PHASE",
      "enabled": true,
      "fee_applies_to_custom_amounts": true,
      "inclusion_type": "ADDITIVE",
      "name": "Sales Tax",
      "percentage": "5.0"
    },
    "type": "TAX"
  },
  "name": "name2",
  "calculation_phase": "TAX_SUBTOTAL_PHASE",
  "inclusion_type": "ADDITIVE",
  "percentage": "percentage0",
  "applies_to_custom_amounts": false
}
```

