
# Gift Card Activity

Represents an action performed on a [gift card](../../doc/models/gift-card.md) that affects its state or balance.
A gift card activity contains information about a specific activity type. For example, a `REDEEM` activity
includes a `redeem_activity_details` field that contains information about the redemption.

## Structure

`Gift Card Activity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The Square-assigned ID of the gift card activity. |
| `type` | [`str (Gift Card Activity Type)`](../../doc/models/gift-card-activity-type.md) | Required | Indicates the type of [gift card activity](../../doc/models/gift-card-activity.md). |
| `location_id` | `str` | Required | The ID of the [business location](entity:Location) where the activity occurred. |
| `created_at` | `str` | Optional | The timestamp when the gift card activity was created, in RFC 3339 format. |
| `gift_card_id` | `str` | Optional | The gift card ID. When creating a gift card activity, `gift_card_id` is not required if<br>`gift_card_gan` is specified. |
| `gift_card_gan` | `str` | Optional | The gift card account number (GAN). When creating a gift card activity, `gift_card_gan`<br>is not required if `gift_card_id` is specified. |
| `gift_card_balance_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `load_activity_details` | [`Gift Card Activity Load`](../../doc/models/gift-card-activity-load.md) | Optional | Represents details about a `LOAD` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `activate_activity_details` | [`Gift Card Activity Activate`](../../doc/models/gift-card-activity-activate.md) | Optional | Represents details about an `ACTIVATE` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `redeem_activity_details` | [`Gift Card Activity Redeem`](../../doc/models/gift-card-activity-redeem.md) | Optional | Represents details about a `REDEEM` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `clear_balance_activity_details` | [`Gift Card Activity Clear Balance`](../../doc/models/gift-card-activity-clear-balance.md) | Optional | Represents details about a `CLEAR_BALANCE` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `deactivate_activity_details` | [`Gift Card Activity Deactivate`](../../doc/models/gift-card-activity-deactivate.md) | Optional | Represents details about a `DEACTIVATE` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `adjust_increment_activity_details` | [`Gift Card Activity Adjust Increment`](../../doc/models/gift-card-activity-adjust-increment.md) | Optional | Represents details about an `ADJUST_INCREMENT` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `adjust_decrement_activity_details` | [`Gift Card Activity Adjust Decrement`](../../doc/models/gift-card-activity-adjust-decrement.md) | Optional | Represents details about an `ADJUST_DECREMENT` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `refund_activity_details` | [`Gift Card Activity Refund`](../../doc/models/gift-card-activity-refund.md) | Optional | Represents details about a `REFUND` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `unlinked_activity_refund_activity_details` | [`Gift Card Activity Unlinked Activity Refund`](../../doc/models/gift-card-activity-unlinked-activity-refund.md) | Optional | Represents details about an `UNLINKED_ACTIVITY_REFUND` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `import_activity_details` | [`Gift Card Activity Import`](../../doc/models/gift-card-activity-import.md) | Optional | Represents details about an `IMPORT` [gift card activity type](../../doc/models/gift-card-activity-type.md).<br>This activity type is used when Square imports a third-party gift card, in which case the<br>`gan_source` of the gift card is set to `OTHER`. |
| `block_activity_details` | [`Gift Card Activity Block`](../../doc/models/gift-card-activity-block.md) | Optional | Represents details about a `BLOCK` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `unblock_activity_details` | [`Gift Card Activity Unblock`](../../doc/models/gift-card-activity-unblock.md) | Optional | Represents details about an `UNBLOCK` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `import_reversal_activity_details` | [`Gift Card Activity Import Reversal`](../../doc/models/gift-card-activity-import-reversal.md) | Optional | Represents details about an `IMPORT_REVERSAL` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `transfer_balance_to_activity_details` | [`Gift Card Activity Transfer Balance To`](../../doc/models/gift-card-activity-transfer-balance-to.md) | Optional | Represents details about a `TRANSFER_BALANCE_TO` [gift card activity type](../../doc/models/gift-card-activity-type.md). |
| `transfer_balance_from_activity_details` | [`Gift Card Activity Transfer Balance From`](../../doc/models/gift-card-activity-transfer-balance-from.md) | Optional | Represents details about a `TRANSFER_BALANCE_FROM` [gift card activity type](../../doc/models/gift-card-activity-type.md). |

## Example (as JSON)

```json
{
  "id": "id8",
  "type": "REDEEM",
  "location_id": "location_id2",
  "created_at": "created_at6",
  "gift_card_id": "gift_card_id6",
  "gift_card_gan": "gift_card_gan4",
  "gift_card_balance_money": {
    "amount": 82,
    "currency": "IRR"
  }
}
```

