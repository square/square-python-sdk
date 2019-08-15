## Location

Represents one of a business's locations.

### Structure

`Location`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The location's unique ID. |
| `name` | `string` | Optional | The location's name. Location names are set by the account owner and displayed<br>in the dashboard as the location's nickname |
| `address` | [`Address`](/doc/models/address.md) | Optional | Represents a physical address. |
| `timezone` | `string` | Optional | The [IANA Timezone Database](https://www.iana.org/time-zones)<br>identifier for the location's timezone. |
| `capabilities` | [`List of str (Location Capability)`](/doc/models/location-capability.md) | Optional | Indicates which Square features are enabled for the location.<br>See [LocationCapability](./models/location-capability.md) for possible values |
| `status` | [`str (Location Status)`](/doc/models/location-status.md) | Optional | Indicates the location's status. |
| `created_at` | `string` | Optional | The time when the location was created, in RFC 3339 format. |
| `merchant_id` | `string` | Optional | The identifier of the merchant that owns the location. |
| `country` | [`str (Country)`](/doc/models/country.md) | Optional | Indicates the country associated with another entity, such as a business.<br>Values are in [ISO 3166-1-alpha-2 format](http://www.iso.org/iso/home/standards/country_codes.htm). |
| `language_code` | `string` | Optional | The language associated with the location in<br>[BCP 47 format](https://tools.ietf.org/html/bcp47#appendix-A). |
| `currency` | [`str (Currency)`](/doc/models/currency.md) | Optional | Indicates the associated currency for an amount of money. Values correspond<br>to [ISO 4217](https://wikipedia.org/wiki/ISO_4217). |
| `phone_number` | `string` | Optional | The location's phone_number. |
| `business_name` | `string` | Optional | The location's business_name which is shown to its customers. For example,<br>this is the name printed on its customer's receipts. |
| `type` | [`str (Location Type)`](/doc/models/location-type.md) | Optional | Indicates the location's type. |
| `website_url` | `string` | Optional | The location's website, as set by the account owner in the Square dashboard.<br><br>Default: none; only exists if explicitly set. |
| `business_hours` | [`Business Hours`](/doc/models/business-hours.md) | Optional | Represents the hours of operation for a business location. |
| `business_email` | `string` | Optional | The email of the location. |
| `description` | `string` | Optional | The business description of the location. |
| `twitter_username` | `string` | Optional | The Twitter username of the location without the ' |
| `instagram_username` | `string` | Optional | The Instagram username of the location without the ' |
| `facebook_url` | `string` | Optional | The Facebook profile URL of the location. The URL should begin with 'facebook.com/'. |
| `coordinates` | [`Coordinates`](/doc/models/coordinates.md) | Optional | Latitude and longitude coordinates. |

### Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "address": null,
  "timezone": null,
  "capabilities": null,
  "status": null,
  "created_at": null,
  "merchant_id": null,
  "country": null,
  "language_code": null,
  "currency": null,
  "phone_number": null,
  "business_name": null,
  "type": null,
  "website_url": null,
  "business_hours": null,
  "business_email": null,
  "description": null,
  "twitter_username": null,
  "instagram_username": null,
  "facebook_url": null,
  "coordinates": null
}
```

