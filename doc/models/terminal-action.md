
# Terminal Action

Represents an action processed by the Square Terminal.

## Structure

`Terminal Action`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | A unique ID for this `TerminalAction`.<br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `255` |
| `device_id` | `string` | Optional | The unique Id of the device intended for this `TerminalAction`.<br>The Id can be retrieved from /v2/devices api. |
| `deadline_duration` | `string` | Optional | The duration as an RFC 3339 duration, after which the action will be automatically canceled.<br>TerminalActions that are `PENDING` will be automatically `CANCELED` and have a cancellation reason<br>of `TIMED_OUT`<br><br>Default: 5 minutes from creation<br><br>Maximum: 5 minutes |
| `status` | `string` | Optional | The status of the `TerminalAction`.<br>Options: `PENDING`, `IN_PROGRESS`, `CANCEL_REQUESTED`, `CANCELED`, `COMPLETED` |
| `cancel_reason` | [`str (Action Cancel Reason)`](../../doc/models/action-cancel-reason.md) | Optional | - |
| `created_at` | `string` | Optional | The time when the `TerminalAction` was created as an RFC 3339 timestamp. |
| `updated_at` | `string` | Optional | The time when the `TerminalAction` was last updated as an RFC 3339 timestamp. |
| `app_id` | `string` | Optional | The ID of the application that created the action. |
| `type` | [`str (Terminal Action Action Type)`](../../doc/models/terminal-action-action-type.md) | Optional | Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’ enum. |
| `save_card_options` | [`Save Card Options`](../../doc/models/save-card-options.md) | Optional | Describes save-card action fields. |
| `receipt_options` | [`Receipt Options`](../../doc/models/receipt-options.md) | Optional | Describes receipt action fields. |
| `device_metadata` | [`Device Metadata`](../../doc/models/device-metadata.md) | Optional | - |

## Example (as JSON)

```json
{
  "device_id": null,
  "deadline_duration": null,
  "cancel_reason": null,
  "type": null,
  "save_card_options": null,
  "receipt_options": null,
  "device_metadata": null
}
```

