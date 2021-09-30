from square.client import Client
from square.configuration import Configuration


client = Client(
    access_token='AccessToken',
)

customers_api = client.customers

result = customers_api.list_customers()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
