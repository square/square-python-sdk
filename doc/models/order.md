## Order

Contains all information related to a single order to process with Square,
including line items that specify the products to purchase. Order objects also
include information on any associated tenders, refunds, and returns.

All Connect V2 Transactions have all been converted to Orders including all associated
itemization data.

### Structure

`Order`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The order's unique ID. |
| `location_id` | `string` |  | The ID of the merchant location this order is associated with. |
| `reference_id` | `string` | Optional | A client specified identifier to associate an entity in another system<br>with this order. |
| `source` | [`Order Source`](/doc/models/order-source.md) | Optional | Represents the origination details of an order. |
| `customer_id` | `string` | Optional | The [Customer](./models/customer.md) ID of the customer associated with the order. |
| `line_items` | [`List of Order Line Item`](/doc/models/order-line-item.md) | Optional | The line items included in the order. |
| `taxes` | [`List of Order Line Item Tax`](/doc/models/order-line-item-tax.md) | Optional | The list of all taxes applied to this order.<br><br>Taxes can be scoped to either `ORDER` or `LINE_ITEM`. For taxes with `LINE_ITEM` scope, an<br>`OrderLineItemAppliedTax` must be added to each line item that the tax applies to. For taxes<br>with `ORDER` scope, the server will generate an `OrderLineItemAppliedTax` for every line item.<br><br>On reads, each tax in the list will include the total amount of that tax applied to the order.<br><br>If `LINE_ITEM` scope is set on any taxes in this field, usage of the deprecated<br>`line_items.taxes` field will result in an error. Please use `line_items.applied_taxes`<br>instead. |
| `discounts` | [`List of Order Line Item Discount`](/doc/models/order-line-item-discount.md) | Optional | The list of all discounts applied to this order.<br><br>Discounts can be scoped to either `ORDER` or `LINE_ITEM`. For discounts scoped to `LINE_ITEM`,<br>an `OrderLineItemAppliedDiscount` must be added to each line item that the discount applies to.<br>For discounts with `ORDER` scope, the server will generate an `OrderLineItemAppliedDiscount`<br>for every line item.<br><br>If `LINE_ITEM` scope is set on any discounts in this field, usage of the deprecated<br>`line_items.discounts` field will result in an error. Please use `line_items.applied_discounts`<br>instead. |
| `service_charges` | [`List of Order Service Charge`](/doc/models/order-service-charge.md) | Optional | A list of service charges applied to the order. |
| `fulfillments` | [`List of Order Fulfillment`](/doc/models/order-fulfillment.md) | Optional | Details on order fulfillment.<br><br>Orders can only be created with at most one fulfillment. However, orders returned<br>by the API may contain multiple fulfillments. |
| `returns` | [`List of Order Return`](/doc/models/order-return.md) | Optional | Collection of items from sale Orders being returned in this one. Normally part of an<br>Itemized Return or Exchange.  There will be exactly one `Return` object per sale Order being<br>referenced. |
| `return_amounts` | [`Order Money Amounts`](/doc/models/order-money-amounts.md) | Optional | A collection of various money amounts. |
| `net_amounts` | [`Order Money Amounts`](/doc/models/order-money-amounts.md) | Optional | A collection of various money amounts. |
| `rounding_adjustment` | [`Order Rounding Adjustment`](/doc/models/order-rounding-adjustment.md) | Optional | A rounding adjustment of the money being returned. Commonly used to apply Cash Rounding<br>when the minimum unit of account is smaller than the lowest physical denomination of currency. |
| `tenders` | [`List of Tender`](/doc/models/tender.md) | Optional | The Tenders which were used to pay for the Order. |
| `refunds` | [`List of Refund`](/doc/models/refund.md) | Optional | The Refunds that are part of this Order. |
| `created_at` | `string` | Optional | Timestamp for when the order was created. In RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z". |
| `updated_at` | `string` | Optional | Timestamp for when the order was last updated. In RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z". |
| `closed_at` | `string` | Optional | Timestamp for when the order was closed. In RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z". |
| `state` | [`str (Order State)`](/doc/models/order-state.md) | Optional | The state of the order. |
| `version` | `int` | Optional | Monotonically increasing version, incremented each time an update is committed to the order.<br>Orders that were not created through the API are not updatable and thus will not include a<br>version. |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_discount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_service_charge_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "id": null,
  "location_id": "location_id4",
  "reference_id": null,
  "source": null,
  "customer_id": null,
  "line_items": null,
  "taxes": null,
  "discounts": null,
  "service_charges": null,
  "fulfillments": null,
  "returns": null,
  "return_amounts": null,
  "net_amounts": null,
  "rounding_adjustment": null,
  "tenders": null,
  "refunds": null,
  "created_at": null,
  "updated_at": null,
  "closed_at": null,
  "state": null,
  "version": null,
  "total_money": null,
  "total_tax_money": null,
  "total_discount_money": null,
  "total_service_charge_money": null
}
```

