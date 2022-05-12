
# Invoice Recipient

Represents a snapshot of customer data. This object stores customer data that is displayed on the invoice
and that Square uses to deliver the invoice.

When you provide a customer ID for a draft invoice, Square retrieves the associated customer profile and populates
the remaining `InvoiceRecipient` fields. You cannot update these fields after the invoice is published.
Square updates the customer ID in response to a merge operation, but does not update other fields.

## Structure

`Invoice Recipient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Optional | The ID of the customer. This is the customer profile ID that<br>you provide when creating a draft invoice.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `given_name` | `string` | Optional | The recipient's given (that is, first) name. |
| `family_name` | `string` | Optional | The recipient's family (that is, last) name. |
| `email_address` | `string` | Optional | The recipient's email address. |
| `address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |
| `phone_number` | `string` | Optional | The recipient's phone number. |
| `company_name` | `string` | Optional | The name of the recipient's company. |
| `tax_ids` | [`Invoice Recipient Tax Ids`](../../doc/models/invoice-recipient-tax-ids.md) | Optional | Represents the tax IDs for an invoice recipient. The country of the seller account determines<br>whether the corresponding `tax_ids` field is available for the customer. For more information,<br>see [Invoice recipient tax IDs](https://developer.squareup.com/docs/invoices-api/overview#recipient-tax-ids). |

## Example (as JSON)

```json
{
  "customer_id": null,
  "given_name": null,
  "family_name": null,
  "email_address": null,
  "address": null,
  "phone_number": null,
  "company_name": null,
  "tax_ids": null
}
```

