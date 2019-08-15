## Create Order Request Modifier

__Deprecated__: Please use the [OrderLineItemModifier](./models/order-line-item-modifier.md) type
instead.

Represents a modifier applied to a single line item.

Modifiers can reference existing objects in a merchant catalog or be constructed ad hoc at the time of purchase by providing a name and price.

### Structure

`CreateOrderRequestModifier`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_id` | `string` | Optional | The catalog object ID of a [CatalogModifier](./models/catalog-modifier.md). |
| `name` | `string` | Optional | Only used for ad hoc modifiers. The name of the modifier. `name` cannot exceed 255 characters.<br><br>Do not provide a value for `name` if you provide a value for `catalog_object_id`. |
| `base_price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money.<br><br>__Important:__ Unlike version 1 of the Connect API, __all monetary amounts<br>returned by v2 endpoints are positive.__ (In v1, monetary amounts are negative<br>if they represent money being paid _by_ a merchant, instead of money being<br>paid _to_ a merchant.) |

### Example (as JSON)

```json
{
  "catalog_object_id": null,
  "name": null,
  "base_price_money": null
}
```

