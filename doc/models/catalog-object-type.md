## Catalog Object Type

Possible kinds of [CatalogObject](#type-catalogobject)s returned from the Catalog, each
containing type-specific properties in the `*_data` field corresponding to the object type.

### Enumeration

`CatalogObjectType`

### Fields

| Name | Description |
|  --- | --- |
| `ITEM` | An item, corresponding to [CatalogItem](#type-catalogitem). The item-specific data<br>will be stored in the `item_data` field. |
| `IMAGE` | An image, corresponding to [CatalogImage](#type-catalogimage). The image-specific data<br>will be stored in the `image_data` field. |
| `CATEGORY` | A category, corresponding to [CatalogCategory](#type-catalogcategory). The category-specific data<br>will be stored in the `category_data` field. |
| `ITEM_VARIATION` | An item variation, corresponding to [CatalogItemVariation](#type-catalogitemvariation). The<br>item variation-specific data will be stored in the `item_variation_data` field. |
| `TAX` | A tax, corresponding to [CatalogTax](#type-catalogtax). The tax-specific data<br>will be stored in the `tax_data` field. |
| `DISCOUNT` | A discount, corresponding to [CatalogDiscount](#type-catalogdiscount). The discount-specific data<br>will be stored in the `discount_data` field. |
| `MODIFIER_LIST` | A modifier list, corresponding to [CatalogModifierList](#type-catalogmodifierlist).<br>The modifier list-specific data will be stored in the `modifier_list_data` field. |
| `MODIFIER` | A modifier, corresponding to [CatalogModifier](#type-catalogmodifier). The modifier-specific data<br>will be stored in the `modifier_data` field. |
| `PRICING_RULE` | A pricing rule, corresponding to [CatalogPricingRule](#type-catalogpricingrule). The pricing-rule-specific data<br>will be stored in the `pricing_rule_data` field. |
| `PRODUCT_SET` | A product set, corresponding to [CatalogProductSet](#type-catalogproductset).<br>The product-set-specific data will be stored in the `product_set_data` field. |
| `TIME_PERIOD` | A time period, corresponding to [CatalogTimePeriod](#type-catalogtimeperiod).<br>The time-period-specific data will be stored in the `time_period_data` field. |
| `MEASUREMENT_UNIT` | A measurement unit, corresponding to [CatalogMeasurementUnit](#type-catalogmeasurementunit). The unit of<br>measure and precision in which an item variation should be sold. |
| `ITEM_OPTION` | Represents a list of item option values that can be assigned to item<br>variations. For example, a color option or size option for a t-shirt. |
| `ITEM_OPTION_VAL` | Represents an option value associated with one or more item options.<br>For example, an item option of "Size" may have item option values such as<br>“Small" or "Medium". |

