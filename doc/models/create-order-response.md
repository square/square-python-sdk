## Create Order Response

Defines the fields that are included in the response body of
a request to the CreateOrder endpoint.

One of `errors` or `order` is present in a given response (never both).

### Structure

`CreateOrderResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`Order`](/doc/models/order.md) | Optional | Contains all information related to a single order to process with Square,<br>including line items that specify the products to purchase. Order objects also<br>include information on any associated tenders, refunds, and returns.<br><br>All Connect V2 Transactions have all been converted to Orders including all associated<br>itemization data. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

### Example (as JSON)

```json
{
  "order": {
    "id": "CAISENgvlJ6jLWAzERDzjyHVybY",
    "location_id": "LOCATION_ID",
    "line_items": [
      {
        "name": "New York Strip Steak",
        "quantity": "1",
        "taxes": [
          {
            "name": "State Sales Tax",
            "type": "ADDITIVE",
            "percentage": "9",
            "applied_money": {
              "amount": 136,
              "currency": "USD"
            }
          }
        ],
        "discounts": [
          {
            "catalog_object_id": "DB7L55ZH2BGWI4H23ULIWOQ7",
            "name": "Membership Discount",
            "type": "FIXED_PERCENTAGE",
            "percentage": "0.5",
            "applied_money": {
              "amount": 8,
              "currency": "USD"
            },
            "scope": "ORDER"
          },
          {
            "name": "Labor Day Sale",
            "type": "FIXED_PERCENTAGE",
            "percentage": "5",
            "applied_money": {
              "amount": 79,
              "currency": "USD"
            },
            "scope": "ORDER"
          }
        ],
        "base_price_money": {
          "amount": 1599,
          "currency": "USD"
        },
        "gross_sales_money": {
          "amount": 1599,
          "currency": "USD"
        },
        "total_tax_money": {
          "amount": 136,
          "currency": "USD"
        },
        "total_discount_money": {
          "amount": 87,
          "currency": "USD"
        },
        "total_money": {
          "amount": 1648,
          "currency": "USD"
        }
      },
      {
        "name": "New York Steak",
        "quantity": "2",
        "catalog_object_id": "BEMYCSMIJL46OCDV4KYIKXIB",
        "variation_name": "Larger",
        "modifiers": [
          {
            "catalog_object_id": "CHQX7Y4KY6N5KINJKZCFURPZ",
            "name": "Well",
            "base_price_money": {
              "amount": 50,
              "currency": "USD"
            },
            "total_price_money": {
              "amount": 100,
              "currency": "USD"
            }
          }
        ],
        "taxes": [
          {
            "name": "State Sales Tax",
            "type": "ADDITIVE",
            "percentage": "9",
            "applied_money": {
              "amount": 374,
              "currency": "USD"
            }
          }
        ],
        "discounts": [
          {
            "catalog_object_id": "DB7L55ZH2BGWI4H23ULIWOQ7",
            "name": "Membership Discount",
            "type": "FIXED_PERCENTAGE",
            "percentage": "0.5",
            "applied_money": {
              "amount": 22,
              "currency": "USD"
            },
            "scope": "ORDER"
          },
          {
            "name": "Labor Day Sale",
            "type": "FIXED_PERCENTAGE",
            "percentage": "5",
            "applied_money": {
              "amount": 224,
              "currency": "USD"
            },
            "scope": "ORDER"
          },
          {
            "name": "Sale - $1.00 off",
            "type": "FIXED_AMOUNT",
            "amount_money": {
              "amount": 100,
              "currency": "USD"
            },
            "applied_money": {
              "amount": 100,
              "currency": "USD"
            },
            "scope": "LINE_ITEM"
          }
        ],
        "base_price_money": {
          "amount": 2200,
          "currency": "USD"
        },
        "gross_sales_money": {
          "amount": 4500,
          "currency": "USD"
        },
        "total_tax_money": {
          "amount": 374,
          "currency": "USD"
        },
        "total_discount_money": {
          "amount": 346,
          "currency": "USD"
        },
        "total_money": {
          "amount": 4528,
          "currency": "USD"
        }
      }
    ],
    "taxes": [
      {
        "name": "State Sales Tax",
        "type": "ADDITIVE",
        "percentage": "9",
        "applied_money": {
          "amount": 510,
          "currency": "USD"
        },
        "scope": "ORDER"
      }
    ],
    "discounts": [
      {
        "catalog_object_id": "DB7L55ZH2BGWI4H23ULIWOQ7",
        "name": "Membership Discount",
        "type": "FIXED_PERCENTAGE",
        "percentage": "0.5",
        "applied_money": {
          "amount": 30,
          "currency": "USD"
        },
        "scope": "ORDER"
      },
      {
        "name": "Labor Day Sale",
        "type": "FIXED_PERCENTAGE",
        "percentage": "5",
        "applied_money": {
          "amount": 303,
          "currency": "USD"
        },
        "scope": "ORDER"
      },
      {
        "name": "Sale - $1.00 off",
        "type": "FIXED_AMOUNT",
        "amount_money": {
          "amount": 100,
          "currency": "USD"
        },
        "applied_money": {
          "amount": 100,
          "currency": "USD"
        },
        "scope": "LINE_ITEM"
      }
    ],
    "total_money": {
      "amount": 6176,
      "currency": "USD"
    },
    "total_tax_money": {
      "amount": 510,
      "currency": "USD"
    },
    "total_discount_money": {
      "amount": 433,
      "currency": "USD"
    }
  }
}
```

