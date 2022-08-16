
# Customer Filter

Represents a set of `CustomerQuery` filters used to limit the set of
customers returned by the [SearchCustomers](../../doc/api/customers.md#search-customers) endpoint.

## Structure

`Customer Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creation_source` | [`Customer Creation Source Filter`](../../doc/models/customer-creation-source-filter.md) | Optional | The creation source filter.<br><br>If one or more creation sources are set, customer profiles are included in,<br>or excluded from, the result if they match at least one of the filter criteria. |
| `created_at` | [`Time Range`](../../doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC 3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevant endpoint-specific documentation to determine<br>how time ranges are handled. |
| `updated_at` | [`Time Range`](../../doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC 3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevant endpoint-specific documentation to determine<br>how time ranges are handled. |
| `email_address` | [`Customer Text Filter`](../../doc/models/customer-text-filter.md) | Optional | A filter to select customers based on exact or fuzzy matching of<br>customer attributes against a specified query. Depending on the customer attributes,<br>the filter can be case-sensitive. This filter can be exact or fuzzy, but it cannot be both. |
| `phone_number` | [`Customer Text Filter`](../../doc/models/customer-text-filter.md) | Optional | A filter to select customers based on exact or fuzzy matching of<br>customer attributes against a specified query. Depending on the customer attributes,<br>the filter can be case-sensitive. This filter can be exact or fuzzy, but it cannot be both. |
| `reference_id` | [`Customer Text Filter`](../../doc/models/customer-text-filter.md) | Optional | A filter to select customers based on exact or fuzzy matching of<br>customer attributes against a specified query. Depending on the customer attributes,<br>the filter can be case-sensitive. This filter can be exact or fuzzy, but it cannot be both. |
| `group_ids` | [`Filter Value`](../../doc/models/filter-value.md) | Optional | A filter to select resources based on an exact field value. For any given<br>value, the value can only be in one property. Depending on the field, either<br>all properties can be set or only a subset will be available.<br><br>Refer to the documentation of the field. |
| `custom_attribute` | [`Customer Custom Attribute Filters`](../../doc/models/customer-custom-attribute-filters.md) | Optional | The custom attribute filters in a set of [customer filters](../../doc/models/customer-filter.md) used in a search query. Use this filter<br>to search based on [custom attributes](../../doc/models/custom-attribute.md) that are assigned to customer profiles. For more information, see<br>[Search by custom attribute](https://developer.squareup.com/docs/customers-api/use-the-api/search-customers#search-by-custom-attribute). |

## Example (as JSON)

```json
{
  "creation_source": null,
  "created_at": null,
  "updated_at": null,
  "email_address": null,
  "phone_number": null,
  "reference_id": null,
  "group_ids": null,
  "custom_attribute": null
}
```

