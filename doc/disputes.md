# Disputes

```python
disputes_api = client.disputes
```

## Class Name

`DisputesApi`

## Methods

* [List Disputes](/doc/disputes.md#list-disputes)
* [Retrieve Dispute](/doc/disputes.md#retrieve-dispute)
* [Accept Dispute](/doc/disputes.md#accept-dispute)
* [List Dispute Evidence](/doc/disputes.md#list-dispute-evidence)
* [Remove Dispute Evidence](/doc/disputes.md#remove-dispute-evidence)
* [Retrieve Dispute Evidence](/doc/disputes.md#retrieve-dispute-evidence)
* [Create Dispute Evidence File](/doc/disputes.md#create-dispute-evidence-file)
* [Create Dispute Evidence Text](/doc/disputes.md#create-dispute-evidence-text)
* [Submit Evidence](/doc/disputes.md#submit-evidence)

## List Disputes

Returns a list of disputes associated
with a particular account.

```python
def list_disputes(self,
                 cursor=None,
                 states=None,
                 location_id=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br>For more information, see [Paginating](https://developer.squareup.com/docs/basics/api101/pagination). |
| `states` | [`str (Dispute State)`](/doc/models/dispute-state.md) | Query, Optional | The dispute states to filter the result.<br>If not specified, the endpoint<br>returns all open disputes (dispute status is not<br>`INQUIRY_CLOSED`, `WON`, or `LOST`). |
| `location_id` | `string` | Query, Optional | The ID of the location for which to return <br>a list of disputes. If not specified,<br>the endpoint returns all open disputes<br>(dispute status is not `INQUIRY_CLOSED`, `WON`, or <br>`LOST`) associated with all locations. |

### Response Type

[`List Disputes Response`](/doc/models/list-disputes-response.md)

### Example Usage

```python
cursor = 'cursor6'
states = 'EVIDENCE_REQUIRED'
location_id = 'location_id4'

result = disputes_api.list_disputes(cursor, states, location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Dispute

Returns details of a specific dispute.

```python
def retrieve_dispute(self,
                    dispute_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | The ID of the dispute you want more details about. |

### Response Type

[`Retrieve Dispute Response`](/doc/models/retrieve-dispute-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.retrieve_dispute(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Accept Dispute

Accepts loss on a dispute. Square returns
the disputed amount to the cardholder and updates the
dispute state to ACCEPTED.

Square debits the disputed amount from the seller’s Square
account. If the Square account balance does not have
sufficient funds, Square debits the associated bank account.
For an overview of the Disputes API, see [Overview](https://developer.squareup.com/docs/docs/disputes-api/overview).

```python
def accept_dispute(self,
                  dispute_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | ID of the dispute you want to accept. |

### Response Type

[`Accept Dispute Response`](/doc/models/accept-dispute-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.accept_dispute(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Dispute Evidence

Returns a list of evidence associated with a dispute.

```python
def list_dispute_evidence(self,
                         dispute_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | The ID of the dispute. |

### Response Type

[`List Dispute Evidence Response`](/doc/models/list-dispute-evidence-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.list_dispute_evidence(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Remove Dispute Evidence

Removes specified evidence from a dispute.

Square does not send the bank any evidence that
is removed. Also, you cannot remove evidence after
submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/docs/reference/square/disputes-api/submit-evidence).

```python
def remove_dispute_evidence(self,
                           dispute_id,
                           evidence_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | The ID of the dispute you want to remove evidence from. |
| `evidence_id` | `string` | Template, Required | The ID of the evidence you want to remove. |

### Response Type

[`Remove Dispute Evidence Response`](/doc/models/remove-dispute-evidence-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'
evidence_id = 'evidence_id2'

result = disputes_api.remove_dispute_evidence(dispute_id, evidence_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Dispute Evidence

Returns the specific evidence metadata associated with a specific dispute.

You must maintain a copy of the evidence you upload if you want to
reference it later. You cannot download the evidence
after you upload it.

```python
def retrieve_dispute_evidence(self,
                             dispute_id,
                             evidence_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | The ID of the dispute that you want to retrieve evidence from. |
| `evidence_id` | `string` | Template, Required | The ID of the evidence to retrieve. |

### Response Type

[`Retrieve Dispute Evidence Response`](/doc/models/retrieve-dispute-evidence-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'
evidence_id = 'evidence_id2'

result = disputes_api.retrieve_dispute_evidence(dispute_id, evidence_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Dispute Evidence File

Uploads a file to use as evidence in a dispute challenge. The endpoint accepts
HTTP multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG,
and TIFF formats.
For more information, see [Challenge a Dispute](https://developer.squareup.com/docs/docs/disputes-api/process-disputes#challenge-a-dispute).

```python
def create_dispute_evidence_file(self,
                                dispute_id,
                                request=None,
                                image_file=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | ID of the dispute you want to upload evidence for. |
| `request` | [`Create Dispute Evidence File Request`](/doc/models/create-dispute-evidence-file-request.md) | Form, Optional | Defines parameters for a CreateDisputeEvidenceFile request. |
| `image_file` | `typing.BinaryIO` | Form, Optional | - |

### Response Type

[`Create Dispute Evidence File Response`](/doc/models/create-dispute-evidence-file-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'
request = {}
request['idempotency_key'] = 'idempotency_key2'
request['evidence_type'] = 'REBUTTAL_EXPLANATION'
request['content_type'] = 'content_type0'
image_file = FileWrapper(open('dummy_file', 'rb'), 'optional-content-type')

result = disputes_api.create_dispute_evidence_file(dispute_id, request, image_file)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Dispute Evidence Text

Uploads text to use as evidence for a dispute challenge. For more information, see
[Challenge a Dispute](https://developer.squareup.com/docs/docs/disputes-api/process-disputes#challenge-a-dispute).

```python
def create_dispute_evidence_text(self,
                                dispute_id,
                                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | The ID of the dispute you want to upload evidence for. |
| `body` | [`Create Dispute Evidence Text Request`](/doc/models/create-dispute-evidence-text-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Dispute Evidence Text Response`](/doc/models/create-dispute-evidence-text-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'
body = {}
body['idempotency_key'] = 'ed3ee3933d946f1514d505d173c82648'
body['evidence_type'] = 'TRACKING_NUMBER'
body['evidence_text'] = '1Z8888888888888888'

result = disputes_api.create_dispute_evidence_text(dispute_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Submit Evidence

Submits evidence to the cardholder's bank.

Before submitting evidence, Square compiles all available evidence. This includes
evidence uploaded using the
[CreateDisputeEvidenceFile](https://developer.squareup.com/docs/reference/square/disputes-api/create-dispute-evidence-file) and
[CreateDisputeEvidenceText](https://developer.squareup.com/docs/reference/square/disputes-api/create-dispute-evidence-text) endpoints,
and evidence automatically provided by Square, when
available. For more information, see
[Challenge a Dispute](https://developer.squareup.com/docs/docs/disputes-api/process-disputes#challenge-a-dispute).

```python
def submit_evidence(self,
                   dispute_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Template, Required | The ID of the dispute you want to submit evidence for. |

### Response Type

[`Submit Evidence Response`](/doc/models/submit-evidence-response.md)

### Example Usage

```python
dispute_id = 'dispute_id2'

result = disputes_api.submit_evidence(dispute_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

