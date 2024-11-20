
# Order Line Item Applied Tax

Represents an applied portion of a tax to a line item in an order.

Order-scoped taxes automatically include the applied taxes in each line item.
Line item taxes must be referenced from any applicable line items.
The corresponding applied money is automatically computed, based on the
set of participating line items.

## Structure

`Order Line Item Applied Tax`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID that identifies the applied tax only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `tax_uid` | `str` | Required | The `uid` of the tax for which this applied tax represents. It must reference<br>a tax present in the `order.taxes` field.<br><br>This field is immutable. To change which taxes apply to a line item, delete and add a new<br>`OrderLineItemAppliedTax`.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `60` |
| `applied_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

## Example (as JSON)

```json
{
  "uid": "uid8",
  "tax_uid": "tax_uid6",
  "applied_money": {
    "amount": 196,
    "currency": "AMD"
  }
}
```

