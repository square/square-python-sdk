
# Register Domain Request

Defines the parameters that can be included in the body of
a request to the [RegisterDomain](../../doc/api/apple-pay.md#register-domain) endpoint.

## Structure

`Register Domain Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domain_name` | `str` | Required | A domain name as described in RFC-1034 that will be registered with ApplePay.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "domain_name": "example.com"
}
```

