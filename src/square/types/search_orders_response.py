# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .order_entry import OrderEntry
import pydantic
from .order import Order
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchOrdersResponse(UncheckedBaseModel):
    """
    Either the `order_entries` or `orders` field is set, depending on whether
    `return_entries` is set on the [SearchOrdersRequest](api-endpoint:Orders-SearchOrders).
    """

    order_entries: typing.Optional[typing.List[OrderEntry]] = pydantic.Field(default=None)
    """
    A list of [OrderEntries](entity:OrderEntry) that fit the query
    conditions. The list is populated only if `return_entries` is set to `true` in the request.
    """

    orders: typing.Optional[typing.List[Order]] = pydantic.Field(default=None)
    """
    A list of
    [Order](entity:Order) objects that match the query conditions. The list is populated only if
    `return_entries` is set to `false` in the request.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If unset,
    this is the final response.
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    [Errors](entity:Error) encountered during the search.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
