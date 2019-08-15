## Search Orders Fulfillment Filter

Filter based on [Order Fulfillment](#type-orderfulfillment) information.

### Structure

`SearchOrdersFulfillmentFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fulfillment_types` | [`List of str (Order Fulfillment Type)`](/doc/models/order-fulfillment-type.md) |  | List of [fulfillment types](./models/order-fulfillment-type.md) to filter<br>for. Will return orders if any of its fulfillments match any of the fulfillment types<br>listed in this field.<br>See [OrderFulfillmentType](#type-orderfulfillmenttype) for possible values |
| `fulfillment_states` | [`List of str (Order Fulfillment State)`](/doc/models/order-fulfillment-state.md) | Optional | List of [fulfillment states](./models/order-fulfillment-state.md) to filter<br>for. Will return orders if any of its fulfillments match any of the<br>fulfillment states listed in this field.<br>See [OrderFulfillmentState](./models/order-fulfillment-state.md) for possible values |

### Example (as JSON)

```json
{
  "fulfillment_types": [
    "SHIPMENT",
    "PICKUP"
  ],
  "fulfillment_states": null
}
```

