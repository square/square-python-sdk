# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .measurement_unit_custom import MeasurementUnitCustomParams
from ..types.measurement_unit_area import MeasurementUnitArea
from ..types.measurement_unit_length import MeasurementUnitLength
from ..types.measurement_unit_volume import MeasurementUnitVolume
from ..types.measurement_unit_weight import MeasurementUnitWeight
from ..types.measurement_unit_generic import MeasurementUnitGeneric
from ..types.measurement_unit_time import MeasurementUnitTime
from ..types.measurement_unit_unit_type import MeasurementUnitUnitType


class MeasurementUnitParams(typing_extensions.TypedDict):
    """
    Represents a unit of measurement to use with a quantity, such as ounces
    or inches. Exactly one of the following fields are required: `custom_unit`,
    `area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.
    """

    custom_unit: typing_extensions.NotRequired[MeasurementUnitCustomParams]
    """
    A custom unit of measurement defined by the seller using the Point of Sale
    app or ad-hoc as an order line item.
    """

    area_unit: typing_extensions.NotRequired[MeasurementUnitArea]
    """
    Represents a standard area unit.
    See [MeasurementUnitArea](#type-measurementunitarea) for possible values
    """

    length_unit: typing_extensions.NotRequired[MeasurementUnitLength]
    """
    Represents a standard length unit.
    See [MeasurementUnitLength](#type-measurementunitlength) for possible values
    """

    volume_unit: typing_extensions.NotRequired[MeasurementUnitVolume]
    """
    Represents a standard volume unit.
    See [MeasurementUnitVolume](#type-measurementunitvolume) for possible values
    """

    weight_unit: typing_extensions.NotRequired[MeasurementUnitWeight]
    """
    Represents a standard unit of weight or mass.
    See [MeasurementUnitWeight](#type-measurementunitweight) for possible values
    """

    generic_unit: typing_extensions.NotRequired[MeasurementUnitGeneric]
    """
    Reserved for API integrations that lack the ability to specify a real measurement unit
    See [MeasurementUnitGeneric](#type-measurementunitgeneric) for possible values
    """

    time_unit: typing_extensions.NotRequired[MeasurementUnitTime]
    """
    Represents a standard unit of time.
    See [MeasurementUnitTime](#type-measurementunittime) for possible values
    """

    type: typing_extensions.NotRequired[MeasurementUnitUnitType]
    """
    Represents the type of the measurement unit.
    See [MeasurementUnitUnitType](#type-measurementunitunittype) for possible values
    """
