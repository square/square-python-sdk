## Order Service Charge

Represents a service charge applied to an order.

### Structure

`OrderServiceCharge`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the service charge only within this order. |
| `name` | `string` | Optional | The name of the service charge. |
| `catalog_object_id` | `string` | Optional | The catalog object ID referencing the service charge [CatalogObject](./models/catalog-object.md). |
| `percentage` | `string` | Optional | The service charge percentage, as a string representation of a decimal number.<br><br>For example, `7.25` indicates 7.25%<br><br>Exactly one of `percentage` or `amount_money` should be set. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `calculation_phase` | [`str (Order Service Charge Calculation Phase)`](/doc/models/order-service-charge-calculation-phase.md) | Optional | Represents a phase in the process of calculating order totals. Service charges will<br>be applied after the phase indicated.<br><br>[Read more about how order totals are calculated.](https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated) |
| `taxable` | `bool` | Optional | Indicates whether the service charge can be taxed. If set to `true`, any order-level<br>taxes will automatically apply to this service charge. Note that service charges calculated<br>in the `TOTAL_PHASE` cannot be marked as taxable. |
| `taxes` | [`List of Order Line Item Tax`](/doc/models/order-line-item-tax.md) | Optional | A list of taxes applied to this service charge. On read or retrieve, this list includes<br>both item-level taxes and any order-level taxes apportioned to this service charge.<br>When creating an Order, set your service charge-level taxes in this list. By default,<br>order-level taxes apply to service charges calculated in the `SUBTOTAL_PHASE` if `taxable` is<br>set to `true`.<br><br>This field has been deprecated in favour of `applied_taxes`. Usage of both this field and<br>`applied_taxes` when creating an order will result in an error. Usage of this field when<br>sending requests to the UpdateOrder endpoint will result in an error. |
| `applied_taxes` | [`List of Order Line Item Applied Tax`](/doc/models/order-line-item-applied-tax.md) | Optional | The list of references to taxes applied to this service charge. Each<br>`OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level<br>`OrderLineItemTax` that is being applied to this service charge. On reads, the amount applied<br>is populated.<br><br>An `OrderLineItemAppliedTax` will be automatically created on every taxable service charge<br>for all `ORDER` scoped taxes that are added to the order. `OrderLineItemAppliedTax` records<br>for `LINE_ITEM` scoped taxes must be added in requests for the tax to apply to any taxable<br>service charge.  Taxable service charges have the `taxable` field set to true and calculated<br>in the `SUBTOTAL_PHASE`.<br><br>To change the amount of a tax, modify the referenced top-level tax. |

### Example (as JSON)

```json
{
  "uid": null,
  "name": null,
  "catalog_object_id": null,
  "percentage": null,
  "amount_money": null,
  "applied_money": null,
  "total_money": null,
  "total_tax_money": null,
  "calculation_phase": null,
  "taxable": null,
  "taxes": null,
  "applied_taxes": null
}
```

