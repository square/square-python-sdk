
# Business Booking Profile

## Structure

`Business Booking Profile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `seller_id` | `string` | Optional | The ID of the seller, obtainable using the Merchants API. |
| `created_at` | `string` | Optional | The RFC-3339 timestamp specifying the booking's creation time. |
| `booking_enabled` | `bool` | Optional | Indicates whether the seller is open for booking. |
| `customer_timezone_choice` | [`str (Business Booking Profile Customer Timezone Choice)`](/doc/models/business-booking-profile-customer-timezone-choice.md) | Optional | Choices of customer-facing time zone used for bookings. |
| `booking_policy` | [`str (Business Booking Profile Booking Policy)`](/doc/models/business-booking-profile-booking-policy.md) | Optional | Policies for accepting bookings. |
| `allow_user_cancel` | `bool` | Optional | Indicates whether customers can cancel or reschedule their own bookings (`true`) or not (`false`). |
| `business_appointment_settings` | [`Business Appointment Settings`](/doc/models/business-appointment-settings.md) | Optional | The service appointment settings, including where and how the service is provided. |

## Example (as JSON)

```json
{
  "seller_id": "seller_id8",
  "created_at": "created_at2",
  "booking_enabled": false,
  "customer_timezone_choice": "BUSINESS_LOCATION_TIMEZONE",
  "booking_policy": "ACCEPT_ALL"
}
```

