## Tender Bank Transfer Details

Represents the details of a tender with `type` `BANK_TRANSFER`.

See [PaymentBankTransferDetails](#type-paymentbanktransferdetails) for more exposed details of a bank transfer payment.

### Structure

`TenderBankTransferDetails`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`str (Tender Bank Transfer Details Status)`](/doc/models/tender-bank-transfer-details-status.md) | Optional | Indicates the bank transfer's current status. |

### Example (as JSON)

```json
{
  "status": "FAILED"
}
```

