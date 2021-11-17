
# Gift Card Activity

Represents an action performed on a gift card that affects its state or balance.

## Structure

`Gift Card Activity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The unique ID of the gift card activity. |
| `type` | [`str (Gift Card Activity Type)`](/doc/models/gift-card-activity-type.md) | Required | Indicates the gift card activity type. |
| `location_id` | `string` | Required | The ID of the location at which the activity occurred. |
| `created_at` | `string` | Optional | The timestamp when the gift card activity was created, in RFC 3339 format. |
| `gift_card_id` | `string` | Optional | The gift card ID. The ID is not required if a GAN is present. |
| `gift_card_gan` | `string` | Optional | The gift card GAN. The GAN is not required if `gift_card_id` is present. |
| `gift_card_balance_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `load_activity_details` | [`Gift Card Activity Load`](/doc/models/gift-card-activity-load.md) | Optional | Present only when `GiftCardActivityType` is LOAD. |
| `activate_activity_details` | [`Gift Card Activity Activate`](/doc/models/gift-card-activity-activate.md) | Optional | Describes a gift card activity of the ACTIVATE type. |
| `redeem_activity_details` | [`Gift Card Activity Redeem`](/doc/models/gift-card-activity-redeem.md) | Optional | Present only when `GiftCardActivityType` is REDEEM. |
| `clear_balance_activity_details` | [`Gift Card Activity Clear Balance`](/doc/models/gift-card-activity-clear-balance.md) | Optional | Describes a gift card activity of the CLEAR_BALANCE type. |
| `deactivate_activity_details` | [`Gift Card Activity Deactivate`](/doc/models/gift-card-activity-deactivate.md) | Optional | Describes a gift card activity of the DEACTIVATE type. |
| `adjust_increment_activity_details` | [`Gift Card Activity Adjust Increment`](/doc/models/gift-card-activity-adjust-increment.md) | Optional | Describes a gift card activity of the ADJUST_INCREMENT type. |
| `adjust_decrement_activity_details` | [`Gift Card Activity Adjust Decrement`](/doc/models/gift-card-activity-adjust-decrement.md) | Optional | Describes a gift card activity of the ADJUST_DECREMENT type. |
| `refund_activity_details` | [`Gift Card Activity Refund`](/doc/models/gift-card-activity-refund.md) | Optional | Present only when `GiftCardActivityType` is REFUND. |
| `unlinked_activity_refund_activity_details` | [`Gift Card Activity Unlinked Activity Refund`](/doc/models/gift-card-activity-unlinked-activity-refund.md) | Optional | Present only when `GiftCardActivityType` is UNLINKED_ACTIVITY_REFUND. |
| `import_activity_details` | [`Gift Card Activity Import`](/doc/models/gift-card-activity-import.md) | Optional | Describes a gift card activity of the IMPORT type and the `GiftCardGANSource` is OTHER<br>(a third-party gift card). |
| `block_activity_details` | [`Gift Card Activity Block`](/doc/models/gift-card-activity-block.md) | Optional | Describes a gift card activity of the BLOCK type. |
| `unblock_activity_details` | [`Gift Card Activity Unblock`](/doc/models/gift-card-activity-unblock.md) | Optional | Present only when `GiftCardActivityType` is UNBLOCK. |
| `import_reversal_activity_details` | [`Gift Card Activity Import Reversal`](/doc/models/gift-card-activity-import-reversal.md) | Optional | Present only when GiftCardActivityType is IMPORT_REVERSAL and GiftCardGANSource is OTHER |

## Example (as JSON)

```json
{
  "id": "id0",
  "type": "ADJUST_INCREMENT",
  "location_id": "location_id4",
  "created_at": "created_at2",
  "gift_card_id": "gift_card_id8",
  "gift_card_gan": "gift_card_gan6",
  "gift_card_balance_money": {
    "amount": 82,
    "currency": "LSL"
  }
}
```

