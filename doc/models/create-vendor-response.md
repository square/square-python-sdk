
# Create Vendor Response

Represents an output from a call to [CreateVendor](../../doc/api/vendors.md#create-vendor).

## Structure

`Create Vendor Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Errors encountered when the request fails. |
| `vendor` | [`Vendor`](../../doc/models/vendor.md) | Optional | Represents a supplier to a seller. |

## Example (as JSON)

```json
{
  "errors": null,
  "vendor": null
}
```

