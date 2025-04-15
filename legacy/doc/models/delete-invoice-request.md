
# Delete Invoice Request

Describes a `DeleteInvoice` request.

## Structure

`Delete Invoice Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `int` | Optional | The version of the [invoice](entity:Invoice) to delete.<br>If you do not know the version, you can call [GetInvoice](api-endpoint:Invoices-GetInvoice) or<br>[ListInvoices](api-endpoint:Invoices-ListInvoices). |

## Example (as JSON)

```json
{
  "version": 26
}
```

