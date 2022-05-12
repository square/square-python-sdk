
# Vendor Contact

Represents a contact of a [Vendor](../../doc/models/vendor.md).

## Structure

`Vendor Contact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | A unique Square-generated ID for the [VendorContact](../../doc/models/vendor-contact.md).<br>This field is required when attempting to update a [VendorContact](../../doc/models/vendor-contact.md).<br>**Constraints**: *Maximum Length*: `100` |
| `name` | `string` | Optional | The name of the [VendorContact](../../doc/models/vendor-contact.md).<br>This field is required when attempting to create a [Vendor](../../doc/models/vendor.md).<br>**Constraints**: *Maximum Length*: `255` |
| `email_address` | `string` | Optional | The email address of the [VendorContact](../../doc/models/vendor-contact.md).<br>**Constraints**: *Maximum Length*: `255` |
| `phone_number` | `string` | Optional | The phone number of the [VendorContact](../../doc/models/vendor-contact.md).<br>**Constraints**: *Maximum Length*: `255` |
| `removed` | `bool` | Optional | The state of the [VendorContact](../../doc/models/vendor-contact.md). |
| `ordinal` | `int` | Required | The ordinal of the [VendorContact](../../doc/models/vendor-contact.md). |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "email_address": null,
  "phone_number": null,
  "removed": null,
  "ordinal": 80
}
```

