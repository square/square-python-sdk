# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CoordinatesParams(typing_extensions.TypedDict):
    """
    Latitude and longitude coordinates.
    """

    latitude: typing_extensions.NotRequired[typing.Optional[float]]
    """
    The latitude of the coordinate expressed in degrees.
    """

    longitude: typing_extensions.NotRequired[typing.Optional[float]]
    """
    The longitude of the coordinate expressed in degrees.
    """
