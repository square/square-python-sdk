## Customer Creation Source Filter

Creation source filter.

If one or more creation sources are set, customer profiles are included in,
or excluded from, the result if they match at least one of the filter
criteria.

### Structure

`CustomerCreationSourceFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `values` | [`List of str (Customer Creation Source)`]($m/CustomerCreationSource) | Optional | The list of creation sources used as filtering criteria.<br>See [CustomerCreationSource](#type-customercreationsource) for possible values |
| `rule` | [`str (Customer Inclusion Exclusion)`]($m/CustomerInclusionExclusion) | Optional | Indicates whether customers should be included in, or excluded from,<br>the result set when they match the filtering criteria. |

### Example (as JSON)

```json
{
  "values": null,
  "rule": null
}
```

