# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FilterValue(UncheckedBaseModel):
    """
    A filter to select resources based on an exact field value. For any given
    value, the value can only be in one property. Depending on the field, either
    all properties can be set or only a subset will be available.

    Refer to the documentation of the field.
    """

    all_: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="all")] = pydantic.Field(
        default=None
    )
    """
    A list of terms that must be present on the field of the resource.
    """

    any: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of terms where at least one of them must be present on the
    field of the resource.
    """

    none: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of terms that must not be present on the field the resource
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
