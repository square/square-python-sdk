
# Create Checkout Request

Defines the parameters that can be included in the body of
a request to the `CreateCheckout` endpoint.

## Structure

`Create Checkout Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Required | A unique string that identifies this checkout among others you have created. It can be<br>any valid string but must be unique for every order sent to Square Checkout for a given location ID.<br><br>The idempotency key is used to avoid processing the same order more than once. If you are<br>unsure whether a particular checkout was created successfully, you can attempt it again with<br>the same idempotency key and all the same other parameters without worrying about creating duplicates.<br><br>You should use a random number/string generator native to the language<br>you are working in to generate strings for your idempotency keys.<br><br>For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `192` |
| `order` | [`Create Order Request`](../../doc/models/create-order-request.md) | Required | - |
| `ask_for_shipping_address` | `bool` | Optional | If `true`, Square Checkout collects shipping information on your behalf and stores<br>that information with the transaction information in the Square Seller Dashboard.<br><br>Default: `false`. |
| `merchant_support_email` | `str` | Optional | The email address to display on the Square Checkout confirmation page<br>and confirmation email that the buyer can use to contact the seller.<br><br>If this value is not set, the confirmation page and email display the<br>primary email address associated with the seller's Square account.<br><br>Default: none; only exists if explicitly set.<br>**Constraints**: *Maximum Length*: `254` |
| `pre_populate_buyer_email` | `str` | Optional | If provided, the buyer's email is prepopulated on the checkout page<br>as an editable text field.<br><br>Default: none; only exists if explicitly set.<br>**Constraints**: *Maximum Length*: `254` |
| `pre_populate_shipping_address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |
| `redirect_url` | `str` | Optional | The URL to redirect to after the checkout is completed with `checkoutId`,<br>`transactionId`, and `referenceId` appended as URL parameters. For example,<br>if the provided redirect URL is `http://www.example.com/order-complete`, a<br>successful transaction redirects the customer to:<br><br>`http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx`<br><br>If you do not provide a redirect URL, Square Checkout displays an order<br>confirmation page on your behalf; however, it is strongly recommended that<br>you provide a redirect URL so you can verify the transaction results and<br>finalize the order through your existing/normal confirmation workflow.<br><br>Default: none; only exists if explicitly set.<br>**Constraints**: *Maximum Length*: `800` |
| `additional_recipients` | [`List Charge Request Additional Recipient`](../../doc/models/charge-request-additional-recipient.md) | Optional | The basic primitive of a multi-party transaction. The value is optional.<br>The transaction facilitated by you can be split from here.<br><br>If you provide this value, the `amount_money` value in your `additional_recipients` field<br>cannot be more than 90% of the `total_money` calculated by Square for your order.<br>The `location_id` must be a valid seller location where the checkout is occurring.<br><br>This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.<br><br>This field is currently not supported in the Square Sandbox. |
| `note` | `str` | Optional | An optional note to associate with the `checkout` object.<br><br>This value cannot exceed 60 characters.<br>**Constraints**: *Maximum Length*: `60` |

## Example (as JSON)

```json
{
  "additional_recipients": [
    {
      "amount_money": {
        "amount": 60,
        "currency": "USD"
      },
      "description": "Application fees",
      "location_id": "057P5VYJ4A5X1"
    }
  ],
  "ask_for_shipping_address": true,
  "idempotency_key": "86ae1696-b1e3-4328-af6d-f1e04d947ad6",
  "merchant_support_email": "merchant+support@website.com",
  "order": {
    "idempotency_key": "12ae1696-z1e3-4328-af6d-f1e04d947gd4",
    "order": {
      "customer_id": "customer_id",
      "discounts": [
        {
          "amount_money": {
            "amount": 100,
            "currency": "USD"
          },
          "scope": "LINE_ITEM",
          "type": "FIXED_AMOUNT",
          "uid": "56ae1696-z1e3-9328-af6d-f1e04d947gd4"
        }
      ],
      "line_items": [
        {
          "applied_discounts": [
            {
              "discount_uid": "56ae1696-z1e3-9328-af6d-f1e04d947gd4"
            }
          ],
          "applied_taxes": [
            {
              "tax_uid": "38ze1696-z1e3-5628-af6d-f1e04d947fg3"
            }
          ],
          "base_price_money": {
            "amount": 1500,
            "currency": "USD"
          },
          "name": "Printed T Shirt",
          "quantity": "2",
          "uid": "uid8",
          "quantity_unit": {
            "measurement_unit": {
              "custom_unit": {
                "name": "name2",
                "abbreviation": "abbreviation4"
              },
              "area_unit": "IMPERIAL_ACRE",
              "length_unit": "IMPERIAL_INCH",
              "volume_unit": "METRIC_LITER",
              "weight_unit": "IMPERIAL_WEIGHT_OUNCE"
            },
            "precision": 54,
            "catalog_object_id": "catalog_object_id0",
            "catalog_version": 12
          },
          "note": "note4",
          "catalog_object_id": "catalog_object_id2"
        },
        {
          "base_price_money": {
            "amount": 2500,
            "currency": "USD"
          },
          "name": "Slim Jeans",
          "quantity": "1",
          "uid": "uid8",
          "quantity_unit": {
            "measurement_unit": {
              "custom_unit": {
                "name": "name2",
                "abbreviation": "abbreviation4"
              },
              "area_unit": "IMPERIAL_ACRE",
              "length_unit": "IMPERIAL_INCH",
              "volume_unit": "METRIC_LITER",
              "weight_unit": "IMPERIAL_WEIGHT_OUNCE"
            },
            "precision": 54,
            "catalog_object_id": "catalog_object_id0",
            "catalog_version": 12
          },
          "note": "note4",
          "catalog_object_id": "catalog_object_id2"
        },
        {
          "base_price_money": {
            "amount": 3500,
            "currency": "USD"
          },
          "name": "Woven Sweater",
          "quantity": "3",
          "uid": "uid8",
          "quantity_unit": {
            "measurement_unit": {
              "custom_unit": {
                "name": "name2",
                "abbreviation": "abbreviation4"
              },
              "area_unit": "IMPERIAL_ACRE",
              "length_unit": "IMPERIAL_INCH",
              "volume_unit": "METRIC_LITER",
              "weight_unit": "IMPERIAL_WEIGHT_OUNCE"
            },
            "precision": 54,
            "catalog_object_id": "catalog_object_id0",
            "catalog_version": 12
          },
          "note": "note4",
          "catalog_object_id": "catalog_object_id2"
        }
      ],
      "location_id": "location_id",
      "reference_id": "reference_id",
      "taxes": [
        {
          "percentage": "7.75",
          "scope": "LINE_ITEM",
          "type": "INCLUSIVE",
          "uid": "38ze1696-z1e3-5628-af6d-f1e04d947fg3"
        }
      ],
      "id": "id6",
      "source": {
        "name": "name4"
      }
    }
  },
  "pre_populate_buyer_email": "example@email.com",
  "pre_populate_shipping_address": {
    "address_line_1": "1455 Market St.",
    "address_line_2": "Suite 600",
    "administrative_district_level_1": "CA",
    "country": "US",
    "first_name": "Jane",
    "last_name": "Doe",
    "locality": "San Francisco",
    "postal_code": "94103",
    "address_line_3": "address_line_32",
    "sublocality": "sublocality6"
  },
  "redirect_url": "https://merchant.website.com/order-confirm"
}
```

