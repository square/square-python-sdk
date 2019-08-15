## Order Line Item Discount Type

Indicates how the discount is applied to the associated line item or order.

### Enumeration

`OrderLineItemDiscountType`

### Fields

| Name | Description |
|  --- | --- |
| `UNKNOWN_DISCOUNT` | Used for reporting only.<br>The original transaction discount type is currently not supported by the API. |
| `FIXED_PERCENTAGE` | Apply the discount as a fixed percentage (e.g., 5%) off the item price. |
| `FIXED_AMOUNT` | Apply the discount as a fixed monetary value (e.g., $1.00) off the item price. |
| `VARIABLE_PERCENTAGE` | Apply the discount as a variable percentage off the item price.<br><br>The variable percentage is defined in Register POS apps. Specific value is assigned at the time of the purchase. |
| `VARIABLE_AMOUNT` | Apply the discount as a variable amount off the item price.<br><br>The variable amount is defined in Square POS app. Specific value is assigned at the time of the purchase. |

