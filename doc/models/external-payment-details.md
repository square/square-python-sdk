## External Payment Details

Additional details about EXTERNAL type payments.

### Structure

`ExternalPaymentDetails`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `string` |  | The type of External payment which can be one of:<br>CHECK - Paid by a physical check<br>BANK_TRANSFER - Paid by ACH or other bank transfer<br>OTHER_GIFT_CARD - Paid by a non-square gift card<br>CRYPTO - Paid via a crypto currency<br>SQUARE_CASH - Paid via Square Cash app<br>SOCIAL - Venmo, WeChatPay, AliPay, etc.<br>EXTERNAL - A 3rd party application gathered this payment outside of Square<br>EMONEY - A Japanese e-money brand Square doesn’t support<br>CREDIT/DEBIT - A credit/debit card Square doesn’t support<br>OTHER - A type not listed here |
| `source` | `string` |  | A description of the source of the external payment, e.g. “Uber Eats”, “Stripe”, “Shopify”.<br><br>Limit 255 characters |
| `source_id` | `string` | Optional | An ID to associate this payment to its originating source<br><br>Limit 255 characters. |
| `source_fee_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

### Example (as JSON)

```json
{
  "type": "type0",
  "source": "source4",
  "source_id": null,
  "source_fee_money": null
}
```

