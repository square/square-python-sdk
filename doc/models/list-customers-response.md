## List Customers Response

Defines the fields that are included in the response body of
a request to the ListCustomers endpoint.

One of `errors` or `customers` is present in a given response (never both).

### Structure

`ListCustomersResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `customers` | [`List of Customer`](/doc/models/customer.md) | Optional | An array of `Customer` objects that match your query. |
| `cursor` | `string` | Optional | A pagination cursor to retrieve the next set of results for your<br>original query to the endpoint. This value is present only if the request<br>succeeded and additional results are available.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |

### Example (as JSON)

```json
{
  "customers": [
    {
      "id": "JDKYHBWT1D4F8MFH63DBMEN8Y4",
      "created_at": "2016-03-23T20:21:54.859Z",
      "updated_at": "2016-03-23T20:21:55Z",
      "given_name": "Amelia",
      "family_name": "Earhart",
      "email_address": "Amelia.Earhart@example.com",
      "address": {
        "address_line_1": "500 Electric Ave",
        "address_line_2": "Suite 600",
        "locality": "New York",
        "administrative_district_level_1": "NY",
        "postal_code": "10003",
        "country": "US"
      },
      "phone_number": "1-212-555-4240",
      "reference_id": "YOUR_REFERENCE_ID",
      "note": "a customer",
      "groups": [
        {
          "id": "16894e93-96eb-4ced-b24b-f71d42bf084c",
          "name": "Aviation Enthusiasts"
        }
      ]
    }
  ]
}
```

