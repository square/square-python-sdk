
# ACH Details

ACH-specific details about `BANK_ACCOUNT` type payments with the `transfer_type` of `ACH`.

## Structure

`ACH Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `routing_number` | `str` | Optional | The routing number for the bank account.<br>**Constraints**: *Maximum Length*: `50` |
| `account_number_suffix` | `str` | Optional | The last few digits of the bank account number.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `4` |
| `account_type` | `str` | Optional | The type of the bank account performing the transfer. The account type can be `CHECKING`,<br>`SAVINGS`, or `UNKNOWN`.<br>**Constraints**: *Maximum Length*: `50` |

## Example (as JSON)

```json
{
  "routing_number": "routing_number6",
  "account_number_suffix": "account_number_suffix6",
  "account_type": "account_type8"
}
```

