
# Customer Details

Details about the customer making the payment.

## Structure

`Customer Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_initiated` | `bool` | Optional | Indicates whether the customer initiated the payment. |
| `seller_keyed_in` | `bool` | Optional | Indicates that the seller keyed in payment details on behalf of the customer.<br>This is used to flag a payment as Mail Order / Telephone Order (MOTO). |

## Example (as JSON)

```json
{
  "customer_initiated": false,
  "seller_keyed_in": false
}
```

