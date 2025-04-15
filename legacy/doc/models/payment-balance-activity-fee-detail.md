
# Payment Balance Activity Fee Detail

## Structure

`Payment Balance Activity Fee Detail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `str` | Optional | The ID of the payment associated with this activity<br>This will only be populated when a principal LedgerEntryToken is also populated.<br>If the fee is independent (there is no principal LedgerEntryToken) then this will likely not<br>be populated. |

## Example (as JSON)

```json
{
  "payment_id": "payment_id2"
}
```

