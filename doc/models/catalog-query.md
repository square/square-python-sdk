## Catalog Query

A query to be applied to a `SearchCatalogObjectsRequest`.
Only one query field may be present.

Where an attribute name is required, it should be specified as the name of any field
marked "searchable" from the structured data types for the desired result object type(s)
(`CatalogItem`, `CatalogItemVariation`, `CatalogCategory`, `CatalogTax`,
`CatalogDiscount`, `CatalogModifierList`, `CatalogModifier`).

For example, a query that should return Items may specify attribute names from
any of the searchable fields of the `CatalogItem` data type, namely
`"name"`, `"description"`, and `"abbreviation"`.

### Structure

`CatalogQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sorted_attribute_query` | [`Catalog Query Sorted Attribute`]($m/CatalogQuerySortedAttribute) | Optional | - |
| `exact_query` | [`Catalog Query Exact`]($m/CatalogQueryExact) | Optional | - |
| `prefix_query` | [`Catalog Query Prefix`]($m/CatalogQueryPrefix) | Optional | - |
| `range_query` | [`Catalog Query Range`]($m/CatalogQueryRange) | Optional | - |
| `text_query` | [`Catalog Query Text`]($m/CatalogQueryText) | Optional | - |
| `items_for_tax_query` | [`Catalog Query Items for Tax`]($m/CatalogQueryItemsForTax) | Optional | - |
| `items_for_modifier_list_query` | [`Catalog Query Items for Modifier List`]($m/CatalogQueryItemsForModifierList) | Optional | - |
| `items_for_item_options_query` | [`Catalog Query Items for Item Options`]($m/CatalogQueryItemsForItemOptions) | Optional | - |
| `item_variations_for_item_option_values_query` | [`Catalog Query Item Variations for Item Option Values`]($m/CatalogQueryItemVariationsForItemOptionValues) | Optional | - |

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

