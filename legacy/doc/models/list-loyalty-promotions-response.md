
# List Loyalty Promotions Response

Represents a [ListLoyaltyPromotions](../../doc/api/loyalty.md#list-loyalty-promotions) response.
One of `loyalty_promotions`, an empty object, or `errors` is present in the response.
If additional results are available, the `cursor` field is also present along with `loyalty_promotions`.

## Structure

`List Loyalty Promotions Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `loyalty_promotions` | [`List Loyalty Promotion`](../../doc/models/loyalty-promotion.md) | Optional | The retrieved loyalty promotions. |
| `cursor` | `str` | Optional | The cursor to use in your next call to this endpoint to retrieve the next page of results<br>for your original request. This field is present only if the request succeeded and additional<br>results are available. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Example (as JSON)

```json
{
  "loyalty_promotions": [
    {
      "available_time": {
        "start_date": "2022-08-16",
        "time_periods": [
          "BEGIN:VEVENT\nDTSTART:20220816T160000\nDURATION:PT2H\nRRULE:FREQ=WEEKLY;BYDAY=TU\nEND:VEVENT"
        ],
        "end_date": "end_date8"
      },
      "created_at": "2022-08-16T08:38:54Z",
      "id": "loypromo_f0f9b849-725e-378d-b810-511237e07b67",
      "incentive": {
        "points_multiplier_data": {
          "multiplier": "3.000",
          "points_multiplier": 3
        },
        "type": "POINTS_MULTIPLIER",
        "points_addition_data": {
          "points_addition": 218
        }
      },
      "loyalty_program_id": "d619f755-2d17-41f3-990d-c04ecedd64dd",
      "name": "Tuesday Happy Hour Promo",
      "qualifying_item_variation_ids": [
        "CJ3RYL56ITAKMD4VRCM7XERS",
        "AT3RYLR3TUA9C34VRCB7X5RR"
      ],
      "status": "ACTIVE",
      "trigger_limit": {
        "interval": "DAY",
        "times": 1
      },
      "updated_at": "2022-08-16T08:38:54Z",
      "canceled_at": "canceled_at0"
    },
    {
      "available_time": {
        "end_date": "2022-08-01",
        "start_date": "2022-07-01",
        "time_periods": [
          "BEGIN:VEVENT\nDTSTART:20220704T090000\nDURATION:PT8H\nRRULE:FREQ=WEEKLY;UNTIL=20220801T000000;BYDAY=MO\nEND:VEVENT",
          "BEGIN:VEVENT\nDTSTART:20220705T090000\nDURATION:PT8H\nRRULE:FREQ=WEEKLY;UNTIL=20220801T000000;BYDAY=TU\nEND:VEVENT",
          "BEGIN:VEVENT\nDTSTART:20220706T090000\nDURATION:PT8H\nRRULE:FREQ=WEEKLY;UNTIL=20220801T000000;BYDAY=WE\nEND:VEVENT",
          "BEGIN:VEVENT\nDTSTART:20220707T090000\nDURATION:PT8H\nRRULE:FREQ=WEEKLY;UNTIL=20220801T000000;BYDAY=TH\nEND:VEVENT",
          "BEGIN:VEVENT\nDTSTART:20220701T090000\nDURATION:PT8H\nRRULE:FREQ=WEEKLY;UNTIL=20220801T000000;BYDAY=FR\nEND:VEVENT"
        ]
      },
      "created_at": "2022-06-27T15:37:38Z",
      "id": "loypromo_e696f057-2286-35ff-8108-132241328106",
      "incentive": {
        "points_multiplier_data": {
          "multiplier": "2.000",
          "points_multiplier": 2
        },
        "type": "POINTS_MULTIPLIER",
        "points_addition_data": {
          "points_addition": 218
        }
      },
      "loyalty_program_id": "d619f755-2d17-41f3-990d-c04ecedd64dd",
      "minimum_spend_amount_money": {
        "amount": 2000,
        "currency": "USD"
      },
      "name": "July Special",
      "qualifying_category_ids": [
        "XTQPYLR3IIU9C44VRCB3XD12"
      ],
      "status": "ENDED",
      "trigger_limit": {
        "interval": "ALL_TIME",
        "times": 5
      },
      "updated_at": "2022-06-27T15:37:38Z",
      "canceled_at": "canceled_at0"
    }
  ],
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ],
  "cursor": "cursor8"
}
```

