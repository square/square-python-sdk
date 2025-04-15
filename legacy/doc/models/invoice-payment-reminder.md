
# Invoice Payment Reminder

Describes a payment request reminder (automatic notification) that Square sends
to the customer. You configure a reminder relative to the payment request
`due_date`.

## Structure

`Invoice Payment Reminder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A Square-assigned ID that uniquely identifies the reminder within the<br>`InvoicePaymentRequest`. |
| `relative_scheduled_days` | `int` | Optional | The number of days before (a negative number) or after (a positive number)<br>the payment request `due_date` when the reminder is sent. For example, -3 indicates that<br>the reminder should be sent 3 days before the payment request `due_date`.<br>**Constraints**: `>= -32767`, `<= 32767` |
| `message` | `str` | Optional | The reminder message.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1000` |
| `status` | [`str (Invoice Payment Reminder Status)`](../../doc/models/invoice-payment-reminder-status.md) | Optional | The status of a payment request reminder. |
| `sent_at` | `str` | Optional | If sent, the timestamp when the reminder was sent, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "uid": "uid6",
  "relative_scheduled_days": 198,
  "message": "message4",
  "status": "SENT",
  "sent_at": "sent_at6"
}
```

