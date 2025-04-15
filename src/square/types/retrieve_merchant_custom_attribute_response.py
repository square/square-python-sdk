# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .custom_attribute import CustomAttribute
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class RetrieveMerchantCustomAttributeResponse(UncheckedBaseModel):
    """
    Represents a [RetrieveMerchantCustomAttribute](api-endpoint:MerchantCustomAttributes-RetrieveMerchantCustomAttribute) response.
    Either `custom_attribute_definition` or `errors` is present in the response.
    """

    custom_attribute: typing.Optional[CustomAttribute] = pydantic.Field(default=None)
    """
    The retrieved custom attribute. If `with_definition` was set to `true` in the request,
    the custom attribute definition is returned in the `definition` field.
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
