
# Checkout Location Settings

## Structure

`Checkout Location Settings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | The ID of the location that these settings apply to. |
| `customer_notes_enabled` | `bool` | Optional | Indicates whether customers are allowed to leave notes at checkout. |
| `policies` | [`List Checkout Location Settings Policy`](../../doc/models/checkout-location-settings-policy.md) | Optional | Policy information is displayed at the bottom of the checkout pages.<br>You can set a maximum of two policies. |
| `branding` | [`Checkout Location Settings Branding`](../../doc/models/checkout-location-settings-branding.md) | Optional | - |
| `tipping` | [`Checkout Location Settings Tipping`](../../doc/models/checkout-location-settings-tipping.md) | Optional | - |
| `coupons` | [`Checkout Location Settings Coupons`](../../doc/models/checkout-location-settings-coupons.md) | Optional | - |
| `updated_at` | `str` | Optional | The timestamp when the settings were last updated, in RFC 3339 format.<br>Examples for January 25th, 2020 6:25:34pm Pacific Standard Time:<br>UTC: 2020-01-26T02:25:34Z<br>Pacific Standard Time with UTC offset: 2020-01-25T18:25:34-08:00 |

## Example (as JSON)

```json
{
  "location_id": "location_id4",
  "customer_notes_enabled": false,
  "policies": [
    {
      "uid": "uid8",
      "title": "title4",
      "description": "description8"
    },
    {
      "uid": "uid8",
      "title": "title4",
      "description": "description8"
    }
  ],
  "branding": {
    "header_type": "FULL_WIDTH_LOGO",
    "button_color": "button_color2",
    "button_shape": "PILL"
  },
  "tipping": {
    "percentages": [
      246,
      247
    ],
    "smart_tipping_enabled": false,
    "default_percent": 46,
    "smart_tips": [
      {
        "amount": 152,
        "currency": "GEL"
      },
      {
        "amount": 152,
        "currency": "GEL"
      }
    ],
    "default_smart_tip": {
      "amount": 58,
      "currency": "KWD"
    }
  }
}
```

