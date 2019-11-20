## Catalog Object

The wrapper object for object types in the Catalog data model. The type
of a particular `CatalogObject` is determined by the value of
`type` and only the corresponding data field may be set.

- if type = `ITEM`, only `item_data` will be populated and it will contain a valid `CatalogItem` object.
- if type = `ITEM_VARIATION`, only `item_variation_data` will be populated and it will contain a valid `CatalogItemVariation` object.
- if type = `MODIFIER`, only `modifier_data` will be populated and it will contain a valid `CatalogModifier` object.
- if type = `MODIFIER_LIST`, only `modifier_list_data` will be populated and it will contain a valid `CatalogModifierList` object.
- if type = `CATEGORY`, only `category_data` will be populated and it will contain a valid `CatalogCategory` object.
- if type = `DISCOUNT`, only `discount_data` will be populated and it will contain a valid `CatalogDiscount` object.
- if type = `TAX`, only `tax_data` will be populated and it will contain a valid `CatalogTax` object.
- if type = `IMAGE`, only `image_data` will be populated and it will contain a valid `CatalogImage` object.

For a more detailed discussion of the Catalog data model, please see the
[Design a Catalog](https://developer.squareup.com/docs/catalog-api/design-a-catalog) guide.

### Structure

`CatalogObject`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`str (Catalog Object Type)`](/doc/models/catalog-object-type.md) |  | Possible types of CatalogObjects returned from the Catalog, each<br>containing type-specific properties in the `*_data` field corresponding to the object type. |
| `id` | `string` |  | An identifier to reference this object in the catalog. When a new `CatalogObject`<br>is inserted, the client should set the id to a temporary identifier starting with<br>a "`#`" character. Other objects being inserted or updated within the same request<br>may use this identifier to refer to the new object.<br><br>When the server receives the new object, it will supply a unique identifier that<br>replaces the temporary identifier for all future references. |
| `updated_at` | `string` | Optional | Last modification [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) in RFC 3339 format, e.g., `"2016-08-15T23:59:33.123Z"`<br>would indicate the UTC time (denoted by `Z`) of August 15, 2016 at 23:59:33 and 123 milliseconds. |
| `version` | `long|int` | Optional | The version of the object. When updating an object, the version supplied<br>must match the version in the database, otherwise the write will be rejected as conflicting. |
| `is_deleted` | `bool` | Optional | If `true`, the object has been deleted from the database. Must be `false` for new objects<br>being inserted. When deleted, the `updated_at` field will equal the deletion time. |
| `catalog_v1_ids` | [`List of Catalog V1 Id`](/doc/models/catalog-v1-id.md) | Optional | The Connect v1 IDs for this object at each location where it is present, where they<br>differ from the object's Connect V2 ID. The field will only be present for objects that<br>have been created or modified by legacy APIs. |
| `present_at_all_locations` | `bool` | Optional | If `true`, this object is present at all locations (including future locations), except where specified in<br>the `absent_at_location_ids` field. If `false`, this object is not present at any locations (including future locations),<br>except where specified in the `present_at_location_ids` field. If not specified, defaults to `true`. |
| `present_at_location_ids` | `List of string` | Optional | A list of locations where the object is present, even if `present_at_all_locations` is `false`. |
| `absent_at_location_ids` | `List of string` | Optional | A list of locations where the object is not present, even if `present_at_all_locations` is `true`. |
| `image_id` | `string` | Optional | Identifies the `CatalogImage` attached to this `CatalogObject`. |
| `item_data` | [`Catalog Item`](/doc/models/catalog-item.md) | Optional | An item (i.e., product family) in the Catalog object model. |
| `category_data` | [`Catalog Category`](/doc/models/catalog-category.md) | Optional | A category to which a `CatalogItem` belongs in the `Catalog` object model. |
| `item_variation_data` | [`Catalog Item Variation`](/doc/models/catalog-item-variation.md) | Optional | An item variation (i.e., product) in the Catalog object model. Each item<br>may have a maximum of 250 item variations. |
| `tax_data` | [`Catalog Tax`](/doc/models/catalog-tax.md) | Optional | A tax in the Catalog object model. |
| `discount_data` | [`Catalog Discount`](/doc/models/catalog-discount.md) | Optional | A discount in the Catalog object model. |
| `modifier_list_data` | [`Catalog Modifier List`](/doc/models/catalog-modifier-list.md) | Optional | A modifier list in the Catalog object model. A `CatalogModifierList`<br>contains `CatalogModifier` objects that can be applied to a `CatalogItem` at<br>the time of sale.<br><br>For example, a modifier list "Condiments" that would apply to a "Hot Dog"<br>`CatalogItem` might contain `CatalogModifier`s "Ketchup", "Mustard", and "Relish".<br>The `selection_type` field specifies whether or not multiple selections from<br>the modifier list are allowed. |
| `modifier_data` | [`Catalog Modifier`](/doc/models/catalog-modifier.md) | Optional | A modifier in the Catalog object model. |
| `time_period_data` | [`Catalog Time Period`](/doc/models/catalog-time-period.md) | Optional | Represents a time period - either a single period or a repeating period. |
| `product_set_data` | [`Catalog Product Set`](/doc/models/catalog-product-set.md) | Optional | Represents a collection of catalog objects for the purpose of applying a<br>`PricingRule`. Including a catalog object will include all of its subtypes.<br>For example, including a category in a product set will include all of its<br>items and associated item variations in the product set. Including an item in<br>a product set will also include its item variations. |
| `pricing_rule_data` | [`Catalog Pricing Rule`](/doc/models/catalog-pricing-rule.md) | Optional | Defines how prices are modified or set for items that match the pricing rule<br>during the active time period. |
| `image_data` | [`Catalog Image`](/doc/models/catalog-image.md) | Optional | An image file to use in Square catalogs. Can be associated with catalog<br>items, item variations, and categories. |
| `measurement_unit_data` | [`Catalog Measurement Unit`](/doc/models/catalog-measurement-unit.md) | Optional | Represents the unit used to measure a `CatalogItemVariation` and<br>specifies the precision for decimal quantities. |
| `item_option_data` | [`Catalog Item Option`](/doc/models/catalog-item-option.md) | Optional | A group of variations for a `CatalogItem`. |
| `item_option_value_data` | [`Catalog Item Option Value`](/doc/models/catalog-item-option-value.md) | Optional | An enumerated value that can link a<br>`CatalogItemVariation` to an item option as one of<br>its item option values. |

### Example (as JSON)

```json
{
  "type": "ITEM_OPTION",
  "id": "id0",
  "updated_at": null,
  "version": null,
  "is_deleted": null,
  "catalog_v1_ids": null,
  "present_at_all_locations": null,
  "present_at_location_ids": null,
  "absent_at_location_ids": null,
  "image_id": null,
  "item_data": null,
  "category_data": null,
  "item_variation_data": null,
  "tax_data": null,
  "discount_data": null,
  "modifier_list_data": null,
  "modifier_data": null,
  "time_period_data": null,
  "product_set_data": null,
  "pricing_rule_data": null,
  "image_data": null,
  "measurement_unit_data": null,
  "item_option_data": null,
  "item_option_value_data": null
}
```

