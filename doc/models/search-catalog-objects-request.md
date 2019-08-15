## Search Catalog Objects Request

### Structure

`SearchCatalogObjectsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Optional | The pagination cursor returned in the previous response. Leave unset for an initial request.<br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `object_types` | [`List of str (Catalog Object Type)`](/doc/models/catalog-object-type.md) | Optional | The desired set of object types to appear in the search results. The legal values are taken from the<br>[CatalogObjectType](./models/catalog-object-type.md) enumeration, namely `"ITEM"`, `"ITEM_VARIATION"`, `"CATEGORY"`,<br>`"DISCOUNT"`, `"TAX"`, `"MODIFIER"`, or `"MODIFIER_LIST"`.<br>See [CatalogObjectType](./models/catalog-object-type.md) for possible values |
| `include_deleted_objects` | `bool` | Optional | If `true`, deleted objects will be included in the results. Deleted objects will have their<br>`is_deleted` field set to `true`. |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested object, as follows:<br><br>If a [CatalogItem](./models/catalog-item.md) is returned in the object field of the response,<br>its associated [CatalogCategory](./models/catalog-category.md), [CatalogTax](./models/catalog-tax.md)es,<br>[CatalogImage](./models/catalog-image.md)s and [CatalogModifierList](./models/catalog-modifier-list.md)s<br>will be included in the `related_objects` field of the response.<br><br>If a [CatalogItemVariation](./models/catalog-item-variation.md) is returned in the object field of the<br>response, its parent [CatalogItem](./models/catalog-item.md) will be included in the `related_objects` field of<br>the response. |
| `begin_time` | `string` | Optional | Return objects modified after this [timestamp](#workingwithdates), in RFC 3339<br>format, e.g., "2016-09-04T23:59:33.123Z". The timestamp is exclusive - objects with a<br>timestamp equal to `begin_time` will not be included in the response. |
| `query` | [`Catalog Query`](/doc/models/catalog-query.md) | Optional | A query to be applied to a [SearchCatalogObjectsRequest](./models/search-catalog-objects-request.md).<br>Only one query field may be present.<br><br>Where an attribute name is required, it should be specified as the name of any field<br>marked "searchable" from the structured data types for the desired result object type(s)<br>([CatalogItem](./models/catalog-item.md), [CatalogItemVariation](./models/catalog-item-variation.md),<br>[CatalogCategory](./models/catalog-category.md), [CatalogTax](./models/catalog-tax.md),<br>[CatalogDiscount](./models/catalog-discount.md), [CatalogModifierList](./models/catalog-modifier-list.md),<br>[CatalogModifier](./models/catalog-modifier.md)).<br><br>For example, a query that should return Items may specify attribute names from<br>any of the searchable fields of the [CatalogItem](./models/catalog-item.md) data type, namely<br>`"name"`, `"description"`, and `"abbreviation"`. |
| `limit` | `int` | Optional | A limit on the number of results to be returned in a single page. The limit is advisory -<br>the implementation may return more or fewer results. If the supplied limit is negative, zero, or<br>is higher than the maximum limit of 1,000, it will be ignored. |

### Example (as JSON)

```json
{
  "object_types": [
    "ITEM"
  ],
  "query": {
    "prefix_query": {
      "attribute_name": "name",
      "attribute_prefix": "tea"
    }
  },
  "limit": 100
}
```

