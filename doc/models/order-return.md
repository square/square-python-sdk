
# Order Return

The set of line items, service charges, taxes, discounts, tips, and other items being returned in an order.

## Structure

`Order Return`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | A unique ID that identifies the return only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `source_order_id` | `string` | Optional | An order that contains the original sale of these return line items. This is unset<br>for unlinked returns. |
| `return_line_items` | [`List of Order Return Line Item`](../../doc/models/order-return-line-item.md) | Optional | A collection of line items that are being returned. |
| `return_service_charges` | [`List of Order Return Service Charge`](../../doc/models/order-return-service-charge.md) | Optional | A collection of service charges that are being returned. |
| `return_taxes` | [`List of Order Return Tax`](../../doc/models/order-return-tax.md) | Optional | A collection of references to taxes being returned for an order, including the total<br>applied tax amount to be returned. The taxes must reference a top-level tax ID from the source<br>order. |
| `return_discounts` | [`List of Order Return Discount`](../../doc/models/order-return-discount.md) | Optional | A collection of references to discounts being returned for an order, including the total<br>applied discount amount to be returned. The discounts must reference a top-level discount ID<br>from the source order. |
| `rounding_adjustment` | [`Order Rounding Adjustment`](../../doc/models/order-rounding-adjustment.md) | Optional | A rounding adjustment of the money being returned. Commonly used to apply cash rounding<br>when the minimum unit of the account is smaller than the lowest physical denomination of the currency. |
| `return_amounts` | [`Order Money Amounts`](../../doc/models/order-money-amounts.md) | Optional | A collection of various money amounts. |

## Example (as JSON)

```json
{
  "uid": null,
  "source_order_id": null,
  "return_line_items": null,
  "return_service_charges": null,
  "return_taxes": null,
  "return_discounts": null,
  "rounding_adjustment": null,
  "return_amounts": null
}
```

