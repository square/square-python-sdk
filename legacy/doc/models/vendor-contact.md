
# Vendor Contact

Represents a contact of a [Vendor](../../doc/models/vendor.md).

## Structure

`Vendor Contact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A unique Square-generated ID for the [VendorContact](entity:VendorContact).<br>This field is required when attempting to update a [VendorContact](entity:VendorContact).<br>**Constraints**: *Maximum Length*: `100` |
| `name` | `str` | Optional | The name of the [VendorContact](entity:VendorContact).<br>This field is required when attempting to create a [Vendor](entity:Vendor).<br>**Constraints**: *Maximum Length*: `255` |
| `email_address` | `str` | Optional | The email address of the [VendorContact](entity:VendorContact).<br>**Constraints**: *Maximum Length*: `255` |
| `phone_number` | `str` | Optional | The phone number of the [VendorContact](entity:VendorContact).<br>**Constraints**: *Maximum Length*: `255` |
| `removed` | `bool` | Optional | The state of the [VendorContact](entity:VendorContact). |
| `ordinal` | `int` | Required | The ordinal of the [VendorContact](entity:VendorContact). |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "email_address": "email_address8",
  "phone_number": "phone_number8",
  "removed": false,
  "ordinal": 244
}
```

