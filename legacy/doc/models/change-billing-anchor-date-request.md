
# Change Billing Anchor Date Request

Defines input parameters in a request to the
[ChangeBillingAnchorDate](../../doc/api/subscriptions.md#change-billing-anchor-date) endpoint.

## Structure

`Change Billing Anchor Date Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monthly_billing_anchor_date` | `int` | Optional | The anchor day for the billing cycle.<br>**Constraints**: `>= 1`, `<= 31` |
| `effective_date` | `str` | Optional | The `YYYY-MM-DD`-formatted date when the scheduled `BILLING_ANCHOR_CHANGE` action takes<br>place on the subscription.<br><br>When this date is unspecified or falls within the current billing cycle, the billing anchor date<br>is changed immediately. |

## Example (as JSON)

```json
{
  "monthly_billing_anchor_date": 1,
  "effective_date": "effective_date8"
}
```

