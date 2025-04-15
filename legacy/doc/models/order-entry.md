
# Order Entry

A lightweight description of an [order](../../doc/models/order.md) that is returned when
`returned_entries` is `true` on a [SearchOrdersRequest](../../doc/api/orders.md#search-orders).

## Structure

`Order Entry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | The ID of the order. |
| `version` | `int` | Optional | The version number, which is incremented each time an update is committed to the order.<br>Orders that were not created through the API do not include a version number and<br>therefore cannot be updated.<br><br>[Read more about working with versions.](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders) |
| `location_id` | `str` | Optional | The location ID the order belongs to. |

## Example (as JSON)

```json
{
  "order_id": "order_id0",
  "version": 72,
  "location_id": "location_id0"
}
```

