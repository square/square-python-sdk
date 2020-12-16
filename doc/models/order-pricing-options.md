
# Order Pricing Options

Pricing options for an order. The options affect how the order's price is calculated.
They can be used, for example, to apply automatic price adjustments that are based on pre-configured
[pricing rules](https://developer.squareup.com/docs/reference/square/objects/CatalogPricingRule).

## Structure

`Order Pricing Options`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_apply_discounts` | `bool` | Optional | The option to determine whether pricing rule-based<br>discounts are automatically applied to an order. |
| `auto_apply_taxes` | `bool` | Optional | The option to determine whether rule-based taxes are automatically<br>applied to an order when the criteria of the corresponding rules are met. |

## Example (as JSON)

```json
{
  "auto_apply_discounts": false,
  "auto_apply_taxes": false
}
```

