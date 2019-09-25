## Customer Sort Field

Indicates the sort criteria for a list of Customers.

### Enumeration

`CustomerSortField`

### Fields

| Name | Description |
|  --- | --- |
| `DEFAULT` | Use the default sort. By default, Customers are sorted<br>alphanumerically by concatenating `given_name` and `family_name`. If<br>neither name field is set, string comparison is performed using one of the<br>remaining fields in the following order: `company_name`, `email`,<br>`phone_number`. |
| `CREATED_AT` | Sort Customers by their creation date (`created_at`). |

