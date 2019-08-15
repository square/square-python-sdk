## Create Mobile Authorization Code Response

Defines the fields that are included in the response body of
a request to the CreateMobileAuthorizationCode endpoint.

### Structure

`CreateMobileAuthorizationCodeResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_code` | `string` | Optional | Generated authorization code that connects a mobile application instance to a Square account. |
| `expires_at` | `string` | Optional | The timestamp when `authorization_code` expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, e.g., "2016-09-04T23:59:33.123Z". |
| `error` | [`Error`](/doc/models/error.md) | Optional | Represents an error encountered during a request to the Connect API. |

### Example (as JSON)

```json
{
  "authorization_code": "YOUR_MOBILE_AUTHZ_CODE",
  "expires_at": "2019-01-10T19:42:08Z"
}
```

