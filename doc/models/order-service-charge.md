## Order Service Charge

Represents a service charge applied to an order.

### Structure

`OrderServiceCharge`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID that identifies the service charge only within this order. |
| `name` | `string` | Optional | The name of the service charge. |
| `catalog_object_id` | `string` | Optional | The catalog object ID referencing the service charge [CatalogObject](#type-catalogobject). |
| `percentage` | `string` | Optional | The service charge percentage as a string representation of a<br>decimal number. For example, `"7.25"` indicates a service charge of 7.25%.<br><br>Exactly 1 of `percentage` or `amount_money` should be set. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `applied_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_tax_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `calculation_phase` | [`str (Order Service Charge Calculation Phase)`](/doc/models/order-service-charge-calculation-phase.md) | Optional | Represents a phase in the process of calculating order totals.<br>Service charges are applied __after__ the indicated phase.<br><br>[Read more about how order totals are calculated.](https://developer.squareup.com/docs/docs/orders-api/how-it-works#how-totals-are-calculated) |
| `taxable` | `bool` | Optional | Indicates whether the service charge can be taxed. If set to `true`,<br>order-level taxes automatically apply to the service charge. Note that<br>service charges calculated in the `TOTAL_PHASE` cannot be marked as taxable. |
| `taxes` | [`List of Order Line Item Tax`](/doc/models/order-line-item-tax.md) | Optional | A list of taxes applied to this service charge. On read or retrieve, this list includes<br>both item-level taxes and any order-level taxes apportioned to this service charge.<br>When creating an Order, set your service charge-level taxes in this list. By default,<br>order-level taxes apply to service charges calculated in the `SUBTOTAL_PHASE` if `taxable` is<br>set to `true`.<br><br>This field has been deprecated in favour of `applied_taxes`. Usage of both this field and<br>`applied_taxes` when creating an order will result in an error. Usage of this field when<br>sending requests to the UpdateOrder endpoint will result in an error. |
| `applied_taxes` | [`List of Order Line Item Applied Tax`](/doc/models/order-line-item-applied-tax.md) | Optional | The list of references to taxes applied to this service charge. Each<br>`OrderLineItemAppliedTax` has a `tax_uid` that references the `uid` of a top-level<br>`OrderLineItemTax` that is being applied to this service charge. On reads, the amount applied<br>is populated.<br><br>An `OrderLineItemAppliedTax` will be automatically created on every taxable service charge<br>for all `ORDER` scoped taxes that are added to the order. `OrderLineItemAppliedTax` records<br>for `LINE_ITEM` scoped taxes must be added in requests for the tax to apply to any taxable<br>service charge.  Taxable service charges have the `taxable` field set to true and calculated<br>in the `SUBTOTAL_PHASE`.<br><br>To change the amount of a tax, modify the referenced top-level tax. |
| `metadata` | `dict` | Optional | Application-defined data attached to this service charge. Metadata fields are intended<br>to store descriptive references or associations with an entity in another system or store brief<br>information about the object. Square does not process this field; it only stores and returns it<br>in relevant API calls. Do not use metadata to store any sensitive information (personally<br>identifiable information, card details, etc.).<br><br>Keys written by applications must be 60 characters or less and must be in the character set<br>`[a-zA-Z0-9_-]`. Entries may also include metadata generated by Square. These keys are prefixed<br>with a namespace, separated from the key with a ':' character.<br><br>Values have a max length of 255 characters.<br><br>An application may have up to 10 entries per metadata field.<br><br>Entries written by applications are private and can only be read or modified by the same<br>application.<br><br>See [Metadata](https://developer.squareup.com/docs/build-basics/metadata) for more information. |

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
  "applied_taxes": null,
  "metadata": null
}
```

