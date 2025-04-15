
# Payment Link

## Structure

`Payment Link`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The Square-assigned ID of the payment link. |
| `version` | `int` | Required | The Square-assigned version number, which is incremented each time an update is committed to the payment link.<br>**Constraints**: `<= 65535` |
| `description` | `str` | Optional | The optional description of the `payment_link` object.<br>It is primarily for use by your application and is not used anywhere.<br>**Constraints**: *Maximum Length*: `4096` |
| `order_id` | `str` | Optional | The ID of the order associated with the payment link.<br>**Constraints**: *Maximum Length*: `192` |
| `checkout_options` | [`Checkout Options`](../../doc/models/checkout-options.md) | Optional | - |
| `pre_populated_data` | [`Pre Populated Data`](../../doc/models/pre-populated-data.md) | Optional | Describes buyer data to prepopulate in the payment form.<br>For more information,<br>see [Optional Checkout Configurations](https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations). |
| `url` | `str` | Optional | The shortened URL of the payment link.<br>**Constraints**: *Maximum Length*: `255` |
| `long_url` | `str` | Optional | The long URL of the payment link.<br>**Constraints**: *Maximum Length*: `255` |
| `created_at` | `str` | Optional | The timestamp when the payment link was created, in RFC 3339 format. |
| `updated_at` | `str` | Optional | The timestamp when the payment link was last updated, in RFC 3339 format. |
| `payment_note` | `str` | Optional | An optional note. After Square processes the payment, this note is added to the<br>resulting `Payment`.<br>**Constraints**: *Maximum Length*: `500` |

## Example (as JSON)

```json
{
  "id": "id2",
  "version": 64,
  "description": "description8",
  "order_id": "order_id4",
  "checkout_options": {
    "allow_tipping": false,
    "custom_fields": [
      {
        "title": "title8"
      },
      {
        "title": "title8"
      }
    ],
    "subscription_plan_id": "subscription_plan_id8",
    "redirect_url": "redirect_url2",
    "merchant_support_email": "merchant_support_email8"
  },
  "pre_populated_data": {
    "buyer_email": "buyer_email8",
    "buyer_phone_number": "buyer_phone_number0",
    "buyer_address": {
      "address_line_1": "address_line_12",
      "address_line_2": "address_line_22",
      "address_line_3": "address_line_38",
      "locality": "locality2",
      "sublocality": "sublocality2"
    }
  }
}
```

