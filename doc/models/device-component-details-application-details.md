
# Device Component Details Application Details

## Structure

`Device Component Details Application Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_type` | [`str (Application Type)`](../../doc/models/application-type.md) | Optional | - |
| `version` | `str` | Optional | The version of the application. |
| `session_location` | `str` | Optional | The location_id of the session for the application. |
| `device_code_id` | `str` | Optional | The id of the device code that was used to log in to the device. |

## Example (as JSON)

```json
{
  "application_type": "TERMINAL_API",
  "version": "version4",
  "session_location": "session_location0",
  "device_code_id": "device_code_id2"
}
```

