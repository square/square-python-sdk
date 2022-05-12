
# Search Catalog Items Response

Defines the response body returned from the [SearchCatalogItems](../../doc/api/catalog.md#search-catalog-items) endpoint.

## Structure

`Search Catalog Items Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `items` | [`List of Catalog Object`](../../doc/models/catalog-object.md) | Optional | Returned items matching the specified query expressions. |
| `cursor` | `string` | Optional | Pagination token used in the next request to return more of the search result. |
| `matched_variation_ids` | `List of string` | Optional | Ids of returned item variations matching the specified query expression. |

## Example (as JSON)

```json
{
  "errors": null,
  "items": null,
  "cursor": null,
  "matched_variation_ids": null
}
```

