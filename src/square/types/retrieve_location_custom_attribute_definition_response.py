# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .custom_attribute_definition import CustomAttributeDefinition
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class RetrieveLocationCustomAttributeDefinitionResponse(UncheckedBaseModel):
    """
    Represents a [RetrieveLocationCustomAttributeDefinition](api-endpoint:LocationCustomAttributes-RetrieveLocationCustomAttributeDefinition) response.
    Either `custom_attribute_definition` or `errors` is present in the response.
    """

    custom_attribute_definition: typing.Optional[CustomAttributeDefinition] = pydantic.Field(default=None)
    """
    The retrieved custom attribute definition.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
