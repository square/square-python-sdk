![Square logo]

# Square Python SDK

[![Travis status](https://travis-ci.org/square/square-python-sdk.svg?branch=master)](https://travis-ci.org/square/square-python-sdk)
[![PyPi version](https://badge.fury.io/py/squareup.svg?new)](https://badge.fury.io/py/squareup)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Use this Python library to manage Square resources (payments, orders, items, inventory, etc.) for your own Square account or on behalf of Square sellers.

## Requirements

The SDK supports the following versions of Python:
* Python 2 versions 2.7.9 and later
* Python 3 versions 3.4 and later

## Installation

Install the latest SDK using pip:

```sh
pip install squareup
```

Alternatively in Python 3, you can download or clone the sdk from [Python SDK] and then install the SDK by running Setuptools in the SDK installation directory:

```sh
python setup.py install --user
```

In Python 2, you can install via pip:

```sh
pip install -r requirement.txt
pip install -r test-requirements.txt
```

### API Client
* [Client]

## API documentation

### Payments
* [Payments]
* [Refunds]
* [Disputes]
* [Checkout]
* [Apple Pay]
* [Terminal]

### Orders
* [Orders]

### Subscriptions
* [Subscriptions]

### Invoices
* [Invoices]

### Items
* [Catalog]
* [Inventory]

### Customers
* [Customers]
* [Customer Groups]
* [Customer Segments]

### Loyalty
* [Loyalty]

### Bookings
* [Bookings]

### Business
* [Merchants]
* [Locations]
* [Devices]

### Team
* [Team]
* [Employees]
* [Labor]
* [Cash Drawers]

### Financials
* [Bank Accounts]

### Authorization APIs
* [Mobile Authorization]
* [O Auth]

### Deprecated APIs
* [V1 Employees]
* [V1 Transactions]
* [V1 Items]
* [Transactions]

## Usage

First time using Square? Here’s how to get started:

1. **Create a Square account.** If you don’t have one already, [sign up for a developer account].
1. **Create an application.** Go to your [Developer Dashboard] and create your first application. All you need to do is give it a name. When you’re doing this for your production application, enter the name as you would want a customer to see it.
1. **Make your first API call.** Almost all Square API calls require a location ID. You’ll make your first call to list_locations, which happens to be one of the API calls that don’t require a location ID. For more information about locations, see the [Locations overview].

Now let’s call your first Square API. Open your favorite text editor, create a new file called `locations.py`, and copy the following code into that file:

```python
from square.client import Client
 
# Create an instance of the API Client 
# and initialize it with the credentials 
# for the Square account whose assets you want to manage
 
client = Client(
    access_token='{{REPLACE_ACCESS_TOKEN}}',
    environment='sandbox',
)
 
# Get an instance of the Square API you want call
api_locations = client.locations
 
# Call list_locations method to get all locations in this Square account
result = api_locations.list_locations()
# Call the success method to see if the call succeeded
if result.is_success():
	# The body property is a list of locations
    locations = result.body['locations']
	# Iterate over the list
    for location in locations:
    	# Each location is represented as a dictionary
        for key, value in location.items():
        	print(f"{key} : {value}")
        print("\n")
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling LocationsApi.listlocations')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")
```

Next, get an access token and reference it in your code. To call the Square API, you need to get an access token and initialize the API Client class with that token. An application has two sets of credentials: production and sandbox. To get started, you’ll use your sandbox token so that you can try things out in a test environment that is completely separate from production. Here’s how:

1. Go back to your application in the Developer Dashboard.
1. View the details of your application.
1. Make sure that Sandbox Settings is set in the lower left corner.
1. In the Sandbox Token box, click Show to display the token.
1. Copy the sandbox access token.
1. In locations.py, replace {{REPLACE_ACCESS_TOKEN}} with that token.

You’ll notice in locations.py that the Client object is initialized with the environment set to sandbox. You use the environment parameter to specify whether you want to access production or sandbox resources.

**Important** When you eventually switch from trying things out on sandbox to actually working with your real production resources, you should not embed the access token in your code. Make sure you store and access your production access tokens securely.

Now save `locations.py` and run it:

```sh
python locations.py
```

If your call is successful, you’ll get a response that looks like this:

```
address : {'address_line_1': '1455 Market Street', 'administrative_district_level_1': 'CA', 'country': 'US', 'locality': 'San Francisco', 'postal_code': '94103'}
# ...
```

Yay! You successfully made your first call. If you didn’t, you would see an error message that looks something like this:

```
Error calling LocationsApi.listlocations
category : AUTHENTICATION_ERROR
code : UNAUTHORIZED
detail : This request could not be authorized.
```

This error was returned when an invalid token was used to call the API.

After you’ve tried out the Square APIs and tested your application using sandbox, you will want to switch to your production credentials so that you can manage real Square resources. Don't forget to switch your access token from sandbox to production for real data.

## SDK patterns
If you know a few patterns, you’ll be able to call any API in the SDK. Here are some important ones:

### Get an access token

To use the Square API to manage the resources (such as payments, orders, customers, etc.) of a Square account, you need to create an application (or use an existing one) in the Developer Dashboard and get an access token for that application.

When you call a Square API, you call it using an access token. An access token has specific permissions to resources in a specific Square account.
Use an access token that is appropriate for your use case. There are two options:

- To manage the resources for your own Square account, use the Personal Access Token for the application created in your Square account.
- To manage resources for other Square accounts, use OAuth to ask owners of the accounts you want to manage so that you can work on their behalf. When you implement OAuth, you ask the Square account holder for permission to manage resources in their account (you can define the specific resources to access) and get an OAuth access token and refresh token for their account. For more information, see the [OAuth overview].

**Important** For both use cases, make sure you store and access the tokens securely.

### Import and Instantiate the Client Class

To use the Square API, you import the Client class, instantiate a Client object, and initialize it with the appropriate access token and environment. Here’s how:

1. Import the Client class from the Square Python SDK module so you can call the Square API:
```python
from square.client import Client
```
1. Instantiate a Client object and initialize it with the access token for the Square account whose resources you want to manage and the environment that you want to use.

To access sandbox resources, initialize the Client with environment set to sandbox:

```python
client = Client(
    access_token='{{REPLACE_ACCESS_TOKEN}}',
    environment='sandbox',
)
```

To access production resources, set environment to production:

```ruby
client = Client(
    access_token='{{REPLACE_ACCESS_TOKEN}}',
    environment='production',
)
```
 
### Get an Instance of an API object and call its methods

Each API is implemented as a class. The Client object instantiates every API class and exposes them as properties so you can easily start using any Square API. You work with an API by calling methods on an instance of an API class. Here’s how:

**Work with an API by calling the methods on the API object.** For example, you would call list_customers to get a list of all customers in the Square account:

```python
result = square.customers.list_customers()
```
See the SDK documentation for the list of methods for each API class.

**Pass complex parameters (such as create, update, search, etc.) as a dictionary.** For example, you would pass a dictionary containing the values used to create a new customer using create_customer:

```python
# Create a unique key for this creation operation so you don't accidentally
# create the customer multiple times if you need to retry this operation.
import uuid
idempotency_key = str(uuid.uuid1())

# To create a customer, you only need 1 of 5 identity values but you'll be
# specifying two.
given_name = "Amelia"
family_name = "Earhardt"
request_body = {'idempotency_key': idempotency_key, 'given_name': given_name, 'family_name': family_name}

# Call create_customer method to create a new customer in this Square account
result = api_customers.create_customer(request_body)
```

If your call succeeds, you’ll see a response that looks like this:
```
{'customer': {'created_at': '2019-06-28T21:23:05.126Z', 'creation_source': 'THIRD_PARTY', 'family_name': 'Earhardt', 'given_name': 'Amelia', 'id': 'CBASEDwl3El91nohQ2FLEk4aBfcgAQ', 'preferences': {'email_unsubscribed': False}, 'updated_at': '2019-06-28T21:23:05.126Z'}}
```

**Use idempotency for create, update, or other calls that you want to avoid calling twice.** To make an idempotent API call, you add the idempotency_key with a unique value in the Hash for the API call’s request.

**Specify a location ID for APIs such as Transactions, Orders, and Checkout that deal with payments.** When a payment or order is created in Square, it is always associated with a location.

### Handle the response

API calls return an ApiResponse object that contains properties that describe both the request (headers and request) and the response (status_code, reason_phrase, text, errors, body, and cursor). Here’s how to handle the response:

**Check whether the response succeeded or failed.** ApiResponse has two helper methods that enable you to easily determine the success or failure of a call:

```python
if result.is_success():
	# Display the response as text
    print({result.text})
# Call the error method to see if the call failed
elif result.is_error():
    print(f"Errors: {result.errors}")
```

**Read the response payload.** The response payload is returned as text in the text property or as a dictionary in the body property. For retrieve calls, a dictionary containing a single item is returned with a key name that is the name of the object (for example, customer). For list calls, a dictionary containing a list of objects is returned with a key name that is the plural of the object name (for example, customers). If there are no objects for a list call to return, it returns an empty dictionary.

**Check the cursor for list operations.** Make sure you get all items returned in a list call by checking the cursor value returned in the API response. When you call a list API the first time, you set the cursor to an empty string in the API request. If the API response contains a cursor value, you call the API again to get the next page of items and continue to call that API again until the cursor is not returned in the API response. Here’s a code snippet that calls list_customers to count the total number of customers:

```python
# Initialize the customer count
total_customers = 0
# Initialize the cursor with an empty string since we are 
# calling list_customers for the first time
cursor = ""
# Count the total number of customers using the list_customers method
while True:
    # Call list_customers method to get all customers in this Square account
    result = api_customers.list_customers(cursor)
    if result.is_success():
        # If any customers are returned, the body property 
        # is a list with the name customers.
        # If there are no customers, APIResponse returns
        # an empty dictionary.
        if result.body:
            customers = result.body['customers']
            total_customers += len(customers)
            # Get the cursor if it exists in the result else set it to None
            cursor = result.body.get('cursor', None)
            print(f"cursor: {cursor}")
        else:
            print("No customers.")
            break
    # Call the error method to see if the call failed
    elif result.is_error():
        print(f"Errors: {result.errors}")
        break
    
    # If there is no cursor, we are at the end of the list.
    if cursor == None:
        break

print(f"Total customers: {total_customers}")
```

## Tests

First, clone the repo locally and `cd` into the directory.

```sh
git clone https://github.com/square/square-python-sdk.git
cd square-python-sdk
```

Next, install dependencies.

```sh
pip install -r test-requirements.txt
```

Before running the tests, find a sandbox token in your [Developer Dashboard] and set a `SQUARE_SANDBOX_TOKEN` environment variable.

```sh
export SQUARE_SANDBOX_TOKEN="YOUR SANDBOX TOKEN HERE"
```

And run the tests.

```sh
nosetests tests
```

## Learn more

The Square Platform is built on the [Square API]. Square has a number of other SDKs that enable you to securely handle credit card information on both mobile and web so that you can process payments via the Square API. 

You can also use the Square API to create applications or services that work with payments, orders, inventory, etc. that have been created and managed in Square’s in-person hardware products (Square Point of Sale and Square Register).


[//]: # "Link anchor definitions"
[Square Logo]: https://docs.connect.squareup.com/images/github/github-square-logo.svg
[Developer Dashboard]: https://developer.squareup.com/apps
[Square API]: https://squareup.com/developers
[sign up for a developer account]: https://squareup.com/signup?v=developers
[Client]: doc/client.md
[Devices]: doc/api/devices.md
[Disputes]: doc/api/disputes.md
[Terminal]: doc/api/terminal.md
[Cash Drawers]: doc/api/cash-drawers.md
[Customer Groups]: doc/api/customer-groups.md
[Customer Segments]: doc/api/customer-segments.md
[Bank Accounts]: doc/api/bank-accounts.md
[Payments]: doc/api/payments.md
[Checkout]: doc/api/checkout.md
[Catalog]: doc/api/catalog.md
[Customers]: doc/api/customers.md
[Employees]: doc/api/employees.md
[Inventory]: doc/api/inventory.md
[Labor]: doc/api/labor.md
[Loyalty]: doc/api/loyalty.md
[Bookings]: doc/api/bookings.md
[Locations]: doc/api/locations.md
[Merchants]: doc/api/merchants.md
[Orders]: doc/api/orders.md
[Invoices]: doc/api/invoices.md
[Apple Pay]: doc/api/apple-pay.md
[Refunds]: doc/api/refunds.md
[Subscriptions]: doc/api/subscriptions.md
[Mobile Authorization]: doc/api/mobile-authorization.md
[O Auth]: doc/api/o-auth.md
[V1 Employees]: doc/api/v1-employees.md
[V1 Transactions]: doc/api/v1-transactions.md
[V1 Items]: doc/api/v1-items.md
[Transactions]: doc/api/transactions.md
[Team]: doc/api/team.md
[Python SDK]: https://github.com/square/square-python-sdk
[Locations overview]: https://developer.squareup.com/docs/locations-api/what-it-does
[OAuth overview]: https://developer.squareup.com/docs/oauth-api/what-it-does
