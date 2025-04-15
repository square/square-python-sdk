
# Cash Drawer Shift Summary

The summary of a closed cash drawer shift.
This model contains only the money counted to start a cash drawer shift, counted
at the end of the shift, and the amount that should be in the drawer at shift
end based on summing all cash drawer shift events.

## Structure

`Cash Drawer Shift Summary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The shift unique ID. |
| `state` | [`str (Cash Drawer Shift State)`](../../doc/models/cash-drawer-shift-state.md) | Optional | The current state of a cash drawer shift. |
| `opened_at` | `str` | Optional | The shift start time in ISO 8601 format. |
| `ended_at` | `str` | Optional | The shift end time in ISO 8601 format. |
| `closed_at` | `str` | Optional | The shift close time in ISO 8601 format. |
| `description` | `str` | Optional | An employee free-text description of a cash drawer shift. |
| `opened_cash_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `expected_cash_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `closed_cash_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `created_at` | `str` | Optional | The shift start time in RFC 3339 format. |
| `updated_at` | `str` | Optional | The shift updated at time in RFC 3339 format. |
| `location_id` | `str` | Optional | The ID of the location the cash drawer shift belongs to. |

## Example (as JSON)

```json
{
  "id": "id0",
  "state": "CLOSED",
  "opened_at": "opened_at8",
  "ended_at": "ended_at2",
  "closed_at": "closed_at2"
}
```

