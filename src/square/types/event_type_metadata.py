# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EventTypeMetadata(UncheckedBaseModel):
    """
    Contains the metadata of a webhook event type.
    """

    event_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event type.
    """

    api_version_introduced: typing.Optional[str] = pydantic.Field(default=None)
    """
    The API version at which the event type was introduced.
    """

    release_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The release status of the event type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
