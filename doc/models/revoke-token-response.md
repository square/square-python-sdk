
# Revoke Token Response

## Structure

`Revoke Token Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Optional | If the request is successful, this is `true`. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | An error object that provides details about how creation of the obtain<br>token failed. |

## Example (as JSON)

```json
{
  "success": true
}
```

