# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .vendor import Vendor
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchVendorsResponse(UncheckedBaseModel):
    """
    Represents an output from a call to [SearchVendors](api-endpoint:Vendors-SearchVendors).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors encountered when the request fails.
    """

    vendors: typing.Optional[typing.List[Vendor]] = pydantic.Field(default=None)
    """
    The [Vendor](entity:Vendor) objects matching the specified search filter.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If unset,
    this is the final response.
    
    See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
