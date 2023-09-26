
# Device Code

## Structure

`Device Code`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique id for this device code. |
| `name` | `str` | Optional | An optional user-defined name for the device code.<br>**Constraints**: *Maximum Length*: `128` |
| `code` | `str` | Optional | The unique code that can be used to login. |
| `device_id` | `str` | Optional | The unique id of the device that used this code. Populated when the device is paired up. |
| `product_type` | `str` | Required, Constant | **Default**: `'TERMINAL_API'` |
| `location_id` | `str` | Optional | The location assigned to this code.<br>**Constraints**: *Maximum Length*: `50` |
| `status` | [`str (Device Code Status)`](../../doc/models/device-code-status.md) | Optional | DeviceCode.Status enum. |
| `pair_by` | `str` | Optional | When this DeviceCode will expire and no longer login. Timestamp in RFC 3339 format. |
| `created_at` | `str` | Optional | When this DeviceCode was created. Timestamp in RFC 3339 format. |
| `status_changed_at` | `str` | Optional | When this DeviceCode's status was last changed. Timestamp in RFC 3339 format. |
| `paired_at` | `str` | Optional | When this DeviceCode was paired. Timestamp in RFC 3339 format. |

## Example (as JSON)

```json
{
  "product_type": "TERMINAL_API",
  "id": "id4",
  "name": "name4",
  "code": "code2",
  "device_id": "device_id0",
  "location_id": "location_id8"
}
```

