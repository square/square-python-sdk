
# Search Loyalty Rewards Request Loyalty Reward Query

The set of search requirements.

## Structure

`Search Loyalty Rewards Request Loyalty Reward Query`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_account_id` | `str` | Required | The ID of the [loyalty account](entity:LoyaltyAccount) to which the loyalty reward belongs.<br>**Constraints**: *Minimum Length*: `1` |
| `status` | [`str (Loyalty Reward Status)`](../../doc/models/loyalty-reward-status.md) | Optional | The status of the loyalty reward. |

## Example (as JSON)

```json
{
  "loyalty_account_id": "loyalty_account_id2",
  "status": "DELETED"
}
```

