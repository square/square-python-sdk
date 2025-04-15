
# Search Terminal Actions Response

## Structure

`Search Terminal Actions Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `action` | [`List Terminal Action`](../../doc/models/terminal-action.md) | Optional | The requested search result of `TerminalAction`s. |
| `cursor` | `str` | Optional | The pagination cursor to be used in a subsequent request. If empty,<br>this is the final response.<br><br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more<br>information. |

## Example (as JSON)

```json
{
  "action": [
    {
      "app_id": "APP_ID",
      "created_at": "2022-04-08T15:14:04.895Z",
      "deadline_duration": "PT5M",
      "device_id": "DEVICE_ID",
      "id": "termapia:oBGWlAats8xWCiCE",
      "location_id": "LOCATION_ID",
      "save_card_options": {
        "customer_id": "CUSTOMER_ID",
        "reference_id": "user-id-1"
      },
      "status": "IN_PROGRESS",
      "type": "SAVE_CARD",
      "updated_at": "2022-04-08T15:14:05.446Z",
      "cancel_reason": "TIMED_OUT"
    },
    {
      "app_id": "APP_ID",
      "created_at": "2022-04-08T15:14:01.210Z",
      "deadline_duration": "PT5M",
      "device_id": "DEVICE_ID",
      "id": "termapia:K2NY2YSSml3lTiCE",
      "location_id": "LOCATION_ID",
      "save_card_options": {
        "card_id": "ccof:CARD_ID",
        "customer_id": "CUSTOMER_ID",
        "reference_id": "user-id-1"
      },
      "status": "COMPLETED",
      "type": "SAVE_CARD",
      "updated_at": "2022-04-08T15:14:09.861Z",
      "cancel_reason": "TIMED_OUT"
    }
  ],
  "cursor": "CURSOR",
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ]
}
```

