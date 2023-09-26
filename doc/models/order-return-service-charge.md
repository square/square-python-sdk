
# Order Return Service Charge

Represents the service charge applied to the original order.

## Structure

`Order Return Service Charge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID that identifies the return service charge only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `source_service_charge_uid` | `str` | Optional | The service charge `uid` from the order containing the original<br>service charge. `source_service_charge_uid` is `null` for<br>unlinked returns.<br>**Constraints**: *Maximum Length*: `60` |
| `name` | `str` | Optional | The name of the service charge.<br>**Constraints**: *Maximum Length*: `255` |
| `catalog_object_id` | `str` | Optional | The catalog object ID of the associated [OrderServiceCharge](entity:OrderServiceCharge).<br>**Constraints**: *Maximum Length*: `192` |
| `catalog_version` | `long\|int` | Optional | The version of the catalog object that this service charge references. |
| `percentage` | `str` | Optional | The percentage of the service charge, as a string representation of<br>a decimal number. For example, a value of `"7.25"` corresponds to a<br>percentage of 7.25%.<br><br>Either `percentage` or `amount_money` should be set, but not both.<br>**Constraints**: *Maximum Length*: `10` |
| `amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `applied_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_tax_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `calculation_phase` | [`str (Order Service Charge Calculation Phase)`](../../doc/models/order-service-charge-calculation-phase.md) | Optional | Represents a phase in the process of calculating order totals.<br>Service charges are applied after the indicated phase.<br><br>[Read more about how order totals are calculated.](https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated) |
| `taxable` | `bool` | Optional | Indicates whether the surcharge can be taxed. Service charges<br>calculated in the `TOTAL_PHASE` cannot be marked as taxable. |
| `applied_taxes` | [`List Order Line Item Applied Tax`](../../doc/models/order-line-item-applied-tax.md) | Optional | The list of references to `OrderReturnTax` entities applied to the<br>`OrderReturnServiceCharge`. Each `OrderLineItemAppliedTax` has a `tax_uid`<br>that references the `uid` of a top-level `OrderReturnTax` that is being<br>applied to the `OrderReturnServiceCharge`. On reads, the applied amount is<br>populated. |
| `treatment_type` | [`str (Order Service Charge Treatment Type)`](../../doc/models/order-service-charge-treatment-type.md) | Optional | Indicates whether the service charge will be treated as a value-holding line item or<br>apportioned toward a line item. |
| `scope` | [`str (Order Service Charge Scope)`](../../doc/models/order-service-charge-scope.md) | Optional | Indicates whether this is a line-item or order-level apportioned<br>service charge. |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "source_service_charge_uid": "source_service_charge_uid6",
  "name": "name0",
  "catalog_object_id": "catalog_object_id4",
  "catalog_version": 18
}
```

