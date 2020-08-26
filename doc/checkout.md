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
body['order']['order'] = {}
body['order']['order']['id'] = 'id6'
body['order']['order']['location_id'] = 'location_id'
body['order']['order']['reference_id'] = 'reference_id'
body['order']['order']['source'] = {}
body['order']['order']['source']['name'] = 'name8'
body['order']['order']['customer_id'] = 'customer_id'
body['order']['order']['line_items'] = []

body['order']['order']['line_items'].append({})
body['order']['order']['line_items'][0]['uid'] = 'uid3'
body['order']['order']['line_items'][0]['name'] = 'Printed T Shirt'
body['order']['order']['line_items'][0]['quantity'] = '2'
body['order']['order']['line_items'][0]['quantity_unit'] = {}
body['order']['order']['line_items'][0]['quantity_unit']['measurement_unit'] = {}
body['order']['order']['line_items'][0]['quantity_unit']['measurement_unit']['area_unit'] = 'IMPERIAL_SQUARE_YARD'
body['order']['order']['line_items'][0]['quantity_unit']['measurement_unit']['length_unit'] = 'METRIC_CENTIMETER'
body['order']['order']['line_items'][0]['quantity_unit']['measurement_unit']['volume_unit'] = 'GENERIC_SHOT'
body['order']['order']['line_items'][0]['quantity_unit']['measurement_unit']['weight_unit'] = 'METRIC_MILLIGRAM'
body['order']['order']['line_items'][0]['quantity_unit']['precision'] = 191
body['order']['order']['line_items'][0]['note'] = 'note1'
body['order']['order']['line_items'][0]['catalog_object_id'] = 'catalog_object_id3'
body['order']['order']['line_items'][0]['applied_taxes'] = []

body['order']['order']['line_items'][0]['applied_taxes'].append({})
body['order']['order']['line_items'][0]['applied_taxes'][0]['uid'] = 'uid3'
body['order']['order']['line_items'][0]['applied_taxes'][0]['tax_uid'] = '38ze1696-z1e3-5628-af6d-f1e04d947fg3'
body['order']['order']['line_items'][0]['applied_taxes'][0]['applied_money'] = {}
body['order']['order']['line_items'][0]['applied_taxes'][0]['applied_money']['amount'] = 53
body['order']['order']['line_items'][0]['applied_taxes'][0]['applied_money']['currency'] = 'GBP'

body['order']['order']['line_items'][0]['applied_discounts'] = []

body['order']['order']['line_items'][0]['applied_discounts'].append({})
body['order']['order']['line_items'][0]['applied_discounts'][0]['uid'] = 'uid7'
body['order']['order']['line_items'][0]['applied_discounts'][0]['discount_uid'] = '56ae1696-z1e3-9328-af6d-f1e04d947gd4'
body['order']['order']['line_items'][0]['applied_discounts'][0]['applied_money'] = {}
body['order']['order']['line_items'][0]['applied_discounts'][0]['applied_money']['amount'] = 161
body['order']['order']['line_items'][0]['applied_discounts'][0]['applied_money']['currency'] = 'LSL'

body['order']['order']['line_items'][0]['base_price_money'] = {}
body['order']['order']['line_items'][0]['base_price_money']['amount'] = 1500
body['order']['order']['line_items'][0]['base_price_money']['currency'] = 'USD'

body['order']['order']['line_items'].append({})
body['order']['order']['line_items'][1]['uid'] = 'uid4'
body['order']['order']['line_items'][1]['name'] = 'Slim Jeans'
body['order']['order']['line_items'][1]['quantity'] = '1'
body['order']['order']['line_items'][1]['quantity_unit'] = {}
body['order']['order']['line_items'][1]['quantity_unit']['measurement_unit'] = {}
body['order']['order']['line_items'][1]['quantity_unit']['measurement_unit']['area_unit'] = 'IMPERIAL_SQUARE_MILE'
body['order']['order']['line_items'][1]['quantity_unit']['measurement_unit']['length_unit'] = 'METRIC_MILLIMETER'
body['order']['order']['line_items'][1]['quantity_unit']['measurement_unit']['volume_unit'] = 'GENERIC_CUP'
body['order']['order']['line_items'][1]['quantity_unit']['measurement_unit']['weight_unit'] = 'IMPERIAL_STONE'
body['order']['order']['line_items'][1]['quantity_unit']['precision'] = 192
body['order']['order']['line_items'][1]['note'] = 'note0'
body['order']['order']['line_items'][1]['catalog_object_id'] = 'catalog_object_id2'
body['order']['order']['line_items'][1]['base_price_money'] = {}
body['order']['order']['line_items'][1]['base_price_money']['amount'] = 2500
body['order']['order']['line_items'][1]['base_price_money']['currency'] = 'USD'

