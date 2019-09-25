## Revoke Token Request

### Structure

`RevokeTokenRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `string` | Optional | Your application's ID, available from the [application dashboard](https://connect.squareup.com/apps). |
| `access_token` | `string` | Optional | The access token of the merchant whose token you want to revoke.<br>Do not provide a value for merchant_id if you provide this parameter. |
| `merchant_id` | `string` | Optional | The ID of the merchant whose token you want to revoke.<br>Do not provide a value for access_token if you provide this parameter. |

### Example (as JSON)

```json
{
  "access_token": "ACCESS_TOKEN",
  "client_id": "CLIENT_ID"
}
```

