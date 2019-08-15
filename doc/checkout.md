# Checkout

```python
checkout_api = client.checkout
```

## Class Name

`CheckoutApi`

## Create Checkout

Links a `checkoutId` to a `checkout_page_url` that customers will
be directed to in order to provide their payment information using a
payment processing workflow hosted on connect.squareup.com.

```python
def create_checkout(self,
                   location_id,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the business location to associate the checkout with. |
| `body` | [`Create Checkout Request`](/doc/models/create-checkout-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Checkout Response`](/doc/models/create-checkout-response.md)

### Example Usage

```python
location_id = 'location_id4'
body = {}
body['idempotency_key'] = '86ae1696-b1e3-4328-af6d-f1e04d947ad6'
body['order'] = {}
body['order']['reference_id'] = 'reference_id'
body['order']['line_items'] = []

body['order']['line_items'].append({})
body['order']['line_items'][0]['name'] = 'Printed T Shirt'
body['order']['line_items'][0]['quantity'] = '2'
body['order']['line_items'][0]['base_price_money'] = {}
body['order']['line_items'][0]['base_price_money']['amount'] = 1500
body['order']['line_items'][0]['base_price_money']['currency'] = Currency.USD
body['order']['line_items'][0]['discounts'] = []

body['order']['line_items'][0]['discounts'].append({})
body['order']['line_items'][0]['discounts'][0]['name'] = '7% off previous season item'
body['order']['line_items'][0]['discounts'][0]['percentage'] = '7'

body['order']['line_items'][0]['discounts'].append({})
body['order']['line_items'][0]['discounts'][1]['name'] = '$3 off Customer Discount'


body['order']['line_items'].append({})
body['order']['line_items'][1]['name'] = 'Slim Jeans'
body['order']['line_items'][1]['quantity'] = '1'
body['order']['line_items'][1]['base_price_money'] = {}
body['order']['line_items'][1]['base_price_money']['amount'] = 2500
body['order']['line_items'][1]['base_price_money']['currency'] = Currency.USD

body['order']['line_items'].append({})
body['order']['line_items'][2]['name'] = 'Woven Sweater'
body['order']['line_items'][2]['quantity'] = '3'
body['order']['line_items'][2]['base_price_money'] = {}
body['order']['line_items'][2]['base_price_money']['amount'] = 3500
body['order']['line_items'][2]['base_price_money']['currency'] = Currency.USD
body['order']['line_items'][2]['taxes'] = []

body['order']['line_items'][2]['taxes'].append({})
body['order']['line_items'][2]['taxes'][0]['name'] = 'Fair Trade Tax'
body['order']['line_items'][2]['taxes'][0]['percentage'] = '5'

body['order']['line_items'][2]['discounts'] = []

body['order']['line_items'][2]['discounts'].append({})
body['order']['line_items'][2]['discounts'][0]['name'] = '$11 off Customer Discount'


body['order']['taxes'] = []

body['order']['taxes'].append({})
body['order']['taxes'][0]['name'] = 'Sales Tax'
body['order']['taxes'][0]['percentage'] = '8.5'

body['order']['discounts'] = []

body['order']['discounts'].append({})
body['order']['discounts'][0]['name'] = 'Father\'s day 12% OFF'
body['order']['discounts'][0]['percentage'] = '12'

body['order']['discounts'].append({})
body['order']['discounts'][1]['name'] = 'Global Sales $55 OFF'

body['ask_for_shipping_address'] = True
body['merchant_support_email'] = 'merchant+support@website.com'
body['pre_populate_buyer_email'] = 'example@email.com'
body['pre_populate_shipping_address'] = {}
body['pre_populate_shipping_address']['address_line_1'] = '1455 Market St.'
body['pre_populate_shipping_address']['address_line_2'] = 'Suite 600'
body['pre_populate_shipping_address']['locality'] = 'San Francisco'
body['pre_populate_shipping_address']['administrative_district_level_1'] = 'CA'
body['pre_populate_shipping_address']['postal_code'] = '94103'
body['pre_populate_shipping_address']['country'] = Country.US
body['pre_populate_shipping_address']['first_name'] = 'Jane'
body['pre_populate_shipping_address']['last_name'] = 'Doe'
body['redirect_url'] = 'https://merchant.website.com/order-confirm'
body['additional_recipients'] = []

body['additional_recipients'].append({})
body['additional_recipients'][0]['location_id'] = '057P5VYJ4A5X1'
body['additional_recipients'][0]['description'] = 'Application fees'


result = checkout_api.create_checkout(location_id, body)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

