
# Obtain Token Response

## Structure

`Obtain Token Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `string` | Optional | A valid OAuth access token. OAuth access tokens are 64 bytes long.<br>Provide the access token in a header with every request to Connect API<br>endpoints. See [OAuth API: Walkthrough](https://developer.squareup.com/docs/oauth-api/walkthrough)<br>for more information. |
| `token_type` | `string` | Optional | This value is always _bearer_. |
| `expires_at` | `string` | Optional | The date when access_token expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format. |
| `merchant_id` | `string` | Optional | The ID of the authorizing merchant's business. |
| `subscription_id` | `string` | Optional | __LEGACY FIELD__. The ID of a subscription plan the merchant signed up<br>for. Only present if the merchant signed up for a subscription during authorization. |
| `plan_id` | `string` | Optional | __LEGACY FIELD__. The ID of the subscription plan the merchant signed<br>up for. Only present if the merchant signed up for a subscription during<br>authorization. |
| `id_token` | `string` | Optional | Then OpenID token belonging to this this person. Only present if the<br>OPENID scope is included in the authorize request. |
| `refresh_token` | `string` | Optional | A refresh token. OAuth refresh tokens are 64 bytes long.<br>For more information, see [OAuth access token management](https://developer.squareup.com/docs/authz/oauth/how-it-works#oauth-access-token-management). |
| `short_lived` | `bool` | Optional | A boolean indicating the access token is a short-lived access token.<br>The short-lived access token returned in the response will expire in 24 hours. |

## Example (as JSON)

```json
{
  "access_token": "ACCESS_TOKEN",
  "expires_at": "2006-01-02T15:04:05Z",
  "merchant_id": "MERCHANT_ID",
  "refresh_token": "REFRESH_TOKEN",
  "token_type": "bearer"
}
```

