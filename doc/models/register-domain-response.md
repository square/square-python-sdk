
# Register Domain Response

Defines the fields that are included in the response body of
a request to the [RegisterDomain](../../doc/api/apple-pay.md#register-domain) endpoint.

Either `errors` or `status` are present in a given response (never both).

## Structure

`Register Domain Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `status` | [`str (Register Domain Response Status)`](../../doc/models/register-domain-response-status.md) | Optional | The status of the domain registration. |

## Example (as JSON)

```json
{
  "status": "VERIFIED"
}
```

