## Catalog Modifier List

A modifier list in the Catalog object model. A [CatalogModifierList](#type-catalogmodifierlist)
contains [Modifier](#type-catalogmodifier)s that can be applied to a [CatalogItem](#type-catalogitem)
at the time of sale.

For example, a modifier list "Condiments" that would apply to a "Hot Dog" [CatalogItem](#type-catalogitem) might
contain [CatalogModifier](#type-catalogmodifier)s "Ketchup", "Mustard", and "Relish". The
`selection_type` field specifies whether or not multiple selections from the modifier list are allowed.

### Structure

`CatalogModifierList`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The [CatalogModifierList](#type-catalogmodifierlist)'s name. Searchable. This field has max length of 255 Unicode code points. |
| `selection_type` | [`str (Catalog Modifier List Selection Type)`](/doc/models/catalog-modifier-list-selection-type.md) | Optional | Indicates whether a [CatalogModifierList](#type-catalogmodifierlist) supports multiple selections. |
| `modifiers` | [`List of Catalog Object`](/doc/models/catalog-object.md) | Optional | The options included in the [CatalogModifierList](#type-catalogmodifierlist).<br>You must include at least one [CatalogModifier](#type-catalogmodifier).<br>Each [CatalogObject](#type-catalogobject) must have type `MODIFIER` and contain<br>[CatalogModifier](#type-catalogmodifier) data. |

### Example (as JSON)

```json
{
  "type": "MODIFIER_LIST",
  "id": "#MilkType",
  "present_at_all_locations": true,
  "modifier_list_data": {
    "name": "Milk Type",
    "selection_type": "SINGLE",
    "modifiers": [
      {
        "type": "MODIFIER",
        "present_at_all_locations": true,
        "modifier_data": {
          "name": "Whole Milk",
          "price_money": {
            "amount": 0,
            "currency": "USD"
          }
        }
      },
      {
        "type": "MODIFIER",
        "present_at_all_locations": true,
        "modifier_data": {
          "name": "Almond Milk",
          "price_money": {
            "amount": 250,
            "currency": "USD"
          }
        }
      },
      {
        "type": "MODIFIER",
        "present_at_all_locations": true,
        "modifier_data": {
          "name": "Soy Milk",
          "price_money": {
            "amount": 250,
            "currency": "USD"
          }
        }
      }
    ]
  }
}
```

