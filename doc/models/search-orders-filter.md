## Search Orders Filter

Filter options to use for a query. Multiple filters will be ANDed together.

### Structure

`SearchOrdersFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state_filter` | [`Search Orders State Filter`](/doc/models/search-orders-state-filter.md) | Optional | Filter by current Order `state`. |
| `date_time_filter` | [`Search Orders Date Time Filter`](/doc/models/search-orders-date-time-filter.md) | Optional | Filter for `Order` objects based on whether their `CREATED_AT`,<br>`CLOSED_AT` or `UPDATED_AT` timestamps fall within a specified time range.<br>You can specify the time range and which timestamp to filter for. You can filter<br>for only one time range at a time.<br><br>For each time range, the start time and end time are inclusive. If the end time<br>is absent, it defaults to the time of the first request for the cursor.<br><br>__Important:__ If you use the DateTimeFilter to filter for `CLOSED_AT` or `UPDATED_AT`,<br>you must also set the [OrdersSort](./models/orders-sort.md).<br>The TimeRange used in DateTimeFilter must correspond to the `sort_field` in<br>the [OrdersSort](./models/orders-sort.md) object. |
| `fulfillment_filter` | [`Search Orders Fulfillment Filter`](/doc/models/search-orders-fulfillment-filter.md) | Optional | Filter based on [Order Fulfillment](#type-orderfulfillment) information. |
| `source_filter` | [`Search Orders Source Filter`](/doc/models/search-orders-source-filter.md) | Optional | Filter based on Order `source` information. |
| `customer_filter` | [`Search Orders Customer Filter`](/doc/models/search-orders-customer-filter.md) | Optional | Filter based on Order `customer_id` and any Tender `customer_id`<br>associated with the Order. Does not filter based on the<br>[FulfillmentRecipient](./models/fulfillment-recipient.md) `customer_id`. |

### Example (as JSON)

```json
{
  "state_filter": null,
  "date_time_filter": null,
  "fulfillment_filter": null,
  "source_filter": null,
  "customer_filter": null
}
```

