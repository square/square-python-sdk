
# Device Metadata

## Structure

`Device Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `battery_percentage` | `string` | Optional | The Terminal’s remaining battery percentage, between 1-100. |
| `charging_state` | `string` | Optional | The current charging state of the Terminal.<br>Options: `CHARGING`, `NOT_CHARGING` |
| `location_id` | `string` | Optional | The ID of the Square seller business location associated with the Terminal. |
| `merchant_id` | `string` | Optional | The ID of the Square merchant account that is currently signed-in to the Terminal. |
| `network_connection_type` | `string` | Optional | The Terminal’s current network connection type.<br>Options: `WIFI`, `ETHERNET` |
| `payment_region` | `string` | Optional | The country in which the Terminal is authorized to take payments. |
| `serial_number` | `string` | Optional | The unique identifier assigned to the Terminal, which can be found on the lower back<br>of the device. |
| `os_version` | `string` | Optional | The current version of the Terminal’s operating system. |
| `app_version` | `string` | Optional | The current version of the application running on the Terminal. |
| `wifi_network_name` | `string` | Optional | The name of the Wi-Fi network to which the Terminal is connected. |
| `wifi_network_strength` | `string` | Optional | The signal strength of the Wi-FI network connection.<br>Options: `POOR`, `FAIR`, `GOOD`, `EXCELLENT` |
| `ip_address` | `string` | Optional | The IP address of the Terminal. |

## Example (as JSON)

```json
{
  "battery_percentage": null,
  "charging_state": null,
  "location_id": null,
  "merchant_id": null,
  "network_connection_type": null,
  "payment_region": null,
  "serial_number": null,
  "os_version": null,
  "app_version": null,
  "wifi_network_name": null,
  "wifi_network_strength": null,
  "ip_address": null
}
```

