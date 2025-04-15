
# Retrieve Subscription Request

Defines input parameters in a request to the
[RetrieveSubscription](../../doc/api/subscriptions.md#retrieve-subscription) endpoint.

## Structure

`Retrieve Subscription Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include` | `str` | Optional | A query parameter to specify related information to be included in the response.<br><br>The supported query parameter values are:<br><br>- `actions`: to include scheduled actions on the targeted subscription. |

## Example (as JSON)

```json
{
  "include": "include2"
}
```

