## Order Entry

A lightweight description of an [Order](./models/order.md) that is returned when `returned_entries` is true on a
[SearchOrderRequest](./models/search-order-request.md)

### Structure

`OrderEntry`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Optional | The id of the Order |
| `version` | `int` | Optional | The current version of the Order. |
| `location_id` | `string` | Optional | The location id the Order belongs to. |

### Example (as JSON)

```json
{
  "order_id": null,
  "version": null,
  "location_id": null
}
```

