
# Obtain Token Response

## Structure

`Obtain Token Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Optional | A valid OAuth access token.<br>Provide the access token in a header with every request to Connect API<br>endpoints. For more information, see [OAuth API: Walkthrough](https://developer.squareup.com/docs/oauth-api/walkthrough).<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `1024` |
| `token_type` | `str` | Optional | This value is always _bearer_.<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `10` |
| `expires_at` | `str` | Optional | The date when the `access_token` expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format.<br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `48` |
| `merchant_id` | `str` | Optional | The ID of the authorizing merchant's business.<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `191` |
| `subscription_id` | `str` | Optional | __LEGACY FIELD__. The ID of a subscription plan the merchant signed up<br>for. The ID is only present if the merchant signed up for a subscription plan during authorization. |
| `plan_id` | `str` | Optional | __LEGACY FIELD__. The ID of the subscription plan the merchant signed<br>up for. The ID is only present if the merchant signed up for a subscription plan during<br>authorization. |
| `id_token` | `str` | Optional | The OpenID token belonging to this person. This token is only present if the<br>OPENID scope is included in the authorization request. |
| `refresh_token` | `str` | Optional | A refresh token.<br>For more information, see [Refresh, Revoke, and Limit the Scope of OAuth Tokens](https://developer.squareup.com/docs/oauth-api/refresh-revoke-limit-scope).<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `1024` |
| `short_lived` | `bool` | Optional | A Boolean indicating that the access token is a short-lived access token.<br>The short-lived access token returned in the response expires in 24 hours. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `refresh_token_expires_at` | `str` | Optional | The date when the `refresh_token` expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format.<br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `48` |

## Example (as JSON)

```json
{
  "access_token": "ACCESS_TOKEN",
  "expires_at": "2006-01-02T15:04:05Z",
  "merchant_id": "MERCHANT_ID",
  "refresh_token": "REFRESH_TOKEN",
  "token_type": "bearer",
  "subscription_id": "subscription_id8"
}
```

