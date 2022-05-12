
# Payout Entry

One or more PayoutEntries that make up a Payout. Each one has a date, amount, and type of activity.
The total amount of the payout will equal the sum of the payout entries for a batch payout

## Structure

`Payout Entry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | A unique ID for the payout entry.<br>**Constraints**: *Minimum Length*: `1` |
| `payout_id` | `string` | Required | The ID of the payout entries’ associated payout.<br>**Constraints**: *Minimum Length*: `1` |
| `effective_at` | `string` | Optional | The timestamp of when the payout entry affected the balance, in RFC 3339 format. |
| `type` | [`str (Activity Type)`](../../doc/models/activity-type.md) | Optional | - |
| `gross_amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `fee_amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `net_amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `type_automatic_savings_details` | [`Payment Balance Activity Automatic Savings Detail`](../../doc/models/payment-balance-activity-automatic-savings-detail.md) | Optional | - |
| `type_automatic_savings_reversed_details` | [`Payment Balance Activity Automatic Savings Reversed Detail`](../../doc/models/payment-balance-activity-automatic-savings-reversed-detail.md) | Optional | - |
| `type_charge_details` | [`Payment Balance Activity Charge Detail`](../../doc/models/payment-balance-activity-charge-detail.md) | Optional | DESCRIPTION OF PaymentBalanceActivityChargeDetail |
| `type_deposit_fee_details` | [`Payment Balance Activity Deposit Fee Detail`](../../doc/models/payment-balance-activity-deposit-fee-detail.md) | Optional | - |
| `type_dispute_details` | [`Payment Balance Activity Dispute Detail`](../../doc/models/payment-balance-activity-dispute-detail.md) | Optional | - |
| `type_fee_details` | [`Payment Balance Activity Fee Detail`](../../doc/models/payment-balance-activity-fee-detail.md) | Optional | - |
| `type_free_processing_details` | [`Payment Balance Activity Free Processing Detail`](../../doc/models/payment-balance-activity-free-processing-detail.md) | Optional | - |
| `type_hold_adjustment_details` | [`Payment Balance Activity Hold Adjustment Detail`](../../doc/models/payment-balance-activity-hold-adjustment-detail.md) | Optional | - |
| `type_open_dispute_details` | [`Payment Balance Activity Open Dispute Detail`](../../doc/models/payment-balance-activity-open-dispute-detail.md) | Optional | - |
| `type_other_details` | [`Payment Balance Activity Other Detail`](../../doc/models/payment-balance-activity-other-detail.md) | Optional | - |
| `type_other_adjustment_details` | [`Payment Balance Activity Other Adjustment Detail`](../../doc/models/payment-balance-activity-other-adjustment-detail.md) | Optional | - |
| `type_refund_details` | [`Payment Balance Activity Refund Detail`](../../doc/models/payment-balance-activity-refund-detail.md) | Optional | - |
| `type_release_adjustment_details` | [`Payment Balance Activity Release Adjustment Detail`](../../doc/models/payment-balance-activity-release-adjustment-detail.md) | Optional | - |
| `type_reserve_hold_details` | [`Payment Balance Activity Reserve Hold Detail`](../../doc/models/payment-balance-activity-reserve-hold-detail.md) | Optional | - |
| `type_reserve_release_details` | [`Payment Balance Activity Reserve Release Detail`](../../doc/models/payment-balance-activity-reserve-release-detail.md) | Optional | - |
| `type_square_capital_payment_details` | [`Payment Balance Activity Square Capital Payment Detail`](../../doc/models/payment-balance-activity-square-capital-payment-detail.md) | Optional | - |
| `type_square_capital_reversed_payment_details` | [`Payment Balance Activity Square Capital Reversed Payment Detail`](../../doc/models/payment-balance-activity-square-capital-reversed-payment-detail.md) | Optional | - |
| `type_tax_on_fee_details` | [`Payment Balance Activity Tax on Fee Detail`](../../doc/models/payment-balance-activity-tax-on-fee-detail.md) | Optional | - |
| `type_third_party_fee_details` | [`Payment Balance Activity Third Party Fee Detail`](../../doc/models/payment-balance-activity-third-party-fee-detail.md) | Optional | - |
| `type_third_party_fee_refund_details` | [`Payment Balance Activity Third Party Fee Refund Detail`](../../doc/models/payment-balance-activity-third-party-fee-refund-detail.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "payout_id": "payout_id6",
  "effective_at": null,
  "type": null,
  "gross_amount_money": null,
  "fee_amount_money": null,
  "net_amount_money": null,
  "type_automatic_savings_details": null,
  "type_automatic_savings_reversed_details": null,
  "type_charge_details": null,
  "type_deposit_fee_details": null,
  "type_dispute_details": null,
  "type_fee_details": null,
  "type_free_processing_details": null,
  "type_hold_adjustment_details": null,
  "type_open_dispute_details": null,
  "type_other_details": null,
  "type_other_adjustment_details": null,
  "type_refund_details": null,
  "type_release_adjustment_details": null,
  "type_reserve_hold_details": null,
  "type_reserve_release_details": null,
  "type_square_capital_payment_details": null,
  "type_square_capital_reversed_payment_details": null,
  "type_tax_on_fee_details": null,
  "type_third_party_fee_details": null,
  "type_third_party_fee_refund_details": null
}
```

