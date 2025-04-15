
# Revoke Token Request

## Structure

`Revoke Token Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | The Square-issued ID for your application, which is available on the **OAuth** page in the<br>[Developer Dashboard](https://developer.squareup.com/apps).<br>**Constraints**: *Maximum Length*: `191` |
| `access_token` | `str` | Optional | The access token of the merchant whose token you want to revoke.<br>Do not provide a value for `merchant_id` if you provide this parameter.<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `1024` |
| `merchant_id` | `str` | Optional | The ID of the merchant whose token you want to revoke.<br>Do not provide a value for `access_token` if you provide this parameter. |
| `revoke_only_access_token` | `bool` | Optional | If `true`, terminate the given single access token, but do not<br>terminate the entire authorization.<br>Default: `false` |

## Example (as JSON)

```json
{
  "access_token": "ACCESS_TOKEN",
  "client_id": "CLIENT_ID",
  "merchant_id": "merchant_id8",
  "revoke_only_access_token": false
}
```

