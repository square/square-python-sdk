
# Loyalty Event Order Filter

Filter events by the order associated with the event.

## Structure

`Loyalty Event Order Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Required | The ID of the [order](entity:Order) associated with the event.<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "order_id": "order_id4"
}
```

