# Disputes

```python
disputes_api = client.disputes
```

## Class Name

`DisputesApi`

## Methods

* [List Disputes](../../doc/api/disputes.md#list-disputes)
* [Retrieve Dispute](../../doc/api/disputes.md#retrieve-dispute)
* [Accept Dispute](../../doc/api/disputes.md#accept-dispute)
* [List Dispute Evidence](../../doc/api/disputes.md#list-dispute-evidence)
* [Create Dispute Evidence File](../../doc/api/disputes.md#create-dispute-evidence-file)
* [Create Dispute Evidence Text](../../doc/api/disputes.md#create-dispute-evidence-text)
* [Delete Dispute Evidence](../../doc/api/disputes.md#delete-dispute-evidence)
* [Retrieve Dispute Evidence](../../doc/api/disputes.md#retrieve-dispute-evidence)
* [Submit Evidence](../../doc/api/disputes.md#submit-evidence)


# List Disputes

Returns a list of disputes associated with a particular account.

```python
def list_disputes(self,
                 cursor=None,
                 states=None,
                 location_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `states` | [`str (Dispute State)`](../../doc/models/dispute-state.md) | Query, Optional | The dispute states used to filter the result. If not specified, the endpoint returns all disputes. |
| `location_id` | `str` | Query, Optional | The ID of the location for which to return a list of disputes.<br>If not specified, the endpoint returns disputes associated with all locations. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Disputes Response`](../../doc/models/list-disputes-response.md).

## Example Usage

```python
result = disputes_api.list_disputes()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Dispute

Returns details about a specific dispute.

```python
def retrieve_dispute(self,
                    dispute_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute you want more details about. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Dispute Response`](../../doc/models/retrieve-dispute-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.retrieve_dispute(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Accept Dispute

Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
updates the dispute state to ACCEPTED.

Square debits the disputed amount from the seller’s Square account. If the Square account
does not have sufficient funds, Square debits the associated bank account.

```python
def accept_dispute(self,
                  dispute_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute you want to accept. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Accept Dispute Response`](../../doc/models/accept-dispute-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.accept_dispute(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Dispute Evidence

Returns a list of evidence associated with a dispute.

```python
def list_dispute_evidence(self,
                         dispute_id,
                         cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute. |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Dispute Evidence Response`](../../doc/models/list-dispute-evidence-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.list_dispute_evidence(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Dispute Evidence File

Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP
multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

```python
def create_dispute_evidence_file(self,
                                dispute_id,
                                request=None,
                                image_file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute for which you want to upload evidence. |
| `request` | [`Create Dispute Evidence File Request`](../../doc/models/create-dispute-evidence-file-request.md) | Form (JSON-Encoded), Optional | Defines the parameters for a `CreateDisputeEvidenceFile` request. |
| `image_file` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Dispute Evidence File Response`](../../doc/models/create-dispute-evidence-file-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.create_dispute_evidence_file(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Dispute Evidence Text

Uploads text to use as evidence for a dispute challenge.

```python
def create_dispute_evidence_text(self,
                                dispute_id,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute for which you want to upload evidence. |
| `body` | [`Create Dispute Evidence Text Request`](../../doc/models/create-dispute-evidence-text-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Dispute Evidence Text Response`](../../doc/models/create-dispute-evidence-text-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

body = {
    'idempotency_key': 'ed3ee3933d946f1514d505d173c82648',
    'evidence_text': '1Z8888888888888888',
    'evidence_type': 'TRACKING_NUMBER'
}

result = disputes_api.create_dispute_evidence_text(
    dispute_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Dispute Evidence

Removes specified evidence from a dispute.
Square does not send the bank any evidence that is removed.

```python
def delete_dispute_evidence(self,
                           dispute_id,
                           evidence_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute from which you want to remove evidence. |
| `evidence_id` | `str` | Template, Required | The ID of the evidence you want to remove. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Dispute Evidence Response`](../../doc/models/delete-dispute-evidence-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

evidence_id = 'evidence_id2'

result = disputes_api.delete_dispute_evidence(
    dispute_id,
    evidence_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Dispute Evidence

Returns the metadata for the evidence specified in the request URL path.

You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be downloaded after you upload it.

```python
def retrieve_dispute_evidence(self,
                             dispute_id,
                             evidence_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute from which you want to retrieve evidence metadata. |
| `evidence_id` | `str` | Template, Required | The ID of the evidence to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Dispute Evidence Response`](../../doc/models/retrieve-dispute-evidence-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

evidence_id = 'evidence_id2'

result = disputes_api.retrieve_dispute_evidence(
    dispute_id,
    evidence_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Submit Evidence

Submits evidence to the cardholder's bank.

The evidence submitted by this endpoint includes evidence uploaded
using the [CreateDisputeEvidenceFile](../../doc/api/disputes.md#create-dispute-evidence-file) and
[CreateDisputeEvidenceText](../../doc/api/disputes.md#create-dispute-evidence-text) endpoints and
evidence automatically provided by Square, when available. Evidence cannot be removed from
a dispute after submission.

```python
def submit_evidence(self,
                   dispute_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `str` | Template, Required | The ID of the dispute for which you want to submit evidence. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Submit Evidence Response`](../../doc/models/submit-evidence-response.md).

## Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.submit_evidence(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

