
# Pre Populated Data

Describes buyer data to prepopulate in the payment form.
For more information,
see [Optional Checkout Configurations](https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations).

## Structure

`Pre Populated Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buyer_email` | `string` | Optional | The buyer email to prepopulate in the payment form.<br>**Constraints**: *Maximum Length*: `256` |
| `buyer_phone_number` | `string` | Optional | The buyer phone number to prepopulate in the payment form.<br>**Constraints**: *Maximum Length*: `17` |
| `buyer_address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |

## Example (as JSON)

```json
{
  "buyer_email": null,
  "buyer_phone_number": null,
  "buyer_address": null
}
```

