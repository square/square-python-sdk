# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .search_orders_filter import SearchOrdersFilter
import pydantic
from .search_orders_sort import SearchOrdersSort
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchOrdersQuery(UncheckedBaseModel):
    """
    Contains query criteria for the search.
    """

    filter: typing.Optional[SearchOrdersFilter] = pydantic.Field(default=None)
    """
    Criteria to filter results by.
    """

    sort: typing.Optional[SearchOrdersSort] = pydantic.Field(default=None)
    """
    Criteria to sort results by.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
