
# Order Return Line Item Modifier

A line item modifier being returned.

## Structure

`Order Return Line Item Modifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID that identifies the return modifier only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `source_modifier_uid` | `str` | Optional | The modifier `uid` from the order's line item that contains the<br>original sale of this line item modifier.<br>**Constraints**: *Maximum Length*: `60` |
| `catalog_object_id` | `str` | Optional | The catalog object ID referencing [CatalogModifier](entity:CatalogModifier).<br>**Constraints**: *Maximum Length*: `192` |
| `catalog_version` | `long\|int` | Optional | The version of the catalog object that this line item modifier references. |
| `name` | `str` | Optional | The name of the item modifier.<br>**Constraints**: *Maximum Length*: `255` |
| `base_price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `quantity` | `str` | Optional | The quantity of the line item modifier. The modifier quantity can be 0 or more.<br>For example, suppose a restaurant offers a cheeseburger on the menu. When a buyer orders<br>this item, the restaurant records the purchase by creating an `Order` object with a line item<br>for a burger. The line item includes a line item modifier: the name is cheese and the quantity<br>is 1. The buyer has the option to order extra cheese (or no cheese). If the buyer chooses<br>the extra cheese option, the modifier quantity increases to 2. If the buyer does not want<br>any cheese, the modifier quantity is set to 0. |

## Example (as JSON)

```json
{
  "uid": "uid4",
  "source_modifier_uid": "source_modifier_uid8",
  "catalog_object_id": "catalog_object_id8",
  "catalog_version": 46,
  "name": "name4"
}
```

