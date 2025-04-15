
# Invoice Accepted Payment Methods

The payment methods that customers can use to pay an [invoice](../../doc/models/invoice.md) on the Square-hosted invoice payment page.

## Structure

`Invoice Accepted Payment Methods`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | `bool` | Optional | Indicates whether credit card or debit card payments are accepted. The default value is `false`. |
| `square_gift_card` | `bool` | Optional | Indicates whether Square gift card payments are accepted. The default value is `false`. |
| `bank_account` | `bool` | Optional | Indicates whether ACH bank transfer payments are accepted. The default value is `false`. |
| `buy_now_pay_later` | `bool` | Optional | Indicates whether Afterpay (also known as Clearpay) payments are accepted. The default value is `false`.<br><br>This option is allowed only for invoices that have a single payment request of the `BALANCE` type. This payment method is<br>supported if the seller account accepts Afterpay payments and the seller location is in a country where Afterpay<br>invoice payments are supported. As a best practice, consider enabling an additional payment method when allowing<br>`buy_now_pay_later` payments. For more information, including detailed requirements and processing limits, see<br>[Buy Now Pay Later payments with Afterpay](https://developer.squareup.com/docs/invoices-api/overview#buy-now-pay-later). |
| `cash_app_pay` | `bool` | Optional | Indicates whether Cash App payments are accepted. The default value is `false`.<br><br>This payment method is supported only for seller [locations](entity:Location) in the United States. |

## Example (as JSON)

```json
{
  "card": false,
  "square_gift_card": false,
  "bank_account": false,
  "buy_now_pay_later": false,
  "cash_app_pay": false
}
```

