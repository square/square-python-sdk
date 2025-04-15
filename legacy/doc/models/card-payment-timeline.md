
# Card Payment Timeline

The timeline for card payments.

## Structure

`Card Payment Timeline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorized_at` | `str` | Optional | The timestamp when the payment was authorized, in RFC 3339 format. |
| `captured_at` | `str` | Optional | The timestamp when the payment was captured, in RFC 3339 format. |
| `voided_at` | `str` | Optional | The timestamp when the payment was voided, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "authorized_at": "authorized_at2",
  "captured_at": "captured_at2",
  "voided_at": "voided_at6"
}
```

