## Order Return Service Charge

The service charge applied to the original order.

### Structure

`OrderReturnServiceCharge`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the return service charge only within this order. |
| `source_service_charge_uid` | `string` | Optional | `uid` of the Service Charge from the Order which contains the original charge of this service charge,<br>null for unlinked returns. |
| `name` | `string` | Optional | The name of the service charge. |
| `catalog_object_id` | `string` | Optional | The ID referencing the service charge [CatalogObject](./models/catalog-object.md) |
| `percentage` | `string` | Optional | The percentage of the service charge, as a string representation of a decimal number.<br><br>A value of `7.25` corresponds to a percentage of 7.25%.<br><br>Exactly one of percentage or amount_money should be set. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `total_tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |
| `calculation_phase` | [`str (Order Service Charge Calculation Phase)`](/doc/models/order-service-charge-calculation-phase.md) | Optional | Represents a phase in the process of calculating order totals. Service charges will<br>be applied after the phase indicated.<br><br>[Read more about how order totals are calculated.](https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated) |
| `taxable` | `bool` | Optional | Indicates whether the surcharge can be taxed. Service charges calculated in the<br>`TOTAL_PHASE` cannot be marked as taxable. |
| `return_taxes` | [`List of Order Return Tax`](/doc/models/order-return-tax.md) | Optional | Taxes applied to the `OrderReturnServiceCharge`. By default, return-level taxes apply to<br>`OrderReturnServiceCharge`s calculated in the `SUBTOTAL_PHASE` if `taxable` is set to `true`.  On<br>read or retrieve, this list includes both item-level taxes and any return-level taxes<br>apportioned to this item.<br><br>This field has been deprecated in favour of `applied_taxes`. |
| `applied_taxes` | [`List of Order Line Item Applied Tax`](/doc/models/order-line-item-applied-tax.md) | Optional | The list of references to `OrderReturnTax`s applied to this `OrderReturnServiceCharge`.<br>Each `OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level<br>`OrderReturnTax` that is being applied to this `OrderReturnServiceCharge`. On reads, the amount<br>applied is populated. |

### Example (as JSON)

```json
{
  "uid": null,
  "source_service_charge_uid": null,
  "name": null,
  "catalog_object_id": null,
  "percentage": null,
  "amount_money": null,
  "applied_money": null,
  "total_money": null,
  "total_tax_money": null,
  "calculation_phase": null,
  "taxable": null,
  "return_taxes": null,
  "applied_taxes": null
}
```

