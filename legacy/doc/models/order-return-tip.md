
# Order Return Tip

A tip being returned.

## Structure

`Order Return Tip`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID that identifies the tip only within this order.<br>**Constraints**: *Maximum Length*: `60` |
| `applied_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `source_tender_uid` | `str` | Optional | The tender `uid` from the order that contains the original application of this tip.<br>**Constraints**: *Maximum Length*: `192` |
| `source_tender_id` | `str` | Optional | The tender `id` from the order that contains the original application of this tip.<br>**Constraints**: *Maximum Length*: `192` |

## Example (as JSON)

```json
{
  "uid": "uid4",
  "applied_money": {
    "amount": 196,
    "currency": "AMD"
  },
  "source_tender_uid": "source_tender_uid6",
  "source_tender_id": "source_tender_id0"
}
```

