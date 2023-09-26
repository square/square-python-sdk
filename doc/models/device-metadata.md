
# Device Metadata

## Structure

`Device Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `battery_percentage` | `str` | Optional | The Terminal’s remaining battery percentage, between 1-100. |
| `charging_state` | `str` | Optional | The current charging state of the Terminal.<br>Options: `CHARGING`, `NOT_CHARGING` |
| `location_id` | `str` | Optional | The ID of the Square seller business location associated with the Terminal. |
| `merchant_id` | `str` | Optional | The ID of the Square merchant account that is currently signed-in to the Terminal. |
| `network_connection_type` | `str` | Optional | The Terminal’s current network connection type.<br>Options: `WIFI`, `ETHERNET` |
| `payment_region` | `str` | Optional | The country in which the Terminal is authorized to take payments. |
| `serial_number` | `str` | Optional | The unique identifier assigned to the Terminal, which can be found on the lower back<br>of the device. |
| `os_version` | `str` | Optional | The current version of the Terminal’s operating system. |
| `app_version` | `str` | Optional | The current version of the application running on the Terminal. |
| `wifi_network_name` | `str` | Optional | The name of the Wi-Fi network to which the Terminal is connected. |
| `wifi_network_strength` | `str` | Optional | The signal strength of the Wi-FI network connection.<br>Options: `POOR`, `FAIR`, `GOOD`, `EXCELLENT` |
| `ip_address` | `str` | Optional | The IP address of the Terminal. |

## Example (as JSON)

```json
{
  "battery_percentage": "battery_percentage4",
  "charging_state": "charging_state6",
  "location_id": "location_id2",
  "merchant_id": "merchant_id8",
  "network_connection_type": "network_connection_type8"
}
```

