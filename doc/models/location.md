
# Location

## Structure

`Location`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-issued ID of the location. |
| `name` | `string` | Optional | The name of the location.<br>This information appears in the dashboard as the nickname.<br>A location name must be unique within a seller account. |
| `address` | [`Address`](/doc/models/address.md) | Optional | Represents a postal address in a country. The address format is based<br>on an [open-source library from Google](https://github.com/google/libaddressinput). For more information,<br>see [AddressValidationMetadata](https://github.com/google/libaddressinput/wiki/AddressValidationMetadata).<br>This format has dedicated fields for four address components: postal code,<br>locality (city), administrative district (state, prefecture, or province), and<br>sublocality (town or village). These components have dedicated fields in the<br>`Address` object because software sometimes behaves differently based on them.<br>For example, sales tax software may charge different amounts of sales tax<br>based on the postal code, and some software is only available in<br>certain states due to compliance reasons.<br><br>For the remaining address components, the `Address` type provides the<br>`address_line_1` and `address_line_2` fields for free-form data entry.<br>These fields are free-form because the remaining address components have<br>too many variations around the world and typical software does not parse<br>these components. These fields enable users to enter anything they want.<br><br>Note that, in the current implementation, all other `Address` type fields are blank.<br>These include `address_line_3`, `sublocality_2`, `sublocality_3`,<br>`administrative_district_level_2`, `administrative_district_level_3`,<br>`first_name`, `last_name`, and `organization`.<br><br>When it comes to localization, the seller's language preferences<br>(see [Language preferences](https://developer.squareup.com/docs/locations-api#location-specific-and-seller-level-language-preferences))<br>are ignored for addresses. Even though Square products (such as Square Point of Sale<br>and the Seller Dashboard) mostly use a seller's language preference in<br>communication, when it comes to addresses, they will use English for a US address,<br>Japanese for an address in Japan, and so on. |
| `timezone` | `string` | Optional | The [IANA Timezone](https://www.iana.org/time-zones) identifier for<br>the timezone of the location. |
| `capabilities` | [`List of str (Location Capability)`](/doc/models/location-capability.md) | Optional | The Square features that are enabled for the location.<br>See [LocationCapability](/doc/models/location-capability.md) for possible values.<br>See [LocationCapability](#type-locationcapability) for possible values |
| `status` | [`str (Location Status)`](/doc/models/location-status.md) | Optional | The status of the location, whether a location is active or inactive. |
| `created_at` | `string` | Optional | The time when the location was created, in RFC 3339 format.<br>For more information, see [Working with Dates](https://developer.squareup.com/docs/build-basics/working-with-dates). |
| `merchant_id` | `string` | Optional | The ID of the merchant that owns the location. |
| `country` | [`str (Country)`](/doc/models/country.md) | Optional | Indicates the country associated with another entity, such as a business.<br>Values are in [ISO 3166-1-alpha-2 format](http://www.iso.org/iso/home/standards/country_codes.htm). |
| `language_code` | `string` | Optional | The language associated with the location, in<br>[BCP 47 format](https://tools.ietf.org/html/bcp47#appendix-A).<br>For more information, see [Location language code](https://developer.squareup.com/docs/locations-api#location-language-code). |
| `currency` | [`str (Currency)`](/doc/models/currency.md) | Optional | Indicates the associated currency for an amount of money. Values correspond<br>to [ISO 4217](https://wikipedia.org/wiki/ISO_4217). |
| `phone_number` | `string` | Optional | The phone number of the location in human readable format. For example, `+353 80 0 098 8099`. |
| `business_name` | `string` | Optional | The business name of the location<br>This is the name visible to the customers of the location.<br>For example, this name appears on customer receipts. |
| `type` | [`str (Location Type)`](/doc/models/location-type.md) | Optional | A location's physical or mobile type. |
| `website_url` | `string` | Optional | The website URL of the location.  For example, `https://squareup.com`. |
| `business_hours` | [`Business Hours`](/doc/models/business-hours.md) | Optional | Represents the hours of operation for a business location. |
| `business_email` | `string` | Optional | The email of the location.<br>This email is visible to the customers of the location.<br>For example, the email appears on customer receipts.<br>For example, `help@squareup.com`. |
| `description` | `string` | Optional | The description of the location. |
| `twitter_username` | `string` | Optional | The Twitter username of the location without the '@' symbol. For example, `Square`. |
| `instagram_username` | `string` | Optional | The Instagram username of the location without the '@' symbol. For example, `square`. |
| `facebook_url` | `string` | Optional | The Facebook profile URL of the location. The URL should begin with 'facebook.com/'. For example, `https://www.facebook.com/square`. |
| `coordinates` | [`Coordinates`](/doc/models/coordinates.md) | Optional | Latitude and longitude coordinates. |
| `logo_url` | `string` | Optional | The URL of the logo image for the location. The Seller must choose this logo in the Seller<br>dashboard (Receipts section) for the logo to appear on transactions (such as receipts, invoices)<br>that Square generates on behalf of the Seller. This image should have an aspect ratio<br>close to 1:1 and is recommended to be at least 200x200 pixels. |
| `pos_background_url` | `string` | Optional | The URL of the Point of Sale background image for the location. |
| `mcc` | `string` | Optional | The merchant category code (MCC) of the location, as standardized by ISO 18245.<br>The MCC describes the kind of goods or services sold at the location. |
| `full_format_logo_url` | `string` | Optional | The URL of a full-format logo image for the location. The Seller must choose this logo in the<br>Seller dashboard (Receipts section) for the logo to appear on transactions (such as receipts, invoices)<br>that Square generates on behalf of the Seller. This image can have an aspect ratio of 2:1 or greater<br>and is recommended to be at least 1280x648 pixels. |
| `tax_ids` | [`Tax Ids`](/doc/models/tax-ids.md) | Optional | The tax IDs that a Location is operating under. |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "address": {
    "address_line_1": "address_line_16",
    "address_line_2": "address_line_26",
    "address_line_3": "address_line_32",
    "locality": "locality6",
    "sublocality": "sublocality6"
  },
  "timezone": "timezone0",
  "capabilities": [
    "AUTOMATIC_TRANSFERS"
  ]
}
```

