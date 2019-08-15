## Create Order Request Discount

__Deprecated__: Please use the [OrderLineItemDiscount](./models/order-line-item-discount.md) type
in the order field of [CreateOrderRequest](./models/create-order-request.md) instead.

Represents a discount that can apply to either a single line item or an entire order.

### Structure

`CreateOrderRequestDiscount`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_id` | `string` | Optional | Only used for catalog discounts.<br>The catalog object ID for an existing [CatalogDiscount](./models/catalog-discount.md).<br><br>Do not provide a value for this field if you provide values in other fields for an ad hoc discount. |
| `name` | `string` | Optional | Only used for ad hoc discounts. The discount's name. |
| `percentage` | `string` | Optional | Only used for ad hoc discounts. The percentage of the discount, as a string representation of a decimal number.<br><br>A value of `7.25` corresponds to a percentage of 7.25%. This value range between 0.0 up to 100.0 |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "catalog_object_id": null,
  "name": null,
  "percentage": null,
  "amount_money": null
}
```

