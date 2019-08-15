from square.client import Client
from square.configuration import Configuration


client = Client(
    access_token='AccessToken',
)

customers_api = client.customers

customer_id = 'customer_id'

result = customers_api.delete(customer_id)

if result.success():
    print(result.body)
    print("success")
elif result.error():
    print(result.errors)
