## Catalog Item

An item (i.e., product family) in the Catalog object model.

### Structure

`CatalogItem`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The item's name. Searchable. This field must not be empty. This field has max length of 512 Unicode code points. |
| `description` | `string` | Optional | The item's description. Searchable. This field has max length of 4096 Unicode code points. |
| `abbreviation` | `string` | Optional | The text of the item's display label in the Square Point of Sale app. Only up to the first five characters of the string are used. Searchable.<br>This field has max length of 24 Unicode code points. |
| `label_color` | `string` | Optional | The color of the item's display label in the Square Point of Sale app. This must be a valid hex color code. |
| `available_online` | `bool` | Optional | If `true`, the item can be added to shipping orders from the merchant's online store. |
| `available_for_pickup` | `bool` | Optional | If `true`, the item can be added to pickup orders from the merchant's online store. |
| `available_electronically` | `bool` | Optional | If `true`, the item can be added to electronically fulfilled orders from the merchant's online store. |
| `category_id` | `string` | Optional | The ID of the item's category, if any. |
| `tax_ids` | `List of string` | Optional | A set of IDs indicating the taxes enabled for<br>this item. When updating an item, any taxes listed here will be added to the item.<br>Taxes may also be added to or deleted from an item using `UpdateItemTaxes`. |
| `modifier_list_info` | [`List of Catalog Item Modifier List Info`]($m/CatalogItemModifierListInfo) | Optional | A set of `CatalogItemModifierListInfo` objects<br>representing the modifier lists that apply to this item, along with the overrides and min<br>and max limits that are specific to this item. Modifier lists<br>may also be added to or deleted from an item using `UpdateItemModifierLists`. |
| `variations` | [`List of Catalog Object`]($m/CatalogObject) | Optional | A list of CatalogObjects containing the `CatalogItemVariation`s for this item. |
| `product_type` | [`str (Catalog Item Product Type)`]($m/CatalogItemProductType) | Optional | The type of a CatalogItem. Connect V2 only allows the creation of `REGULAR` or `APPOINTMENTS_SERVICE` items. |
| `skip_modifier_screen` | `bool` | Optional | If `false`, the Square Point of Sale app will present the `CatalogItem`'s<br>details screen immediately, allowing the merchant to choose `CatalogModifier`s<br>before adding the item to the cart.  This is the default behavior.<br><br>If `true`, the Square Point of Sale app will immediately add the item to the cart with the pre-selected<br>modifiers, and merchants can edit modifiers by drilling down onto the item's details.<br><br>Third-party clients are encouraged to implement similar behaviors. |
| `item_options` | [`List of Catalog Item Option for Item`]($m/CatalogItemOptionForItem) | Optional | List of item options IDs for this item. Used to manage and group item<br>variations in a specified order.<br><br>Maximum: 6 item options. |

### Example (as JSON)

```json
{
  "object": {
    "type": "ITEM",
    "id": "#Cocoa",
    "present_at_all_locations": true,
    "item_data": {
      "name": "Cocoa",
      "description": "Hot chocolate",
      "abbreviation": "Ch",
      "visibility": "PRIVATE"
    }
  }
}
```

