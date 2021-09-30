from square.client import Client
from square.configuration import Configuration


client = Client(
    access_token='AccessToken',
)

customers_api = client.customers

customer_id = 'customer_id'

result = customers_api.delete_customer(customer_id)

if result.is_success():
    print(result.body)
    print("success")
elif result.is_error():
    print(result.errors)
