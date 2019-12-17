## V1 Cash Drawer Event

V1CashDrawerEvent

### Structure

`V1CashDrawerEvent`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The event's unique ID. |
| `employee_id` | `string` | Optional | The ID of the employee that created the event. |
| `event_type` | [`str (V1 Cash Drawer Event Event Type)`]($m/V1CashDrawerEventEventType) | Optional | - |
| `event_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `created_at` | `string` | Optional | The time when the event occurred, in ISO 8601 format. |
| `description` | `string` | Optional | An optional description of the event, entered by the employee that created it. |

### Example (as JSON)

```json
{
  "id": null,
  "employee_id": null,
  "event_type": null,
  "event_money": null,
  "created_at": null,
  "description": null
}
```

