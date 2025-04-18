# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .loyalty_event import LoyaltyEvent
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchLoyaltyEventsResponse(UncheckedBaseModel):
    """
    A response that contains loyalty events that satisfy the search
    criteria, in order by the `created_at` date.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    events: typing.Optional[typing.List[LoyaltyEvent]] = pydantic.Field(default=None)
    """
    The loyalty events that satisfy the search criteria.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent 
    request. If empty, this is the final response. 
    For more information, 
    see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
