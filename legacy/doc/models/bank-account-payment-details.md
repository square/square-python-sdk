
# Bank Account Payment Details

Additional details about BANK_ACCOUNT type payments.

## Structure

`Bank Account Payment Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_name` | `str` | Optional | The name of the bank associated with the bank account.<br>**Constraints**: *Maximum Length*: `100` |
| `transfer_type` | `str` | Optional | The type of the bank transfer. The type can be `ACH` or `UNKNOWN`.<br>**Constraints**: *Maximum Length*: `50` |
| `account_ownership_type` | `str` | Optional | The ownership type of the bank account performing the transfer.<br>The type can be `INDIVIDUAL`, `COMPANY`, or `ACCOUNT_TYPE_UNKNOWN`.<br>**Constraints**: *Maximum Length*: `50` |
| `fingerprint` | `str` | Optional | Uniquely identifies the bank account for this seller and can be used<br>to determine if payments are from the same bank account.<br>**Constraints**: *Maximum Length*: `255` |
| `country` | `str` | Optional | The two-letter ISO code representing the country the bank account is located in.<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `statement_description` | `str` | Optional | The statement description as sent to the bank.<br>**Constraints**: *Maximum Length*: `1000` |
| `ach_details` | [`ACH Details`](../../doc/models/ach-details.md) | Optional | ACH-specific details about `BANK_ACCOUNT` type payments with the `transfer_type` of `ACH`. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information about errors encountered during the request. |

## Example (as JSON)

```json
{
  "bank_name": "bank_name4",
  "transfer_type": "transfer_type8",
  "account_ownership_type": "account_ownership_type8",
  "fingerprint": "fingerprint6",
  "country": "country4"
}
```

