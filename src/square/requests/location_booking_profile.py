# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class LocationBookingProfileParams(typing_extensions.TypedDict):
    """
    The booking profile of a seller's location, including the location's ID and whether the location is enabled for online booking.
    """

    location_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the [location](entity:Location).
    """

    booking_site_url: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Url for the online booking site for this location.
    """

    online_booking_enabled: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates whether the location is enabled for online booking.
    """
