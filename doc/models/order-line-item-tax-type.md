## Order Line Item Tax Type

Indicates how the tax is applied to the associated line item or order.

### Enumeration

`OrderLineItemTaxType`

### Fields

| Name | Description |
|  --- | --- |
| `UNKNOWN_TAX` | Used for reporting only.<br>The original transaction tax type is currently not supported by the API. |
| `ADDITIVE` | The tax is an additive tax. The tax amount is added on top of the price.<br>For example, a $1.00 item with a 10% additive tax would have a total cost to the buyer of $1.10. |
| `INCLUSIVE` | The tax is an inclusive tax. Inclusive taxes are already included in the line item price or order total.<br>For example, a $1.00 item with a 10% inclusive tax would have a pre-tax cost of $0.91 (91 cents)<br>and a $0.09 (9 cents) tax for a total cost of $1 to the buyer. |

