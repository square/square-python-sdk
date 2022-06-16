
# Catalog Subscription Plan

Describes a subscription plan. For more information, see
[Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan).

## Structure

`Catalog Subscription Plan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | The name of the plan. |
| `phases` | [`List of Subscription Phase`](../../doc/models/subscription-phase.md) | Required | A list of SubscriptionPhase containing the [SubscriptionPhase](../../doc/models/subscription-phase.md) for this plan. |

## Example (as JSON)

```json
{
  "name": "name0",
  "phases": [
    {
      "uid": null,
      "cadence": "EVERY_FOUR_MONTHS",
      "periods": null,
      "recurring_price_money": null,
      "ordinal": null
    },
    {
      "uid": null,
      "cadence": "QUARTERLY",
      "periods": null,
      "recurring_price_money": null,
      "ordinal": null
    }
  ]
}
```

