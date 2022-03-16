
# Search Orders Fulfillment Filter

Filter based on [order fulfillment](../../doc/models/order-fulfillment.md) information.

## Structure

`Search Orders Fulfillment Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fulfillment_types` | [`List of str (Order Fulfillment Type)`](../../doc/models/order-fulfillment-type.md) | Optional | A list of [fulfillment types](../../doc/models/order-fulfillment-type.md) to filter<br>for. The list returns orders if any of its fulfillments match any of the fulfillment types<br>listed in this field.<br>See [OrderFulfillmentType](#type-orderfulfillmenttype) for possible values |
| `fulfillment_states` | [`List of str (Order Fulfillment State)`](../../doc/models/order-fulfillment-state.md) | Optional | A list of [fulfillment states](../../doc/models/order-fulfillment-state.md) to filter<br>for. The list returns orders if any of its fulfillments match any of the<br>fulfillment states listed in this field.<br>See [OrderFulfillmentState](#type-orderfulfillmentstate) for possible values |

## Example (as JSON)

```json
{
  "fulfillment_types": [
    "SHIPMENT",
    "PICKUP"
  ],
  "fulfillment_states": [
    "PROPOSED"
  ]
}
```

