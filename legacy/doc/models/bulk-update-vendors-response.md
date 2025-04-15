
# Bulk Update Vendors Response

Represents an output from a call to [BulkUpdateVendors](../../doc/api/vendors.md#bulk-update-vendors).

## Structure

`Bulk Update Vendors Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Errors encountered when the request fails. |
| `responses` | [`Dict Str Update Vendor Response`](../../doc/models/update-vendor-response.md) | Optional | A set of [UpdateVendorResponse](entity:UpdateVendorResponse) objects encapsulating successfully created [Vendor](entity:Vendor)<br>objects or error responses for failed attempts. The set is represented by a collection of `Vendor`-ID/`UpdateVendorResponse`-object or<br>`Vendor`-ID/error-object pairs. |

## Example (as JSON)

```json
{
  "responses": {
    "INV_V_FMCYHBWT1TPL8MFH52PBMEN92A": {
      "vendor": {
        "address": {
          "address_line_1": "202 Mill St",
          "administrative_district_level_1": "NJ",
          "country": "US",
          "locality": "Moorestown",
          "postal_code": "08057",
          "address_line_2": "address_line_26",
          "address_line_3": "address_line_32",
          "sublocality": "sublocality6"
        },
        "contacts": [
          {
            "email_address": "annie@annieshotsauce.com",
            "id": "INV_VC_ABYYHBWT1TPL8MFH52PBMENPJ4",
            "name": "Annie Thomas",
            "ordinal": 0,
            "phone_number": "1-212-555-4250"
          }
        ],
        "created_at": "2022-03-16T10:21:54.859Z",
        "id": "INV_V_FMCYHBWT1TPL8MFH52PBMEN92A",
        "name": "Annie’s Hot Sauce",
        "status": "ACTIVE",
        "updated_at": "2022-03-16T20:21:54.859Z",
        "version": 11
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
        },
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        }
      ]
    },
    "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4": {
      "vendor": {
        "account_number": "4025391",
        "address": {
          "address_line_1": "505 Electric Ave",
          "address_line_2": "Suite 600",
          "administrative_district_level_1": "NY",
          "country": "US",
          "locality": "New York",
          "postal_code": "10003",
          "address_line_3": "address_line_32",
          "sublocality": "sublocality6"
        },
        "contacts": [
          {
            "email_address": "joe@joesfreshseafood.com",
            "id": "INV_VC_FMCYHBWT1TPL8MFH52PBMEN92A",
            "name": "Joe Burrow",
            "ordinal": 0,
            "phone_number": "1-212-555-4250"
          }
        ],
        "created_at": "2022-03-16T10:10:54.859Z",
        "id": "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4",
        "name": "Joe's Fresh Seafood",
        "note": "favorite vendor",
        "status": "ACTIVE",
        "updated_at": "2022-03-16T20:21:54.859Z",
        "version": 31
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
        },
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        }
      ]
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
```

