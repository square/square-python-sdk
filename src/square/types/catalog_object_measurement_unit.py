# This file was auto-generated by Fern from our API Definition.

from .catalog_object_base import CatalogObjectBase
import typing
from .catalog_measurement_unit import CatalogMeasurementUnit
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogObjectMeasurementUnit(CatalogObjectBase):
    measurement_unit_data: typing.Optional[CatalogMeasurementUnit] = pydantic.Field(default=None)
    """
    Structured data for a `CatalogMeasurementUnit`, set for CatalogObjects of type `MEASUREMENT_UNIT`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
