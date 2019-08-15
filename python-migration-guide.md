## Migration guide

Follow the instructions below to migrate your apps from the deprecated `squareconnect` library to the new `square`library.

### Install the new library

Install the [latest SDK](https://github.com/square/square-python-sdk) using pip:
```python
pip install squareup
```


### Update your code

1. Change all instances of `import 'squareconnect'` to `import 'square'`.
1. Replace models with plain Python dictionary equivalents.
1. Update client instantiation to follow the method outlined below.
1. Update code for accessing response data to follow the method outlined below.
1. Check `response.is_success` or `response.is_error` rather than rescuing
   exceptions for flow control.

We also recommend that you use method chaining to access APIs instead of explicitly instantiating them to simplify your code.

#### Client instantiation

```python
from square.client import Client

square = Client(
    access_token='YOUR ACCESS TOKEN'
)

response = square.API.ENDPOINT(body=BODY)
```

#### Accessing response data

```python
if response.is_success():
    print({response.body})
elif response.is_error():
    print({response.errors})
```

### An example code migration

As a specific example, consider the following code for creating a new customer from this dictionary:

```python
new_customer = {
 'given_name': 'Ava',
 'address': {
   'address_line_1': '555 Electric Ave',
   'locality': 'Los Angeles',
   'country': 'US'
 }
}
```

With the deprecated `squareconnect` library, this is how you instantiate a client for the Customers API, format the request, and call the endpoint:
```python
from squareconnect import ApiClient
from squareconnect.rest import ApiException
from squareconnect.apis.customers_api import CustomersApi
from squareconnect.models.create_customer_request import CreateCustomerRequest

# Instantiate the client
api_client = ApiClient()
api_client.configuration.access_token = 'YOUR ACCESS TOKEN'
api_instance = CustomersApi(api_client)
create_customer_request = CreateCustomerRequest(
    given_name=new_customer['given_name'],
    address=new_customer['address'],
)

try:
    api_response = api_instance.create_customer(create_customer_request)
    print(f"Success: {api_response.customer}")
except ApiException as err:
    print(f"Exception when calling CustomersApi->create_customer: {err}")
```

Now consider equivalent code using the new `square` library:

```python
from square.client import Client
# Initialize client
client = Client(
    access_token='YOUR ACCESS TOKEN',
)
 
# Get an instance of the Square API you want call
api_customers = client.customers

# Call create_customer method to create a new customer
result = api_customers.create_customer(new_customer)
if result.is_success():
    # Display the response as text
    print(f"Success: {result.text}")
# Call the error method to see if the call failed
elif result.is_error():
    print(f"Errors: {result.errors}")
```

That's it! What was once a multi-block process can be handled in 2 lines of code and an `if/elif` block. Migrating to the `square` library reduces boilerplate and lets you can focus on the parts of your code that really matter.

### Ask the Community

Please join us in our [Square developer community](https://squ.re/slack) if you
have any questions!
