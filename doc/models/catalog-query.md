
# Catalog Query

A query composed of one or more different types of filters to narrow the scope of targeted objects when calling the `SearchCatalogObjects` endpoint.

Although a query can have multiple filters, only certain query types can be combined per call to [SearchCatalogObjects](#endpoint-Catalog-SearchCatalogObjects).
Any combination of the following types may be used together:

- [exact_query](#type-CatalogExactQuery)
- [prefix_query](#type-CatalogPrefixQuery)
- [range_query](#type-CatalogRangeQuery)
- [sorted_attribute_query](#type-CatalogSortedAttribute)
- [text_query](#type-CatalogTextQuery)
  All other query types cannot be combined with any others.

When a query filter is based on an attribute, the attribute must be searchable.
Searchable attributes are listed as follows, along their parent types that can be searched for with applicable query filters.

* Searchable attribute and objects queryable by searchable attributes **

- `name`:  `CatalogItem`, `CatalogItemVariation`, `CatelogCatogry`, `CatalogTax`, `CatalogDiscount`, `CatalogModifier`, 'CatalogModifierList`,`CatalogItemOption`,`CatalogItemOptionValue`
- `description`: `CatalogItem`, `CatalogItemOptionValue`
- `abbreviation`: `CatalogItem`
- `upc`: `CatalogItemVariation`
- `sku`: `CatalogItemVariation`
- `caption`: `CatalogImage`
- `display_name`: `CatalogItemOption`

For example, to search for [CatalogItem](#type-CatalogItem) objects by searchable attributes, you can use
the `"name"`, `"description"`, or `"abbreviation"` attribute in an applicable query filter.

## Structure

`Catalog Query`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sorted_attribute_query` | [`Catalog Query Sorted Attribute`](/doc/models/catalog-query-sorted-attribute.md) | Optional | The query expression to specify the key to sort search results. |
| `exact_query` | [`Catalog Query Exact`](/doc/models/catalog-query-exact.md) | Optional | The query filter to return the search result by exact match of the specified attribute name and value. |
| `set_query` | [`Catalog Query Set`](/doc/models/catalog-query-set.md) | Optional | The query filter to return the search result(s) by exact match of the specified `attribute_name` and any of<br>the `attribute_values`. |
| `prefix_query` | [`Catalog Query Prefix`](/doc/models/catalog-query-prefix.md) | Optional | The query filter to return the search result whose named attribute values are prefixed by the specified attribute value. |
| `range_query` | [`Catalog Query Range`](/doc/models/catalog-query-range.md) | Optional | The query filter to return the search result whose named attribute values fall between the specified range. |
| `text_query` | [`Catalog Query Text`](/doc/models/catalog-query-text.md) | Optional | The query filter to return the search result whose searchable attribute values contain all of the specified keywords or tokens, independent of the token order or case. |
| `items_for_tax_query` | [`Catalog Query Items for Tax`](/doc/models/catalog-query-items-for-tax.md) | Optional | The query filter to return the items containing the specified tax IDs. |
| `items_for_modifier_list_query` | [`Catalog Query Items for Modifier List`](/doc/models/catalog-query-items-for-modifier-list.md) | Optional | The query filter to return the items containing the specified modifier list IDs. |
| `items_for_item_options_query` | [`Catalog Query Items for Item Options`](/doc/models/catalog-query-items-for-item-options.md) | Optional | The query filter to return the items containing the specified item option IDs. |
| `item_variations_for_item_option_values_query` | [`Catalog Query Item Variations for Item Option Values`](/doc/models/catalog-query-item-variations-for-item-option-values.md) | Optional | The query filter to return the item variations containing the specified item option value IDs. |

## Example (as JSON)

```json
{
  "sorted_attribute_query": {
    "attribute_name": "attribute_name0",
    "initial_attribute_value": "initial_attribute_value8",
    "sort_order": "DESC"
  },
  "exact_query": {
    "attribute_name": "attribute_name4",
    "attribute_value": "attribute_value6"
  },
  "set_query": {
    "attribute_name": "attribute_name2",
    "attribute_values": [
      "attribute_values6"
    ]
  },
  "prefix_query": {
    "attribute_name": "attribute_name6",
    "attribute_prefix": "attribute_prefix8"
  },
  "range_query": {
    "attribute_name": "attribute_name0",
    "attribute_min_value": 208,
    "attribute_max_value": 138
  }
}
```

