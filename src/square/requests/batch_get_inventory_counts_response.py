# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .inventory_count import InventoryCountParams


class BatchGetInventoryCountsResponseParams(typing_extensions.TypedDict):
    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    counts: typing_extensions.NotRequired[typing.Sequence[InventoryCountParams]]
    """
    The current calculated inventory counts for the requested objects
    and locations.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    The pagination cursor to be used in a subsequent request. If unset,
    this is the final response.
    
    See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    """
