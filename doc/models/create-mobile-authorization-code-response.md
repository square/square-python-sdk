
# Create Mobile Authorization Code Response

Defines the fields that are included in the response body of
a request to the `CreateMobileAuthorizationCode` endpoint.

## Structure

`Create Mobile Authorization Code Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_code` | `string` | Optional | The generated authorization code that connects a mobile application instance<br>to a Square account.<br>**Constraints**: *Maximum Length*: `191` |
| `expires_at` | `string` | Optional | The timestamp when `authorization_code` expires, in<br>[RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, "2016-09-04T23:59:33.123Z").<br>**Constraints**: *Minimum Length*: `20`, *Maximum Length*: `48` |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "authorization_code": "YOUR_MOBILE_AUTHORIZATION_CODE",
  "expires_at": "2019-01-10T19:42:08Z",
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "REFUND_ALREADY_PENDING",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "PAYMENT_NOT_REFUNDABLE",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "REFUND_DECLINED",
      "detail": "detail3",
      "field": "field1"
    }
  ]
}
```

