
# Search Orders Customer Filter

A filter based on the order `customer_id` and any tender `customer_id`
associated with the order. It does not filter based on the
[FulfillmentRecipient](../../doc/models/order-fulfillment-recipient.md) `customer_id`.

## Structure

`Search Orders Customer Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_ids` | `List of string` | Optional | A list of customer IDs to filter by.<br><br>Max: 10 customer IDs. |

## Example (as JSON)

```json
{
  "customer_ids": null
}
```

