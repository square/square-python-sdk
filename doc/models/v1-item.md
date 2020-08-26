## V1 Item

V1Item

### Structure

`V1Item`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The item's ID. Must be unique among all entity IDs ever provided on behalf of the merchant. You can never reuse an ID. This value can include alphanumeric characters, dashes (-), and underscores (_). |
| `name` | `string` | Optional | The item's name. |
| `description` | `string` | Optional | The item's description. |
| `type` | [`str (V1 Item Type)`](/doc/models/v1-item-type.md) | Optional | - |
| `color` | [`str (V1 Item Color)`](/doc/models/v1-item-color.md) | Optional | - |
| `abbreviation` | `string` | Optional | The text of the item's display label in Square Point of Sale. Only up to the first five characters of the string are used. |
| `visibility` | [`str (V1 Item Visibility)`](/doc/models/v1-item-visibility.md) | Optional | - |
| `available_online` | `bool` | Optional | If true, the item can be added to shipping orders from the merchant's online store. |
| `master_image` | [`V1 Item Image`](/doc/models/v1-item-image.md) | Optional | V1ItemImage |
| `category` | [`V1 Category`](/doc/models/v1-category.md) | Optional | V1Category |
| `variations` | [`List of V1 Variation`](/doc/models/v1-variation.md) | Optional | The item's variations. You must specify at least one variation. |
| `modifier_lists` | [`List of V1 Modifier List`](/doc/models/v1-modifier-list.md) | Optional | The modifier lists that apply to the item, if any. |
| `fees` | [`List of V1 Fee`](/doc/models/v1-fee.md) | Optional | The fees that apply to the item, if any. |
| `taxable` | `bool` | Optional | Deprecated. This field is not used. |
| `category_id` | `string` | Optional | The ID of the item's category, if any. |
| `available_for_pickup` | `bool` | Optional | If true, the item can be added to pickup orders from the merchant's online store. Default value: false |
| `v2_id` | `string` | Optional | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. |

### Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "description": "description0",
  "type": "OTHER",
  "color": "0b8000"
}
```

