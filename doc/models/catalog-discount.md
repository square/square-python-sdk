## Catalog Discount

A discount in the Catalog object model.

### Structure

`CatalogDiscount`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The discount's name. Searchable. This field has max length of 255 Unicode code points. |
| `discount_type` | [`str (Catalog Discount Type)`](/doc/models/catalog-discount-type.md) | Optional | How to apply a [CatalogDiscount](#type-catalogdiscount) to a [CatalogItem](#type-catalogitem). |
| `percentage` | `string` | Optional | The percentage of the discount as a string representation of a decimal number, using a `.` as the decimal<br>separator and without a `%` sign. A value of `7.5` corresponds to `7.5%`. Specify a percentage of `0` if `discount_type`<br>is `VARIABLE_PERCENTAGE`.<br><br>Do not include this field for amount-based or variable discounts. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |
| `pin_required` | `bool` | Optional | Indicates whether a mobile staff member needs to enter their PIN to apply the<br>discount to a payment in the Square Point of Sale app. |
| `label_color` | `string` | Optional | The color of the discount's display label in the Square Point of Sale app. This must be a valid hex color code. |

### Example (as JSON)

```json
{
  "object": {
    "type": "DISCOUNT",
    "id": "#Maythe4th",
    "present_at_all_locations": true,
    "discount_data": {
      "name": "Welcome to the Dark(Roast) Side!",
      "discount_type": "FIXED_PERCENTAGE",
      "percentage": "5.4",
      "pin_required": false,
      "label_color": "red"
    }
  }
}
```

