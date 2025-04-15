# Events

```python
events_api = client.events
```

## Class Name

`EventsApi`

## Methods

* [Search Events](../../doc/api/events.md#search-events)
* [Disable Events](../../doc/api/events.md#disable-events)
* [Enable Events](../../doc/api/events.md#enable-events)
* [List Event Types](../../doc/api/events.md#list-event-types)


# Search Events

Search for Square API events that occur within a 28-day timeframe.

```python
def search_events(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Events Request`](../../doc/models/search-events-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Events Response`](../../doc/models/search-events-response.md).

## Example Usage

```python
body = {}

result = events_api.search_events(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Disable Events

Disables events to prevent them from being searchable.
All events are disabled by default. You must enable events to make them searchable.
Disabling events for a specific time period prevents them from being searchable, even if you re-enable them later.

```python
def disable_events(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Disable Events Response`](../../doc/models/disable-events-response.md).

## Example Usage

```python
result = events_api.disable_events()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Enable Events

Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

```python
def enable_events(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Enable Events Response`](../../doc/models/enable-events-response.md).

## Example Usage

```python
result = events_api.enable_events()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Event Types

Lists all event types that you can subscribe to as webhooks or query using the Events API.

```python
def list_event_types(self,
                    api_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_version` | `str` | Query, Optional | The API version for which to list event types. Setting this field overrides the default version used by the application. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Event Types Response`](../../doc/models/list-event-types-response.md).

## Example Usage

```python
result = events_api.list_event_types()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

