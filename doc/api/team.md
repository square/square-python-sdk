# Team

```python
team_api = client.team
```

## Class Name

`TeamApi`

## Methods

* [Create Team Member](../../doc/api/team.md#create-team-member)
* [Bulk Create Team Members](../../doc/api/team.md#bulk-create-team-members)
* [Bulk Update Team Members](../../doc/api/team.md#bulk-update-team-members)
* [Search Team Members](../../doc/api/team.md#search-team-members)
* [Retrieve Team Member](../../doc/api/team.md#retrieve-team-member)
* [Update Team Member](../../doc/api/team.md#update-team-member)
* [Retrieve Wage Setting](../../doc/api/team.md#retrieve-wage-setting)
* [Update Wage Setting](../../doc/api/team.md#update-wage-setting)


# Create Team Member

Creates a single `TeamMember` object. The `TeamMember` object is returned on successful creates.
You must provide the following values in your request to this endpoint:

- `given_name`
- `family_name`

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).

```python
def create_team_member(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Team Member Request`](../../doc/models/create-team-member-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Team Member Response`](../../doc/models/create-team-member-response.md)

## Example Usage

```python
body = {
    'idempotency_key': 'idempotency-key-0',
    'team_member': {
        'reference_id': 'reference_id_1',
        'status': 'ACTIVE',
        'given_name': 'Joe',
        'family_name': 'Doe',
        'email_address': 'joe_doe@gmail.com',
        'phone_number': '+14159283333',
        'assigned_locations': {
            'assignment_type': 'EXPLICIT_LOCATIONS',
            'location_ids': [
                'YSGH2WBKG94QZ',
                'GA2Y9HSJ8KRYT'
            ]
        }
    }
}

result = team_api.create_team_member(body)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Create Team Members

Creates multiple `TeamMember` objects. The created `TeamMember` objects are returned on successful creates.
This process is non-transactional and processes as much of the request as possible. If one of the creates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed create.

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).

```python
def bulk_create_team_members(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Create Team Members Request`](../../doc/models/bulk-create-team-members-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Bulk Create Team Members Response`](../../doc/models/bulk-create-team-members-response.md)

## Example Usage

```python
body = {
    'team_members': {
        "idempotency-key-1": {
            'team_member': {
                'reference_id': 'reference_id_1',
                'given_name': 'Joe',
                'family_name': 'Doe',
                'email_address': 'joe_doe@gmail.com',
                'phone_number': '+14159283333',
                'assigned_locations': {
                    'assignment_type': 'EXPLICIT_LOCATIONS',
                    'location_ids': [
                        'YSGH2WBKG94QZ',
                        'GA2Y9HSJ8KRYT'
                    ]
                }
            }
        },
        "idempotency-key-2": {
            'team_member': {
                'reference_id': 'reference_id_2',
                'given_name': 'Jane',
                'family_name': 'Smith',
                'email_address': 'jane_smith@gmail.com',
                'phone_number': '+14159223334',
                'assigned_locations': {
                    'assignment_type': 'ALL_CURRENT_AND_FUTURE_LOCATIONS'
                }
            }
        }
    }
}

result = team_api.bulk_create_team_members(body)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Update Team Members

Updates multiple `TeamMember` objects. The updated `TeamMember` objects are returned on successful updates.
This process is non-transactional and processes as much of the request as possible. If one of the updates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed update.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).

```python
def bulk_update_team_members(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Update Team Members Request`](../../doc/models/bulk-update-team-members-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Bulk Update Team Members Response`](../../doc/models/bulk-update-team-members-response.md)

## Example Usage

```python
body = {
    'team_members': {
        "AFMwA08kR-MIF-3Vs0OE": {
            'team_member': {
                'reference_id': 'reference_id_2',
                'is_owner': False,
                'status': 'ACTIVE',
                'given_name': 'Jane',
                'family_name': 'Smith',
                'email_address': 'jane_smith@gmail.com',
                'phone_number': '+14159223334',
                'assigned_locations': {
                    'assignment_type': 'ALL_CURRENT_AND_FUTURE_LOCATIONS'
                }
            }
        },
        "fpgteZNMaf0qOK-a4t6P": {
            'team_member': {
                'reference_id': 'reference_id_1',
                'is_owner': False,
                'status': 'ACTIVE',
                'given_name': 'Joe',
                'family_name': 'Doe',
                'email_address': 'joe_doe@gmail.com',
                'phone_number': '+14159283333',
                'assigned_locations': {
                    'assignment_type': 'EXPLICIT_LOCATIONS',
                    'location_ids': [
                        'YSGH2WBKG94QZ',
                        'GA2Y9HSJ8KRYT'
                    ]
                }
            }
        }
    }
}

result = team_api.bulk_update_team_members(body)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Team Members

Returns a paginated list of `TeamMember` objects for a business.
The list can be filtered by the following:

- location IDs
- `status`

```python
def search_team_members(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Team Members Request`](../../doc/models/search-team-members-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Team Members Response`](../../doc/models/search-team-members-response.md)

## Example Usage

```python
body = {
    'query': {
        'filter': {
            'location_ids': [
                '0G5P3VGACMMQZ'
            ],
            'status': 'ACTIVE'
        }
    },
    'limit': 10
}

result = team_api.search_team_members(body)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Team Member

Retrieves a `TeamMember` object for the given `TeamMember.id`.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).

```python
def retrieve_team_member(self,
                        team_member_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to retrieve. |

## Response Type

[`Retrieve Team Member Response`](../../doc/models/retrieve-team-member-response.md)

## Example Usage

```python
team_member_id = 'team_member_id0'

result = team_api.retrieve_team_member(team_member_id)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Team Member

Updates a single `TeamMember` object. The `TeamMember` object is returned on successful updates.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).

```python
def update_team_member(self,
                      team_member_id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to update. |
| `body` | [`Update Team Member Request`](../../doc/models/update-team-member-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Update Team Member Response`](../../doc/models/update-team-member-response.md)

## Example Usage

```python
team_member_id = 'team_member_id0'

body = {
    'team_member': {
        'reference_id': 'reference_id_1',
        'status': 'ACTIVE',
        'given_name': 'Joe',
        'family_name': 'Doe',
        'email_address': 'joe_doe@gmail.com',
        'phone_number': '+14159283333',
        'assigned_locations': {
            'assignment_type': 'EXPLICIT_LOCATIONS',
            'location_ids': [
                'YSGH2WBKG94QZ',
                'GA2Y9HSJ8KRYT'
            ]
        }
    }
}

result = team_api.update_team_member(
    team_member_id,
    body
)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Wage Setting

Retrieves a `WageSetting` object for a team member specified
by `TeamMember.id`.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

```python
def retrieve_wage_setting(self,
                         team_member_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member for which to retrieve the wage setting. |

## Response Type

[`Retrieve Wage Setting Response`](../../doc/models/retrieve-wage-setting-response.md)

## Example Usage

```python
team_member_id = 'team_member_id0'

result = team_api.retrieve_wage_setting(team_member_id)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Wage Setting

Creates or updates a `WageSetting` object. The object is created if a
`WageSetting` with the specified `team_member_id` does not exist. Otherwise,
it fully replaces the `WageSetting` object for the team member.
The `WageSetting` is returned on a successful update.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

```python
def update_wage_setting(self,
                       team_member_id,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member for which to update the `WageSetting` object. |
| `body` | [`Update Wage Setting Request`](../../doc/models/update-wage-setting-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Update Wage Setting Response`](../../doc/models/update-wage-setting-response.md)

## Example Usage

```python
team_member_id = 'team_member_id0'

body = {
    'wage_setting': {
        'job_assignments': [
            {
                'job_title': 'Manager',
                'pay_type': 'SALARY',
                'annual_rate': {
                    'amount': 3000000,
                    'currency': 'USD'
                },
                'weekly_hours': 40
            },
            {
                'job_title': 'Cashier',
                'pay_type': 'HOURLY',
                'hourly_rate': {
                    'amount': 1200,
                    'currency': 'USD'
                }
            }
        ],
        'is_overtime_exempt': True
    }
}

result = team_api.update_wage_setting(
    team_member_id,
    body
)
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

