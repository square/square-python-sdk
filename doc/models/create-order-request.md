## Create Order Request

### Structure

`CreateOrderRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`Order`](/doc/models/order.md) | Optional | Contains all information related to a single order to process with Square,<br>including line items that specify the products to purchase. Order objects also<br>include information on any associated tenders, refunds, and returns.<br><br>All Connect V2 Transactions have all been converted to Orders including all associated<br>itemization data. |
| `location_id` | `string` | Optional | The ID of the business location to associate the order with. |
| `idempotency_key` | `string` | Optional | A value you specify that uniquely identifies this<br>order among orders you've created.<br><br>If you're unsure whether a particular order was created successfully,<br>you can reattempt it with the same idempotency key without<br>worrying about creating duplicate orders.<br><br>See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information. |

### Example (as JSON)

```json
{
  "idempotency_key": "8193148c-9586-11e6-99f9-28cfe92138cf",
  "order": {
    "reference_id": "my-order-001",
    "location_id": "057P5VYJ4A5X1",
    "line_items": [
      {
        "name": "New York Strip Steak",
        "quantity": "1",
        "base_price_money": {
          "amount": 1599,
          "currency": "USD"
        }
      },
      {
        "quantity": "2",
        "catalog_object_id": "BEMYCSMIJL46OCDV4KYIKXIB",
        "modifiers": [
          {
            "catalog_object_id": "CHQX7Y4KY6N5KINJKZCFURPZ"
          }
        ],
        "applied_discounts": [
          {
            "discount_uid": "one-dollar-off"
          }
        ]
      }
    ],
    "taxes": [
      {
        "uid": "state-sales-tax",
        "name": "State Sales Tax",
        "percentage": "9",
        "scope": "ORDER"
      }
    ],
    "discounts": [
      {
        "uid": "labor-day-sale",
        "name": "Labor Day Sale",
        "percentage": "5",
        "scope": "ORDER"
      },
      {
        "uid": "membership-discount",
        "catalog_object_id": "DB7L55ZH2BGWI4H23ULIWOQ7",
        "scope": "ORDER"
      },
      {
        "uid": "one-dollar-off",
        "name": "Sale - $1.00 off",
        "amount_money": {
          "amount": 100,
          "currency": "USD"
        },
        "scope": "LINE_ITEM"
      }
    ]
  }
}
```

