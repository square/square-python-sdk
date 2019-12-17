## V1 Discount

V1Discount

### Structure

`V1Discount`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The discount's unique ID. |
| `name` | `string` | Optional | The discount's name. |
| `rate` | `string` | Optional | The rate of the discount, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. This rate is 0 if discount_type is VARIABLE_PERCENTAGE. |
| `amount_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `discount_type` | [`str (V1 Discount Discount Type)`]($m/V1DiscountDiscountType) | Optional | - |
| `pin_required` | `bool` | Optional | Indicates whether a mobile staff member needs to enter their PIN to apply the discount to a payment. |
| `color` | [`str (V1 Discount Color)`]($m/V1DiscountColor) | Optional | - |
| `v2_id` | `string` | Optional | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. |

### Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "rate": null,
  "amount_money": null,
  "discount_type": null,
  "pin_required": null,
  "color": null,
  "v2_id": null
}
```

