
# Device Attributes

## Structure

`Device Attributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `str` | Required, Constant | An enum identifier of the device type.<br>**Default**: `'TERMINAL'` |
| `manufacturer` | `str` | Required | The maker of the device. |
| `model` | `str` | Optional | The specific model of the device. |
| `name` | `str` | Optional | A seller-specified name for the device. |
| `manufacturers_id` | `str` | Optional | The manufacturer-supplied identifier for the device (where available). In many cases,<br>this identifier will be a serial number. |
| `updated_at` | `str` | Optional | The RFC 3339-formatted value of the most recent update to the device information.<br>(Could represent any field update on the device.) |
| `version` | `str` | Optional | The current version of software installed on the device. |
| `merchant_token` | `str` | Optional | The merchant_token identifying the merchant controlling the device. |

## Example (as JSON)

```json
{
  "type": "TERMINAL",
  "manufacturer": "manufacturer0",
  "model": "model4",
  "name": "name6",
  "manufacturers_id": "manufacturers_id2",
  "updated_at": "updated_at2",
  "version": "version2"
}
```

