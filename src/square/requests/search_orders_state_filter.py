# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing
from ..types.order_state import OrderState


class SearchOrdersStateFilterParams(typing_extensions.TypedDict):
    """
    Filter by the current order `state`.
    """

    states: typing.Sequence[OrderState]
    """
    States to filter for.
    See [OrderState](#type-orderstate) for possible values
    """
