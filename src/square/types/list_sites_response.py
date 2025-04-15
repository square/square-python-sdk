# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .site import Site
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListSitesResponse(UncheckedBaseModel):
    """
    Represents a `ListSites` response. The response can include either `sites` or `errors`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    sites: typing.Optional[typing.List[Site]] = pydantic.Field(default=None)
    """
    The sites that belong to the seller.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
