
# V1 Tender

A tender represents a discrete monetary exchange. Square represents this
exchange as a money object with a specific currency and amount, where the
amount is given in the smallest denomination of the given currency.

Square POS can accept more than one form of tender for a single payment (such
as by splitting a bill between a credit card and a gift card). The `tender`
field of the Payment object lists all forms of tender used for the payment.

Split tender payments behave slightly differently from single tender payments:

The receipt_url for a split tender corresponds only to the first tender listed
in the tender field. To get the receipt URLs for the remaining tenders, use
the receipt_url fields of the corresponding Tender objects.

*A note on gift cards**: when a customer purchases a Square gift card from a
merchant, the merchant receives the full amount of the gift card in the
associated payment.

When that gift card is used as a tender, the balance of the gift card is
reduced and the merchant receives no funds. A `Tender` object with a type of
`SQUARE_GIFT_CARD` indicates a gift card was used for some or all of the
associated payment.

## Structure

`V1 Tender`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The tender's unique ID. |
| `type` | [`str (V1 Tender Type)`](../../doc/models/v1-tender-type.md) | Optional | - |
| `name` | `str` | Optional | A human-readable description of the tender. |
| `employee_id` | `str` | Optional | The ID of the employee that processed the tender. |
| `receipt_url` | `str` | Optional | The URL of the receipt for the tender. |
| `card_brand` | [`str (V1 Tender Card Brand)`](../../doc/models/v1-tender-card-brand.md) | Optional | The brand of a credit card. |
| `pan_suffix` | `str` | Optional | The last four digits of the provided credit card's account number. |
| `entry_method` | [`str (V1 Tender Entry Method)`](../../doc/models/v1-tender-entry-method.md) | Optional | - |
| `payment_note` | `str` | Optional | Notes entered by the merchant about the tender at the time of payment, if any. Typically only present for tender with the type: OTHER. |
| `total_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `tendered_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `tendered_at` | `str` | Optional | The time when the tender was created, in ISO 8601 format. |
| `settled_at` | `str` | Optional | The time when the tender was settled, in ISO 8601 format. |
| `change_back_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `refunded_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `is_exchange` | `bool` | Optional | Indicates whether or not the tender is associated with an exchange. If is_exchange is true, the tender represents the value of goods returned in an exchange not the actual money paid. The exchange value reduces the tender amounts needed to pay for items purchased in the exchange. |

## Example (as JSON)

```json
{
  "id": "id6",
  "type": "SQUARE_WALLET",
  "name": "name6",
  "employee_id": "employee_id4",
  "receipt_url": "receipt_url2"
}
```

