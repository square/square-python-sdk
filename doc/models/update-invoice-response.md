
# Update Invoice Response

Describes a `UpdateInvoice` response.

## Structure

`Update Invoice Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Optional | Stores information about an invoice. You use the Invoices API to create and manage<br>invoices. For more information, see [Invoices API Overview](https://developer.squareup.com/docs/invoices-api/overview). |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information about errors encountered during the request. |

## Example (as JSON)

```json
{
  "invoice": {
    "accepted_payment_methods": {
      "bank_account": false,
      "buy_now_pay_later": false,
      "card": true,
      "cash_app_pay": false,
      "square_gift_card": false
    },
    "created_at": "2020-06-18T17:45:13Z",
    "custom_fields": [
      {
        "label": "Event Reference Number",
        "placement": "ABOVE_LINE_ITEMS",
        "value": "Ref. #1234"
      },
      {
        "label": "Terms of Service",
        "placement": "BELOW_LINE_ITEMS",
        "value": "The terms of service are..."
      }
    ],
    "delivery_method": "EMAIL",
    "description": "We appreciate your business!",
    "id": "inv:0-ChCHu2mZEabLeeHahQnXDjZQECY",
    "invoice_number": "inv-100",
    "location_id": "ES0RJRZYEC39A",
    "next_payment_amount_money": {
      "amount": 10000,
      "currency": "USD"
    },
    "order_id": "CAISENgvlJ6jLWAzERDzjyHVybY",
    "payment_requests": [
      {
        "automatic_payment_source": "NONE",
        "computed_amount_money": {
          "amount": 10000,
          "currency": "USD"
        },
        "due_date": "2030-01-24",
        "request_type": "BALANCE",
        "tipping_enabled": false,
        "total_completed_amount_money": {
          "amount": 0,
          "currency": "USD"
        },
        "uid": "2da7964f-f3d2-4f43-81e8-5aa220bf3355"
      }
    ],
    "primary_recipient": {
      "customer_id": "JDKYHBWT1D4F8MFH63DBMEN8Y4",
      "email_address": "Amelia.Earhart@example.com",
      "family_name": "Earhart",
      "given_name": "Amelia",
      "phone_number": "1-212-555-4240",
      "address": {
        "address_line_1": "address_line_16",
        "address_line_2": "address_line_26",
        "address_line_3": "address_line_32",
        "locality": "locality6",
        "sublocality": "sublocality6"
      }
    },
    "sale_or_service_date": "2030-01-24",
    "scheduled_at": "2030-01-13T10:00:00Z",
    "status": "UNPAID",
    "store_payment_method_enabled": false,
    "timezone": "America/Los_Angeles",
    "title": "Event Planning Services",
    "updated_at": "2020-06-18T18:23:11Z",
    "version": 2
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

