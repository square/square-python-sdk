# Reporting

```python
reporting_api = client.reporting
```

## Class Name

`ReportingApi`

## Methods

* [List Additional Recipient Receivable Refunds](/doc/reporting.md#list-additional-recipient-receivable-refunds)
* [List Additional Recipient Receivables](/doc/reporting.md#list-additional-recipient-receivables)

## List Additional Recipient Receivable Refunds

Returns a list of refunded transactions (across all possible originating locations) relating to monies
credited to the provided location ID by another Square account using the `additional_recipients` field in a transaction.

Max results per [page](#paginatingresults): 50

```python
def list_additional_recipient_receivable_refunds(self,
                                                location_id,
                                                begin_time=None,
                                                end_time=None,
                                                sort_order=None,
                                                cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to list AdditionalRecipientReceivableRefunds for. |
| `begin_time` | `string` | Query, Optional | The beginning of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time minus one year. |
| `end_time` | `string` | Query, Optional | The end of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time. |
| `sort_order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | The order in which results are listed in the response (`ASC` for<br>oldest first, `DESC` for newest first).<br><br>Default value: `DESC` |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |

### Response Type

[`List Additional Recipient Receivable Refunds Response`](/doc/models/list-additional-recipient-receivable-refunds-response.md)

### Example Usage

```python
location_id = 'location_id4'

result = reporting_api.list_additional_recipient_receivable_refunds(location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Additional Recipient Receivables

Returns a list of receivables (across all possible sending locations) representing monies credited
to the provided location ID by another Square account using the `additional_recipients` field in a transaction.

Max results per [page](#paginatingresults): 50

```python
def list_additional_recipient_receivables(self,
                                         location_id,
                                         begin_time=None,
                                         end_time=None,
                                         sort_order=None,
                                         cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to list AdditionalRecipientReceivables for. |
| `begin_time` | `string` | Query, Optional | The beginning of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time minus one year. |
| `end_time` | `string` | Query, Optional | The end of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time. |
| `sort_order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | The order in which results are listed in the response (`ASC` for<br>oldest first, `DESC` for newest first).<br><br>Default value: `DESC` |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |

### Response Type

[`List Additional Recipient Receivables Response`](/doc/models/list-additional-recipient-receivables-response.md)

### Example Usage

```python
location_id = 'location_id4'

result = reporting_api.list_additional_recipient_receivables(location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

