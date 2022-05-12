
# Update Payment Link Request

## Structure

`Update Payment Link Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_link` | [`Payment Link`](../../doc/models/payment-link.md) | Required | - |

## Example (as JSON)

```json
{
  "payment_link": {
    "checkout_options": {
      "ask_for_shipping_address": true
    },
    "version": 1
  }
}
```

