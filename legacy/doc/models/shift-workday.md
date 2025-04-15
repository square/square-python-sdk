
# Shift Workday

A `Shift` search query filter parameter that sets a range of days that
a `Shift` must start or end in before passing the filter condition.

## Structure

`Shift Workday`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_range` | [`Date Range`](../../doc/models/date-range.md) | Optional | A range defined by two dates. Used for filtering a query for Connect v2<br>objects that have date properties. |
| `match_shifts_by` | [`str (Shift Workday Matcher)`](../../doc/models/shift-workday-matcher.md) | Optional | Defines the logic used to apply a workday filter. |
| `default_timezone` | `str` | Optional | Location-specific timezones convert workdays to datetime filters.<br>Every location included in the query must have a timezone or this field<br>must be provided as a fallback. Format: the IANA timezone database<br>identifier for the relevant timezone. |

## Example (as JSON)

```json
{
  "date_range": {
    "start_date": "start_date6",
    "end_date": "end_date2"
  },
  "match_shifts_by": "END_AT",
  "default_timezone": "default_timezone2"
}
```

