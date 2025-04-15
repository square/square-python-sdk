
# Payment

Represents a payment processed by the Square API.

## Structure

`Payment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A unique ID for the payment.<br>**Constraints**: *Maximum Length*: `192` |
| `created_at` | `str` | Optional | The timestamp of when the payment was created, in RFC 3339 format.<br>**Constraints**: *Maximum Length*: `32` |
| `updated_at` | `str` | Optional | The timestamp of when the payment was last updated, in RFC 3339 format.<br>**Constraints**: *Maximum Length*: `32` |
| `amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `tip_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `total_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `app_fee_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `approved_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `processing_fee` | [`List Processing Fee`](../../doc/models/processing-fee.md) | Optional | The processing fees and fee adjustments assessed by Square for this payment. |
| `refunded_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `status` | `str` | Optional | Indicates whether the payment is APPROVED, PENDING, COMPLETED, CANCELED, or FAILED.<br>**Constraints**: *Maximum Length*: `50` |
| `delay_duration` | `str` | Optional | The duration of time after the payment's creation when Square automatically applies the<br>`delay_action` to the payment. This automatic `delay_action` applies only to payments that<br>do not reach a terminal state (COMPLETED, CANCELED, or FAILED) before the `delay_duration`<br>time period.<br><br>This field is specified as a time duration, in RFC 3339 format.<br><br>Notes:<br>This feature is only supported for card payments.<br><br>Default:<br><br>- Card-present payments: "PT36H" (36 hours) from the creation time.<br>- Card-not-present payments: "P7D" (7 days) from the creation time. |
| `delay_action` | `str` | Optional | The action to be applied to the payment when the `delay_duration` has elapsed.<br><br>Current values include `CANCEL` and `COMPLETE`. |
| `delayed_until` | `str` | Optional | The read-only timestamp of when the `delay_action` is automatically applied,<br>in RFC 3339 format.<br><br>Note that this field is calculated by summing the payment's `delay_duration` and `created_at`<br>fields. The `created_at` field is generated by Square and might not exactly match the<br>time on your local machine. |
| `source_type` | `str` | Optional | The source type for this payment.<br><br>Current values include `CARD`, `BANK_ACCOUNT`, `WALLET`, `BUY_NOW_PAY_LATER`, `SQUARE_ACCOUNT`,<br>`CASH` and `EXTERNAL`. For information about these payment source types,<br>see [Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).<br>**Constraints**: *Maximum Length*: `50` |
| `card_details` | [`Card Payment Details`](../../doc/models/card-payment-details.md) | Optional | Reflects the current status of a card payment. Contains only non-confidential information. |
| `cash_details` | [`Cash Payment Details`](../../doc/models/cash-payment-details.md) | Optional | Stores details about a cash payment. Contains only non-confidential information. For more information, see<br>[Take Cash Payments](https://developer.squareup.com/docs/payments-api/take-payments/cash-payments). |
| `bank_account_details` | [`Bank Account Payment Details`](../../doc/models/bank-account-payment-details.md) | Optional | Additional details about BANK_ACCOUNT type payments. |
| `external_details` | [`External Payment Details`](../../doc/models/external-payment-details.md) | Optional | Stores details about an external payment. Contains only non-confidential information.<br>For more information, see<br>[Take External Payments](https://developer.squareup.com/docs/payments-api/take-payments/external-payments). |
| `wallet_details` | [`Digital Wallet Details`](../../doc/models/digital-wallet-details.md) | Optional | Additional details about `WALLET` type payments. Contains only non-confidential information. |
| `buy_now_pay_later_details` | [`Buy Now Pay Later Details`](../../doc/models/buy-now-pay-later-details.md) | Optional | Additional details about a Buy Now Pay Later payment type. |
| `square_account_details` | [`Square Account Details`](../../doc/models/square-account-details.md) | Optional | Additional details about Square Account payments. |
| `location_id` | `str` | Optional | The ID of the location associated with the payment.<br>**Constraints**: *Maximum Length*: `50` |
| `order_id` | `str` | Optional | The ID of the order associated with the payment.<br>**Constraints**: *Maximum Length*: `192` |
| `reference_id` | `str` | Optional | An optional ID that associates the payment with an entity in<br>another system.<br>**Constraints**: *Maximum Length*: `40` |
| `customer_id` | `str` | Optional | The ID of the customer associated with the payment. If the ID is<br>not provided in the `CreatePayment` request that was used to create the `Payment`,<br>Square may use information in the request<br>(such as the billing and shipping address, email address, and payment source)<br>to identify a matching customer profile in the Customer Directory.<br>If found, the profile ID is used. If a profile is not found, the<br>API attempts to create an<br>[instant profile](https://developer.squareup.com/docs/customers-api/what-it-does#instant-profiles).<br>If the API cannot create an<br>instant profile (either because the seller has disabled it or the<br>seller's region prevents creating it), this field remains unset. Note that<br>this process is asynchronous and it may take some time before a<br>customer ID is added to the payment.<br>**Constraints**: *Maximum Length*: `191` |
| `employee_id` | `str` | Optional | __Deprecated__: Use `Payment.team_member_id` instead.<br><br>An optional ID of the employee associated with taking the payment.<br>**Constraints**: *Maximum Length*: `192` |
| `team_member_id` | `str` | Optional | An optional ID of the [TeamMember](entity:TeamMember) associated with taking the payment.<br>**Constraints**: *Maximum Length*: `192` |
| `refund_ids` | `List[str]` | Optional | A list of `refund_id`s identifying refunds for the payment. |
| `risk_evaluation` | [`Risk Evaluation`](../../doc/models/risk-evaluation.md) | Optional | Represents fraud risk information for the associated payment.<br><br>When you take a payment through Square's Payments API (using the `CreatePayment`<br>endpoint), Square evaluates it and assigns a risk level to the payment. Sellers<br>can use this information to determine the course of action (for example,<br>provide the goods/services or refund the payment). |
| `terminal_checkout_id` | `str` | Optional | An optional ID for a Terminal checkout that is associated with the payment. |
| `buyer_email_address` | `str` | Optional | The buyer's email address.<br>**Constraints**: *Maximum Length*: `255` |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |
| `shipping_address` | [`Address`](../../doc/models/address.md) | Optional | Represents a postal address in a country.<br>For more information, see [Working with Addresses](https://developer.squareup.com/docs/build-basics/working-with-addresses). |
| `note` | `str` | Optional | An optional note to include when creating a payment.<br>**Constraints**: *Maximum Length*: `500` |
| `statement_description_identifier` | `str` | Optional | Additional payment information that gets added to the customer's card statement<br>as part of the statement description.<br><br>Note that the `statement_description_identifier` might get truncated on the statement description<br>to fit the required information including the Square identifier (SQ *) and the name of the<br>seller taking the payment. |
| `capabilities` | `List[str]` | Optional | Actions that can be performed on this payment:<br><br>- `EDIT_AMOUNT_UP` - The payment amount can be edited up.<br>- `EDIT_AMOUNT_DOWN` - The payment amount can be edited down.<br>- `EDIT_TIP_AMOUNT_UP` - The tip amount can be edited up.<br>- `EDIT_TIP_AMOUNT_DOWN` - The tip amount can be edited down.<br>- `EDIT_DELAY_ACTION` - The delay_action can be edited. |
| `receipt_number` | `str` | Optional | The payment's receipt number.<br>The field is missing if a payment is canceled.<br>**Constraints**: *Maximum Length*: `4` |
| `receipt_url` | `str` | Optional | The URL for the payment's receipt.<br>The field is only populated for COMPLETED payments.<br>**Constraints**: *Maximum Length*: `255` |
| `device_details` | [`Device Details`](../../doc/models/device-details.md) | Optional | Details about the device that took the payment. |
| `application_details` | [`Application Details`](../../doc/models/application-details.md) | Optional | Details about the application that took the payment. |
| `is_offline_payment` | `bool` | Optional | Whether or not this payment was taken offline. |
| `offline_payment_details` | [`Offline Payment Details`](../../doc/models/offline-payment-details.md) | Optional | Details specific to offline payments. |
| `version_token` | `str` | Optional | Used for optimistic concurrency. This opaque token identifies a specific version of the<br>`Payment` object. |

## Example (as JSON)

```json
{
  "id": "id8",
  "created_at": "created_at6",
  "updated_at": "updated_at4",
  "amount_money": {
    "amount": 186,
    "currency": "AUD"
  },
  "tip_money": {
    "amount": 190,
    "currency": "TWD"
  }
}
```

