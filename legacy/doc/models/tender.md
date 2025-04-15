
# Tender

Represents a tender (i.e., a method of payment) used in a Square transaction.

## Structure

`Tender`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The tender's unique ID. It is the associated payment ID.<br>**Constraints**: *Maximum Length*: `192` |
| `location_id` | `str` | Optional | The ID of the transaction's associated location.<br>**Constraints**: *Maximum Length*: `50` |
| `transaction_id` | `str` | Optional | The ID of the tender's associated transaction.<br>**Constraints**: *Maximum Length*: `192` |
| `created_at` | `str` | Optional | The timestamp for when the tender was created, in RFC 3339 format.<br>**Constraints**: *Maximum Length*: `32` |
| `note` | `str` | Optional | An optional note associated with the tender at the time of payment.<br>**Constraints**: *Maximum Length*: `500` |
| `amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `tip_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `processing_fee_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `customer_id` | `str` | Optional | If the tender is associated with a customer or represents a customer's card on file,<br>this is the ID of the associated customer.<br>**Constraints**: *Maximum Length*: `191` |
| `type` | [`str (Tender Type)`](../../doc/models/tender-type.md) | Required | Indicates a tender's type. |
| `card_details` | [`Tender Card Details`](../../doc/models/tender-card-details.md) | Optional | Represents additional details of a tender with `type` `CARD` or `SQUARE_GIFT_CARD` |
| `cash_details` | [`Tender Cash Details`](../../doc/models/tender-cash-details.md) | Optional | Represents the details of a tender with `type` `CASH`. |
| `bank_account_details` | [`Tender Bank Account Details`](../../doc/models/tender-bank-account-details.md) | Optional | Represents the details of a tender with `type` `BANK_ACCOUNT`.<br><br>See [BankAccountPaymentDetails](../../doc/models/bank-account-payment-details.md)<br>for more exposed details of a bank account payment. |
| `buy_now_pay_later_details` | [`Tender Buy Now Pay Later Details`](../../doc/models/tender-buy-now-pay-later-details.md) | Optional | Represents the details of a tender with `type` `BUY_NOW_PAY_LATER`. |
| `square_account_details` | [`Tender Square Account Details`](../../doc/models/tender-square-account-details.md) | Optional | Represents the details of a tender with `type` `SQUARE_ACCOUNT`. |
| `additional_recipients` | [`List Additional Recipient`](../../doc/models/additional-recipient.md) | Optional | Additional recipients (other than the merchant) receiving a portion of this tender.<br>For example, fees assessed on the purchase by a third party integration. |
| `payment_id` | `str` | Optional | The ID of the [Payment](entity:Payment) that corresponds to this tender.<br>This value is only present for payments created with the v2 Payments API.<br>**Constraints**: *Maximum Length*: `192` |

## Example (as JSON)

```json
{
  "id": "id8",
  "location_id": "location_id2",
  "transaction_id": "transaction_id6",
  "created_at": "created_at6",
  "note": "note4",
  "type": "SQUARE_ACCOUNT"
}
```