body['order']['order']['line_items'].append({})
body['order']['order']['line_items'][2]['uid'] = 'uid5'
body['order']['order']['line_items'][2]['name'] = 'Woven Sweater'
body['order']['order']['line_items'][2]['quantity'] = '3'
body['order']['order']['line_items'][2]['quantity_unit'] = {}
body['order']['order']['line_items'][2]['quantity_unit']['measurement_unit'] = {}
body['order']['order']['line_items'][2]['quantity_unit']['measurement_unit']['area_unit'] = 'METRIC_SQUARE_CENTIMETER'
body['order']['order']['line_items'][2]['quantity_unit']['measurement_unit']['length_unit'] = 'IMPERIAL_MILE'
body['order']['order']['line_items'][2]['quantity_unit']['measurement_unit']['volume_unit'] = 'GENERIC_PINT'
body['order']['order']['line_items'][2]['quantity_unit']['measurement_unit']['weight_unit'] = 'IMPERIAL_POUND'
body['order']['order']['line_items'][2]['quantity_unit']['precision'] = 193
body['order']['order']['line_items'][2]['note'] = 'note9'
body['order']['order']['line_items'][2]['catalog_object_id'] = 'catalog_object_id1'
body['order']['order']['line_items'][2]['base_price_money'] = {}
body['order']['order']['line_items'][2]['base_price_money']['amount'] = 3500
body['order']['order']['line_items'][2]['base_price_money']['currency'] = 'USD'

body['order']['order']['taxes'] = []

body['order']['order']['taxes'].append({})
body['order']['order']['taxes'][0]['uid'] = '38ze1696-z1e3-5628-af6d-f1e04d947fg3'
body['order']['order']['taxes'][0]['catalog_object_id'] = 'catalog_object_id7'
body['order']['order']['taxes'][0]['name'] = 'name9'
body['order']['order']['taxes'][0]['type'] = 'INCLUSIVE'
body['order']['order']['taxes'][0]['percentage'] = '7.75'
body['order']['order']['taxes'][0]['scope'] = 'LINE_ITEM'

body['order']['order']['discounts'] = []

body['order']['order']['discounts'].append({})
body['order']['order']['discounts'][0]['uid'] = '56ae1696-z1e3-9328-af6d-f1e04d947gd4'
body['order']['order']['discounts'][0]['catalog_object_id'] = 'catalog_object_id1'
body['order']['order']['discounts'][0]['name'] = 'name7'
body['order']['order']['discounts'][0]['type'] = 'FIXED_AMOUNT'
body['order']['order']['discounts'][0]['percentage'] = 'percentage5'
body['order']['order']['discounts'][0]['amount_money'] = {}
body['order']['order']['discounts'][0]['amount_money']['amount'] = 100
body['order']['order']['discounts'][0]['amount_money']['currency'] = 'USD'
body['order']['order']['discounts'][0]['scope'] = 'LINE_ITEM'

body['order']['location_id'] = 'location_id4'
body['order']['idempotency_key'] = '12ae1696-z1e3-4328-af6d-f1e04d947gd4'
body['ask_for_shipping_address'] = True
body['merchant_support_email'] = 'merchant+support@website.com'
body['pre_populate_buyer_email'] = 'example@email.com'
body['pre_populate_shipping_address'] = {}
body['pre_populate_shipping_address']['address_line_1'] = '1455 Market St.'
body['pre_populate_shipping_address']['address_line_2'] = 'Suite 600'
body['pre_populate_shipping_address']['address_line_3'] = 'address_line_36'
body['pre_populate_shipping_address']['locality'] = 'San Francisco'
body['pre_populate_shipping_address']['sublocality'] = 'sublocality0'
body['pre_populate_shipping_address']['administrative_district_level_1'] = 'CA'
body['pre_populate_shipping_address']['postal_code'] = '94103'
body['pre_populate_shipping_address']['country'] = 'US'
body['pre_populate_shipping_address']['first_name'] = 'Jane'
body['pre_populate_shipping_address']['last_name'] = 'Doe'
body['redirect_url'] = 'https://merchant.website.com/order-confirm'
body['additional_recipients'] = []

body['additional_recipients'].append({})
body['additional_recipients'][0]['location_id'] = '057P5VYJ4A5X1'
body['additional_recipients'][0]['description'] = 'Application fees'


result = checkout_api.create_checkout(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

