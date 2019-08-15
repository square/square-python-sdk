## Search Orders Customer Filter

Filter based on Order `customer_id` and any Tender `customer_id`
associated with the Order. Does not filter based on the
[FulfillmentRecipient](./models/fulfillment-recipient.md) `customer_id`.

### Structure

`SearchOrdersCustomerFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_ids` | `List of string` | Optional | Filter by orders with any of the listed `customer_id`s.<br><br>Max: 10 `customer_id`s. |

### Example (as JSON)

```json
{
  "customer_ids": null
}
```

