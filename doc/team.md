# Team

```python
team_api = client.team
```

## Class Name

`TeamApi`

## Methods

* [Create Team Member](/doc/team.md#create-team-member)
* [Bulk Create Team Members](/doc/team.md#bulk-create-team-members)
* [Bulk Update Team Members](/doc/team.md#bulk-update-team-members)
* [Search Team Members](/doc/team.md#search-team-members)
* [Retrieve Team Member](/doc/team.md#retrieve-team-member)
* [Update Team Member](/doc/team.md#update-team-member)
* [Retrieve Wage Setting](/doc/team.md#retrieve-wage-setting)
* [Update Wage Setting](/doc/team.md#update-wage-setting)

## Create Team Member

Creates a single `TeamMember` object. The `TeamMember` will be returned on successful creates.
You must provide the following values in your request to this endpoint:
- `first_name`
- `last_name`
Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#createteammember).

```python
def create_team_member(self,
                      body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Team Member Request`](/doc/models/create-team-member-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Team Member Response`](/doc/models/create-team-member-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = 'idempotency-key-0'
body['team_member'] = {}
body['team_member']['id'] = 'id2'
body['team_member']['reference_id'] = 'reference_id_1'
body['team_member']['is_owner'] = False
body['team_member']['status'] = 'ACTIVE'
body['team_member']['given_name'] = 'Joe'
body['team_member']['family_name'] = 'Doe'
body['team_member']['email_address'] = 'joe_doe@gmail.com'
body['team_member']['phone_number'] = '+14159283333'
body['team_member']['assigned_locations'] = {}
body['team_member']['assigned_locations']['assignment_type'] = 'EXPLICIT_LOCATIONS'
body['team_member']['assigned_locations']['location_ids'] = ['YSGH2WBKG94QZ', 'GA2Y9HSJ8KRYT']

result = team_api.create_team_member(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Bulk Create Team Members

Creates multiple `TeamMember` objects. The created `TeamMember` objects will be returned on successful creates.
This process is non-transactional and will process as much of the request as is possible. If one of the creates in
the request cannot be successfully processed, the request will NOT be marked as failed, but the body of the response
will contain explicit error information for this particular create.

Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#bulkcreateteammembers).

```python
def bulk_create_team_members(self,
                            body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Create Team Members Request`](/doc/models/bulk-create-team-members-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Bulk Create Team Members Response`](/doc/models/bulk-create-team-members-response.md)

### Example Usage

```python
body = {}
body['team_members'] = {}

result = team_api.bulk_create_team_members(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Bulk Update Team Members

Updates multiple `TeamMember` objects. The updated `TeamMember` objects will be returned on successful updates.
This process is non-transactional and will process as much of the request as is possible. If one of the updates in
the request cannot be successfully processed, the request will NOT be marked as failed, but the body of the response
will contain explicit error information for this particular update.
Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#bulkupdateteammembers).

```python
def bulk_update_team_members(self,
                            body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Update Team Members Request`](/doc/models/bulk-update-team-members-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Bulk Update Team Members Response`](/doc/models/bulk-update-team-members-response.md)

### Example Usage

```python
body = {}
body['team_members'] = {}

result = team_api.bulk_update_team_members(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Team Members

Returns a paginated list of `TeamMember` objects for a business.
The list to be returned can be filtered by:
- location IDs **and**
- `is_active`

```python
def search_team_members(self,
                       body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Team Members Request`](/doc/models/search-team-members-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Team Members Response`](/doc/models/search-team-members-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['location_ids'] = ['0G5P3VGACMMQZ']
body['query']['filter']['status'] = 'ACTIVE'
body['limit'] = 10
body['cursor'] = 'cursor0'

result = team_api.search_team_members(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Team Member

Retrieve a `TeamMember` object for the given `TeamMember.id`
Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#retrieveteammember).

```python
def retrieve_team_member(self,
                        team_member_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to retrieve. |

### Response Type

[`Retrieve Team Member Response`](/doc/models/retrieve-team-member-response.md)

### Example Usage

```python
team_member_id = 'team_member_id0'

result = team_api.retrieve_team_member(team_member_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Team Member

Updates a single `TeamMember` object. The `TeamMember` will be returned on successful updates.
Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#updateteammember).

```python
def update_team_member(self,
                      team_member_id,
                      body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to update. |
| `body` | [`Update Team Member Request`](/doc/models/update-team-member-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Team Member Response`](/doc/models/update-team-member-response.md)

### Example Usage

```python
team_member_id = 'team_member_id0'
body = {}
body['team_member'] = {}
body['team_member']['id'] = 'id2'
body['team_member']['reference_id'] = 'reference_id_1'
body['team_member']['is_owner'] = False
body['team_member']['status'] = 'ACTIVE'
body['team_member']['given_name'] = 'Joe'
body['team_member']['family_name'] = 'Doe'
body['team_member']['email_address'] = 'joe_doe@gmail.com'
body['team_member']['phone_number'] = '+14159283333'
body['team_member']['assigned_locations'] = {}
body['team_member']['assigned_locations']['assignment_type'] = 'EXPLICIT_LOCATIONS'
body['team_member']['assigned_locations']['location_ids'] = ['YSGH2WBKG94QZ', 'GA2Y9HSJ8KRYT']

result = team_api.update_team_member(team_member_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Wage Setting

Retrieve a `WageSetting` object for a team member specified
by `TeamMember.id`.
Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#retrievewagesetting).

```python
def retrieve_wage_setting(self,
                         team_member_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to retrieve wage setting for |

### Response Type

[`Retrieve Wage Setting Response`](/doc/models/retrieve-wage-setting-response.md)

### Example Usage

```python
team_member_id = 'team_member_id0'

result = team_api.retrieve_wage_setting(team_member_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Wage Setting

Creates or updates a `WageSetting` object. The object is created if a
`WageSetting` with the specified `team_member_id` does not exist. Otherwise,
it fully replaces the `WageSetting` object for the team member.
The `WageSetting` will be returned upon successful update.
Learn about [Troubleshooting the Teams API](https://developer.squareup.com/docs/docs/team/troubleshooting#updatewagesetting).

```python
def update_wage_setting(self,
                       team_member_id,
                       body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to update the `WageSetting` object for. |
| `body` | [`Update Wage Setting Request`](/doc/models/update-wage-setting-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Wage Setting Response`](/doc/models/update-wage-setting-response.md)

### Example Usage

```python
team_member_id = 'team_member_id0'
body = {}
body['wage_setting'] = {}
body['wage_setting']['team_member_id'] = 'team_member_id2'
body['wage_setting']['job_assignments'] = []

body['wage_setting']['job_assignments'].append({})
body['wage_setting']['job_assignments'][0]['job_title'] = 'Manager'
body['wage_setting']['job_assignments'][0]['pay_type'] = 'SALARY'
body['wage_setting']['job_assignments'][0]['hourly_rate'] = {}
body['wage_setting']['job_assignments'][0]['hourly_rate']['amount'] = 117
body['wage_setting']['job_assignments'][0]['hourly_rate']['currency'] = 'ERN'
body['wage_setting']['job_assignments'][0]['annual_rate'] = {}
body['wage_setting']['job_assignments'][0]['annual_rate']['amount'] = 3000000
body['wage_setting']['job_assignments'][0]['annual_rate']['currency'] = 'USD'
body['wage_setting']['job_assignments'][0]['weekly_hours'] = 40

body['wage_setting']['job_assignments'].append({})
body['wage_setting']['job_assignments'][1]['job_title'] = 'Cashier'
body['wage_setting']['job_assignments'][1]['pay_type'] = 'HOURLY'
body['wage_setting']['job_assignments'][1]['hourly_rate'] = {}
body['wage_setting']['job_assignments'][1]['hourly_rate']['amount'] = 1200
body['wage_setting']['job_assignments'][1]['hourly_rate']['currency'] = 'USD'
body['wage_setting']['job_assignments'][1]['annual_rate'] = {}
body['wage_setting']['job_assignments'][1]['annual_rate']['amount'] = 58
body['wage_setting']['job_assignments'][1]['annual_rate']['currency'] = 'DZD'
body['wage_setting']['job_assignments'][1]['weekly_hours'] = 226

body['wage_setting']['is_overtime_exempt'] = True
body['wage_setting']['version'] = 122
body['wage_setting']['created_at'] = 'created_at0'

result = team_api.update_wage_setting(team_member_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

