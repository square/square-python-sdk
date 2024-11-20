
# Merchant

Represents a business that sells with Square.

## Structure

`Merchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The Square-issued ID of the merchant. |
| `business_name` | `str` | Optional | The name of the merchant's overall business. |
| `country` | [`str (Country)`](../../doc/models/country.md) | Required | Indicates the country associated with another entity, such as a business.<br>Values are in [ISO 3166-1-alpha-2 format](http://www.iso.org/iso/home/standards/country_codes.htm). |
| `language_code` | `str` | Optional | The code indicating the [language preferences](https://developer.squareup.com/docs/build-basics/general-considerations/language-preferences) of the merchant, in [BCP 47 format](https://tools.ietf.org/html/bcp47#appendix-A). For example, `en-US` or `fr-CA`. |
| `currency` | [`str (Currency)`](../../doc/models/currency.md) | Optional | Indicates the associated currency for an amount of money. Values correspond<br>to [ISO 4217](https://wikipedia.org/wiki/ISO_4217). |
| `status` | [`str (Merchant Status)`](../../doc/models/merchant-status.md) | Optional | - |
| `main_location_id` | `str` | Optional | The ID of the [main `Location`](https://developer.squareup.com/docs/locations-api#about-the-main-location) for this merchant. |
| `created_at` | `str` | Optional | The time when the merchant was created, in RFC 3339 format.<br>For more information, see [Working with Dates](https://developer.squareup.com/docs/build-basics/working-with-dates). |

## Example (as JSON)

```json
{
  "id": "id2",
  "business_name": "business_name6",
  "country": "HM",
  "language_code": "language_code0",
  "currency": "BTC",
  "status": "ACTIVE"
}
```

