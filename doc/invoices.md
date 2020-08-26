# Invoices

```python
invoices_api = client.invoices
```

## Class Name

`InvoicesApi`

## Methods

* [List Invoices](/doc/invoices.md#list-invoices)
* [Create Invoice](/doc/invoices.md#create-invoice)
* [Search Invoices](/doc/invoices.md#search-invoices)
* [Delete Invoice](/doc/invoices.md#delete-invoice)
* [Get Invoice](/doc/invoices.md#get-invoice)
* [Update Invoice](/doc/invoices.md#update-invoice)
* [Cancel Invoice](/doc/invoices.md#cancel-invoice)
* [Publish Invoice](/doc/invoices.md#publish-invoice)

## List Invoices

Returns a list of invoices for a given location. The response 
is paginated. If truncated, the response includes a `cursor` that you    
use in a subsequent request to fetch the next set of invoices.
For more information about retrieving invoices, see [Retrieve invoices](https://developer.squareup.com/docs/docs/invoices-api/overview#retrieve-invoices).

```python
def list_invoices(self,
                 location_id,
                 cursor=None,
                 limit=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Query, Required | The ID of the location for which to list invoices. |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint. <br>Provide this cursor to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination). |
| `limit` | `int` | Query, Optional | The maximum number of invoices to return (200 is the maximum `limit`). <br>If not provided, the server <br>uses a default limit of 100 invoices. |

### Response Type

[`List Invoices Response`](/doc/models/list-invoices-response.md)

### Example Usage

```python
location_id = 'location_id4'
cursor = 'cursor6'
limit = 172

result = invoices_api.list_invoices(location_id, cursor, limit)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Invoice

Creates a draft [invoice](#type-invoice) 
for an order created using the Orders API.

A draft invoice remains in your account and no action is taken. 
You must publish the invoice before Square can process it (send it to the customer's email address or charge the customer’s card on file). 
For more information, see [Manage Invoices Using the Invoices API](https://developer.squareup.com/docs/docs/invoices-api/overview).

```python
def create_invoice(self,
                  body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Invoice Request`](/doc/models/create-invoice-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Invoice Response`](/doc/models/create-invoice-response.md)

### Example Usage

```python
body = {}
body['invoice'] = {}
body['invoice']['id'] = 'id0'
body['invoice']['version'] = 38
body['invoice']['location_id'] = 'ES0RJRZYEC39A'
body['invoice']['order_id'] = 'CAISENgvlJ6jLWAzERDzjyHVybY'
body['invoice']['primary_recipient'] = {}
body['invoice']['primary_recipient']['customer_id'] = 'JDKYHBWT1D4F8MFH63DBMEN8Y4'
body['invoice']['primary_recipient']['given_name'] = 'given_name6'
body['invoice']['primary_recipient']['family_name'] = 'family_name8'
body['invoice']['primary_recipient']['email_address'] = 'email_address2'
body['invoice']['primary_recipient']['address'] = {}
body['invoice']['primary_recipient']['address']['address_line_1'] = 'address_line_10'
body['invoice']['primary_recipient']['address']['address_line_2'] = 'address_line_20'
body['invoice']['primary_recipient']['address']['address_line_3'] = 'address_line_36'
body['invoice']['primary_recipient']['address']['locality'] = 'locality0'
body['invoice']['primary_recipient']['address']['sublocality'] = 'sublocality0'
body['invoice']['payment_requests'] = []

body['invoice']['payment_requests'].append({})
body['invoice']['payment_requests'][0]['uid'] = 'uid4'
body['invoice']['payment_requests'][0]['request_method'] = 'EMAIL'
body['invoice']['payment_requests'][0]['request_type'] = 'BALANCE'
body['invoice']['payment_requests'][0]['due_date'] = '2030-01-24'
body['invoice']['payment_requests'][0]['fixed_amount_requested_money'] = {}
body['invoice']['payment_requests'][0]['fixed_amount_requested_money']['amount'] = 52
body['invoice']['payment_requests'][0]['fixed_amount_requested_money']['currency'] = 'USS'
body['invoice']['payment_requests'][0]['tipping_enabled'] = True
body['invoice']['payment_requests'][0]['reminders'] = []

body['invoice']['payment_requests'][0]['reminders'].append({})
body['invoice']['payment_requests'][0]['reminders'][0]['uid'] = 'uid2'
body['invoice']['payment_requests'][0]['reminders'][0]['relative_scheduled_days'] = -1
body['invoice']['payment_requests'][0]['reminders'][0]['message'] = 'Your invoice is due tomorrow'
body['invoice']['payment_requests'][0]['reminders'][0]['status'] = 'PENDING'
body['invoice']['payment_requests'][0]['reminders'][0]['sent_at'] = 'sent_at2'


body['invoice']['invoice_number'] = 'inv-100'
body['invoice']['title'] = 'Event Planning Services'
body['invoice']['description'] = 'We appreciate your business!'
body['invoice']['scheduled_at'] = '2030-01-13T10:00:00Z'
body['idempotency_key'] = 'ce3748f9-5fc1-4762-aa12-aae5e843f1f4'

result = invoices_api.create_invoice(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Invoices

Searches for invoices from a location specified in 
the filter. You can optionally specify customers in the filter for whom to 
retrieve invoices. In the current implementation, you can only specify one location and 
optionally one customer.

The response is paginated. If truncated, the response includes a `cursor` 
that you use in a subsequent request to fetch the next set of invoices. 
For more information about retrieving invoices, see [Retrieve invoices](https://developer.squareup.com/docs/docs/invoices-api/overview#retrieve-invoices).

```python
def search_invoices(self,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Invoices Request`](/doc/models/search-invoices-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Invoices Response`](/doc/models/search-invoices-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['location_ids'] = ['ES0RJRZYEC39A']
body['query']['filter']['customer_ids'] = ['JDKYHBWT1D4F8MFH63DBMEN8Y4']
body['query']['sort'] = {}
body['query']['sort']['field'] = 'INVOICE_SORT_DATE'
body['query']['sort']['order'] = 'DESC'
body['limit'] = 164
body['cursor'] = 'cursor0'

result = invoices_api.search_invoices(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Delete Invoice

Deletes the specified invoice. When an invoice is deleted, the 
associated Order status changes to CANCELED. You can only delete a draft 
invoice (you cannot delete an invoice scheduled for publication, or a 
published invoice).

```python
def delete_invoice(self,
                  invoice_id,
                  version=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `string` | Template, Required | The ID of the invoice to delete. |
| `version` | `int` | Query, Optional | The version of the [invoice](#type-invoice) to delete.<br>If you do not know the version, you can call [GetInvoice](#endpoint-Invoices-GetInvoice) or <br>[ListInvoices](#endpoint-Invoices-ListInvoices). |

### Response Type

[`Delete Invoice Response`](/doc/models/delete-invoice-response.md)

### Example Usage

```python
invoice_id = 'invoice_id0'
version = 172

result = invoices_api.delete_invoice(invoice_id, version)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Invoice

Retrieves an invoice by invoice ID.

```python
def get_invoice(self,
               invoice_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `string` | Template, Required | The id of the invoice to retrieve. |

### Response Type

[`Get Invoice Response`](/doc/models/get-invoice-response.md)

### Example Usage

```python
invoice_id = 'invoice_id0'

result = invoices_api.get_invoice(invoice_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Invoice

Updates an invoice by modifying field values, clearing field values, or both 
as specified in the request. 
There are no restrictions to updating an invoice in a draft state. 
However, there are guidelines for updating a published invoice. 
For more information, see [Update an invoice](https://developer.squareup.com/docs/docs/invoices-api/overview#update-an-invoice).

```python
def update_invoice(self,
                  invoice_id,
                  body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `string` | Template, Required | The id of the invoice to update. |
| `body` | [`Update Invoice Request`](/doc/models/update-invoice-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Invoice Response`](/doc/models/update-invoice-response.md)

### Example Usage

```python
invoice_id = 'invoice_id0'
body = {}
body['invoice'] = {}
body['invoice']['id'] = 'id0'
body['invoice']['version'] = 38
body['invoice']['location_id'] = 'location_id4'
body['invoice']['order_id'] = 'order_id6'
body['invoice']['primary_recipient'] = {}
body['invoice']['primary_recipient']['customer_id'] = 'customer_id2'
body['invoice']['primary_recipient']['given_name'] = 'given_name6'
body['invoice']['primary_recipient']['family_name'] = 'family_name8'
body['invoice']['primary_recipient']['email_address'] = 'email_address2'
body['invoice']['primary_recipient']['address'] = {}
body['invoice']['primary_recipient']['address']['address_line_1'] = 'address_line_10'
body['invoice']['primary_recipient']['address']['address_line_2'] = 'address_line_20'
body['invoice']['primary_recipient']['address']['address_line_3'] = 'address_line_36'
body['invoice']['primary_recipient']['address']['locality'] = 'locality0'
body['invoice']['primary_recipient']['address']['sublocality'] = 'sublocality0'
body['invoice']['payment_requests'] = []

body['invoice']['payment_requests'].append({})
body['invoice']['payment_requests'][0]['uid'] = '2da7964f-f3d2-4f43-81e8-5aa220bf3355'
body['invoice']['payment_requests'][0]['request_method'] = 'EMAIL'
body['invoice']['payment_requests'][0]['request_type'] = 'DEPOSIT'
body['invoice']['payment_requests'][0]['due_date'] = 'due_date2'
body['invoice']['payment_requests'][0]['fixed_amount_requested_money'] = {}
body['invoice']['payment_requests'][0]['fixed_amount_requested_money']['amount'] = 52
body['invoice']['payment_requests'][0]['fixed_amount_requested_money']['currency'] = 'USS'
body['invoice']['payment_requests'][0]['tipping_enabled'] = False

body['idempotency_key'] = '4ee82288-0910-499e-ab4c-5d0071dad1be'
body['fields_to_clear'] = ['payments_requests[2da7964f-f3d2-4f43-81e8-5aa220bf3355].reminders']

result = invoices_api.update_invoice(invoice_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Cancel Invoice

Cancels an invoice. The seller cannot collect payments for 
the canceled invoice.

You cannot cancel an invoice in a terminal state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.

```python
def cancel_invoice(self,
                  invoice_id,
                  body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `string` | Template, Required | The ID of the [invoice](#type-invoice) to cancel. |
| `body` | [`Cancel Invoice Request`](/doc/models/cancel-invoice-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Cancel Invoice Response`](/doc/models/cancel-invoice-response.md)

### Example Usage

```python
invoice_id = 'invoice_id0'
body = {}
body['version'] = 0

result = invoices_api.cancel_invoice(invoice_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Publish Invoice

Publishes the specified draft invoice. 

After an invoice is published, Square 
follows up based on the invoice configuration. For example, Square 
sends the invoice to the customer's email address, charges the customer's card on file, or does 
nothing. Square also makes the invoice available on a Square-hosted invoice page. 

The invoice `status` also changes from `DRAFT` to a status 
based on the invoice configuration. For example, the status changes to `UNPAID` if 
Square emails the invoice or `PARTIALLY_PAID` if Square charge a card on file for a portion of the 
invoice amount).

For more information, see 
[Create and publish an invoice](https://developer.squareup.com/docs/docs/invoices-api/overview#create-and-publish-an-invoice).

```python
def publish_invoice(self,
                   invoice_id,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `string` | Template, Required | The id of the invoice to publish. |
| `body` | [`Publish Invoice Request`](/doc/models/publish-invoice-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Publish Invoice Response`](/doc/models/publish-invoice-response.md)

### Example Usage

```python
invoice_id = 'invoice_id0'
body = {}
body['version'] = 1
body['idempotency_key'] = '32da42d0-1997-41b0-826b-f09464fc2c2e'

result = invoices_api.publish_invoice(invoice_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

