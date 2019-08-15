## Catalog Query

A query to be applied to a [SearchCatalogObjectsRequest](./models/search-catalog-objects-request.md).
Only one query field may be present.

Where an attribute name is required, it should be specified as the name of any field
marked "searchable" from the structured data types for the desired result object type(s)
([CatalogItem](./models/catalog-item.md), [CatalogItemVariation](./models/catalog-item-variation.md),
[CatalogCategory](./models/catalog-category.md), [CatalogTax](./models/catalog-tax.md),
[CatalogDiscount](./models/catalog-discount.md), [CatalogModifierList](./models/catalog-modifier-list.md),
[CatalogModifier](./models/catalog-modifier.md)).

For example, a query that should return Items may specify attribute names from
any of the searchable fields of the [CatalogItem](./models/catalog-item.md) data type, namely
`"name"`, `"description"`, and `"abbreviation"`.

### Structure

`CatalogQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sorted_attribute_query` | [`Catalog Query Sorted Attribute`](/doc/models/catalog-query-sorted-attribute.md) | Optional | - |
| `exact_query` | [`Catalog Query Exact`](/doc/models/catalog-query-exact.md) | Optional | - |
| `prefix_query` | [`Catalog Query Prefix`](/doc/models/catalog-query-prefix.md) | Optional | - |
| `range_query` | [`Catalog Query Range`](/doc/models/catalog-query-range.md) | Optional | - |
| `text_query` | [`Catalog Query Text`](/doc/models/catalog-query-text.md) | Optional | - |
| `items_for_tax_query` | [`Catalog Query Items for Tax`](/doc/models/catalog-query-items-for-tax.md) | Optional | - |
| `items_for_modifier_list_query` | [`Catalog Query Items for Modifier List`](/doc/models/catalog-query-items-for-modifier-list.md) | Optional | - |
| `items_for_item_options_query` | [`Catalog Query Items for Item Options`](/doc/models/catalog-query-items-for-item-options.md) | Optional | - |
| `item_variations_for_item_option_values_query` | [`Catalog Query Item Variations for Item Option Values`](/doc/models/catalog-query-item-variations-for-item-option-values.md) | Optional | - |

### Example (as JSON)

```json
{
  "sorted_attribute_query": null,
  "exact_query": null,
  "prefix_query": null,
  "range_query": null,
  "text_query": null,
  "items_for_tax_query": null,
  "items_for_modifier_list_query": null,
  "items_for_item_options_query": null,
  "item_variations_for_item_option_values_query": null
}
```

