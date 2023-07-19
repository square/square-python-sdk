
# Bulk Delete Location Custom Attributes Response

Represents a [BulkDeleteLocationCustomAttributes](../../doc/api/location-custom-attributes.md#bulk-delete-location-custom-attributes) response,
which contains a map of responses that each corresponds to an individual delete request.

## Structure

`Bulk Delete Location Custom Attributes Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `values` | [`Dict`](../../doc/models/bulk-delete-location-custom-attributes-response-location-custom-attribute-delete-response.md) | Required | A map of responses that correspond to individual delete requests. Each response has the<br>same key as the corresponding request. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "values": {
    "id1": {
      "errors": [],
      "location_id": "L0TBCBTB7P8RQ"
    },
    "id2": {
      "errors": [],
      "location_id": "L9XMD04V3STJX"
    },
    "id3": {
      "errors": [],
      "location_id": "L0TBCBTB7P8RQ"
    }
  },
  "errors": [
    {
      "category": "REFUND_ERROR",
      "code": "MERCHANT_SUBSCRIPTION_NOT_FOUND",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "BAD_REQUEST",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "EXTERNAL_VENDOR_ERROR",
      "code": "MISSING_REQUIRED_PARAMETER",
      "detail": "detail3",
      "field": "field1"
    }
  ]
}
```

