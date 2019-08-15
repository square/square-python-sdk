## Catalog Product Set

Represents a collection of catalog objects for the purpose of applying a
[PricingRule](./models/pricing-rule.md). Including a catalog object will include all of
its subtypes. For example, including a category in a product set will include
all of its items and associated item variations in the product set. Including
an item in a product set will also include its item variations.

### Structure

`CatalogProductSet`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | User-defined name for the product set. For example, "Clearance Items"<br>or "Winter Sale Items". |
| `product_ids_any` | `List of string` | Optional | Unique IDs for any [CatalogObjects](./models/catalog-objects.md)s to include in this<br>product set. Any number of these catalog objects can be in an order for a<br>pricing rule to apply.<br><br>This can be used with `product_ids_all` in a parent [CatalogProductSet](./models/catalog-product-set.md)<br>to match groups of products for a bulk discount, such as a discount for an entree and side combo.<br><br>Only one of `product_ids_all`, `product_ids_any`, or `all_products` can be set.<br><br>Max: 500 catalog object IDs. |
| `product_ids_all` | `List of string` | Optional | Unique IDs for [CatalogObjects](./models/catalog-objects.md) to include in this product set.<br>All objects in this set must be included in an order for a pricing rule to apply.<br><br>Only one of `product_ids_all`, `product_ids_any`, or `all_products` can be set.<br><br>Max: 500 catalog object IDs. |
| `quantity_exact` | `long|int` | Optional | If set, there must be exactly this many items from `products_any` or `products_all`<br>in the cart for the discount to apply.<br><br>Cannot be combined with either `quantity_min` or `quantity_max`. |
| `quantity_min` | `long|int` | Optional | If set, there must be at least this many items from `products_any` or `products_all`<br>in a cart for the discount to apply. See `quantity_exact`. Defaults to 0 if<br>`quantity_exact`, `quantity_min` and<br>`quantity_max` are all unspecified. |
| `quantity_max` | `long|int` | Optional | If set, the pricing rule will apply to a maximum of this many items from<br>`products_any` or `products_all`. |
| `all_products` | `bool` | Optional | If set to `true`, the product set will include every item in the catalog.<br><br>Only one of `product_ids_all`, `product_ids_any`, or `all_products` can be set. |

### Example (as JSON)

```json
{
  "name": null,
  "product_ids_any": null,
  "product_ids_all": null,
  "quantity_exact": null,
  "quantity_min": null,
  "quantity_max": null,
  "all_products": null
}
```

