
# Bulk Upsert Order Custom Attributes Response

Represents a response from a bulk upsert of order custom attributes.

## Structure

`Bulk Upsert Order Custom Attributes Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `values` | [`Dict Str Upsert Order Custom Attribute Response`](../../doc/models/upsert-order-custom-attribute-response.md) | Required | A map of responses that correspond to individual upsert operations for custom attributes. |

## Example (as JSON)

```json
{
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ],
  "values": {
    "key0": {
      "custom_attribute": {
        "key": "key2",
        "value": {
          "key1": "val1",
          "key2": "val2"
        },
        "version": 102,
        "visibility": "VISIBILITY_READ_ONLY",
        "definition": {
          "key": "key0",
          "schema": {
            "key1": "val1",
            "key2": "val2"
          },
          "name": "name0",
          "description": "description0",
          "visibility": "VISIBILITY_HIDDEN"
        }
      },
      "errors": [
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        },
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        }
      ]
    }
  }
}
```

