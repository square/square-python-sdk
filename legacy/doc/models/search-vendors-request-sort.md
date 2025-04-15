
# Search Vendors Request Sort

Defines a sorter used to sort results from [SearchVendors](../../doc/api/vendors.md#search-vendors).

## Structure

`Search Vendors Request Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`str (Search Vendors Request Sort Field)`](../../doc/models/search-vendors-request-sort-field.md) | Optional | The field to sort the returned [Vendor](../../doc/models/vendor.md) objects by. |
| `order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "field": "NAME",
  "order": "DESC"
}
```

