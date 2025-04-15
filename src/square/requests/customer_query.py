# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .customer_filter import CustomerFilterParams
from .customer_sort import CustomerSortParams


class CustomerQueryParams(typing_extensions.TypedDict):
    """
    Represents filtering and sorting criteria for a [SearchCustomers](api-endpoint:Customers-SearchCustomers) request.
    """

    filter: typing_extensions.NotRequired[CustomerFilterParams]
    """
    The filtering criteria for the search query. A query can contain multiple filters in any combination.
    Multiple filters are combined as `AND` statements.
    
    __Note:__ Combining multiple filters as `OR` statements is not supported. Instead, send multiple single-filter
    searches and join the result sets.
    """

    sort: typing_extensions.NotRequired[CustomerSortParams]
    """
    Sorting criteria for query results. The default behavior is to sort 
    customers alphabetically by `given_name` and `family_name`.
    """
