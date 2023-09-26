
# Terminal Action

Represents an action processed by the Square Terminal.

## Structure

`Terminal Action`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A unique ID for this `TerminalAction`.<br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `255` |
| `device_id` | `str` | Optional | The unique Id of the device intended for this `TerminalAction`.<br>The Id can be retrieved from /v2/devices api. |
| `deadline_duration` | `str` | Optional | The duration as an RFC 3339 duration, after which the action will be automatically canceled.<br>TerminalActions that are `PENDING` will be automatically `CANCELED` and have a cancellation reason<br>of `TIMED_OUT`<br><br>Default: 5 minutes from creation<br><br>Maximum: 5 minutes |
| `status` | `str` | Optional | The status of the `TerminalAction`.<br>Options: `PENDING`, `IN_PROGRESS`, `CANCEL_REQUESTED`, `CANCELED`, `COMPLETED` |
| `cancel_reason` | [`str (Action Cancel Reason)`](../../doc/models/action-cancel-reason.md) | Optional | - |
| `created_at` | `str` | Optional | The time when the `TerminalAction` was created as an RFC 3339 timestamp. |
| `updated_at` | `str` | Optional | The time when the `TerminalAction` was last updated as an RFC 3339 timestamp. |
| `app_id` | `str` | Optional | The ID of the application that created the action. |
| `location_id` | `str` | Optional | The location id the action is attached to, if a link can be made.<br>**Constraints**: *Maximum Length*: `64` |
| `type` | [`str (Terminal Action Action Type)`](../../doc/models/terminal-action-action-type.md) | Optional | Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’ enum. |
| `qr_code_options` | [`Qr Code Options`](../../doc/models/qr-code-options.md) | Optional | Fields to describe the action that displays QR-Codes. |
| `save_card_options` | [`Save Card Options`](../../doc/models/save-card-options.md) | Optional | Describes save-card action fields. |
| `signature_options` | [`Signature Options`](../../doc/models/signature-options.md) | Optional | - |
| `confirmation_options` | [`Confirmation Options`](../../doc/models/confirmation-options.md) | Optional | - |
| `receipt_options` | [`Receipt Options`](../../doc/models/receipt-options.md) | Optional | Describes receipt action fields. |
| `data_collection_options` | [`Data Collection Options`](../../doc/models/data-collection-options.md) | Optional | - |
| `select_options` | [`Select Options`](../../doc/models/select-options.md) | Optional | - |
| `device_metadata` | [`Device Metadata`](../../doc/models/device-metadata.md) | Optional | - |
| `await_next_action` | `bool` | Optional | Indicates the action will be linked to another action and requires a waiting dialog to be<br>displayed instead of returning to the idle screen on completion of the action.<br><br>Only supported on SIGNATURE, CONFIRMATION, DATA_COLLECTION, and SELECT types. |
| `await_next_action_duration` | `str` | Optional | The timeout duration of the waiting dialog as an RFC 3339 duration, after which the<br>waiting dialog will no longer be displayed and the Terminal will return to the idle screen.<br><br>Default: 5 minutes from when the waiting dialog is displayed<br><br>Maximum: 5 minutes |

## Example (as JSON)

```json
{
  "id": "id8",
  "device_id": "device_id4",
  "deadline_duration": "deadline_duration0",
  "status": "status0",
  "cancel_reason": "TIMED_OUT"
}
```

