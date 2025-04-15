# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchSubscriptionsFilter(UncheckedBaseModel):
    """
    Represents a set of query expressions (filters) to narrow the scope of targeted subscriptions returned by
    the [SearchSubscriptions](api-endpoint:Subscriptions-SearchSubscriptions) endpoint.
    """

    customer_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A filter to select subscriptions based on the subscribing customer IDs.
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A filter to select subscriptions based on the location.
    """

    source_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A filter to select subscriptions based on the source application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
