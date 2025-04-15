
# Cash App Details

Additional details about `WALLET` type payments with the `brand` of `CASH_APP`.

## Structure

`Cash App Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buyer_full_name` | `str` | Optional | The name of the Cash App account holder.<br>**Constraints**: *Maximum Length*: `255` |
| `buyer_country_code` | `str` | Optional | The country of the Cash App account holder, in ISO 3166-1-alpha-2 format.<br><br>For possible values, see [Country](entity:Country).<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `buyer_cashtag` | `str` | Optional | $Cashtag of the Cash App account holder.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `21` |

## Example (as JSON)

```json
{
  "buyer_full_name": "buyer_full_name0",
  "buyer_country_code": "buyer_country_code0",
  "buyer_cashtag": "buyer_cashtag2"
}
```

