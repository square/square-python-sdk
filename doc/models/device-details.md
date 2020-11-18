
# Device Details

Details about the device that took the payment.

## Structure

`Device Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Optional | The Square-issued ID of the device. |
| `device_installation_id` | `string` | Optional | The Square-issued installation ID for the device. |
| `device_name` | `string` | Optional | The name of the device set by the seller. |

## Example (as JSON)

```json
{
  "device_id": "device_id6",
  "device_installation_id": "device_installation_id8",
  "device_name": "device_name2"
}
```

