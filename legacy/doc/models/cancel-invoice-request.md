
# Cancel Invoice Request

Describes a `CancelInvoice` request.

## Structure

`Cancel Invoice Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `int` | Required | The version of the [invoice](entity:Invoice) to cancel.<br>If you do not know the version, you can call<br>[GetInvoice](api-endpoint:Invoices-GetInvoice) or [ListInvoices](api-endpoint:Invoices-ListInvoices). |

## Example (as JSON)

```json
{
  "version": 0
}
```

