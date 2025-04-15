
# Order Fulfillment Recipient

Information about the fulfillment recipient.

## Structure

`Order Fulfillment Recipient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Optional | The ID of the customer associated with the fulfillment.<br>If `customer_id` is provided, the fulfillment recipient's `display_name`,<br>`email_address`, and `phone_number` are automatically populated from the<br>targeted customer profile. If these fields are set in the request, the request<br>values override the information from the customer profile. If the<br>targeted customer profile does not contain the necessary information and<br>these fields are left unset, the request results in an error.<br>**Constraints**: *Maximum Length*: `191` |
| `display_name` | `str` | Optional | The display name of the fulfillment recipient. This field is required.<br>If provided, the display name overrides the corresponding customer profile value<br>indicated by `customer_id`.<br>**Constraints**: *Maximum Length*: `255` |
| `email_address` | `str` | Optional | The email address of the fulfillment recipient.<br>If provided, the email address overrides the corresponding customer profile value<br>indicated by `customer_id`.<br>**Constraints**: *Maximum Length*: `255` |
| `phone_number` | `str` | Optional | The phone number of the fulfillment recipient. This field is required.<br>If provided, the phone number overrides the corresponding customer profile value<br>indicated by `customer_id`.<br>**Constraints**: *Maximum Length*: `17` |
| `address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |

## Example (as JSON)

```json
{
  "customer_id": "customer_id0",
  "display_name": "display_name2",
  "email_address": "email_address0",
  "phone_number": "phone_number0",
  "address": {
    "address_line_1": "address_line_16",
    "address_line_2": "address_line_26",
    "address_line_3": "address_line_32",
    "locality": "locality6",
    "sublocality": "sublocality6"
  }
}
```

