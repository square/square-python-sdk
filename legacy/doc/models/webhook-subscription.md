
# Webhook Subscription

Represents the details of a webhook subscription, including notification URL,
event types, and signature key.

## Structure

`Webhook Subscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A Square-generated unique ID for the subscription.<br>**Constraints**: *Maximum Length*: `64` |
| `name` | `str` | Optional | The name of this subscription.<br>**Constraints**: *Maximum Length*: `64` |
| `enabled` | `bool` | Optional | Indicates whether the subscription is enabled (`true`) or not (`false`). |
| `event_types` | `List[str]` | Optional | The event types associated with this subscription. |
| `notification_url` | `str` | Optional | The URL to which webhooks are sent. |
| `api_version` | `str` | Optional | The API version of the subscription.<br>This field is optional for `CreateWebhookSubscription`.<br>The value defaults to the API version used by the application. |
| `signature_key` | `str` | Optional | The Square-generated signature key used to validate the origin of the webhook event. |
| `created_at` | `str` | Optional | The timestamp of when the subscription was created, in RFC 3339 format. For example, "2016-09-04T23:59:33.123Z". |
| `updated_at` | `str` | Optional | The timestamp of when the subscription was last updated, in RFC 3339 format.<br>For example, "2016-09-04T23:59:33.123Z". |

## Example (as JSON)

```json
{
  "id": "id8",
  "name": "name8",
  "enabled": false,
  "event_types": [
    "event_types6"
  ],
  "notification_url": "notification_url2"
}
```

