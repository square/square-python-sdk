
# Order Fulfillment Updated

## Structure

`Order Fulfillment Updated`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | The order's unique ID. |
| `version` | `int` | Optional | The version number, which is incremented each time an update is committed to the order.<br>Orders that were not created through the API do not include a version number and<br>therefore cannot be updated.<br><br>[Read more about working with versions.](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders) |
| `location_id` | `str` | Optional | The ID of the seller location that this order is associated with. |
| `state` | [`str (Order State)`](../../doc/models/order-state.md) | Optional | The state of the order. |
| `created_at` | `str` | Optional | The timestamp for when the order was created, in RFC 3339 format. |
| `updated_at` | `str` | Optional | The timestamp for when the order was last updated, in RFC 3339 format. |
| `fulfillment_update` | [`List Order Fulfillment Updated Update`](../../doc/models/order-fulfillment-updated-update.md) | Optional | The fulfillments that were updated with this version change. |

## Example (as JSON)

```json
{
  "order_id": "order_id0",
  "version": 8,
  "location_id": "location_id0",
  "state": "OPEN",
  "created_at": "created_at4"
}
```

