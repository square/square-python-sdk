
# Customer Tax Ids

Represents the tax ID associated with a [customer profile](../../doc/models/customer.md). The corresponding `tax_ids` field is available only for customers of sellers in EU countries or the United Kingdom.
For more information, see [Customer tax IDs](https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids).

## Structure

`Customer Tax Ids`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `eu_vat` | `str` | Optional | The EU VAT identification number for the customer. For example, `IE3426675K`. The ID can contain alphanumeric characters only.<br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "eu_vat": "eu_vat6"
}
```

