# This file was auto-generated by Fern from our API Definition.

# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
import typing_extensions
import typing_extensions
import typing
from square.core.serialization import FieldMetadata


class Base(typing_extensions.TypedDict):
    id: str


class Shape_CircleParams(Base):
    shape_type: typing_extensions.Annotated[typing.Literal["circle"], FieldMetadata(alias="shapeType")]
    radius_measurement: typing_extensions.Annotated[float, FieldMetadata(alias="radiusMeasurement")]


class Shape_SquareParams(Base):
    shape_type: typing_extensions.Annotated[typing.Literal["square"], FieldMetadata(alias="shapeType")]
    length_measurement: typing_extensions.Annotated[float, FieldMetadata(alias="lengthMeasurement")]


ShapeParams = typing.Union[Shape_CircleParams, Shape_SquareParams]
