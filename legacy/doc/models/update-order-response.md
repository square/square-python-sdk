
# Update Order Response

Defines the fields that are included in the response body of
a request to the [UpdateOrder](../../doc/api/orders.md#update-order) endpoint.

## Structure

`Update Order Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`Order`](../../doc/models/order.md) | Optional | Contains all information related to a single order to process with Square,<br>including line items that specify the products to purchase. `Order` objects also<br>include information about any associated tenders, refunds, and returns.<br><br>All Connect V2 Transactions have all been converted to Orders including all associated<br>itemization data. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "order": {
    "created_at": "2019-08-23T18:26:18.243Z",
    "id": "DREk7wJcyXNHqULq8JJ2iPAsluJZY",
    "line_items": [
      {
        "base_price_money": {
          "amount": 500,
          "currency": "USD"
        },
        "gross_sales_money": {
          "amount": 500,
          "currency": "USD"
        },
        "name": "Small Coffee",
        "quantity": "1",
        "total_discount_money": {
          "amount": 0,
          "currency": "USD"
        },
        "total_money": {
          "amount": 500,
          "currency": "USD"
        },
        "total_service_charge_money": {
          "amount": 0,
          "currency": "USD"
        },
        "total_tax_money": {
          "amount": 0,
          "currency": "USD"
        },
        "uid": "EuYkakhmu3ksHIds5Hiot",
        "variation_total_price_money": {
          "amount": 500,
          "currency": "USD"
        },
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
          "amount": 200,
          "currency": "USD"
        },
        "gross_sales_money": {
          "amount": 400,
          "currency": "USD"
        },
        "name": "COOKIE",
        "quantity": "2",
        "total_discount_money": {
          "amount": 0,
          "currency": "USD"
        },
        "total_money": {
          "amount": 400,
          "currency": "USD"
        },
        "total_service_charge_money": {
          "amount": 0,
          "currency": "USD"
        },
        "total_tax_money": {
          "amount": 0,
          "currency": "USD"
        },
        "uid": "cookie_uid",
        "variation_total_price_money": {
          "amount": 400,
          "currency": "USD"
        },
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
    "location_id": "MXVQSVNDGN3C8",
    "net_amounts": {
      "discount_money": {
        "amount": 0,
        "currency": "USD"
      },
      "service_charge_money": {
        "amount": 0,
        "currency": "USD"
      },
      "tax_money": {
        "amount": 0,
        "currency": "USD"
      },
      "total_money": {
        "amount": 900,
        "currency": "USD"
      }
    },
    "source": {
      "name": "Cookies"
    },
    "state": "OPEN",
    "total_discount_money": {
      "amount": 0,
      "currency": "USD"
    },
    "total_money": {
      "amount": 900,
      "currency": "USD"
    },
    "total_service_charge_money": {
      "amount": 0,
      "currency": "USD"
    },
    "total_tax_money": {
      "amount": 0,
      "currency": "USD"
    },
    "updated_at": "2019-08-23T18:33:47.523Z",
    "version": 2,
    "reference_id": "reference_id4",
    "customer_id": "customer_id4"
  },
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ]
}
```

