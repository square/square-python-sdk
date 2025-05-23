# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .search_vendors_request_sort_field import SearchVendorsRequestSortField
import pydantic
from .sort_order import SortOrder
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchVendorsRequestSort(UncheckedBaseModel):
    """
    Defines a sorter used to sort results from [SearchVendors](api-endpoint:Vendors-SearchVendors).
    """

    field: typing.Optional[SearchVendorsRequestSortField] = pydantic.Field(default=None)
    """
    Specifies the sort key to sort the returned vendors.
    See [Field](#type-field) for possible values
    """

    order: typing.Optional[SortOrder] = pydantic.Field(default=None)
    """
    Specifies the sort order for the returned vendors.
    See [SortOrder](#type-sortorder) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
