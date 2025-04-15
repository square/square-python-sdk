# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponse(UncheckedBaseModel):
    """
    Represents an individual delete response in a [BulkDeleteLocationCustomAttributes](api-endpoint:LocationCustomAttributes-BulkDeleteLocationCustomAttributes)
    request.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the location associated with the custom attribute.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors that occurred while processing the individual LocationCustomAttributeDeleteRequest request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
