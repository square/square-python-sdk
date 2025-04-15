
# Quantity Ratio

A whole number or unreduced fractional ratio.

## Structure

`Quantity Ratio`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity` | `int` | Optional | The whole or fractional quantity as the numerator. |
| `quantity_denominator` | `int` | Optional | The whole or fractional quantity as the denominator.<br>With fractional quantity this field is the denominator and quantity is the numerator.<br>The default value is `1`. For example, when `quantity=3` and `quantity_denominator` is unspecified,<br>the quantity ratio is `3` or `3/1`. |

## Example (as JSON)

```json
{
  "quantity": 86,
  "quantity_denominator": 18
}
```

