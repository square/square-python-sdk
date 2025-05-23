# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .order_entry import OrderEntryParams
from .order import OrderParams
from .error import ErrorParams


class SearchOrdersResponseParams(typing_extensions.TypedDict):
    """
    Either the `order_entries` or `orders` field is set, depending on whether
    `return_entries` is set on the [SearchOrdersRequest](api-endpoint:Orders-SearchOrders).
    """

    order_entries: typing_extensions.NotRequired[typing.Sequence[OrderEntryParams]]
    """
    A list of [OrderEntries](entity:OrderEntry) that fit the query
    conditions. The list is populated only if `return_entries` is set to `true` in the request.
    """

    orders: typing_extensions.NotRequired[typing.Sequence[OrderParams]]
    """
    A list of
    [Order](entity:Order) objects that match the query conditions. The list is populated only if
    `return_entries` is set to `false` in the request.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    The pagination cursor to be used in a subsequent request. If unset,
    this is the final response.
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    [Errors](entity:Error) encountered during the search.
    """
