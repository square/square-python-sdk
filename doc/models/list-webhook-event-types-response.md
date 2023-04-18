
# List Webhook Event Types Response

Defines the fields that are included in the response body of
a request to the [ListWebhookEventTypes](../../doc/api/webhook-subscriptions.md#list-webhook-event-types) endpoint.

Note: if there are errors processing the request, the event types field will not be
present.

## Structure

`List Webhook Event Types Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `event_types` | `List of string` | Optional | The list of event types. |
| `metadata` | [`List of Event Type Metadata`](../../doc/models/event-type-metadata.md) | Optional | Contains the metadata of a webhook event type. For more information, see [EventTypeMetadata](entity:EventTypeMetadata). |

## Example (as JSON)

```json
{
  "event_types": [
    "inventory.count.updated"
  ],
  "metadata": [
    {
      "api_version_introduced": "2018-07-12",
      "event_type": "inventory.count.updated",
      "release_status": "PUBLIC"
    }
  ]
}
```

