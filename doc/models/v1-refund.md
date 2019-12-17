## V1 Refund

V1Refund

### Structure

`V1Refund`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`str (V1 Refund Type)`]($m/V1RefundType) | Optional | - |
| `reason` | `string` | Optional | The merchant-specified reason for the refund. |
| `refunded_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_processing_fee_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_tax_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_additive_tax_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_additive_tax` | [`List of V1 Payment Tax`]($m/V1PaymentTax) | Optional | All of the additive taxes associated with the refund. |
| `refunded_inclusive_tax_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_inclusive_tax` | [`List of V1 Payment Tax`]($m/V1PaymentTax) | Optional | All of the inclusive taxes associated with the refund. |
| `refunded_tip_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_discount_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_surcharge_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `refunded_surcharges` | [`List of V1 Payment Surcharge`]($m/V1PaymentSurcharge) | Optional | A list of all surcharges associated with the refund. |
| `created_at` | `string` | Optional | The time when the merchant initiated the refund for Square to process, in ISO 8601 format. |
| `processed_at` | `string` | Optional | The time when Square processed the refund on behalf of the merchant, in ISO 8601 format. |
| `payment_id` | `string` | Optional | A Square-issued ID associated with the refund. For single-tender refunds, payment_id is the ID of the original payment ID. For split-tender refunds, payment_id is the ID of the original tender. For exchange-based refunds (is_exchange == true), payment_id is the ID of the original payment ID even if the payment includes other tenders. |
| `merchant_id` | `string` | Optional | - |
| `is_exchange` | `bool` | Optional | Indicates whether or not the refund is associated with an exchange. If is_exchange is true, the refund reflects the value of goods returned in the exchange not the total money refunded. |

### Example (as JSON)

```json
{
  "type": null,
  "reason": null,
  "refunded_money": null,
  "refunded_processing_fee_money": null,
  "refunded_tax_money": null,
  "refunded_additive_tax_money": null,
  "refunded_additive_tax": null,
  "refunded_inclusive_tax_money": null,
  "refunded_inclusive_tax": null,
  "refunded_tip_money": null,
  "refunded_discount_money": null,
  "refunded_surcharge_money": null,
  "refunded_surcharges": null,
  "created_at": null,
  "processed_at": null,
  "payment_id": null,
  "merchant_id": null,
  "is_exchange": null
}
```

