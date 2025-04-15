# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogObjectReference(UncheckedBaseModel):
    """
    A reference to a Catalog object at a specific version. In general this is
    used as an entry point into a graph of catalog objects, where the objects exist
    at a specific version.
    """

    object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the referenced object.
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
