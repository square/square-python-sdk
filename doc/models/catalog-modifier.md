## Catalog Modifier

A modifier in the Catalog object model.

### Structure

`CatalogModifier`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The modifier's name. Searchable. This field has max length of 255 Unicode code points. |
| `price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned. |

### Example (as JSON)

```json
{
  "object": {
    "type": "MODIFIER",
    "present_at_all_locations": true,
    "modifier_data": {
      "name": "Almond Milk",
      "price_money": {
        "amount": 250,
        "currency": "USD"
      }
    }
  }
}
```

