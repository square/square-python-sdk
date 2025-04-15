
# Bulk Update Customer Data

Defines the customer data provided in individual update requests for a
[BulkUpdateCustomers](../../doc/api/customers.md#bulk-update-customers) operation.

## Structure

`Bulk Update Customer Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `given_name` | `str` | Optional | The given name (that is, the first name) associated with the customer profile.<br>**Constraints**: *Maximum Length*: `300` |
| `family_name` | `str` | Optional | The family name (that is, the last name) associated with the customer profile.<br>**Constraints**: *Maximum Length*: `300` |
| `company_name` | `str` | Optional | A business name associated with the customer profile.<br>**Constraints**: *Maximum Length*: `500` |
| `nickname` | `str` | Optional | A nickname for the customer profile.<br>**Constraints**: *Maximum Length*: `100` |
| `email_address` | `str` | Optional | The email address associated with the customer profile.<br>**Constraints**: *Maximum Length*: `254` |
| `address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |
| `phone_number` | `str` | Optional | The phone number associated with the customer profile. The phone number must be valid<br>and can contain 9–16 digits, with an optional `+` prefix and country code. For more information,<br>see [Customer phone numbers](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#phone-number). |
| `reference_id` | `str` | Optional | An optional second ID used to associate the customer profile with an<br>entity in another system.<br>**Constraints**: *Maximum Length*: `100` |
| `note` | `str` | Optional | An custom note associates with the customer profile. |
| `birthday` | `str` | Optional | The birthday associated with the customer profile, in `YYYY-MM-DD` or `MM-DD` format.<br>For example, specify `1998-09-21` for September 21, 1998, or `09-21` for September 21.<br>Birthdays are returned in `YYYY-MM-DD` format, where `YYYY` is the specified birth year or<br>`0000` if a birth year is not specified. |
| `tax_ids` | [`Customer Tax Ids`](../../doc/models/customer-tax-ids.md) | Optional | Represents the tax ID associated with a [customer profile](../../doc/models/customer.md). The corresponding `tax_ids` field is available only for customers of sellers in EU countries or the United Kingdom.<br>For more information, see [Customer tax IDs](https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids). |
| `version` | `long\|int` | Optional | The current version of the customer profile.<br><br>As a best practice, you should include this field to enable<br>[optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)<br>control. |

## Example (as JSON)

```json
{
  "given_name": "given_name4",
  "family_name": "family_name4",
  "company_name": "company_name8",
  "nickname": "nickname8",
  "email_address": "email_address0"
}
```

