
# Search Loyalty Rewards Request

A request to search for loyalty rewards.

## Structure

`Search Loyalty Rewards Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | [`Search Loyalty Rewards Request Loyalty Reward Query`](../../doc/models/search-loyalty-rewards-request-loyalty-reward-query.md) | Optional | The set of search requirements. |
| `limit` | `int` | Optional | The maximum number of results to return in the response. The default value is 30.<br>**Constraints**: `>= 1`, `<= 30` |
| `cursor` | `str` | Optional | A pagination cursor returned by a previous call to<br>this endpoint. Provide this to retrieve the next set of<br>results for the original query.<br>For more information,<br>see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Example (as JSON)

```json
{
  "limit": 10,
  "query": {
    "loyalty_account_id": "5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd",
    "status": "ISSUED"
  },
  "cursor": "cursor4"
}
```

