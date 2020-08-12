## Search Subscriptions Filter

Represents a set of SearchSubscriptionsQuery filters used to limit the set of Subscriptions returned by SearchSubscriptions.

### Structure

`SearchSubscriptionsFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_ids` | `List of string` | Optional | A filter to select subscriptions based on the customer. |
| `location_ids` | `List of string` | Optional | A filter to select subscriptions based the location. |

### Example (as JSON)

```json
{
  "customer_ids": null,
  "location_ids": null
}
```

