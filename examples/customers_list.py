from square.client import Client
from square.configuration import Configuration


client = Client(
    access_token='AccessToken',
)

customers_api = client.customers

result = customers_api.list()

if result.success():
    print(result.body)
elif result.error():
    print(result.errors)
