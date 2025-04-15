# Gift Card Activities

```python
gift_card_activities_api = client.gift_card_activities
```

## Class Name

`GiftCardActivitiesApi`

## Methods

* [List Gift Card Activities](../../doc/api/gift-card-activities.md#list-gift-card-activities)
* [Create Gift Card Activity](../../doc/api/gift-card-activities.md#create-gift-card-activity)


# List Gift Card Activities

Lists gift card activities. By default, you get gift card activities for all
gift cards in the seller's account. You can optionally specify query parameters to
filter the list. For example, you can get a list of gift card activities for a gift card,
for all gift cards in a specific region, or for activities within a time window.

```python
def list_gift_card_activities(self,
                             gift_card_id=None,
                             mtype=None,
                             location_id=None,
                             begin_time=None,
                             end_time=None,
                             limit=None,
                             cursor=None,
                             sort_order=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gift_card_id` | `str` | Query, Optional | If a gift card ID is provided, the endpoint returns activities related<br>to the specified gift card. Otherwise, the endpoint returns all gift card activities for<br>the seller. |
| `mtype` | `str` | Query, Optional | If a [type](entity:GiftCardActivityType) is provided, the endpoint returns gift card activities of the specified type.<br>Otherwise, the endpoint returns all types of gift card activities. |
| `location_id` | `str` | Query, Optional | If a location ID is provided, the endpoint returns gift card activities for the specified location.<br>Otherwise, the endpoint returns gift card activities for all locations. |
| `begin_time` | `str` | Query, Optional | The timestamp for the beginning of the reporting period, in RFC 3339 format.<br>This start time is inclusive. The default value is the current time minus one year. |
| `end_time` | `str` | Query, Optional | The timestamp for the end of the reporting period, in RFC 3339 format.<br>This end time is inclusive. The default value is the current time. |
| `limit` | `int` | Query, Optional | If a limit is provided, the endpoint returns the specified number<br>of results (or fewer) per page. The maximum value is 100. The default value is 50.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>If a cursor is not provided, the endpoint returns the first page of the results.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `sort_order` | `str` | Query, Optional | The order in which the endpoint returns the activities, based on `created_at`.<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Gift Card Activities Response`](../../doc/models/list-gift-card-activities-response.md).

## Example Usage

```python
result = gift_card_activities_api.list_gift_card_activities()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Gift Card Activity

Creates a gift card activity to manage the balance or state of a [gift card](../../doc/models/gift-card.md).
For example, create an `ACTIVATE` activity to activate a gift card with an initial balance before first use.

```python
def create_gift_card_activity(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Gift Card Activity Request`](../../doc/models/create-gift-card-activity-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Gift Card Activity Response`](../../doc/models/create-gift-card-activity-response.md).

## Example Usage

```python
body = {
    'idempotency_key': 'U16kfr-kA70er-q4Rsym-7U7NnY',
    'gift_card_activity': {
        'type': 'ACTIVATE',
        'location_id': '81FN9BNFZTKS4',
        'gift_card_id': 'gftc:6d55a72470d940c6ba09c0ab8ad08d20',
        'activate_activity_details': {
            'order_id': 'jJNGHm4gLI6XkFbwtiSLqK72KkAZY',
            'line_item_uid': 'eIWl7X0nMuO9Ewbh0ChIx'
        }
    }
}

result = gift_card_activities_api.create_gift_card_activity(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

