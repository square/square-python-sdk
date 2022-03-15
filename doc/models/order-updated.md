
# Order Updated

## Structure

`Order Updated`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Optional | The order's unique ID. |
| `version` | `int` | Optional | The version number, which is incremented each time an update is committed to the order.<br>Orders that were not created through the API do not include a version number and<br>therefore cannot be updated.<br><br>[Read more about working with versions.](../../https://developer.squareup.com/docs/orders-api/manage-orders#update-orders) |
| `location_id` | `string` | Optional | The ID of the seller location that this order is associated with. |
| `state` | [`str (Order State)`](../../doc/models/order-state.md) | Optional | The state of the order. |
| `created_at` | `string` | Optional | The timestamp for when the order was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp for when the order was last updated, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "order_id": "order_id6",
  "version": 172,
  "location_id": "location_id4",
  "state": "OPEN",
  "created_at": "created_at2"
}
```

